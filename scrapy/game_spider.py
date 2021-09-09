#first spider for one page of ocean of games
import scrapy

class GameSpider(scrapy.Spider):
    
#    note :- these first variable name should same
#    name of the spider
    name='game'
    
#    urls that is required to scrap
    start_urls=[
        'http://oceanofgames.com/'
    ]
    
#    this is function for getting code and scrape data
#response parameter contains source code of webpage
#self is just instance


    def parse(self, response):
        game_names=response.css("div.post-details h2.title a::text").extract()
        links_of_game=response.css("div.post-details h2.title a::attr(href)").extract()
#        link=response.xpath("//div.post-details/a/@href")
        yield{'Names':game_names,
              'links':links_of_game,
#              'done':link
             }
    
#extract() is method for extracting our founded data
#yield is for returning data