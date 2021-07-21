import os
import pandas as pd
from env import user, host, password 

def get_connection(db, user=user, host=host, password=password):
    '''
    Creates a connection URL from desired database to access from SQL, and login credentials.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# def new_curriculum_logs_data():
#     '''
#     Returns curriculum logs into a dataframe
#     '''
#     sql_query = '''select * from logs join cohorts on cohorts.id=logs.cohort_id'''
#     df = pd.read_sql(sql_query, get_connection('curriculum_logs'))
#     return df 

# def get_curriculum_logs_data():
#     '''get connection, returns curriculum log's logs table into a dataframe and creates a csv for us'''
#     if os.path.isfile('curriculum-access.csv'):
#         df = pd.read_csv('curriculum-access.csv', index_col=0)
#     else:
#         df = new_curriculum_logs_data()
#         df.to_csv('curriculum-access.csv')
#     return df

def get_curriculum_data(cached=False):
    '''
    This function returns the curriculum logs database as a pandas dataframe. 
    If the data is cached or the file exists in the directory, the function will read the data into a df and return it. 
    Otherwise, the function will read the database into a dataframe, cache it as a csv file
    and return the dataframe.
    '''
    # If the cached parameter is false, or the csv file is not on disk, read from the database into a dataframe
    if cached == False or os.path.isfile('curriculum-access.csv') == False:
        sql_query = '''
        SELECT start_date, end_date, created_at, name as cohort, program_id, logs.date, logs.time, path AS endpoint, user_id, ip
                FROM cohorts 
                RIGHT JOIN logs ON cohorts.id=logs.cohort_id;
        '''
        curriculum_df = pd.read_sql(sql_query, get_connection('curriculum_logs'))
        #also cache the data we read from the db, to a file on disk
        curriculum_df.to_csv('curriculum-access.csv')
    else:
        # either the cached parameter was true, or a file exists on disk. Read that into a df instead of going to the database
        curriculum_df = pd.read_csv('curriculum-access.csv', index_col=0)
    # return our dataframe regardless of its origin
    return curriculum_df