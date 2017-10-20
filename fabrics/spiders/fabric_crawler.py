import scrapy
import json
import codecs
import shutil
import os
from bs4 import BeautifulSoup


class CoreSpider(scrapy.Spider):
    name = "fabrics"

    def start_requests(self):
        urls = []
        with open("../china_fabrics.json", "r") as infile:
            fabrics = json.loads(infile.read())
            for item in fabrics:
                urls.append(item['website'])
        print(urls)

        for url in urls:
            b = scrapy.Request(url=url, callback=self.parse)
            if "ENGLISH" in b.body or "English" in b.body:
                url = 
                response = scrapy.Request(url=)

    def parse(self, response):

        page = response.url.split("//")[-1]
        if not os.path.isdir("core_pages"):
            os.makedirs("core_pages")

        filename = 'core_pages/fabric_%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


    def parse1(self, response):
        pass

    def save_data(self, website):
        pass