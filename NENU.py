import requests
import re
import grequests
import getpass

#The server address may change.
server = '222.27.96.95'
jx0502zbid = 109

headers={
    'origin': 'http://' +str(server),
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'cache-control': "no-cache",
    'Referer': 'http://'+str(server)+'/qzxk/xk/getXkInfo?jx0502zbid='+str(jx0502zbid)+'&jx0502id=47&sfktx=1&sfkxk=1'
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
    url_login='http://'+str(server)+'/qzxk/xk/LoginToXkLdap?url=http://'+str(server)+':80/qzxk/xk/LoginToXkLdap'
    res=requests.post(url_login,data=data,headers=headers)
    url_skip='http://'+str(server)+'/qzxk/xk/AccessToXk'
    res=requests.get(url_skip,headers=headers).text
    print(res)
    url_show =  "http://"+str(server)+"/qzxk/xk/getXkInfo?jx0502zbid="+str(jx0502zbid)+"&jx0502id=47&sfktx=1&sfkxk=1"
    res = requests.get(url_show,headers = headers).text
    print(res)
    if "课程性质" not in res:
        print('Something is wrong,check the url')
        exit(0)

    url_2 = 'http://'+str(server)+'/qzxk/xk/processXk'

    num = input('抢几节课：')
    data_list = []
    for i in range(int(num)):
        code = input('课程号'+str(i+1)+':')
        is_second = input('此课堂名称有（2）的标志吗（1有0没有）:')
        res = requests.post('http://'+str(server)+'/qzxk/xk/GetXkRs',data = {"jx0502id": "47","kch": int(code)},headers = headers).text
        code = re.findall('id":"(.*?)",',res)[int(is_second)]
        data = {
        'jx0502id': '47',
        'jx0404id': code,
        'jx0502zbid': str(jx0502zbid)
        }
        data_list.append(data)
    tasks = [grequests.post(url_2,headers=headers,data=data,session=requests,timeout = (3,0.01)) for data in data_list]
    print('抢课中，按Ctrl+c停止')
    while 1 :
        res = grequests.map(tasks, size=100)


if __name__=='__main__':
    account = input('账号：')
    password = getpass.getpass('密码：')

    main(account, password)



