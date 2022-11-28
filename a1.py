import os
import argparse
import re



# create variables that can be entered in the command line

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=str, metavar='C:\Users\Gautham's PC\Gauri\Downloads\Assessment\file_pairA_1.tsv', required=True)

parser.add_argument('-o', type=str, metavar='C:\Users\Gautham's PC\Gauri\Downloads\Assessment\file_pairA_2.tsv', required=True)



file_pairA_1, file_pairA_2



with open(file_pairA_1, 'r') as A_1, open(file_pairA_2, 'w') as A_2:    

    for line in A_1:

        if line:

            Scaffold, Position, Ref_Allele_Count, Alt_Allele_Count, Coverage_Depth, Alt_Allele_Frequency 

            A_3 = [ sum(A_1[3,4,5],A_2[3,4,5]) if 'A_1[2]==A_2[2]']


            print(Scaffold, Position, Ref_Allele_Count, Alt_Allele_Count, Coverage_Depth, Alt_Allele_Frequency)
            


