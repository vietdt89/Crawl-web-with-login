import requests
from bs4 import BeautifulSoup

values = {'name': 'vietdt89',
          'pass': 'hr4e9ei'}

login_url = "https://www.manager-tools.com/user"

login = ''
password = ''

cookies = {
    '_ga': 'GA1.2.405544073.1678090874',
    '_gid': 'GA1.2.1316744096.1679278354',
    'sampleId': '4142982315',
    'customerID': '1006066',
    'signUpDate': '2023-03-06',
    'userID': '0',
    '_gat_UA-95599-15': '1',
    '_gali': 'edit-submit',
    '__gahits': '35',
}

headers = {
    'authority': 'manager-tools.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.2.405544073.1678090874; _gid=GA1.2.1316744096.1679278354; sampleId=4142982315; customerID=1006066; signUpDate=2023-03-06; userID=0; _gat_UA-95599-15=1; _gali=edit-submit; __gahits=35',
    'origin': 'https://manager-tools.com',
    'referer': 'https://manager-tools.com/user?destination=we-answer-your-questions-how-be-better-manager-and-have-more-successful-career',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

params = {
    'destination': 'we-answer-your-questions-how-be-better-manager-and-have-more-successful-career',
}

data = {
    'name': 'vietdt89',
    'pass': 'hr4ei9ei',
    'form_build_id': 'form-jNFUj_bXKwJ4nCo3-AC_FE5u2OU6VZM1XYgu_EgKzPw',
    'form_id': 'user_login',
    'op': 'Log in',
}

print("start")
session = requests.Session()
response = session.post('https://manager-tools.com/user', params=params, cookies=cookies, headers=headers, data=data)

itemList = []
with open("myfile.txt") as file:
    for line in file:
        itemList.append(line.rstrip())
ind = 1
for link in itemList:
    page = session.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')

    for data in soup.find_all('a', href=True):
        if data.text:
            sbstr = "print"
            if sbstr in data['href']:
                print(ind)
                noteLink = "https://manager-tools.com" + data['href']
                print(noteLink)
                fileName = link.split("/")[-1:][0] + '.html'
                with open(fileName, 'wb+') as f:
                    pageChild = session.get(noteLink)
                    f.write(pageChild.content)
                    print("Done writting")
                ind+=1
print("done")
