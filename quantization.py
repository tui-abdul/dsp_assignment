"""
def vectorQuantization(data,codebook):
    input_data=data
    code_book=codebook
    output = input_data
    storeVector =[]
    value1 = 0
    for i in range(0,len(input_data)):
        for j in range(0,len(code_book)):
            value1=np.sqrt((input_data[i][0] - code_book[j][0])**2+(input_data[i][1] - code_book[j][1])**2)
            storeVector.append(value1)
        temp1 = min(storeVector)
        addressIndex = storeVector.index(temp1)
        output[i][0] = code_book[addressIndex][0]
        output[i][1] = code_book[addressIndex][1]
        storeVector=[]
    temp2 = np.array(output)
    final_output = temp2.flatten()
    return final_output
"""""
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten

def generatCodebook(a,n):
    codeVectors,dist=kmeans(a,n)
    return codeVectors,dist
"""""
