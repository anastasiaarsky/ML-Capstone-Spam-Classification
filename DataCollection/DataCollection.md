### 1. Datasets Explored

*Note: the "ham" label means that the message was legitimate*.  

There are a couple publicly available Spam Email datasets:

##### i. [Enron Spam dataset](https://www2.aueb.gr/users/ion/data/enron-spam/)
This dataset contains the raw text of emails (including the their headers), along with the date of the email. The labels are determined by the directory that the file is contained in (ham/spam). There are a total of 33,716 messages, with 16,545 labeled as ham and 17,171 labeled as spam. 

The original dataset is structured so that each email is contained in a separate text file, and distributed across multiple directories. For this reason, I have chosen to download the Enron Spam data as a CSV file from [MWiechmann's GitHub repository](https://github.com/MWiechmann/enron_spam_data).

##### ii. [SpamAssassin dataset](https://spamassassin.apache.org/old/publiccorpus/)
This dataset contains the raw text, like the Enron dataset. And just like the Enron dataset, the SpamAssassin dataset contains multiple directories, each containing the raw text files:  
-`easy-ham-1`: easier to detect non-spam e-mails (2500 messages)   
-`easy-ham-2`: easier to detect non-spam e-mails collected at a later date (1400 messages)  
-`hard-ham-1`: harder to detect non-spam e-mails (250 messages)   
-`spam-1`: spam e-mails (500 messages)    
-`spam-2`: spam e-mails collected at a later date (1397 messages)  
There are a total of 6,047 messages, with 4,150 labeled as ham and 1,897 labeled as spam. 

I was able to find the dataset (excluding `hard-ham-1`) as a CSV file online at [Kaggle](https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset). However, if I want to use the complete dataset, so I will need to write a script to process the raw data. This [notebook](https://www.kaggle.com/code/cesaber/getting-started-in-spam-classification?scriptVersionId=122108078) will guide me in converting the raw SpamAssassin files to CSV files.

##### iii. [Spambase dataset](https://archive.ics.uci.edu/ml/datasets/spambase)
Unlike the other two datasets, the Spambase data is contained in a single file and does not include the raw text of the messages. Instead, most of the attributes indicate whether a particular word or character was frequently occurring in the e-mail. There are 4,601 total messages, with 2,788 labeled as ham and 1,813 labeled as spam.  
I will not be using the data set as I prefer the ones that actually contain the raw text. 


### 2. Code for Data Collection

My code can be found at DataCollection.py.  

What it does: 
1. Processes the raw data from the [SpamAssassin dataset](https://spamassassin.apache.org/old/publiccorpus/) into a pandas dataframe
2. Updates the SpamAssassin dataframe to include the Enron Spam data from [MWiechmann's GitHub repository](https://github.com/MWiechmann/enron_spam_data)
3. Ouputs a CSV file of the merged data

### 3. Actual Dataset

The final dataset I will use will be the Enron Spam dataset merged with the Spam Assassin dataset. It can be found in the Data.csv file.
