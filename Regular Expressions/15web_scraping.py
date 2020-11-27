import urllib.request
from re import findall

url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)

html = response.read()

html_str = html.decode()

pdata = findall("\(\d{3}\) \d{3}-\d{4}", html_str)

for item in pdata:
    print(item)