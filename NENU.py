import requests
import re
import grequests
import getpass

headers={
    'origin': "http://222.27.96.95",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'cache-control': "no-cache",
    'Referer': 'http://222.27.96.95/qzxk/xk/getXkInfo?jx0502zbid=108&jx0502id=47&sfktx=1&sfkxk=1'
}
requests = requests.session()
requests.keep_alive=False


def parse(html):
    pattern=re.compile('sRand=(.*?)"',re.S)
    item=re.findall(pattern, html)[0]
    return item

def main(account,password):

    url_get='http://xk.nenu.edu.cn/'
    code=parse(requests.get(url_get,headers=headers).text)
    data={
        'IDToken1':	account,
        'IDToken2':	password,
        'RANDOMCODE':	code,
        'ymyzm':	code
    }
    url_login='http://222.27.96.95/qzxk/xk/LoginToXkLdap?url=http://222.27.96.95:80/qzxk/xk/LoginToXkLdap'
    res=requests.post(url_login,data=data,headers=headers)
    url_skip='http://222.27.96.95/qzxk/xk/AccessToXk'
    res=requests.get(url_skip,headers=headers).text
    print(res)
    url_show = "http://222.27.96.95/qzxk/xk/getXkInfo?jx0502zbid=108&jx0502id=47&sfktx=1&sfkxk=1"
    print(requests.get(url_show,headers = headers).text)

    url_2 = 'http://222.27.96.95/qzxk/xk/processXk'

    code1 = input('课程号1:')
    res = requests.post('http://222.27.96.95/qzxk/xk/GetXkRs',data = {"jx0502id": "47","kch": code1},headers = headers).text
    code1 = re.findall('id":"(.*?)",',res)[0]

    code2 = input('课程号2:')
    res = requests.post('http://222.27.96.95/qzxk/xk/GetXkRs',data = {"jx0502id": "47","kch": code2},headers = headers).text
    code2 = re.findall('id":"(.*?)",',res)[0]

    code3 = input('课程号3:')
    res = requests.post('http://222.27.96.95/qzxk/xk/GetXkRs',data = {"jx0502id": "47","kch": code3},headers = headers).text
    code3 = re.findall('id":"(.*?)",',res)[0]

    code4 = input('课程号4:')
    res = requests.post('http://222.27.96.95/qzxk/xk/GetXkRs',data = {"jx0502id": "47","kch": code4},headers = headers).text
    code4 = re.findall('id":"(.*?)",',res)[0]


    data1 = {
        'jx0502id': '47',
        'jx0404id': code1,
        'jx0502zbid': '108'
    }
    data2 = {
        'jx0502id': '47',
        'jx0404id': code2,
        'jx0502zbid': '108'
    }
    data3 = {
        'jx0502id': '47',
        'jx0404id': code3,
        'jx0502zbid': '108'
    }
    data4 = {
        'jx0502id': '47',
        'jx0404id': code4,
        'jx0502zbid': '108'
    }

    tasks = [grequests.post(url_2,headers=headers,data=data1,session=requests),
             grequests.post(url_2,headers=headers,data=data2,session=requests),
             grequests.post(url_2,headers=headers,data=data3,session=requests),
             grequests.post(url_2,headers=headers,data=data3,session=requests)]
    while 1:
        res = grequests.map(tasks, size=300)
        print(res[0].text)



if __name__=='__main__':
    account = input('账号：')
    password = getpass.getpass('密码：')

    main(account, password)



