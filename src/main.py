import pandas as pd
import matplotlib.pyplot as plt

temperature_in_miami = pd.read_csv(
    "data/temperature_data.csv", index_col=0, parse_dates=True
)
temperature_in_miami.head()
temperature_in_miami.plot(figsize=(10, 6))
plt.show()
