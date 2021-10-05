import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = '17A8XSTDGE0H43H7'

ts = TimeSeries(key=api_key, output_format = 'pandas')
data, meta_data = ts.get_intraday(symbol='AMZN', interval='1min', outputsize='full')
print(data)

i = 1
while i==1:
    data.to_excel('output.xlsx')
    time.sleep(60) # 1 minute

close_data =['4. close']
percent_change =close_data.pct_change()
print(percent_change)

last_change = percent_change[-1]
if abs(last_change) > 0.0004:
    print('AMZN alert!' + last_change)

# Test This Script from # In India:- 9:30am to 4:00pm # in US:- 9:30 to 16:00pm
#SUBSCRIBE!!!







