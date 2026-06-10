import joblib

model = joblib.load("model/CandyDistributerModel_joblib")


response = model.predict([["4","4","52","1","5","6.50",	"6.50"	,"2.28"	,"20"	,"1"]])

print(response)