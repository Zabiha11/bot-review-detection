import pandas as pd
import networkx as nx

import community as community_louvain


class GraphFeatureEngineer:

    def __init__(self, df):

        self.df = df

    def build_graph(self):

        G = nx.Graph()

        for _, row in self.df.iterrows():

            user = (
                f"user_{row['user_id']}"
            )

            product = (
                f"product_{row['product_id']}"
            )

            G.add_node(
                user,
                type="user"
            )

            G.add_node(
                product,
                type="product"
            )

            G.add_edge(
                user,
                product
            )

        self.G = G

    def centrality_features(self):

        degree_centrality = (
            nx.degree_centrality(
                self.G
            )
        )

        pagerank = nx.pagerank(
            self.G
        )

        self.df[
            "degree_centrality"
        ] = (
            self.df["user_id"]
            .apply(
                lambda x:
                degree_centrality.get(
                    f"user_{x}",
                    0
                )
            )
        )

        self.df["pagerank"] = (
            self.df["user_id"]
            .apply(
                lambda x:
                pagerank.get(
                    f"user_{x}",
                    0
                )
            )
        )

        return self.df

    def community_features(self):

        partition = (
            community_louvain
            .best_partition(self.G)
        )

        self.df["community_id"] = (
            self.df["user_id"]
            .apply(
                lambda x:
                partition.get(
                    f"user_{x}",
                    -1
                )
            )
        )

        return self.df

    def clustering_features(self):

        clustering = nx.clustering(
            self.G
        )

        self.df["clustering_coeff"] = (
            self.df["user_id"]
            .apply(
                lambda x:
                clustering.get(
                    f"user_{x}",
                    0
                )
            )
        )

        return self.df

    def build(self):

        print("Building graph...")
        self.build_graph()

        print("Generating centrality...")
        self.centrality_features()

        print("Generating communities...")
        self.community_features()

        print("Generating clustering...")
        self.clustering_features()

        return self.df