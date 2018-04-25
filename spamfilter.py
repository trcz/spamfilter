import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#TRAINING PART

emails = [os.path.join("train-mails", f) for f in os.listdir("train-mails")]
all_docs = []


for mail in emails:
    with open(mail, "rt") as myFile:
        all_docs += [myFile.readlines()[2]] #body of mail is 3rd line of each .txt file


vectorizer = TfidfVectorizer()
representation = vectorizer.fit(all_docs)
train_features = vectorizer.transform(all_docs)
train_labels = np.zeros(644)
train_labels[322:644]=1

model1 = MultinomialNB()
model1.fit(train_features, train_labels)


##TESTING PART


test_emails = [os.path.join("test-mails", f) for f in os.listdir("test-mails")]
test_docs = []

for mail in test_emails:
    with open(mail, "rt") as myFile:
        test_docs += [myFile.readlines()[2]] #body of mail is 3rd line of each .txt file

test_features =  vectorizer.transform(test_docs)
test_labels = np.zeros(318)
test_labels[159:318]=1

result1 = model1.predict(test_features)
counter = 0

for i in range(len(test_labels)):
    if test_labels[i] == result1[i]:
        counter += 1

print("Precision of prediction is {0:.2f} percent".format(counter/len(test_labels)*100))
