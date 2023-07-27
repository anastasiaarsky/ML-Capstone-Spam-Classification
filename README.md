# ML Capstone

## Description

Spam is unwanted and unsolicited messages sent electronically. These spam messages often have malicious intent, and range from misleading advertising to phishing and malware spreads. Thus, spam is detrimental to both users and services, and creates mistrust and wariness between the two parties. 

Furthermore, spam is rapidly on the rise, with the Federal Trade Commision reporting $8.8 billion in total reported losses in 2022, compared to the $6.1 billion in 2021 and the mere $1.2 billion in 2020 ([FTC.gov](https://www.ftc.gov/business-guidance/blog/2023/02/ftc-crunches-2022-numbers-see-where-scammers-continue-crunch-consumers)). Therefore, it is increasingly important for companies and services to detect and filter spam messages. 

My capstone project aims to create an *ML model that is capable of detecting spam email messages*. 

My full project proposal can be found at: [ProjectProposal.pdf](https://github.com/anastasiaarsky/ML_Capstone/blob/main/ProjectProposal.pdf).

## Data

[FullData.csv](https://github.com/anastasiaarsky/ML_Capstone/blob/main/FullData.csv.zip) includes 39,763 entries, with 20,695 labeled as ham and 19,068 as spam.    
The dataset contains the following columns:
| Column      | Description |
| ----------- | ----------- |
| **Subject**      | The subject line of the email        |
| **Message**   | The content of the e-mail. Can contain an empty string if the message had only a subject line and no body. In case of forwarded emails or replies, this also contains the original message with subject line, "from:", "to:", etc.        |
| **Label**   | Whether the email was spam (1) or not (0)          |
 
This dataset is made up of two premade datasets: 
- [SpamAssassin dataset](https://spamassassin.apache.org/old/publiccorpus/)
- [Enron Spam dataset](https://www2.aueb.gr/users/ion/data/enron-spam/)   

Further details about these two datasets can be found at: [DataCollection.md](https://github.com/anastasiaarsky/ML_Capstone/blob/main/DataCollection/DataCollection.md).

[DataCollection.py](https://github.com/anastasiaarsky/ML_Capstone/blob/main/DataCollection/DataCollection.py) contains the script for processing the SpamAssassin dataset, as well as merging it with the Enron Spam dataset before outputting it as Data.csv.   

## Model Benchmarking

I created a Custom Classifier Model in Amazon Comprehend in order to benchmark my model. After training, the model had an accuracy score of 0.99+ as well as an F1 score of 0.99+. 

Further details can be found at: [ComprehendResults.md](https://github.com/anastasiaarsky/ML_Capstone/blob/main/Benchmarking/ComprehendResults.md).

## Data Wrangling & Exploration

**Data Wrangling:**

I first concatenated the Subject and Message columns of my data into a single column. 

Next, my text preprocessing/normalization process was as follows:
1. Transform each token to lower case
2. Replace URLs with the string 'URL'
3. Replace emails with the string 'email'
4. Replace numbers with the string 'number'
5. Remove any extra newlines or whitespace
6. Remove stopwords
7. Remove non-ASCII characters

I chose not to remove punctuation as I believed it to be important in the detection of Spam emails.

**Data exploration:**

The key takeways were as follows:
1. My dataset was fairly balanced: 52% ham to 48% spam.
2. The most common tokens were numbers, punctuation, and emails as well as the words 'enron' , 'ect', 'company', and 'subject'.  
a. Ham emails commonly featured emails and the words 'enron', 'subject', 'ect', and 'energy'.   
b. Spam emails commonly featured urls and the words 'company', 'information', and 'font'.  
3. The average email length was around 201 tokens, but the longest email contained 28,624 tokens.


The Jupyter Notebook for this phase can be found here: [DataWrangling&Exploration.ipynb](https://github.com/anastasiaarsky/ML_Capstone/blob/main/DataWrangling%26Exploration.ipynb)

## Reproduction of Available Solutions

