import requests
from bs4 import BeautifulSoup
import pandas as pd
rows = []
datasets = []
monthvalue = 1
yearvalue = 1992
baseurl = "https://www.timeanddate.com/weather/usa/san-jose/historic?"
while(yearvalue<2016):
    while(monthvalue<13):
        strmonth = str(monthvalue)
        url = baseurl+'month='+strmonth+'&year='+str(yearvalue)
        if (len(strmonth)==1):
            strmonth = "0"+ strmonth
        rows.append(str(yearvalue)+strmonth)
        s = requests.session()
        data = s.get(url).text
        dom = BeautifulSoup(data)
        table = dom.find(attrs={'class':'zebra tb-wt fw tb-hover'})
        tds = [t.text for t in table.find_all('td')]
        rows.append(tds[0][:2])
        rows.append(tds[1][:3])
        datasets.append(rows)
        rows = []
        monthvalue = monthvalue + 1
    yearvalue = yearvalue + 1
    monthvalue = 1
df = pd.DataFrame(datasets, columns=["MONTHYEAR","HIGHTEMP","HUMIDITY"])
df.to_csv('/Users/Jia/Documents/weather/weather.csv') 
print("Job Finished")
