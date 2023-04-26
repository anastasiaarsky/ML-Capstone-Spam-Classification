# ML Capstone

## Description

Spam is unwanted and unsolicited messages sent electronically. These spam messages often have malicious intent, and range from misleading advertising to phishing and malware spreads. Thus, spam is detrimental to both users and services, and creates mistrust and wariness between the two parties. 

Furthermore, spam is rapidly on the rise, with the Federal Trade Commision reporting $8.8 billion in total reported losses in 2022, compared to the $6.1 billion in 2021 and the mere $1.2 billion in 2020 ([FTC.gov](https://www.ftc.gov/business-guidance/blog/2023/02/ftc-crunches-2022-numbers-see-where-scammers-continue-crunch-consumers)). Therefore, it is increasingly important for companies and services to detect and filter spam messages. 

My capstone project aims to create an ML model that is capable of detecting spam email messages.  

## Data

[Data.csv](https://github.com/anastasiaarsky/ML_Capstone/blob/main/Data.csv) includes 39,513 entries, with 20,445 labeled as ham and 19,068 as spam. 
The dataset contains the following columns:
| Column      | Description |
| ----------- | ----------- |
| **Subject**      | The subject line of the email        |
| **Message**   | The content of the e-mail. Can contain an empty string if the message had only a subject line and no body. In case of forwarded emails or replies, this also contains the original message with subject line, "from:", "to:", etc.        |
| **Label**   | Whether the email was spam (1) or not (0)          |
 
This dataset is made up of two premade datasets: 
- [SpamAssassin dataset](https://spamassassin.apache.org/old/publiccorpus/)
- [Enron Spam dataset](https://www2.aueb.gr/users/ion/data/enron-spam/)   

Further details about these two datasets can be found at: [DataCollection.md](https://github.com/anastasiaarsky/ML_Capstone/blob/main/DataCollection.md).

[DataCollection.py](https://github.com/anastasiaarsky/ML_Capstone/blob/main/DataCollection.py) contains the script for processing the SpamAssassin dataset, as well as merging it with the Enron Spam dataset before outputting it as Data.csv.   

## Credits

TO-DO
