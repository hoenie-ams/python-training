import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/sales.csv")

df["Profits"] = df["Sales"] - df["Costs"]

df = df.sort_values("Profits", ascending=False)

print(df)

import matplotlib.pyplot as plt
df.nlargest(10, columns=["Profits"]).plot(kind="bar", x="Country")
plt.savefig("plaatje.jpg")

