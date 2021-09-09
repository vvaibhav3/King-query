import scrapy

class MovieSpider(scrapy.Spider):
    name='movie'
    
    start_urls=[
        'https://rdxhd.cool/'
    ]
    
    def parse(self, response):
        
        data=response.xpath("//div[@class='ml-item']/a[@class='ml-mask jt']")
        for code in data:
            movie_name=code.xpath("@oldtitle").extract()
            movie_link=code.xpath("@href").extract()
            yield{
                'movie_names':movie_name,
                'movie_links':movie_link
            }