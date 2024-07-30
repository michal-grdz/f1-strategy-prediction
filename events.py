from urllib.request import urlopen
import json
import pandas as pd

response = urlopen('https://api.openf1.org/v1/race_control?session_key=latest')
data = json.loads(response.read().decode('utf-8'))
df = pd.DataFrame(data)
df= df[['category', 'driver_number', 'flag', 'meeting_key', 'message']]
print(df)

