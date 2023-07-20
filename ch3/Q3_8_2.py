import pickle

with open("test1.pkl", "rd") as f:
    x = pickle.load(f)
    print(x)
