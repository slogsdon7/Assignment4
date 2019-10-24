import requests
from datetime import datetime
url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'

dates = [
    ('2016-01-01', '2017-01-01'),
    ('2017-01-01', '2018-01-01'),
('2018-01-01', '2019-01-01'),
('2019-01-01', '2019-10-02')
]

def fetch(url, params):
    response = requests.get(url, params)
    if response.status_code == 200:
        return response.text
    else:
        print(response.text)


if __name__ == '__main__':
    first = True
    for start, end in dates:
        params = {'format': 'csv', 'minmagnitude': 4.0, 'starttime': start, 'endtime': end}
        data = fetch(url, params)
        with open('data.csv', 'a') as fp:
            if not first:
                lines = data.split('\n')
                for line in lines[1:]:
                    fp.write(line + '\n')
            else:
                fp.write(data)
                first = False


