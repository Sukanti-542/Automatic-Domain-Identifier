from scrapy.crawler import CrawlerProcess

# import the defined spider
from domainspider.spiders.domainspider import DomainSpider

scraping_data = [
    {
        'domain': 'Computer Science',
        'url': '',
        'initial_page': 1,
        'final_page': 300
    },
    {
        'domain': 'Physics',
        'url': '',
        'initial_page': 1,
        'final_page': 200
    },
    {
        'domain': 'Chemistry',
        'url': '',
        'initial_page': 1,
        'final_page': 400
    },
    {
        'domain': 'Medical Science',
        'url': '',
        'initial_page': 1,
        'final_page': 600
    }
]

# Sample url has the format 'https://www.url.com/view&page='
# Initial_page and final_page are required for pages that have pagination. The spider is configured to
# automatically navigate through different pages based on this.
# The domain name specified will be the key against which all words are stored in the db

if __name__ == '__main__':
    print('Starting Main Program')
    # Define custom settings object. We will be using this for initiating the spider
    settings = {
        "BOT_NAME": 'domainspider',
        "SPIDER_MODULES": ['domainspider.spiders'],
        "NEWSPIDER_MODULE": 'domainspider.spiders',
        "USER_AGENT": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36' 'http://www.expedia.com',
        "ROBOTSTXT_OBEY": True,
        "DOWNLOADER_MIDDLEWARES": {
            'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
            'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
        },
        "ITEM_PIPELINES": {
            'domainspider.pipelines.DomainSpiderPipeline': 300,
        },
        "CONCURRENT_REQUESTS": 5

    }
    # Initiate process variable
    process = CrawlerProcess()

    # Iterate through the list scraping_data
    for data in scraping_data:
        # Define each process individually. Spider will internally form an array of process and run them one by one
        process = CrawlerProcess(settings)
        process.crawl(DomainSpider, domain=data['domain'], url=data['url'], initial_page=data['initial_page'],
                      final_page=data['final_page'])
    # Start the crawling
    process.start()
