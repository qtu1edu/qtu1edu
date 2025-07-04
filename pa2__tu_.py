# -*- coding: utf-8 -*-
"""PA2-<Tu>

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jnTI3bdrbum_-wAWhOvtQ1UOKuANk1KB
"""

'''
@filename: PA2
@authors: Qianxun Tu
@description: the program finds the most common substring in file
initial6000.txt. The function takes the set sequence string and an k and finds
the k-letter sequence that occurs most frequently in the given length and
number of times.
@date: 10/29/23
@version: 1.00
'''

from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/My Drive/initial6000.txt'

# Open the file and read its contents
with open(file_path) as f:
    dna = f.read()

# Function to find the highest occurring sequence of length k in a string
def find_highest_occurrence(string, k):
    sequences = {}
    for i in range(len(string) - k + 1):
        sequence = string[i:i+k]
        if sequence in sequences:
            sequences[sequence] += 1
        else:
            sequences[sequence] = 1
    highest_sequence = max(sequences, key=sequences.get)
    highest_count = sequences[highest_sequence]
    return highest_sequence, highest_count

# Function to find the highest occurring sequence within a range of lengths
def find_highest_occurrence_range(string, min_length, max_length):
    highest_sequence = ''
    highest_count = 0
    for k in range(min_length, max_length + 1):
        sequence, count = find_highest_occurrence(string, k)
        print(f"For k={k}, the highest occurring sequence is '{sequence}' with a count of {count}.")
        if count > highest_count:
            highest_sequence = sequence
            highest_count = count
    return highest_sequence, highest_count

# Specify the range of k values you're interested in
min_length = 2
max_length = 8

# Find the highest occurring sequence within the specified range and print results for each k
highest_sequence, highest_count = find_highest_occurrence_range(dna, min_length, max_length)

# Print the overall highest occurring sequence
print(f"\nThe overall highest occurring sequence is '{highest_sequence}' with a count of {highest_count}.")