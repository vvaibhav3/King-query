import scrapy

class ExtraMovieSpider(scrapy.Spider):
    name='extramovie'
    
    start_urls=[
        'http://extramovies.host/'
    ]
    
    def parse(self, response):   
        data=response.xpath("//div[@class='imag']/div[@class='thumbnail']")
        for code in data:
            movie_name=code.xpath("a/@title").extract()
            movie_link=code.xpath("a/@href").extract()
            yield{'movie_names':movie_name,
            'movie_links':movie_link}
        
        next_page=response.xpath("//div[@class='wp-pagenavi']/a[@class='next page-numbers']/@href")[0].extract() 
#        yield{'next_page':next_page}    
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)      