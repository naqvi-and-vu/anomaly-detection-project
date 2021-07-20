import pandas as pd
import numpy as np

def prep_logs(df):
    df.index = pd.to_datetime(df.index)
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    df = df.rename(columns={'path':'endpoint',
                       'name':'cohort'})
    df = df.drop(columns=['id'])
    return df