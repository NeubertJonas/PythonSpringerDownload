import pandas as pd
import requests
from bs4 import BeautifulSoup
import progressbar
import time
import re

# Use the Excel file provided by Springer
df = pd.read_excel(r'germanBooks2.xlsx') 
rowCount = df.shape[0]

progress = progressbar.ProgressBar()
for p in progress(range(rowCount)):
    url = df.iloc[p, 18]
    year = str(df.iloc[p, 4])
    author = str(df.iloc[p, 1])
    title = str(df.iloc[p, 0])
    filename = author + ' ('+year+') '+title
    filenameValid = re.sub("[/:*?<>|]", "-", filename)
    # Use your own username or custom location
    saveLocation = '/Users/username/Downloads/Python/' + filenameValid + '.pdf'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    table = soup.find('a', attrs={'class': 'test-bookpdf-link'})
    table = table.get("href")
    link = "https://link.springer.com" + table

    r2 = requests.get(link)
    with open(saveLocation, 'wb') as f:
        f.write(r2.content)

    print('Successful download: ', title)
