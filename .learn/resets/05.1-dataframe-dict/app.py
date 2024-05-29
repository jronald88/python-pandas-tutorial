import pandas as pd

#ex1
#print("Hello World")
""""
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")

print(data_frame)

data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

print(pd.date_range(start = "2021-05-01",end="2021-05-12"))

my_series = pd.Series([2, 4, 6, 8, 10])
print(my_series.apply(lambda x: x/2))
"""
#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
#df = pd.DataFrame(data, columns = ["Brand","Model","Color"])
#print(df.head())

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    }
    {   "brand": "Tesla"
        "model": "Model S"
        "color":"Red"
        }
]

#df.loc[len(df.index)] = ["Tesla","Model S","Red"]
print(df)