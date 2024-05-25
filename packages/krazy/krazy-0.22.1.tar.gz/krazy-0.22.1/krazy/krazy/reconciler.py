
import pandas as pd
import numpy as np
import datetime
import os
from pathlib import Path
from operator import itemgetter

def df_import_clean_files(dir:Path=False, clean=True, df=False)->list[pd.DataFrame, list, list, list, list]:
    '''
    import multiple files from a folder into pandas dataframe
    dir:    Required:   Path to the folder containing the files
    clean:  Optional:   Clean the dataframe. Default is True
    df:     Optional:   Pass a dataframe. This is required if dir is false and clean is True
    
    to only clean a dataframe already imported, pass df and dont pass dir or pass dir = False

    Returns: List[DataFrame, Possible Date Columns, Possible Amount Columns, Possible ID Columns, Files Skipped]
    '''
    if dir != False:
        df = pd.DataFrame()
        files_skipped = []

        for file in os.listdir(dir):
            file_path = dir.joinpath(file)
            if file_path.suffix.lower() == '.csv':
                df_temp = pd.read_csv(dir.joinpath(file))
                df = pd.concat([df, df_temp], axis=0)
            elif file_path.suffix.lower() == '.xlsx':
                df_temp = pd.read_excel(dir.joinpath(file))
                df = pd.concat([df, df_temp], axis=0)
                ic()
            else:
                files_skipped.append(file)

    date_cols = df.select_dtypes(include='datetime').columns
    object_cols = df.select_dtypes(include='object').columns
    float_cols = df.select_dtypes(include='float').columns
    int_cols = df.select_dtypes(include='int').columns

    # identify possible date, amount columns imported as object cols
    possible_date_cols = [col for col in object_cols if 'date' in col.lower()]
    possible_amount_cols = [col for col in object_cols if 'amount' in col.lower()]
    possible_amt_cols = [col for col in object_cols if 'amt' in col.lower()]

    if len(possible_amt_cols)>0:
        possible_amount_cols.extend(possible_amt_cols)
     
    del possible_amt_cols

    # possible columns which are not date or amount
    possible_id_cols = [col for col in df.columns if col not in possible_date_cols]
    possible_id_cols = [col for col in possible_id_cols if col not in possible_amount_cols]

    # clean date and amount cols
    if clean is True and df is not False:

        if len(possible_date_cols)>0:
            for col in possible_date_cols:
                print(f'Converting column: {col} to date')
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        if len(possible_amount_cols)>0:
            for col in possible_amount_cols:
                print(f'Converting column: {col} to float')
                df[col] = df[col].str.replace(',', '').replace('-',0).astype(float)

    if clean is True and df is False:
        print('No dataframe to clean')
        return False

    return [df, possible_date_cols, possible_amount_cols, possible_id_cols, files_skipped]

def df_common_cols(df1:pd.DataFrame, df2:pd.DataFrame)->list:
    '''
    takes 2 dataframes and returns common cols and different cols
    Returns: List[common_cols, different_cols]
    '''
    common_cols = df1.columns.intersection(df2.columns).tolist()
    different_cols = df1.columns.difference(df2.columns).tolist()
    return [common_cols, different_cols]

def df_find_unique_col(df:pd.DataFrame)->pd.DataFrame:
    '''
    takes dataframe and returns relevant stats about columns in dataframe
    Returns: DataFrame
    '''
    df_counts = pd.DataFrame(columns=['Column', 'DF Length', 'Count', 'Unique', 'Diff'])
    # object columns
    cols = df.select_dtypes(include='object').columns

    for col in cols:
        diff = df[col].count() - df[col].nunique()
        df_counts.loc[len(df_counts)] = [col, len(df), df[col].count(), df[col].nunique(), diff]

    df_counts['Perc'] = df_counts['Unique']/df_counts['Count']
    df_counts['Non Blank'] = df_counts['DF Length'] - df_counts['Count']
    
    return df_counts

def reconciler(df1, df2)->pd.DataFrame:
    '''
    takes two dataframes and returns the possible columns on which dataframes reconciles
    Returns: DataFrame
    '''
    # get unique values in columns
    df1_counts = df_find_unique_col(df1)
    df2_counts = df_find_unique_col(df2)

    df1_counts.sort_values(by='Diff', ascending=True, inplace=True)
    df2_counts.sort_values(by='Diff', ascending=True, inplace=True)

    # find top 5 unique identifier columns
    unique_identifier_1 = df1_counts[0:5]['Column'].tolist()
    unique_identifier_2 = df2_counts[0:5]['Column'].tolist()

    # Level 1: direct column name match
    matched_cols = []

    for col in unique_identifier_1:
        try:
            assert df2[col]
            matched_cols.append(col)
        except AssertionError:
            pass
        except Exception as e:
            pass

    matched_outcome_1 = pd.DataFrame(columns=['df1_Col','df2_Col', 'Matched_Percentage'])
    for col in matched_cols:
        df_merged = pd.merge(df1, df2, on=col, how='outer', indicator='Source')
        matched_perc = len(df_merged.loc[df_merged['Source']=='both'])/len(df_merged)
        matched_outcome_1[len(matched_outcome_1)] = [col, col, matched_perc]
    
    matched_outcome_1.sort_values(by='Matched_Percentage', ascending=False, inplace=True)
    matched_outcome_1['Reco_Level'] = 'Level 1 - Direct Col Name Match'

    # Level 2: top 5 column values match        
    matched_outcome_2 = pd.DataFrame(columns=['df1_Col','df2_Col', 'Matched_Percentage'])
    for col in unique_identifier_1:
        col_as_list = df1[col].tolist()
        for col2 in unique_identifier_2:
            col2_as_list = df2[col2].tolist()
            matched = set(col_as_list) & set(col2_as_list)
            matched_perc = len(matched)/len(set(col_as_list))
            matched_outcome_2.loc[len(matched_outcome_2)] = [col, col2, matched_perc]

    matched_outcome_2.sort_values(by='Matched_Percentage', ascending=False, inplace=True)
    matched_outcome_2['Reco_Level'] = 'Level 2 - Top 5 Col Values Match'

    # combine results
    matched_outcome = pd.concat([matched_outcome_1, matched_outcome_2], axis=0)
    matched_outcome.sort_values(by='Matched_Percentage', ascending=False, inplace=True)

    return matched_outcome

