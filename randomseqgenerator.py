'''
05/04/2018
Python script to generate a random string of DNA sequences
'''
import random
import sys
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Generate a random DNA sequence')

# Required positional argument
parser.add_argument('seq_arg', type=int,
                    help='A required integer argument stating the length of sequence required')
parser.add_argument('output_fa', type=str,
                    help='Fasta output file')

# Parse arguments
args = parser.parse_args()


# Function that takes the length of sequence as input and uses the random function to randomly choose A, C, G or T for the length of the sequence
def generate_string(N, alphabet='ACGT'):
    return ''.join([random.choice(alphabet) for i in xrange(N)])

# Takes the sequence length as input from the command line and passes it as an argument to the generate_string function 
dna = generate_string(args.seq_arg)

# File output takes the second input argument as the filename to write sequence
fileOutput = open(args.output_fa, "w")
# Inserts the header for the sequence also including sequence length and writes out sequence
fileOutput.write(">" + "random sequence" + "| " + str(len(dna)) + " bp" + "\n")
fileOutput.write(dna + "\n")
# Close file
fileOutput.close()


