import pandas as pd
import numpy as np
import os
from email.parser import BytesParser
from email.policy import default

# Part 1: process SpamAssassin data
# Initialize paths
ham_path = '/Users/anastasiaarsky/PycharmProjects/ML_Capstone/CapstoneData/SpamAssassin/ham/easy_ham/'
hard_ham_path = '/Users/anastasiaarsky/PycharmProjects/ML_Capstone/CapstoneData/SpamAssassin/ham/hard_ham/'
spam_path = '/Users/anastasiaarsky/PycharmProjects/ML_Capstone/CapstoneData/SpamAssassin/spam/'


# Given path and a boolean that determines whether the data is ham or spam,
# reads the raw email data and returns a dataframe
def read_emails(path, spam):
    files = os.listdir(path)
    df = pd.DataFrame(columns=['Subject', 'Message', 'Label'])
    for i in range(len(files)):
        with open(path + files[i], 'rb') as content:
            cont = content.read()
            subject = BytesParser(policy=default).parsebytes(cont)['Subject']
            message = BytesParser(policy=default).parsebytes(cont).get_payload()
        content.close()
        if spam:
            df.loc[len(df.index)] = [subject, message, 1]
        else:
            df.loc[len(df.index)] = [subject, message, 0]
    return df


# Create dataframes using the read_emails() method for the (easy) ham emails,
# the hard ham emails, and the spam emails
ham_df = read_emails(ham_path, False)
hard_ham_df = read_emails(hard_ham_path, False)
spam_df = read_emails(spam_path, True)
print(len(ham_df), 3900)
print(len(hard_ham_df), 250)
print(len(spam_df), 1897)

# Concatenate the previous dataframes:
# data = ham_df, spam_df
# full_data = ham_df, spam_df, hard_ham_df
data = pd.concat([ham_df, spam_df], axis=0, ignore_index=True)
full_data = pd.concat([data, hard_ham_df], axis=0, ignore_index=True)
print(len(data), 5797)
print(len(full_data), 6047)

# Part 2: Merge with Enron Spam data

# load enron csv
enron_df = pd.read_csv('/Users/anastasiaarsky/PycharmProjects/ML_Capstone/CapstoneData/enron_spam_data.csv')

# standardize the Enron data to match the SpamAssassin data
enron_df.rename(columns={'Spam/Ham': 'Label'}, inplace=True)
enron_df['Label'] = enron_df['Label'].map({'spam': 1.0, 'ham': 0.0})
enron_df = enron_df.drop(columns=['Message ID', 'Date'])
print(len(enron_df), 33716)


# Concatenate the SpamAssassin df to the enron dataframe
data = pd.concat([data, enron_df], axis=0, ignore_index=True)
print(len(data), 39513)
full_data = pd.concat([full_data, enron_df], axis=0, ignore_index=True)
print(len(full_data), 39763)

# Step 3: Output to CSV file

# Data.csv contain all data except hard_spam
# Full_data.csv contains all data
data.to_csv('Data.csv', index=False)
full_data.to_csv('Full_data.csv', index=False)
