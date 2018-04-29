# spamfilter
Spam filtering algorithm using python scikit

**Dataset source:** http://www.aueb.gr/users/ion/data/lingspam_public.tar.gz  

**Spamfilter for sample**:  
I've sampled 962 mails, spam:ham ratio is 1:1  
About 66% (644) mails are training set, the rest (314) will be used for testing  
I've preprocessed the sample data manually   
Mails directories are in .rar due to upload limits 
Predicting models used: MultinomialNB  
Achieved precision for this sample: over 96%  
  
**Spamfilter for whole dataset**:  
I've used whole dataset, 66% for training and 33% for testing  
Spam:ham ratio is the same for training and testing part of set  
Predicting models used: MultinomialNB and LinearSVC  
Achieved precision for this dataset: over 93% for MultinomialNB and over 80% for LinearSVC
  
**Instructions for spamfilter_sample.py:**  
- unpack .rar files  
- run the script  
  
 **Instructions for spamfilter_whole.py:**  
- use preprocess.py  
- run the script  
  
**Instructions for preprocess.py:**  
- download the dataset  
- unpack it directly in script directory  
- run the script
