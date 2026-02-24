import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
response = requests.get(url)
print(response.status_code)
data = response.json()
features=data["features"]

eq = []
for el in features:
    eq.append({
        "place" : el["properties"]["place"],
        "magnitude" : el["properties"]["mag"],
        "time" : el["properties"]["time"],
        "depth": el['geometry']['coordinates'][2],
    })
df = pd.DataFrame(eq)

df=df[df["magnitude"]>3.0]
df["time"] = pd.to_datetime(df["time"], unit='ms')
df=df.dropna()
print(df.head())
mean_mag=(df["magnitude"]).mean()
median_mag=(df["magnitude"]).median()
max_mag=(df["magnitude"]).max()

print(mean_mag)
print(median_mag)
print(max_mag)

top5=df.nlargest(5,"magnitude")["place","magnitude","time"]
print(top5)
cor=df.["magnitude"].corr(df["depth"])
print(cor)
region_counts=df.["region"].value_counts()
print(region_counts.head())
plt.hist(df["Magnitude"], bins=20)
plt.xlabel("Магнітуда")
plt.ylabel("Кількість")
plt.title("Розподіл магнітуд землетрусів (>3.0)")
plt.show()











