# spamfilter
Spam filtering algorithm using python scikit

**Dataset source:** http://www.aueb.gr/users/ion/data/lingspam_public.tar.gz  
I've sampled 962 mails, spam:ham ratio is 1:1  
About 66% (644) mails are training set, the rest (314) will be used for testing  
I've preprocessed the sample data manually   
Mails directories are in .rar due to upload limits  
Achieved precision for this sample: over 96%  
  
**Instructions for spamfilter.py:**  
- unpack .rar files  
- run the script  
  
**To-do list:**  
[+] automatize preprocessing  
[+] import mails' bodies  
[+] create feature matrix for training  
[+] create MultinomialNB model  
[+] test the algorithm  
[-] improve the code  
[-] create algorithm for bigger number of mails  
