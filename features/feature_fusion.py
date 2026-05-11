class FeatureFusion:

    def __init__(self, df):

        self.df = df

    def select_features(self):

        drop_cols = [

            "review_text",

            "clean_text",

            "timestamp",

            "prev_timestamp"
        ]

        self.df = self.df.drop(
            columns=[
                col
                for col in drop_cols
                if col in self.df.columns
            ]
        )

        return self.df

    def build(self):

        self.select_features()

        return self.df