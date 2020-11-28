import requests
import bs4

url = 'https://jadwalsholat.pkpu.or.id/?id=135'
content = requests.get(url)
#print(content.text)
soup = bs4.BeautifulSoup(content.text, "html.parser")
#print(asd)
hari_ini = soup.find('tr', 'table_highlight')
#print(hari_ini)
sholat = {}
i = 0
for h in hari_ini:
#    print(h.get_text())
    if i==1:
        print(h.get_text())
        sholat['subuh'] = h.get_text()
    elif i==2:
        print(h.get_text())
        sholat['dzuhur'] = h.get_text()
    elif i==3:
        print(h.get_text())
        sholat['ashar'] = h.get_text()
    elif i==4:
        print(h.get_text())
        sholat['magrib'] = h.get_text()
    elif i==5:
        print(h.get_text())
        sholat['isyak'] = h.get_text()

    i += 1

print(sholat)
print(sholat['magrib'])
