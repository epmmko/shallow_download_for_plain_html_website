from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import ssl
import sqlite3
import os

for i in range(1000):
    download_folder_name = './download_{:04d}'.format(i)
    if(not os.path.exists(download_folder_name)):
        os.makedirs(download_folder_name)
        break
else:
    sys.exit("1000 of download folders are already exist, delete and rerun.")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('url for shallow download:')
if(len(url) < 1):
    url = r'https://www.pg4e.com/code/'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
raw_file_names = []
for tag in tags:
    raw_file_names.append(tag.get('href', None))

clean_file_names = [i for i in raw_file_names if i.find(".") != -1]

print(clean_file_names)
print("\n\n\n")

conn = sqlite3.connect('download_log.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS DownloadLog;

CREATE TABLE DownloadLog(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    file_name TEXT,
    header TEXT
);
'''
)
conn.commit()

for file_name in clean_file_names:
    try:
        print(url)
        print(url+file_name)
        local_filename, headers = urlretrieve(url + file_name, download_folder_name + '/' + file_name)
        print(local_filename, str(headers))
        sql_command = "INSERT INTO DownloadLog(file_name,header) VALUES (?,?)"
        cur.execute(sql_command, (local_filename, str(headers)))
    except Exception as exc:
        print(exc)
      
conn.commit()
conn.close()
