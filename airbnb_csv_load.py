import os
import shutil

import gdown
import numpy as np
from numpy import genfromtxt
from currency_converter import CurrencyConverter


np.set_printoptions(suppress=True)

# Download file from Google Drive
# This file is based on data from: http://insideairbnb.com/get-the-data/
file_id_1 = "13fyESiH1ZEnMV6eabAyhe20t4W6peEWK"
downloaded_file_1 = "WK1_Airbnb_Amsterdam_listings_proj.csv"

# Download the file from Google Drive
# gdown.download(id=file_id_1, output=downloaded_file_1)
matrix_1 = genfromtxt("WK1_Airbnb_Amsterdam_listings_proj.csv", dtype='unicode', delimiter='|')
print(f"The shape of matrix is {matrix_1.shape}")
print(f"The dimension of matrix is {matrix_1.ndim}")
print(f"The size of the matrix is {matrix_1.size}")
print(f"The type of matrix is {matrix_1.dtype}")
# print(matrix_1[:, :4])
matrix_1 = matrix_1[1:, 1:]
matrix_1 = matrix_1.T
print(matrix_1[4097])

# replace a particular character in the matrix
matrix_1 = np.char.replace(matrix_1, '$', '')
matrix_1 = np.char.replace(matrix_1, ',', '')
# find a particular character in the elements of the matrix
out_matrix = matrix_1[(np.char.find(matrix_1, ",") > -1) | (np.char.find(matrix_1, "$") > -1)]
print(f"The matrix with , and $ is {out_matrix}")
matrix_1 = matrix_1.astype(float)

cc = CurrencyConverter()
currency_set = cc.currencies

print(currency_set)
print(cc.convert(100, "USD", "GBP"))
print(np.around(12.5678, decimals=1))




