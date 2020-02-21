from vicorrect.model import CorrectVietnameseSentence

# dataFile = "./data/VNESEcorpus.txt"

# dataset = open(dataFile).read().splitlines()

# print(len(dataset))

# corrector = CorrectVietnameseSentence(verbose=True)
# corrector.fit(dataset)

testcase = [
    "troi buon. troi do con mua.",
    "con chim dau",
    "chim dau canh da troi do mua"
]

import pickle

# pickle.dump(corrector, open("corrector.pkl", "wb"))

model = pickle.load(open("./models/corrector.pkl", "rb"))

print(model.predict(testcase))