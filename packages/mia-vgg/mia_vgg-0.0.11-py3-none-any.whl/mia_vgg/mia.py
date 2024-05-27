from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import pickle

def mia():
    path = Path("data", "mia.pickle")
    with open(path, 'rb') as f:
    clf = RandomForestClassifier()
    clf.fit(

if __name__=="__main__":
    pass

