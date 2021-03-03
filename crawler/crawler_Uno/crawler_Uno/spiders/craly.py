import scrapy

class  Qutoes_spider(scrapy.Spider):
    name='quotesData'
    def start_requests(self):
        urls=['https://www.pepperfry.com/site_product/search?q=sofa+set&as=0&src=os',
]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response, **kwargs):
        page_number=response.url.split('/')[-2]
        fileName='quotes%s.html'%page_number


        for data in response.css("div.pf-col xs-12"):
            name = data.css('h2::text').get()
            price = data.css('span.clip-offr-price::text').get()
            cashback = data.css('div.clip__caskback-text::text').get()

            yield {
                'text':name
                ,'author':price
                ,'tags':cashback
            }