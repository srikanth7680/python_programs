from bs4 import BeautifulSoup
import requests
x = requests.get('http://www.hostinghome.in/login/admin/index.php')
y = BeautifulSoup(x.content, 'html')
print(y.prettify())
