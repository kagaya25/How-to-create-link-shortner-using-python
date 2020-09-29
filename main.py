import pyshorteners

link = "https://kagayajohn.com"
shortener =pyshorteners.Shortener()
url = shortener.tinyurl.short(link)
print(url)

