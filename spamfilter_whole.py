import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

'''
This is almost exact copy of spamfilter_sample
Changed arrays' indexes to fit
Added LinearSVC model to test it
'''



#TRAINING PART

emails = [os.path.join("train-mails-ling", f) for f in os.listdir("train-mails-ling")]
all_docs = []


for mail in emails:
    with open(mail, "rt") as myFile:
        all_docs += [myFile.readlines()[2]] #body of mail is 3rd line of each .txt file


vectorizer = TfidfVectorizer()
representation = vectorizer.fit(all_docs)
train_features = vectorizer.transform(all_docs)
train_labels = np.zeros(7636)
train_labels[6367:7636]=1

model1 = MultinomialNB()
model2 = LinearSVC()
model1.fit(train_features, train_labels)
model2.fit(train_features, train_labels)


##TESTING PART


test_emails = [os.path.join("test-mails-ling", f) for f in os.listdir("test-mails-ling")]
test_docs = []

for mail in test_emails:
    with open(mail, "rt") as myFile:
        test_docs += [myFile.readlines()[2]] #body of mail is 3rd line of each .txt file

test_features =  vectorizer.transform(test_docs)
test_labels = np.zeros(3936)
test_labels[3281:318]=1

result1 = model1.predict(test_features)
result2 = model2.predict(test_features)
counter1 = 0
counter2 = 0

for i in range(len(test_labels)):
    if test_labels[i] == result1[i]:
        counter1 += 1
    if test_labels[i] == result2[i]:
        counter2 += 1

print("Precision of prediction for MultinomialNB is {0:.2f} percent".format(counter1/len(test_labels)*100))
print("Precision of prediction for LinearSVC is {0:.2f} percent".format(counter2/len(test_labels)*100))