"""
Excercise 10.7

Question 9: Sarah is a data analyst working for a marketing agency. She has been given
a list of customer ages from a recent survey conducted by her company.
The list contains a mix of integers representing ages and some strings due
to data entry errors. Sarah needs to clean up this data by removing the
erroneous entries (non-integer values) and then analyze the data to find
the following:
(a) The youngest and oldest customers.
(b) The average age of the customers.
(c) The most common age in the list.
"""

from statistics import mode

def analyze_data(data):
    data = [x for x in data if isinstance(x, int)]
    return {
        "min": min(data),
        "max": max(data),
        "mode": mode(data)
    }
    

