from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import pickle

def mia():
    path = Path("data", "mia.pickle")
    with open(path, 'rb') as f:
        data = pickle.load(path)
    clf = RandomForestClassifier()
    train, test = split(data)
    clf.fit(train["loss"], train["member"])
    member_hat = clf.predict(test["loss"])



if __name__=="__main__":
    pass

