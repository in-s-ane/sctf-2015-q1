import urllib, urllib2, cookielib


cred = {
    'username': '##############',
    'password': '##############',
    'login': 'Login',
}
auth_url = 'http://compete.sctf.io/login.php'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36')]
urllib2.install_opener(opener)

def login():
    response = urllib2.urlopen(auth_url)
    content = response.read()
    text_to_find = '<input type="hidden" name="token" value="'
    i = content.find(text_to_find)
    j = content.find('"', i+len(text_to_find))
    token = content[i+len(text_to_find):j]
    cred['token'] = token

    data = urllib.urlencode(cred)
    req = urllib2.Request(auth_url, data)
    response = urllib2.urlopen(req)
    #print response.info(), response.read()

def main():
    ''' # This attacks the problems server that is linked to in the problem. Maybe the page changes every 7 seconds?
    handler = urllib2.urlopen('http://compete.sctf.io/problems.php')
    content = handler.read()
    print content, "\n------------------------------------------------------\n"

    while True:
        handler = urllib2.urlopen('http://compete.sctf.io/problems.php')
        temp = handler.read()
        if temp != content:
            print temp
            break
    '''
    ''' # This code attacks the checking server. Maybe every 7 seconds, it allows any input?
    data = urllib.urlencode({
        'ans': "BABY IS BORN????",
        'probcode': "38",
        'probname': "Every 7 Seconds"
    })
    while True:
        req = urllib2.Request('http://compete.sctf.io/checkproblem.php', data)
        response = urllib2.urlopen(req)
        print response.read()
    '''

login()
main()
