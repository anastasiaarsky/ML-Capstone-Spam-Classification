# ML Capstone

## Description

Spam is unwanted and unsolicited messages sent electronically. These spam messages often have malicious intent, and range from misleading advertising to phishing and malware spreads. Thus, spam is detrimental to both users and services, and creates mistrust and wariness between the two parties. 

Furthermore, spam is rapidly on the rise, with the Federal Trade Commision reporting $8.8 billion in total reported losses in 2022, compared to the $6.1 billion in 2021 and the mere $1.2 billion in 2020 ([FTC.gov](https://www.ftc.gov/business-guidance/blog/2023/02/ftc-crunches-2022-numbers-see-where-scammers-continue-crunch-consumers)). Therefore, it is increasingly important for companies and services to detect and filter spam messages. 

My capstone project aims to create an ML model that is capable of detecting spam email messages.  

## Data

Data.csv contains two premade datasets: 
- [SpamAssassin dataset](https://spamassassin.apache.org/old/publiccorpus/)
- [Enron Spam dataset](https://www2.aueb.gr/users/ion/data/enron-spam/)   

Further dataset details can be found at: [DataCollection.md](https://github.com/anastasiaarsky/ML_Capstone/blob/main/DataCollection.md).

The SpamAssassin dataset was intitailly structured so that each email was contained in a separate text file and distributed across multiple directories, so it had to first be processed for use. The Enron Spam dataset was structured similarly to the SpamAssassin dataset, but I was able to save some time by finding an already-processed CSV version of the data at [MWiechmann's GitHub repository](https://github.com/MWiechmann/enron_spam_data).

[DataCollection.py](https://github.com/anastasiaarsky/ML_Capstone/blob/main/DataCollection.py) contains the script for processing the SpamAssassin dataset, as well as merging it with the Enron Spam dataset before outputting it as Data.csv. 

## Credits

TO-DO
