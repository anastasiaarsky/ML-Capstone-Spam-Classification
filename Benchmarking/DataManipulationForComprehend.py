import pandas as pd


# reformatForComprehend method: given the path to the CSV file and the name for the new CSV,
# generates a new CSV file with two columns total, where the first column is the label and
# the second is the email subject line and message
def reformatForComprehend(path, filename):
    df = pd.read_csv(path)
    df["FullMessage"] = df['Subject'].astype(str) + " " + df["Message"]

    neworder = ['Label', 'FullMessage']
    df = df.reindex(columns=neworder)
    df.to_csv(filename, index=False, header=False)


# reformat Data.csv and export to ComprehendData.csv
reformatForComprehend('/Users/anastasiaarsky/PycharmProjects/ML_Capstone/DataCollection/Data.csv', 'ComprehendData.csv')

# reformat Full_data.csv and export to ComprehendFullData.csv
reformatForComprehend('/Users/anastasiaarsky/PycharmProjects/ML_Capstone/DataCollection/Full_data.csv', 'ComprehendFullData.csv')
