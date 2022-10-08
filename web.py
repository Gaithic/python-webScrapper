from urllib import response
import requests
import json
from bs4 import BeautifulSoup
import requests, openpyxl


excel = openpyxl.Workbook()

print(excel.sheetnames)


url = "https://www.tyroola.com.au/tyre/michelin/pcr/pilot-sport-4/?buy_3_for_4=0&instant_cash=0&clearance=0&rft=0"


sheet = excel.active
sheet.title = "Micheline Tyres"
print(excel.sheetnames)
sheet.append(['Brand Name', 'Model Name', 'Size', 'Image Link', 'Price'])


r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
script = soup.find_all('script')[3].text.strip()[19:-366]
data = json.loads(json.dumps(script))

sheet.append([data])
print(data)

excel.save('micheline tierss.xlsx')