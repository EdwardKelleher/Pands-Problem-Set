from urllib.request import urlretrieve
import pandas as pd
iris = https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv
urlretrieve(iris)
df = pd.read_csv(iris, sep=',')
attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
print(df.head())

