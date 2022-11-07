import json
import pandas as pd

studentsList=[]
with open('/Users/hacosta/github/data-engineering-exercise-python/uncommitted/votes_test.json', 'r') as j:
    for jsonObj in j:
        studentDict = json.loads(jsonObj)
        studentsList.append(studentDict)

df = pd.DataFrame(studentsList)
print(df.head(5))
