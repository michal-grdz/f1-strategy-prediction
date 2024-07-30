from urllib.request import urlopen
import os
import json
import pandas as pd

response = urlopen('https://api.openf1.org/v1/drivers?&session_key=latest')
data = json.loads(response.read().decode('utf-8'))
df = pd.DataFrame(data)
df = df[['driver_number', 'name_acronym', 'team_name']]
drivers = df.drop_duplicates()
print(drivers)

data_dir = os.path.join(os.getcwd(), 'data')
drivers.to_csv(os.path.join(data_dir, 'drivers.csv'), index=False)
