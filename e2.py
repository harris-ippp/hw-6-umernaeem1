import requests

from bs4 import BeautifulSoup as bs

from e1 import *

link = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
for x in ELECTION_ID:
    resp = requests.get(link.replace('{}',str(x[1])))
    file_name = 'president_general_' + str(x[0]) + '.csv'
    with open(file_name, 'w') as out:
        out.write(resp.text)
    
    
