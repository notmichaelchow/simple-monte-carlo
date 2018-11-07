
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')
start = dt.date(2018,10,6)
end = dt.date(2018,11,6)

DOCU = web.DataReader('DOCU', 'iex', start, end)['close']
returns = DOCU.pct_change()
last_price = DOCU[-1]

num_sims = 500 #number of simulations
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_sims):
	count = 0
	daily_vol = returns.std()

	price_series = []

	price = last_price * (1 + np.random.normal(0, daily_vol))
	price_series.append(price)

	for y in range(num_days):
		if count == 251:
			break
		price = price_series[count] * (1 + np.random.normal(0, daily_vol))
		price_series.append(price)
		count += 1

	simulation_df[x] = price_series

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: DOCU')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()

