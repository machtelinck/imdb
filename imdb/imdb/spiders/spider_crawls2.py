import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class CrawlerBooksSpider(CrawlSpider):
    name = 'crawler_books'
    allowed_domains = ['imdb.com']

  
    
   
class SpiderCrawlsSpider(CrawlSpider):
    name = 'spider_crawls2'
    allowed_domains = ['www.imdb.com']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    rules = (
        Rule(LinkExtractor(restrict_xpaths = "/html/body/div[2]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr/td[2]/a"), callback='parse_item', follow=True),
    )
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250', headers={
            'User-Agent': self.user_agent
        })
        

        
    
    
    

 
    
    
    
    
    def parse_item(self, response):
        """ duree = 0
        if len(response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/text()").getall()) == 5:
            duree = int(response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/text()").getall()[0]) * 60 + int(response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/text()").getall()[3])
        else:
            duree = int(response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/text()").getall()[0])
 """    
        duree = response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[4]/text()").getall()
        if len(duree)==5:
            duree = int(duree[0])*60+int(duree[3])
        else:
            duree = int(duree[0])
        yield{
        'title':response.xpath("//h1/text()").get(),
        'Score' : response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]/text()").get(), #ok
        'Genre' : response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/div[2]/a/span/text()").extract(), # ok 
        'Date': response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]/a/text()").get(), # ok 
        'duree' : duree,
        'Descriptions':response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[3]/text()").get(), #" ok "
        'Acteurs': response.xpath("/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[3]/ul/li/div/ul/li/a/text()").extract(), 
        'Public' : response.xpath("//html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/a/text()").get(), 

        }


"""     def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents)
 """
"""     def parse_dir_contents(self, response):
      for sel in response.xpath('//ul/li'):
         item = DmozItem()
         item['title'] = sel.xpath('a/text()').extract()
         item['link'] = sel.xpath('a/@href').extract()
         item['desc'] = sel.xpath('text()').extract()
         yield item """
