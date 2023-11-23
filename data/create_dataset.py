import os

import numpy as np
import pandas as pd


def create_data(folder_path):
    dfs = []
    for filename in os.listdir(folder_path):

        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path,filename)
            file_path = file_path.split(".")[0]
            df = pd.read_csv(file_path)
            df['config'] = filename  #Add config column to df
            dfs.append(df)
    
    final_df_ = pd.concat(dfs,ignore_index=True)
    return final_df

direct_folder_path = "/Users/smoothoperator/Documents/GitHub/CS7200-project/data/direct_transitivity"
direct_df = create_data(direct_folder_path)
direct_df.to_csv('direct_transitivity_data.csv',index = False)
vertical_folder_path = "/Users/smoothoperator/Documents/GitHub/CS7200-project/data/vertical_transitivity"
vertical_df = create_data(vertical_folder_path)
vertical_df.to_csv('vertical_transitivity_data.csv',index = False)

