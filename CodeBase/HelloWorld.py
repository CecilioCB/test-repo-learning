
print("Hello World")

## Cut funtion
import pandas as pd

df= pd.DataFrame(
    {
        "Name" : ["Sajjad", "Ali Reza", "David", "Mohammad", "John"],
        "Mark" : [86, 61,49,92,100]
    }
)
print(df)
cutoff = [0,50,70,90,100]
labels= ["Failed", "C", "B", "A"]
df["Betyg"]=pd.cut(df["Mark"],bins=cutoff,labels=labels)
print(df)
