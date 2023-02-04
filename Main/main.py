import pyshorteners
def url(link):
    url = pyshorteners.Shortener()
    print(url.tinyurl.short(link))
    print("DONE")
link = input("Input your URL: ")

url(link)
