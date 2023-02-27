import pandas as pd
import numpy as np

data = pd.Series(['Nirvi', 'Abhyuday', 'Neha', 'Nishank'])
print(data)
print(data.values)
print(data.index)


def create_pandas_dataframe():
    """Returns a Pandas DataFrame with a 2D array
    containing values 1, 2, 3, and 4, and columns
    named 'column_1' and 'column_2'
    """
    return pd.DataFrame(data=np.array([[1, 2], [3, 4]]), columns=['column_1', 'column_2'])


python_list = [1, 2, 3, 4, 5]
numpy_arr = np.array(python_list)
pandas_series = pd.Series(data=numpy_arr, index=['a', 'b', 'c', 'd', 'e'])
print(pandas_series)
print(pandas_series[1:3])

## Creating pandas from dictionaries

index_list = ["cost per night", "average room capacity"]
# python dictionary
dataframe_dict = {
    "Amestradam": ["$100", "2 people"],
    "London": ["$200", "3 people"],
    "Delhi": ["$50", "4 people"]
}
print(pd.Series(data=dataframe_dict, index=["Mumbai", "Bengaluru", "Noida"]))
print(pd.DataFrame(data=dataframe_dict, index=index_list))
# Python list
python_2dList = [["$100", "$200", "$50"], ["2 people", "3 people", "4 people"]]
python_column_list = ["Amestradam", "London", "Delhi"]
print(pd.DataFrame(data=python_2dList, columns=python_column_list, index=index_list))

print(pd.DataFrame(data=np.array([["$100", "$200", "$50"], ["2 people", "3 people", "4 people"]]),
                   columns=python_column_list, index=index_list))


def create_dataframe():

    index1_list = ["score", "reviews", "popularity"]
    pandas_dict = {
        "Arsenal": [5, 512, 5],
        "Barcelona": [4.5, 111.0, 9.5],
        "Real Madrid": [6, 380, 9],
        "Man Utd": [8, 500, 8],
        "Man City": [5, 453, 7],
        "PSG": [8, 563, 9.7],
    }
    return pd.DataFrame(data=pandas_dict, index=index1_list)

print(create_dataframe())
dataframe_obj = create_dataframe()
obj1 = dataframe_obj.loc[:, "Arsenal"]
obj2 = dataframe_obj.iloc[:, 1]
# print(obj1)
print(obj2)

