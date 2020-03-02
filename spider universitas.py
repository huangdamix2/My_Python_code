import requests
import bs4

Ulist=[]
def get_html(url):
    try:
        responce = requests.get(url, timeout=10)
        responce.encoding = responce.apparent_encoding
        responce.raise_for_status()
        #print(responce.status_code)
        demo = responce.text
        soup = bs4.BeautifulSoup(demo, 'html.parser')
        return soup
    except:
        return ''


def Ulist_infor(Ulsit,soup):
    for tr in soup.tbody.children:
        if isinstance(tr,bs4.element.Tag):#isinstance 检测tr标签的类型，如果有标签不是bs4库定义的Tag类型将过滤掉
            tds = tr.find_all('td')
            #print(tds[0],tds[1],tds[2])
            Ulist.append([tds[0].string,tds[1].string,tds[3].string])
    #for tr in soup.find('tbody').children:
    #    print(tr)
def print_Ulist(Ulist,num):
    tplt = '{:^10}{:^10}{:^10}'
    print(tplt.format('排名','学校名称','总分'))
    for i in range(num):
        u = Ulist[i]
        print(tplt.format(u[0],u[1],u[2]))

if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'

    soup = get_html(url)
    Ulist_infor(Ulist,soup)
    print_Ulist(Ulist,20)