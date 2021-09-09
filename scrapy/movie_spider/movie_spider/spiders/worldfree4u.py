import scrapy

class Worldfree4u(scrapy.Spider):
    name='worldfree4u'
    start_urls=[
        'https://world4ufree.pro/page/374/'
    ]
    
    def parse(self, response):              
        data=response.xpath("//main[@class='content']/article/header[@class='entry-header']/h2[@class='entry-title']")
#        yield{'data':data}
        for code in data:
            movie_name=code.xpath("a[@class='entry-title-link']/text()").extract()
            movie_link=code.xpath("a[@class='entry-title-link']/@href").extract()
            yield{
                'movie_names':movie_name,
                'movie_links':movie_link
            }
            
        next_page=response.xpath("//div[@class='archive-pagination pagination']/ul/li[@class='pagination-next']/a/@href")[0].extract()
#        yield{'next':next_page}
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)