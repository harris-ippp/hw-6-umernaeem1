import requests

from bs4 import BeautifulSoup as bs

resp = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General")
soup = bs(resp.content, "html.parser")

rows = soup.find_all("tr", "election_item")
#print([[int(x.find("td").contents[0]), int(x.get("id").split("-")[2])] for x in rows])
ELECTION_ID = [[int(x.find("td").contents[0]), int(x.get("id").split("-")[2])] for x in rows]
