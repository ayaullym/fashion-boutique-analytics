import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv("../data/fashion_boutique_dataset.csv")