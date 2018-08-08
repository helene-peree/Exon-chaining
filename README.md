# Exon chaining
## Hélène Perée

**Assignment for my master in Bioinformatics and Modelling (ULB)**

**Course**: Algorithms in computational biology (2016-2017)

### Programming language
Python 3 (no libraries)

### Application in biology
Exon chaining enables to predict which putative exons among several ones are indeed exons. Exons do not overlap in genes. They are here characterized by left and right end positions as well as by a local alignment score (= weight).

### Input
- Several intervals (composed of a left end > 0 and of a right end > left end) in an increasing order
- The same number of weights (they are assumed to be positive)

### Output
Printing of:
- the maximum total weight obtained by combination of disjoint/nonoverlapping intervals (= independent sets)
- the intervals in this set

### Algorithm (dynamic programming)
The algorithm uses an interval graph: it is implemented as a dictionary where the keys are the positions ranging from 1 to the maximum right end and the values are the total weight at each position.

The maximum total weight corresponds to the total weight at the last position. The intervals used to obtain this maximum total weight are found thanks to a backtracking in the interval graph.

### Example 1
Input:
- Intervals: (1,5), (3,9), (4,10), (7,13), (10,17), (11,16), (14,19), (17,19)
- Weights: 4, 3, 3, 6, 10, 2, 1, 8

Output:
- Maximum total weight: 22
- Intervals used: [(1, 5), (10, 17), (17, 19)]

### Example 2
Input:
- Intervals: (1,5), (2,3), (4,8), (6,12), (7,17), (9,10), (11,15), (13,14), (16,18)
- Weights: 5, 3, 6, 10, 12, 1, 7, 0, 4

Output:
- Maximum total weight: 21
- Intervals used: [(2, 3), (4, 8), (9, 10), (11, 15), (16, 18)]


### Source
N. C. Jones and A. Pevzner, "Introduction to Bioinformatics Algorithms", Chapter 6, Sections 6.13 and 6.14
