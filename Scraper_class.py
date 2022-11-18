import requests
from bs4 import BeautifulSoup
import validators


"""
1 - Set URL
2 - return links
3 - return tags
4 - return HTML
"""


class Scraper:
    def __init__(self):
        self.url = ""
        self.links = []
        self.headers = {}
        if self.url != "":
            self.json = self.getJson()
        self.images = []
        self.html = []
        self.crawlFlag = False

    def getHtml(self):
        r = requests.get(self.url)
        self.html.append(r.text)
        print(r.text)

    def __urlError(self):
        print("No URL set")

    def hasJson(self):
        r = requests.get(self.url)
        if r.json() is not None:
            return True

    def showHeaders(self):
        if self.url != "":
            r = requests.get(self.url)
            self.headers.update(r.headers)
            print(r.headers)
        else:
            self.__urlError()

    def getJson(self):
        r = requests.get(self.url)
        return r.json()

    def flush(self):
        self.links = []
        self.headers.clear()
        self.images.clear()
        self.html.clear()

    def setUrl(self, url):
        self.url = url

    def getLinks(self, url):
        links = []
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            links.append(link)
            continue
        return links

    def returnLinks(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            self.links.append(link.get('href'))
            print(link.get('href'), "found")

        for link in self.links:
            try:
                if not validators.url(link):
                    self.links.remove(link)
            except Exception:
                continue

    def crawlLinks(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            self.links.append(link.get('href'))
        for link in self.links:
            try:
                if not validators.url(link):
                    self.links.remove(link)
            except Exception:
                continue

    def getImages(self):
        if self.url != "":
            r = requests.get(self.url)
            soup = BeautifulSoup(r.text, 'html.parser')
            for item in soup.find_all('img'):
                print(item['src'])
                self.images.append(item['src'])

    def getPdfs(self):
        i = 0
        for link in self.links:
            if '.pdf' in link.get('href', []):
                i +=1
                print("Downloading File")
                response = requests.get(link.get('href'))
                pdf = open("pdf"+str(i)+'.pdf', 'wb')
                pdf.write(response.content)
                pdf.close()
                print("File ", i, " downloaded")
        print("All files downloaded")

    def crawl(self):
        """
        Function should start from self.url, pull all urls into self.links, then continuously open with an infinite while loop statement
        """
        self.returnLinks()
        self.crawlFlag = True
        try:
            while self.crawlFlag:
                for link in self.links:
                    self.crawlLinks(link)
                    if link is None:
                        self.links.remove(link)
        except KeyboardInterrupt:
            print("keyboard interrupted")



def main():
    scraper = Scraper()
    scraper.setUrl('https://gatewayfoundation.org')
    scraper.crawl()
    scraper.flush()


if __name__ == "__main__":
    main()