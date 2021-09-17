# Data analytics project for freecodecamp
# mean_variance_stddeviation_calculator
import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError
        # the list must contain 9 elements 
        # since it will be used to create a
        # 3X3 matrix
    
    # take the list and reshape it into a 3X3 matrix
    list = np.array(list).reshape((3,3))

    # finding the values of variables
    mean = [list.mean(axis = 0).tolist(), list.mean(axis = 1).tolist(), np.mean(list).tolist()]
    # calculate the mean in a list and keep it in the list using tolist()
    variance = [list.var(axis = 0).tolist(), list.var(axis = 1).tolist(), np.var(list).tolist()]
    std_dev = [list.std(axis = 0).tolist(), list.var(axis = 1).tolist(), np.std(list).tolist()]
    max = [list.max(axis = 0).tolist(), list.max(axis = 1).tolist(), np.max(list).tolist()]
    min = [list.min(axis = 0).tolist(), list.min(axis = 1).tolist(), np.min(list).tolist()]
    sum = [list.sum(axis = 0).tolist(), list.sum(axis = 1).tolist(), np.sum(list).tolist()]
    # created all the variable

    # return a dictionary of all the above variables
    return {
        'mean':mean,
        'variance':variance,
        'standard_deviation':std_dev,
        'max':max,
        'min':min,
        'sum':sum
    }

print(calculate([1,2,3,4,5,6,7,8,9]))