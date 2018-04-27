import os
import shutil
import re

'''
DATASET SOURCE: http://www.aueb.gr/users/ion/data/lingspam_public.tar.gz
Dataset unpacked consists of 4 main directories: bare, lemm, lemm_stop, stop
Each main directory has subdirectories filled with mails (one .txt file per mail)
Filenames are duplicate among main directories
'''




#function sorting array elements in alphanumeric order

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

#moving all mails from all subdirectories to new directory "allmails/"
mail_dirs = ["bare", "lemm", "lemm_stop", "stop"]
main_dir = "lingspam_public"
os.makedirs("allmails")

for d in mail_dirs:
    for sd in sorted_alphanumeric(os.listdir(os.path.join(main_dir,d))):
        for mf in sorted_alphanumeric(os.listdir(os.path.join(main_dir,d,sd))):
            shutil.move(os.path.join(main_dir,d,sd,mf), "allmails/"+mf+d+".txt") #making .txt files' names unique

#dividing dataset for train and test sets
#i want to have same ham:spam ratio in train and test set
#i've chosen the ratio 2:1
ham_count = 0
spam_count = 0
for ml in os.listdir("allmails"):
    if ml[0].isnumeric():
        ham_count += 1
    else:
        spam_count += 1

ham_index = int(0.66*ham_count)
spam_index = int(0.66*spam_count)

train_ham = sorted_alphanumeric(os.listdir("allmails"))[0:ham_index] #names of train ham mails
train_spam = sorted_alphanumeric(os.listdir("allmails"))[-1-spam_index:-1] #names of train spam mails

os.makedir("train-mails-ling") #creating directory for training mails
for r in train_ham:
    shutil.move("allmails/"+r, "train-mails-ling")

for q in train_spam:
    shutil.move("allmails/"+q, "train-mails-ling")

os.rename("allmails", "test-mails-ling") #test mails are remaining in allmails directory so i only have to change its name
