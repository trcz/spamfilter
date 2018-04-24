import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer

emails = [os.path.join("train-mails", f) for f in os.listdir("train-mails")]
all_docs = []


for mail in emails:
    with open(mail, "rt") as myFile:
        all_docs += [myFile.readlines()[2]] ##body of mail is 3rd line of each .txt file


with open(emails[0], "rt") as myFile:
    print(type(myFile.readlines()[2]))


print(len(all_docs))
vectorizer = TfidfVectorizer()
representation = vectorizer.fit(all_docs)
train_features = vectorizer.transform(all_docs)
print(np.size(train_features, 0))