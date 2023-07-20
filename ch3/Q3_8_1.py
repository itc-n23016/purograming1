import pickle

with open("test1.pkl", "wd") as f:
    x = list(range(1, 11))
    pickle.dump(x, f)
