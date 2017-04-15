import math

class StatisticsError(ValueError):
    pass

def total(data):
    # Adds up all datapoints to find the total
    t = 0
    for elem in data:
        t += elem
    return t

def mean(data):
    # Accepts a list of data and returns its arithmetic mean
    # total divided by number of data points
    return total(data)/len(data)

def low_median(data):
    # Finds the middle value of an odd numbered list, or the lower-middle value of an even-numbered list
    data.sort() #makes sure data are sorted
    # oddness condition
    if len(data)%2 != 0:
        return data[math.floor(len(data)/2)]
    # even
    else:
        midpoint = len(data)/2
        return data[int(midpoint-1)]

def high_median(data):
    # Finds the middle value of an odd numbered list, or the higher-middle value of an even-numbered list
    data.sort() #makes sure data are sorted
    # oddness condition
    if len(data)%2 != 0:
        return data[math.floor(len(data)/2)]
    # even
    else:
        midpoint = len(data)/2
        return data[int(midpoint)]

def median(data):
    # Finds the middle value of a sorted odd-numbered list, or the average of the middle two values of an even-numbered list (interpolated mean)
    # oddness condition
    data.sort() #makes sure data are sorted
    if len(data)%2 != 0:
        return data[math.floor(len(data)/2)]
    # even
    else:
        midpoint = len(data)/2
        return (data[int(midpoint-1)] + data[int(midpoint)])/2

def geometric_mean(data):
    # Finds the nth root of the product of all n numbers in a dataset
    geo_total = 1
    for elem in data:
        geo_total *= elem
    return geo_total**(1/len(data))

def harmonic_mean(data):
    # Finds the reciprocal of the arithmetic mean of the reciprocals
    har_total = 0
    for elem in data:
        har_total += 1/elem
    return len(data)/har_total

def frequencies(data, freq_sort = True, desc = True):
    # Returns an ordered list of tuples, one for each unique value in the data with the number of times it occurs
    # If freq_sort == True (default), the list will be sorted by how many times each point occurs
    # Otherwise, it will be sorted by the value of the data point
    # If desc = true, the list will be sorted in descending order
    # Otherwise, it will be sorted in ascending order
    import operator
    freqs = {}
    for elem in data:
        if elem not in freqs:
            freqs[elem] = 1
        else:
            freqs[elem] += 1
    # freq_sort == True: sort dict by value
    if freq_sort:
        return sorted(freqs.items(), key = operator.itemgetter(1), reverse = desc)
    # freq_sort == False: sort dict by key
    else:
        return sorted(freqs.items(), key = operator.itemgetter(0), reverse = desc)

def freq_list(data, freq_sort = True, desc = True):
    # Prints a each value in the data and how many times it appears
    # See frequencies for explanations of freq_sort and desc
    for tup in frequencies(data, freq_sort, desc):
        print("Value: {0} -- Frequency: {1}".format(tup[0], tup[1]))


def mode(data):
    # returns the value in the data that appears the most
    f = frequencies(data)
    # tests to see if *one* value appears most often
    if f[0][1] > f[1][1]:
        return f[0][0]
    else:
        raise StatisticsError("This data contains no single mode")


