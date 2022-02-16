from forex_python.converter import CurrencyRates
import pandas as pd

c = CurrencyRates()

date = pd.date_range('2021-01-01', '2021-01-10', freq='D')

dates = []
names = []
values = []

for d in date:
    for name, value in c.get_rates('USD', d.date()).items():
        dates.append(d.date())
        names.append(name)
        values.append(value)

df = pd.DataFrame({"Date":dates, "Names":names, "Values": values})
df.to_csv(r"C:\Users\ozgur\Desktop\USD-Currency\Currencies.csv", index=False)






