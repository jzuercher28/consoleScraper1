from facebook_scraper import get_profile
from facebook_scraper import get_posts


class SocialScraper:
    def __init__(self):
        self.fb_data = {}

    def get_fb_profile(self, profileid):
        new_dict = {profileid: {}}
        self.fb_data.update(new_dict)
        self.fb_data[profileid] = get_profile(profileid)
        print(self.fb_data[profileid])

    def getPosts(self, string, pages=10):
        for post in get_posts(string, pages=pages):
            print(post['text'][:50])


def main():
    facebookScraper = SocialScraper()
    facebookScraper.get_fb_profile('tom')
    print(facebookScraper.fb_data)


if __name__ == "__main__":
    main()