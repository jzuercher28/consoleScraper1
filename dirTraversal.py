import os
from bs4 import BeautifulSoup

directory ='/Users/xxxxx/Documents/sample/'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        fname = os.path.join(directory,filename)
        with open(fname, 'r') as f:
            soup = BeautifulSoup(f.read(),'html.parser')
            # parse the html as you wish
 root, dirs, files in os.walk('')