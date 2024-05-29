import pandas as pd
import os

os.chdir("..")

from optialgo import Dataset, Regression

df = pd.read_csv("dataset_ex/Housing.csv")

print(df.columns.tolist())
