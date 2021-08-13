import requests, json


def users(url):
    res = requests.get(url).text
    page_data = json.loads(res)

    data = page_data['data']
    count = 0
    list_id = []
    for i in data:
        c = (i['id'])
        list_id.append(c)
    # print(k)
    for j in list_id:
        count += 1
    print("total users per pages", count)


for pages in range(1, 13):
    url= "https://reqres.in/api/users?page=" + str(pages)
    users(url)

