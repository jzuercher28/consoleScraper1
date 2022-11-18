from Scraper_class import Scraper


class Console:
    def __init__(self):
        self.flag = False
        self.inp = ""
        self.url = ""
        self.scraper = Scraper()
        self.urlList = []
        self.prompt = """(Type 'quit' or 'exit' to exit)
        1 - help
        2 - run
        3 - options
        4 - set url
        5 - clear links
        6 - get links
        7 - show urllist
        8 - clear urllist
        9 - run crawler
        10 - choose url
        """

    def start(self):
        self.flag = True
        secondPrompt = "$scraper_console$> "
        print(self.prompt)
        while self.flag:
            self.inp = input(secondPrompt)
            if self.inp.lower() == "quit" or self.inp == "exit":
                self.flag = False
            elif self.inp.lower() == "help":
                self.help()
            elif self.inp.lower() == "run":
                self.run()
            elif self.inp.lower() == "options":
                self.options()
            elif self.inp.lower() == "set url":
                self.setUrl()
            elif self.inp.lower() == "clear links":
                self.flushLinks()
            elif self.inp.lower() == "get links":
                self.getLinks()
            elif self.inp.lower() == "show urllist":
                self.showUrls()
            elif self.inp.lower() == "clear urllist":
                self.urlList.clear()
                print("list cleared")
            elif self.inp.lower() == "run crawler":
                self.crawl()
            elif self.inp.lower() == "choose url":
                self.chooseUrl()

    def help(self):
        print()
        print("\tHELP MENU:\n")
        print("This is a terminal based web scraping program. To start, you must set a url to start from.")
        print("""To do this, type 'set url' and press enter and input your given starting url of any form (http, https or www.)""")
        print("\n\tCOMMANDS:\n")
        print("<options>: Displays options menu")
        print("<set url>: Sets url to start scraping from")
        print("<get links>: With the url set, this will print out links within the html code on that url only.")


    def run(self):
        print("run\n")

    def options(self):
        print(self.prompt)

    def setUrl(self):
        self.url = input("Enter URL: ")
        if self.url.startswith('www'):
            self.url = 'https://' + self.url
        elif not self.url.startswith('http') or not self.url.startswith('www'):
            self.url = 'https://www.' + self.url
        self.scraper.setUrl(self.url)
        print("URL set for scraper\n")
        self.urlList.append(self.url)

    def crawl(self):
        try:
            self.scraper.crawl()
        except KeyboardInterrupt:
            print("Keyboard interrupted")

    def flushLinks(self):
        self.scraper.flush()
        print("links flushed from list\n")

    def getLinks(self):
        if self.url != "":
            self.scraper.returnLinks()
            for x in self.scraper.links:
                print(x, end='\n')
        else:
            print("please set a URL first with the 'set url' command\n")

    def showUrls(self):
        i = 1
        for url in self.urlList:
            print(i, " - ", url)
            i += 1
        if len(self.urlList) <= 0:
            print("No urls to show")

    def chooseUrl(self):
        i = 0
        for choice in self.urlList:
            print(i, " ", choice)
            i += 1
        y = int(input("choose from above: "))
        for x in self.urlList:
            if y == self.urlList.index(x):
                self.scraper.setUrl(x)
                print("URL set", self.scraper.url)


def main():
    console = Console()
    console.start()


if __name__ == "__main__":
    main()