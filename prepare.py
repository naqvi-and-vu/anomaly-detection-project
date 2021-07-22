import pandas as pd
import numpy as np

def prep_logs(df):
    '''
    prep_logs will take in the curriculum log data and prepare it for use by 
    setting date to the index, and converting it to datetime format,
    changing start date and end date to datetime format,
    renaming columns for easier use, drop unecessary columns, create new features,
    create objectified columns for easier read, and drops duplicates
    '''
    #date to datetime
    df.date = pd.to_datetime(df.date)
    #set our index as date
    df = df.set_index(df.date)
    
    #change start_date object column to datetime format
    df.start_date = pd.to_datetime(df.start_date)
    
    #change end_date object column to datetime format
    df.end_date = pd.to_datetime(df.end_date)
    
    
    #create accessed_after column which tells us if the user accessed the material after their graduation date at the time of query
    df['accessed_after'] = df.index > df.end_date
    
    #turn accessed_after to integers instead of booleans
    df['accessed_after'] = df['accessed_after'].astype(int)
    
    #df = df.program_id.replace(np.NaN, 2.0)
    df = df.dropna()
    
    #create program_name column
    df['program_name'] = 0
    
    
    #program_id of 1 is Full Stack PHP
    df['program_name'] = np.where(df['program_id']==1, 'Full Stack PHP', 0)
    
    #program_id of 2 is Web Development
    df['program_name'] = np.where(df['program_id']==2, 'Web Development', df['program_name'])
    
    #program_id of 3 is Data Science
    df['program_name'] = np.where(df['program_id']==3, 'Data Science', df['program_name'])
    
    #program_id of 4 is Front End
    df['program_name'] = np.where(df['program_id']==4, 'Front End', df['program_name'])
    
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