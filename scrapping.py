import urllib
def getPageContent(url):
    print("getting")
    page = urllib.request.urlopen(url)
    print("reading")
    pageContent = page.read()
    print(pageContent)
