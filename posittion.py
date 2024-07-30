from urllib.request import urlopen
import os
import json
import pandas as pd

data_dir = os.path.join(os.getcwd(), 'data')
drivers = pd.read_csv(os.path.join(data_dir, 'drivers.csv'))

response = urlopen('https://api.openf1.org/v1/position?meeting_key=latest&session_key=latest')
data = json.loads(response.read().decode('utf-8'))
df = pd.DataFrame(data)

#df = df.drop('date', axis=1)
search_box = df
seen = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
final_grid = []

search_box = search_box.sort_values(by = 'date', ascending = False)
for index, row in search_box.iterrows():
    pos = row['position']
    if pos in seen:
        seen.remove(pos)
        final_grid.append((pos, row['driver_number']))


final_grid.sort(key = lambda tup: tup[0])
final_grid = pd.DataFrame(final_grid, columns=['Position', 'Driver Number'])
final_grid = final_grid.join(drivers.set_index('driver_number'), on = 'Driver Number')
print("Final grid:")
print(final_grid)
