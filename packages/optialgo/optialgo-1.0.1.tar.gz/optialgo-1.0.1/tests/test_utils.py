import pandas as pd
import numpy as np
import unittest
from optialgo import *


df = pd.read_csv("../dataset_ex/drug200.csv")
target = "Drug"
features = df.columns.tolist()
n_features = 3


class TestFeatureSelection(unittest.TestCase):
    def setUp(self):
        self.df = df
        self.features = features
        self.target = target
        self.n_features = n_features

    def test_feature_selection(self):
        selected_features:dict = feature_selection(self.df,target=self.target,n_features=self.n_features,show_score=False)
        self.assertIsInstance(selected_features,dict)



if __name__ == '__main__':
    unittest.main()
