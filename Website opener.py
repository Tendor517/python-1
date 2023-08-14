#copied the method from code-it-up lectures.
def a ():
    j=input("enter the url of the website:")
    weburl=j
    return weburl
while 1==1:
    import urllib.request
    import webbrowser
    weburl=a()
    opens=urllib.request.urlopen(weburl)
    html=opens.read()
    data=opens.getcode()
    url=opens.geturl()
    hd=opens.headers
    inf=opens.info()
    print(opens)
    print(html)
    print(url)
    print(hd)
    print(inf)
    print("1.The Website linked with this url:",weburl,"is")
    webbrowser.open_new(url)
