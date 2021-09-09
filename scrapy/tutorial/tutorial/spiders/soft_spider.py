#first spider for one page of ocean of games
import scrapy

class SoftSpider(scrapy.Spider):
    
#    note :- these first variable name should same
#    name of the spider
    name='software'
    
#    urls that is required to scrap
    start_urls=[
        'https://getintopc.com/'
    ]
    
#    this is function for getting code and scrape data
#response parameter contains source code of webpage
#self is just instance


    def parse(self, response):
        data=response.css("div.post-details h2.title")
        for a in data:
            soft_names=a.css("a::text").extract()
            link_of_soft=a.css("a::attr(href)").extract()
            
            yield{'Names':soft_names,
                 'links':link_of_soft}
        next_page=response.xpath("//div[@class='page-navi pagination numbers  clear-block']/a[@class='next']/@href")[0].extract()
#        yield{'next_link':next_page}
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
#        links_of_game=response.css("div.post-details h2.title a::attr(href)").extract()  
#        for b in links_of_game:
#            yield{'links':b
#                 }
    
#extract() is method for extracting our founded data
#yield is for returning data