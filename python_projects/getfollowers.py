import requests
import fake_useragent
ua=fake_useragent.UserAgent()
headers={'User-Agent':ua.random}

url='url'

r=requests.get(url,headers=headers)

data=r.json()
with open("file.txt", "w",encoding="utf-8") as external_file:
    for item in data['response']['items']:
        try:
            print(item['id'],item['first_name'],item['last_name'],item['bdate'],item['city']['title'],file=external_file)
        except KeyError:
            print(item['id'],item['first_name'],item['last_name'],file=external_file)
        number=item['id']
        url=f'url,id={number}'
        r2=requests.get(url,headers=headers)
        data2=r2.json()
        if 'response'not in data2:
            print('\t','private',file=external_file)
        else:
            for i in data2['response']['items']:
                try:
                    print('\t',i['id'],i['first_name'],i['last_name'],i['bdate'],i['city']['title'],file=external_file)
                except KeyError:
                    print(i['id'],i['first_name'],i['last_name'],file=external_file)
