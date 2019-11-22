""" Coverage Caluclator by Abhinaya Nakka

Input Parameters:
    reads.csv (This file contains approximately 2 million reads, one read per row, with two columns corresponding to the
start position and length of the read.)
    loci.csv (This file contains 1000 positions of interest and a blank "coverage" column.)

Procedure:
    The data from reads.csv is populated into a dictionary of dictionaries.
    While the data is being read in, it takes into account different read lengths at the same start positions,
    and multiple occurences of it.
    The maximum read length is also calculated.
    The start positions (referred to as read_keys) are populated in a list.
    The read_keys_list is further sorted.
    For a particular locus of interest, to calculate the coverage:
        Firstly, the start_loci_key_index in the sorted read_keys_list is calculated.
        This is done to identify the short range in which the read keys need to be checked, to identify coverage.
        The reads which fall in the range (locus - max_read_length, locus + max+read_length) are identified as
        the subset of focus.
        The reads which fall in that subset are then identified, and coverage is calculated,
        by iterating through the list of reads and their corresponding read lengths,
        while checking if they enclose the locus.

Output:
    The coverage of the loci is populated in loci.csv

"""

import os
import bisect
import csv


def get_data_in_dictionary(reads_data):
    """
    The data from reads.csv is populated into a dictionary of dictionaries

    Args:
        reads_data(list of strings): The raw data read from reads.csv serves as the input.
        The first row of the data is a header, which is excluded while populating the dictionary.

    Returns:
        max_read_length(int) : Gives the maximum read length of all the reads in read.csv
        Reads(dict) :  A dictionary of dictionaries populated with main keys as the start positions,
        and subkeys as the length and subvalues as the number of occurences of that length.
    eq: A ={1250: {130: 1}, 1340: {120: 1}, 1560: {180: 1}, 1690: {160: 2, 150: 1}}
    [1250, 1340, 1560, 1690] - start positions
    [130, 120, 180, 160] - length of the read
    1690: {160: 2, 150: 1} -signifies at start position 1690, there are 2 read length od 160 and 1 read length of 150
    """

    reads = {}
    max_read_length = 1
    for line_index in range(1, len(reads_data)):
        read_start = int(reads_data[line_index].split(',')[0])
        read_length = int(reads_data[line_index].split(',')[1].rstrip('\n'))
        if read_length > max_read_length:
            max_read_length = read_length
        if read_start in reads:  # checking for key in Reads dict
            if read_length in reads[read_start]:
                reads[read_start][read_length] += 1
            else:
                reads[read_start][read_length] = 1
        else:
            reads[read_start] = {}
            reads[read_start][read_length] = 1
    return max_read_length, reads


def get_start_loci_key_index(loci_key, read_key_list, max_read_length):
    """
    Finds the first start_loci_key_index to figure out the subset of keys to be read, as per the locus

    Args:
        loci_key(int) : Value of the locus read from loci.csv
        read_key_list (list) : sorted read_key_list with the start positions sorted.
        max_read_length(int) : Maximum read length of all the reads.

    Returns:
        start_loci_index(int): start position of the subset range
    """
    loci_min_range = loci_key - max_read_length
    start_loci_index = bisect.bisect_right(read_key_list, loci_min_range)
    return start_loci_index


def get_narrowed_read_keys(loci_key, read_key_list, start_loci_index, max_read_length):
    """
    Get the subset of read keys which fall in the range (locus - max_read_length, locus + max+read_length)

    Args:
        loci_key(int) : Value of the locus read from loci.csv
        read_key_list (list) : sorted read_key_list with the start positions sorted.
        start_loci_index(int): start position of the subset range
        max_read_length(int) : Maximum read length of all the reads.

    Returns:
        loci_keys_list(list): A list of the subset of reads of interest
    """
    loci_keys_list = []
    while read_key_list[start_loci_index] <= (loci_key + max_read_length):
        loci_keys_list.append(read_key_list[start_loci_index])
        start_loci_index += 1
    return loci_keys_list


def get_coverage(loci_key, loci_keys_list, Reads):
    """
    Gets the coverage of a particular locus of focus

    Args:
        loci_key(int) : Value of the locus read from loci.csv
        loci_keys_list(list): A list of the subset of reads of interest
        Reads(dict) :  A dictionary of dictionaries populated with main keys as the start positions,
        and subkeys as the length and subvalues as the number of occurences of that length.

    Returns:
        coverage(int) : Coverage of a particular locus
    """
    key_coverage = 0
    for key in loci_keys_list:
        for read_value in Reads[key].keys():
            if key <= loci_key and (key + read_value) > loci_key:
                key_coverage += Reads[key][read_value]
    return key_coverage


if __name__ == '__main__':

    # Reading the data from reads.csv
    dirpath = os.getcwd()

    with open(f'{dirpath}/reads.csv', 'r') as file:
        reads_data = file.readlines()

    # Setting up the data in a dictionary of dictionaries
    max_read_length, Reads = get_data_in_dictionary(reads_data)

    # Finding the list of start positions
    read_key_list = list(Reads.keys())

    # Sorted the list as per the keys in increasing order
    read_key_list.sort()

    # Reading loci from loci.csv
    with open(f'{dirpath}/loci.csv', 'r') as file:
        loci_data = file.readlines()

    # Adding the header to loci.csv
    with open(f'{dirpath}/loci.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['start', 'length'])

        # Started the index from 1 as the first line is the header
        for line_index in range(1, len(loci_data)):

            loci_key = int(loci_data[line_index].split(',')[0])

            start_loci_index = get_start_loci_key_index(loci_key, read_key_list, max_read_length)

            loci_keys_list = get_narrowed_read_keys(loci_key, read_key_list, start_loci_index, max_read_length)

            coverage = get_coverage(loci_key, loci_keys_list, Reads)

            writer.writerow([loci_key, coverage])
