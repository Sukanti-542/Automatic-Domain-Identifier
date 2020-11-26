import scrapy
from ..items import DomainSpiderItem
from scraper_api import ScraperAPIClient

# we are using scraper API for proxy here. Paste your auth key below
client = ScraperAPIClient('')


class DomainSpider(scrapy.Spider):
    name = 'domainspider'

    # The default constructor. This determines the initial start urls for the spider
    def __init__(self, domain='', url='', initial_page='', final_page='', *args, **kwargs):
        super(DomainSpider, self).__init__(*args, **kwargs)
        self.start_urls = []
        self.start_urls.append(client.scrapyGet(url=url + str(initial_page)))
        self.url = url
        self.final_page = final_page
        self.domain = domain
        self.initial_page = initial_page
        print(self.start_urls)

    # This parses the response, populates the items and generates the next page to be crawled
    def parse(self, response):
        items = DomainSpiderItem()
        print(self.domain)
        words = response.css('#searchContent a::text').extract()
        words_stripped = [st.strip() for st in words]
        items['domain'] = self.domain
        items['page'] = self.initial_page
        items['words'] = words_stripped

        yield items

        if self.initial_page < self.final_page:
            self.initial_page += 1
            next_page = client.scrapyGet(url=self.url + str(self.initial_page))
            print("next_page", next_page)
            # Crawl the next url
            yield response.follow(next_page, callback=self.parse)
