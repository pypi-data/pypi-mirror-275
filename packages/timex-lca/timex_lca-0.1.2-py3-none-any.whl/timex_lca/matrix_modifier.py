import bw2data as bd
import bw_processing as bwp
import uuid
import numpy as np
import pandas as pd
from typing import Optional
from datetime import datetime


class MatrixModifier:
    """
    This class is responsible for modifying the original LCA matrices to contain the time-explicit processes and to relink them to the time-explicit background databasess. 
    
    It does this by ccreating datapackages that contain new matrix entries all changes in the matrices, based on a timeline dataframe (created from TimelineBuilder.build_timeline()).

    """

    def __init__(
        self,
        timeline: pd.DataFrame,
        database_date_dict_static_only: dict,
        demand_timing: dict,
        name: Optional[str] = None,
    ) -> None:
        """
        Initializes the MatrixModifier object.

        Parameters
        ----------
        timeline : pd.DataFrame
            A DataFrame of the timeline of exchanges
        database_date_dict_static_only : dict
            A dictionary mapping the static background databases to dates.
        demand_timing : dict
            A dictionary mapping the demand to its timing.
        name : str, optional   
            An optional name for the MatrixModifier instance. Default is None.
        temporalized_process_ids : set
            A set to collect the ids the "exploded" processes, instantiated empty
        temporal_market_ids : set
            A set to collect the ids of the "temporal markets" , instantiated empty
        """

        self.timeline = timeline
        self.database_date_dict_static_only = database_date_dict_static_only
        self.demand_timing = demand_timing
        self.name = name
        self.temporalized_process_ids = set()
        self.temporal_market_ids = set()

    def create_technosphere_datapackage(self) -> bwp.Datapackage:
        """
        Creates patches to the technosphere matrix from a given timeline of grouped exchanges to add these temporal processes to the technopshere database.
        Patches are datapackages that add or overwrite datapoints in the LCA matrices before LCA calculations.

        The heavy lifting of this function happens in its inner function `add_row_to_datapackage()`:
        Here, each node with a temporal distribution is "exploded", which means each occurrence of this node (e.g. steel production on 2020-01-01
        and steel production 2015-01-01) becomes a separate, time-explicit new node, by adding the respective elements to the technosphere matrix.
        For processes at the interface with background databases, the timing of the exchanges determines which background database to link to in so called "Temporal Markets".

        Parameters
        ----------
        None

        Returns
        -------
        bwp.Datapackage
            A datapackage containing the patches for the technosphere matrix.
        """

        def add_row_to_datapackage(
            row: pd.core.frame,
            datapackage: bwp.Datapackage,
            database_date_dict_static_only: dict,
            demand_timing: dict,
            new_nodes: set,
        ) -> None:
            """
            This adds the required technosphere matrix modifications for each time-dependent exchange (edge) as datapackage elements to a given `bwp.Datapackage`.
            Modifications include:
            1) Exploded processes: new matrix elements between exploded consumer and exploded producer, representing the temporal edge between them.
            2) Temporal markets: new matrix entries between "temporal markets" and the producers in temporally matching background databases, with shares based on interpolation.
               Processes in the background databases are matched on name, reference product and location.
            3) Diagonal entries: ones on the diagonal for new nodes.

            This function also updates the sets of new nodes with the ids of any new nodes created during this process.

            Parameters
            ----------
            row : pd.core.frame
                A row of the timeline DataFrame representing an temporalized edge
            datapackage : bwp.Datapackage
                Append to this datapackage, if available. Otherwise create a new datapackage.
            database_date_dict_static_only : dict
                A dict of the available background databases: their names (key) and temporal representativeness (value).
            demand_timing : dict
                A dict of the demand ids and their timing. Can be created using `TimexLCA.create_demand_timing_dict()`.
            new_nodes : set
                Set to which new node ids are added.

            Returns
            -------
            None but updates the set new_nodes and adds a patch for this new edge to the bwp.Datapackage.
            """

            if row.consumer == -1:  # functional unit
                new_producer_id = row.time_mapped_producer
                new_nodes.add(new_producer_id)
                self.temporalized_process_ids.add(
                    new_producer_id
                )  # comes from foreground, so it is a temporalized process
                return

            new_consumer_id = row.time_mapped_consumer
            new_nodes.add(new_consumer_id)

            new_producer_id = row.time_mapped_producer
            new_nodes.add(new_producer_id)

            previous_producer_id = row.producer
            previous_producer_node = bd.get_node(
                id=previous_producer_id
            )  # in future versions, insead of getting node, just provide list of producer ids

            # Add entry between exploded consumer and exploded producer (not in background database)
            datapackage.add_persistent_vector(
                matrix="technosphere_matrix",
                name=uuid.uuid4().hex,
                data_array=np.array([row.amount], dtype=float),
                indices_array=np.array(
                    [(new_producer_id, new_consumer_id)],
                    dtype=bwp.INDICES_DTYPE,
                ),
                flip_array=np.array(
                    [True], dtype=bool
                ),  
            )

            # Check if previous producer comes from background database
            if (
                previous_producer_node["database"]
                in self.database_date_dict_static_only.keys()
            ):
                # Create new edges based on interpolation_weights from the row
                for database, db_share in row.interpolation_weights.items():
                    # Get the producer activity in the corresponding background database
                    try:
                        producer_id_in_background_db = bd.get_node(
                            **{
                                "database": database,
                                "name": previous_producer_node["name"],
                                "product": previous_producer_node["reference product"],
                                "location": previous_producer_node["location"],
                            }
                        ).id
                    except:
                        print(
                            f"Could not find producer in database {database} with name {previous_producer_node['name']}, product {previous_producer_node['reference product']}, location {previous_producer_node['location']}"
                        )
                        raise SystemExit

                    # Add entry between exploded producer and producer in background database ("Temporal Market")
                    datapackage.add_persistent_vector(
                        matrix="technosphere_matrix",
                        name=uuid.uuid4().hex,
                        data_array=np.array(
                            [db_share], dtype=float
                        ),  # temporal markets produce 1, so shares divide amount between dbs
                        indices_array=np.array(
                            [(producer_id_in_background_db, new_producer_id)],
                            dtype=bwp.INDICES_DTYPE,
                        ),
                        flip_array=np.array([True], dtype=bool),
                    )
                    self.temporal_market_ids.add(new_producer_id)
            else:
                self.temporalized_process_ids.add(
                    new_producer_id
                )  # comes from foreground, so it is a temporalized process

        datapackage = bwp.create_datapackage(
            sum_inter_duplicates=False
        )  # 'sum_inter_duplicates=False': If the same market is used by multiple foreground processes, the market gets created again, inputs should not be summed.

        new_nodes = set()

        for row in self.timeline.iloc[::-1].itertuples():
            add_row_to_datapackage(
                row,
                datapackage,
                self.database_date_dict_static_only,
                self.demand_timing,
                new_nodes,
            )

        # Adding ones on diagonal for new nodes
        datapackage.add_persistent_vector(
            matrix="technosphere_matrix",
            name=uuid.uuid4().hex,
            data_array=np.ones(len(new_nodes)),
            indices_array=np.array(
                [(i, i) for i in new_nodes], dtype=bwp.INDICES_DTYPE
            ),
        )

        return datapackage

    def create_biosphere_datapackage(self) -> bwp.Datapackage:
        """
        Creates list of patches formatted as datapackages for modifications to the biosphere matrix.
        It adds the biosphere flows to the exploded technosphere processes.

        This function iterates over each unique producer and for each biosphere exchange of the original activity,
        it creates a new biosphere exchange for the new node.

        Temporal markets have to biosphere exchanges, as they only divide the amount of the technosphere exchange between the different databases.

        Parameters
        ----------
        None

        Returns
        -------
        bwp.Datapackage
            An updated datapackage containing the patches for the biosphere matrix.
        """
        unique_producers = (
            self.timeline.groupby(["producer", "time_mapped_producer"])
            .count()
            .index.values
        )  # array of unique (producer, timestamp) tuples

        datapackage_bio = bwp.create_datapackage(sum_inter_duplicates=False)

        for producer in unique_producers:
            if (
                bd.get_activity(producer[0])["database"]
                not in self.database_date_dict_static_only.keys()  # skip temporal markets
            ):
                producer_id = producer[1]
                # the producer_id is a combination of the activity_id and the timestamp
                producer_node = bd.get_node(id=producer[0])
                indices = (
                    []
                )  # list of (biosphere, technosphere) indices for the biosphere flow exchanges
                amounts = []  # list of amounts corresponding to the bioflows
                for exc in producer_node.biosphere():
                    indices.append(
                        (exc.input.id, producer_id)
                    )  # directly build a list of tuples to pass into the datapackage, the producer_id is used to for the column of that activity
                    amounts.append(exc.amount)

                datapackage_bio.add_persistent_vector(
                    matrix="biosphere_matrix",
                    name=uuid.uuid4().hex,
                    data_array=np.array(amounts, dtype=float),
                    indices_array=np.array(
                        indices,
                        dtype=bwp.INDICES_DTYPE,
                    ),
                    flip_array=np.array([False], dtype=bool),
                )
        return datapackage_bio

    def create_datapackage(self) -> None:
        """
        Creates a list of datapackages for the technosphere and biosphere matrices, by calling the respective functions.

        Parameters
        ----------
        None

        Returns
        -------
        list
            A list of the technosphere and biosphere datapackages.
        """
        technosphere_datapackage = self.create_technosphere_datapackage()
        biosphere_datapackage = self.create_biosphere_datapackage()
        
        return [technosphere_datapackage, biosphere_datapackage]
