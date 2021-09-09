import scrapy


class BestWap(scrapy.Spider):
    name='song'
    start_urls=[
        'https://downloadming.onl/bollywood-mp3'
    ]
    
#    flag=1 
    
    def parse(self, response,flag=1):
        if flag == 1:
            category=response.xpath("//table/tbody/tr/td/h2/strong")
        def parse(self, response):
            data2=response.xpath("//div[@class='entry clearfix']/ul[@class='lcp_catlist']/text()").extarct()
            yield{'data':data2}
        #        yield{'data':category}
#        for cat in category:
#            links_of_cat=cat.xpath("h2/strong/a/@href")[0].extract()
#            yield{'category ':links_of_cat}
        for data in category:
            cat=data.xpath("a/@href")[0].extract()

            if cat is not None:
                print(cat)
                flag = 0
#                data()
                link_of_page=response.urljoin(cat)
                yield scrapy.Request(url=link_of_page, callback=self.parse)
                