import pandas as pd
import numpy as np

def prep_logs(df):
    df.index = pd.to_datetime(df.index)
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    df = df.rename(columns={'path':'endpoint',
                       'name':'cohort'})
    df = df.drop(columns=['id'])
    df['accessed_after'] = df.index > df.end_date
    df['accessed_after'] = df['accessed_after'].astype(int)
    
    # check for duplicates 
    num_dups = df.duplicated().sum()
    # if we found duplicate rows, we will remove them, log accordingly and proceed
    if num_dups > 0:
        print(f'There are {num_dups} duplicate rows in your dataset - these will be dropped.')
        print ('----------------')
        # remove the duplicates found
        df = df.drop_duplicates()
    else:
        # otherwise, we log that there are no dupes, and proceed with our process
        print(f'There are no duplicate rows in your dataset.')
        print('----------------')

    return df