# pratlib/preprocessing/encoder.py
from pyspark.ml.feature import OneHotEncoder as SparkOneHotEncoder, StringIndexer

class OneHotEncoder:
    def __init__(self, **kwargs):
        self.encoder = SparkOneHotEncoder(**kwargs)

    def fit(self, df, input_col, output_col):
        self.encoder.setInputCol(input_col).setOutputCol(output_col)
        self.model = self.encoder.fit(df)
        return self

    def transform(self, df):
        return self.model.transform(df)

class LabelEncoder:
    def __init__(self, **kwargs):
        self.indexer = StringIndexer(**kwargs)

    def fit(self, df, input_col, output_col):
        self.indexer.setInputCol(input_col).setOutputCol(output_col)
        self.model = self.indexer.fit(df)
        return self

    def transform(self, df):
        return self.model.transform(df)
