from urllib.request import urlopen
import json
import os
import pandas as pd

response = urlopen('https://api.openf1.org/v1/laps?session_key=latest&driver_number=4')
data = json.loads(response.read().decode('utf-8'))
df = pd.DataFrame(data)
df = df[['date_start', 'driver_number', 'lap_duration', 'lap_number', 'session_key']]
print(df)
