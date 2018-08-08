"""
Exon chaining

Author: Hélène Perée

Last modified date: 02/08/18

Python 3 (no libraries)
"""

def importIntervals():
    """
    :return: the intervals (list of tuples).
    """
    raw = input("Enter the intervals: ")
    raw = raw.replace("(", "").replace(")", "")
    raw = raw.split(",")
    
    intervals = []
    for k in range(0, len(raw), 2):
        step = (int(raw[k])), int(raw[k+1]) # creation of the tuples
        intervals.append(step)

    return intervals


def importWeights():
    """
    :return: the weights (list of integers).
    """
    weights = input("\n" + "Enter the weights: ")
    weights = weights.split(",")
    
    for k in range(len(weights)):
        weights[k] = int(weights[k])

    return weights


def computeMax(intervals, length):
    """
    :return: the maximum right end among all intervals (int).
    """
    maximum = 1
    for k in range(length):
        if intervals[k][1] > maximum:
            maximum = intervals[k][1]

    return maximum


def computeGraph(intervals, length, weights, maximum):
    """
    This function creates the interval graph dictionary: the keys are the positions
    ranging from 1 to the maximum right end and the values are the total weight
    at each position.
    
    :return: the interval graph (dict)
    """
    graph = {1: 0} # initialization of the graph
    for vertex in range(2,maximum+1): # index shift because Python starts at 0
        graph[vertex] = graph[vertex-1]

        for k in range(length):
            if vertex == intervals[k][1] and weights[k] != 0:
                # the vertex is updated when it corresponds to a right end
                graph[vertex] = max(graph[intervals[k][0]] + weights[k], graph[vertex-1])

    return graph


def findIntervals(intervals, length, weights, maximum, graph):
    """
    This function finds which intervals were used to obtain the maximum total
    weight (thanks to a backtracking in the interval graph).
    
    :return: the list of intervals used (list of tuples)
    """
    intervals_used = []
    vertex = maximum
    while vertex > 1:
        for k in range(length):
            if vertex == intervals[k][1] and weights[k] != 0 \
               and graph[vertex] == graph[intervals[k][0]] + weights[k]:
                intervals_used.insert(0, intervals[k]) # insertion at the beginning
                vertex = intervals[k][0] + 1 # +1 because of adjacent intervals
        vertex -= 1
        
    return intervals_used


def printOutput(intervals, length, weights):
    """
    This function prints the maximum total weight and the intervals used to
    obtain this maximum total weight.
    """
    maximum = computeMax(intervals, length)
    graph = computeGraph(intervals, length, weights, maximum)
    print("\n" + "Maximum total weight: ", graph[maximum])
    
    intervals_used = findIntervals(intervals, length, weights, maximum, graph)
    print("\n" + "Intervals used: ", intervals_used)


i = importIntervals()

l = len(i)

w = importWeights()

if l == len(w):
    printOutput(i, l, w)

else:
    print("\n" + "The number of intervals and weights is different, please try again.")
