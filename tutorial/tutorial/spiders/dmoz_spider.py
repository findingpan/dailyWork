from scrapy.spider import BaseSpider 
  
class DmozSpider(BaseSpider): 
    name = "dmoz" 
    allowed_domains = ["ncich.com.cn"] 
    start_urls = [ 
        "http://www.ncich.com.cn/?page_id=7329", 
        "http://www.ncich.com.cn/?page_id=1294" 
    ] 
  
    def parse(self, response): 
        filename = response.url.split("/")[-2] 
        open(filename, 'wb').write(response.body) 