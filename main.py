import requests
from bs4 import BeautifulSoup
import lxml
import re
from inform import send_email
url = "https://www.coupang.com/vp/products/6884681205?itemId=16509749179&vendorItemId=83697119196&q=surface&itemsCount=27&searchId=a93e0b605154493da6af1d2d77eb775c&rank=0&isAddedCart="
headrs = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language':'en-US,en;q=0.9'
}
response = requests.get(url,headers=headrs)
soup = BeautifulSoup(response.text, 'lxml')
price = soup.select_one('strong').getText()
price_to_compare = price
price_to_compare = int(re.sub('\D','', price_to_compare))

#Compare
with open('current_price.txt', 'r') as current_data:
    old_price =int(current_data.read())
    print(old_price)
if price_to_compare < old_price:
    with open('current_price.txt','w') as current_data:
        current_data.write(str(price_to_compare))
    #send mail
    send_email(price=price,link=url)