from urllib.request import urlopen
import os
import json
import pandas as pd

response_race_control = urlopen('https://api.openf1.org/v1/race_control?&driver_number=16&date>=2024-01-01&date<2024-09-01')
response_meeting = urlopen('https://api.openf1.org/v1/meetings?&date_start>=2024-01-01')
data_flags = json.loads(response_race_control.read().decode('utf-8'))
data_meetings = json.loads(response_meeting.read().decode('utf-8'))
df_flags = pd.DataFrame(data_flags) 
df_meetings = pd.DataFrame(data_meetings) 

df_meetings = df_meetings[['meeting_key', 'circuit_short_name', 'meeting_name', 'date_start']]
df_flags = df_flags[['category', 'driver_number', 'flag', 'meeting_key', 'message']]

print(df_flags)
print(df_meetings)

data_dir = os.path.join(os.getcwd(), 'data')
df_meetings.to_csv(os.path.join(data_dir, 'meetings.csv'))
