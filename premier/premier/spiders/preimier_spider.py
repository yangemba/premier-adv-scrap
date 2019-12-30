import scrapy
import bs4
import requests


class BlogSpider(scrapy.Spider):
    name = 'premier'
    # start_urls = ['https://blog.scrapinghub.com']
    url = 'https://premier.ua/zhilaia-nedvizhimost/'
    list_names2 = []

    def get_lin_list(self):
        response = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(response.text, "html.parser")
        # self.name_area = self.soup.find(id="CategoryHeader120")
        # self.name = self.soup.find(id='headerItema')
        self.list = [f"https://premier.ua/{x.attrs['href']}" for x in
                     self.soup.select('.catlist a')]
        self.list_names = [f"{x.attrs['title']}" for x in
                           self.soup.select('.catlist a')]

        dict_linksname = self.list_names2[1:]
        print(dict_linksname)
        return dict_linksname  # self.name

    def parse_category(self):
        for link in self.get_lin_list():
            yield requests.get(link)

    def parse(self, response=parse_category()):



