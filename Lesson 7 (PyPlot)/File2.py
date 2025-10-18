import pandas as pd


df = pd.read_csv("education.csv").dropna()

info = (df[df['Year'] == 1950][["Entity", "Share of population with at least some basic education"]])
info2 = info.sort_values('Share of population with at least some basic education', ascending=True).head(10)
print(info2)
print("\n\n\n\n\n")
print(info)
