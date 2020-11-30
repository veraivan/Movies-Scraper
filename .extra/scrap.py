import requests, random, lxml.html, useragent, re, os, base64
from threading import Thread, Lock 


null = "\033[0m"
white = "\033[1;37m"
blue = "\033[0;34m"
light_red = "\033[1;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
esp = f"{blue}[{white}+{blue}]{null}"

#global variable
key = []

def extract_links_page(url):
    host = re.search(r'(?<=//)[^\/]*', url)
    dispatcher[host.group(0)](url)


def f1_extract(url):
    try:
        headers = {'User-Agent': random.choice(useragent.userList)}
        website = requests.get(url, headers=headers)
        div_content = lxml.html.fromstring(website.content).xpath('//div[@class="watch-text"]/div')[0]
        list_table = div_content.xpath('//table') 
        list_title = div_content.xpath('//div[@class = "accordion__heading accordion" or @class = "accordion__ser accordion"]/text()')
        work_thread((start_scrap, zip(list_title, list_table)))
        print(f'\n{light_red}Password: {white}hackstore.net', end='\n')
    except requests.exceptions.MissingSchema as error:
        print(error)


def start_scrap(body, lock):
    if not body[1].xpath('./caption'):
        tr_list = body[1].xpath('./tbody/tr')
        tupla_list = [get_colum(tr.xpath('./td')) for tr in tr_list]
        servers = []
        for tupla in tupla_list:
            if  tupla[1][-2:] == '==':
                servers.append(f"{green}%s: {white}%s" % (tupla[0], 'Link down'))
            else:
                servers.append(f"{green}%s: {white}%s" % (tupla[0], decryption_link(tupla[1])))
        with lock:
            print(f"{blue}[{white}+{blue}] {body[0]}", end='\n ')
            print(*servers, sep='\n ')
            print("")


#Extract link for each td of content 
def get_colum(td_list):
        text_script =session_req({
            'link': td_list[2].xpath('./a/@href')[0],
            'domain': 'hackshort.me',
            'value': 'dW5weGZnYmVyLmFyZw==',
            'linkser': 'unpxfgber.arg'
        })
        search_pattern = re.search(r'(?<=var link_out =).*', text_script)
        tupla = (td_list[0].xpath('./b/text()')[0], search_pattern.group(0)[2:-2]) 
        return tupla 


def session_req(json):
    with requests.Session() as session:
        session.headers = {'User-Agent': random.choice(useragent.userList)}
        cookie = requests.cookies.create_cookie(domain=json['domain'], name='PHPINFO', value=json['value'])
        session.cookies.set_cookie(cookie)
        body = session.get(json['link']) 
        get_action_form = lxml.html.fromstring(body.content).xpath('//form/@action')[0]
        body = session.post(
            get_action_form,
            headers=  {'Content-Type': 'application/x-www-form-urlencoded'},
            data={'linkser': json['linkser']}
        )
        link_out = lxml.html.fromstring(body.content).xpath('//script/text()')[0]
    return link_out


#Function decode link 
def decryption_link(encode_link):
    output = os.popen('node .extra/decodeJS/decode.js ' + encode_link).read()[:-1]
    dec_link= re.search(r'(?<=\?s=).*', output)
    req = requests.get(dec_link.group(0))
    return req.url 


def f2_extract(url):
    with requests.Session() as session:
        session.headers = {'User-Agent': random.choice(useragent.userList)}
        site = session.get(url)
        href = lxml.html.fromstring(site.content).xpath('//a[@class="myButton"]/@href')[0]
        cod = re.search(r'(?<=link#!).*', href)
        req = session.post(
            'https://acortar.info/redir?TVRZd05qRXdNems0TWc9PQ==',
            headers=  {'Content-Type': 'application/x-www-form-urlencoded'},
            data={'hash': cod.group(0) } 
        )
        href = lxml.html.fromstring(req.content).xpath('//a/@href')[0]
        body = session.get(href)
        links = lxml.html.fromstring(body.content).xpath('//div[@id="tab1"]/a/@href')
        print(f"{blue}[{white}+{blue}] Links{null}", end='\n\t')
        print(*links, sep=f'\n\t')
        print("")


def f3_extract(url):
    headers = {'User-Agent': random.choice(useragent.userList)}
    site = requests.get(url, headers=headers)
    tag_tbody = lxml.html.fromstring(site.content).xpath('//table/tbody')[1]
    tr_list = tag_tbody.xpath('./tr')[:-1] 
    work_thread((start_f3, tr_list))
    print(f"{blue}[{white}+{blue}] Links", end=f'\n{yellow}')
    work_thread((get_link, key))


def get_link(url, lock):
    body = requests.get(url, headers={'User-Agent': random.choice(useragent.userList)}) 
    ad_form_data = lxml.html.fromstring(body.content).xpath('//form/input[@name="ad_form_data"]/@value')[0]
    req = requests.post(
        'https://fc.lc/links/go',
        headers={
            'User-Agent': random.choice(useragent.userList), 
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data= {
            'ad_form_data': ad_form_data,
            'random_token': '53bea9046eaee7b41a2855d783c73fce',
            'visitor': 'YToyOntzOjI6ImlwIjtzOjE0OiIxODEuMTI3Ljg2LjE4MSI7czo0OiJkYXRlIjtzOjE5OiIyMDIwLTExLTI3IDE0OjU2OjEyIjt9',
            '_method': 'POST',
            'ab': 2,
            '_Token[fields]': '1c4be3ba52757104884592b853a243d3%3Aad_form_data',
            'Token[unlocked]': 'adcopy_challenge%7Cadcopy_response%7Ccoinhive-captcha-token%7Cg-recaptcha-response'
        }
    )
    body = requests.get(req.json()['url'])
    list_div = lxml.html.fromstring(body.content).xpath('//div[@class="tab_container"]/div[@class="tab_content"]')
    for tag_div in list_div:
        list_href = tag_div.xpath('./a/@href')
        decode_links = [ decode_base64(href) for href in list_href ]
    with lock:
        print(*decode_links, sep=f'\n{yellow}')


def decode_base64(link):
    match = re.search(r'(?<=\?).*', link)
    dec = base64.b64decode(match.group(0))
    return str(dec, encoding='utf-8')


def start_f3(tag_tr, lock):
    global key
    tags_td = tag_tr.xpath('./td')
    href_link = tags_td[1].xpath('./a/@href')[0] 
    text_code = session_req({
        'link': href_link,
        'domain': 'megalinks.site',
        'value': 'enJ0bjEwODBjLmJldA==',
        'linkser': 'zrtn1080c.bet'
    })
    search_pattern = re.search(r'(?<=var link_out =).*', text_code)
    output = os.popen('node .extra/decodeJS/decode.js ' + search_pattern.group(0)[2:-2]).read()[:-1] 
    match = re.search(r'(?<=lc\/).*', output)
    with lock:
        link = 'https://short.fc-lc.com/' + match.group(0)
        if link not in key:
            key.append(link)


def work_thread(input):
    #lock the state 
    lock = Lock()
    threads = []
    for element in input[1]:
        thread = Thread(target=input[0], args=(element, lock))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()


dispatcher = {
    'hackstore.net': f1_extract,
    'www.peliculas1mega.com': f2_extract,
    'mega1080p.org': f3_extract
}