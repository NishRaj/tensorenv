import numpy as np
import pandas as pd

def create_dataframe():

    index1_list = ["score", "reviews", "popularity"]
    pandas_dict = {
        "Arsenal": [5, 512, 5],
        "Barcelona": [4.5, 111.0, 9.5],
        "Real Madrid": [6, 380, 9],
        "Man Utd": [8, 500, 8],
        "Man City": [7, 453, 7],
        "PSG": [8, 563, 9.7],
    }
    return pd.DataFrame(data=pandas_dict, index=index1_list)


data_frame = create_dataframe()
print(data_frame)
# replacing by giving a single value
new_data_frame = data_frame.replace(to_replace=8, value=2)
#print(new_data_frame)
# replacing by giving dictionary iterable
new_data_frame_dict = data_frame.replace(to_replace={5: 'Five', 500: 'Five Hundred'})
#print(new_data_frame_dict)
# replace a particular value in column
new_data_frame_spec_col = data_frame.replace(to_replace={'Arsenal': 512}, value=9999)
#print(new_data_frame_spec_col)

# replace a particular value in the column
new_data_frame_spec_col1 = data_frame.replace(to_replace={'Arsenal': {5: 'Five', 512: 'Five hundred'}, 'Real Madrid': {6: 'Six'}})
print(new_data_frame_spec_col1)