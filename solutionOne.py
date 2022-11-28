import pandas as pd
import argparse
import json


def read_data(filename):
    return pd.read_csv("data_files/"+filename, sep='\t')


def arguments_required():
    """
    The user input the files to be merged (assuming if there are more than 2 files in the location and
    user wants to try with different files sometimes).
    :return:
    """
    parser = argparse.ArgumentParser(description="Merge the two files passed as arguments in double quotes.")
    parser.add_argument("file1", type=str)
    parser.add_argument("file2", type=str)
    args = parser.parse_args()

    print(args)
    solution3(args.file1, args.file2)


def solution():
    """
    failed one. Cannot make it work.
    :return:
    """
    file1 = read_data(r"data_files/file_pairA_1.tsv")
    file2 = read_data(r"data_files/file_pairA_2.tsv")

    # print(file1)
    # print(file2)

    df_merged = file1.loc[:, file1.columns.drop(['Ref_Allele_Count', 'Alt_Allele_Count',
                                                 'Coverage_Depth', 'Alt_Allele_Frequency'])]
    df_merged.assign(Ref_Allele_Count=file1.Ref_Allele_Count.add(file2.Ref_Allele_Count).
                     where(file1.Position.eq(file2.Position)))
    df_merged.assign(Alt_Allele_Count=file1.Alt_Allele_Count.add(file2.Alt_Allele_Count).
                     where(file1.Position.eq(file2.Position)))
    df_merged.assign(Coverage_Depth=file1.Coverage_Depth.add(file2.Coverage_Depth).
                     where(file1.Position.eq(file2.Position), inplace=True))
    # df_merged['Alt_Allele_Frequency'] = df_merged['Alt_Allele_Count']/df_merged['Coverage_depth']
    # df_merged.assign(Alt_Allele_Frequency=df_merged.Alt_Allele_Count.div(df_merged.Coverage_Depth).
    #                where(file1.Position.eq(file2.Position)))

    # df.assign(math=df.col3.add(10).where(df.col1.eq('B')))
    print(df_merged)


def solution2():
    """
    Here I am not able to put any condition based on which the Count and Coverage_depth values are calculated
    :return:
    """
    file1 = read_data(r"data_files/file_pairA_1.tsv")
    file2 = read_data(r"data_files/file_pairA_2.tsv")

    df_merged = file1.loc[:, file1.columns.drop(['Ref_Allele_Count', 'Alt_Allele_Count',
                                                 'Coverage_Depth', 'Alt_Allele_Frequency'])]

    df_merged.insert(2, "Ref_Allele_Count", (file1.Ref_Allele_Count.add(file2.Ref_Allele_Count)))
    df_merged.insert(3, "Alt_Allele_Count", (file1.Alt_Allele_Count.add(file2.Alt_Allele_Count)))
    df_merged.insert(4, "Coverage_Depth", (file1.Coverage_Depth.add(file2.Coverage_Depth)))
    df_merged.assign(Alt_Allele_Frequency=lambda x: x.Alt_Allele_Count / x.Coverage_Depth)

    print(df_merged)


def solution3(filename1, filename2):
    """
    This seems to be correct. You do the merge based on the columns - Scaffold and Position.
    Then do the changes on the merged dataframe.
    :return:
    """
    file1 = read_data(filename1)
    file2 = read_data(filename2)  # read_data(r"file_pairA_2.tsv")

    df_merged = file1.merge(file2, how='inner', on=['Position', 'Scaffold'])
    print(df_merged.columns)

    df_merged.insert(2, "Ref_Allele_Count", (df_merged.Ref_Allele_Count_x.add(df_merged.Ref_Allele_Count_y)))
    df_merged.insert(3, "Alt_Allele_Count", (df_merged.Alt_Allele_Count_x.add(df_merged.Alt_Allele_Count_y)))
    df_merged.insert(4, "Coverage_Depth", (df_merged.Coverage_Depth_x.add(df_merged.Coverage_Depth_y)))

    df_merged.insert(5, "Alt_Allele_Frequency", (df_merged.Alt_Allele_Count.div(df_merged.Coverage_Depth)))

    df_merged.drop(labels=['Ref_Allele_Count_x', 'Alt_Allele_Count_x', 'Coverage_Depth_x', 'Alt_Allele_Frequency_x',
                           'Ref_Allele_Count_y', 'Alt_Allele_Count_y', 'Coverage_Depth_y', 'Alt_Allele_Frequency_y'],
                   inplace=True, axis=1)

    print(df_merged.head())


if __name__ == '__main__':
    # solution()
    # solution2()
    # solution3()
    arguments_required()
