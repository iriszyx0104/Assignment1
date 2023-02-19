import pandas as pd


def clean(input_file1,input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    merged_table = pd.merge(df1,df2,left_on="respondent_id", right_on="id").drop('id', axis=1)
    drop1 = merged_table.dropna()
    drop2 = drop1[~(drop1['job'].str.contains("insurance|Insurance"))]
    return drop2


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Data file (CSV)')
    parser.add_argument('other_info_file', help='Data file (CSV)')
    parser.add_argument('output_file', help='Cleaned data file (CSV)')
    args = parser.parse_args()
    cleaned = clean(args.contact_info_file, args.other_info_file)
    print(cleaned.shape)
    cleaned.to_csv(args.output_file, index=False)