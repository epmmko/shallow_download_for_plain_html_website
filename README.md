# Shallow Download for a Plain File Sharing Website
This python code do a shallow download of all files for the old-style file sharing website.

![old_style_website](https://user-images.githubusercontent.com/26897526/189505077-6bdb7939-e214-4f56-8c6b-afb821870c7a.png)

It works best when "a href" tag links to a file directly for example `<a href="myutils.py">myutils.py</a>`

The websites that this code was tested for include
1) https://www.dj4e.com/code/http/
2) https://www.pg4e.com/code/

It is known to not work for a new website or the page that "a href" tag does not directly link to the file.
It does not work for github.com.

## Working Mechanism
After calling the script by `python shallow_download.py`, enter the website URL (need slash at the end, "/").
Then, it will download all files (excluding the files in subdirectories). It creates log file in sqlite format.

## Requirements
1. Sqlite3 (comes with Python, https://docs.python.org/3.8/library/sqlite3.html)
2. BeautifulSoup (pip install beautifulsoup4), test with version 4.9.3py
3. Python (test with Python 3.8.5)
