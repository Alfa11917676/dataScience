import scrapy
import re
import requests
import os
import json
class crawler(scrapy.Spider):
    i=0
    name = 'pep'
    BASE_DIR= 'F:\\dataScience\\crawler\\pepper\\'
    Limit=20
    def start_requests(self):
        baseurl='https://www.pepperfry.com/site_product/search?q='
        items=['king bed','queen bed','tea table','study table','dinning table','almirah','sofa set','couch','easy chair','office chairs','crib']
        urls=[]
        directories=[]
        for item in items:
            Uurl = '+'.join(item.split(" "))
            Udir = "-".join(item.split(" "))
            urls.append(baseurl + Uurl)
            directories.append(Udir)
            directoryPath = self.BASE_DIR + Udir
            if not os.path.exists(directoryPath):
                os.mkdir(directoryPath)
        for i in range(len(urls)):
            d={
                'Dir-Name':directories[i]
            }

            resp=scrapy.Request(url=urls[i],callback=self.parse,dont_filter=True)
            resp.meta['Dir-Name']=directories[i]
            yield resp
    def parse(self, response,**meta):

        product_url=response.css(".clip-prd-dtl::attr(href)").extract()
        #print(product_url)
        counter=0
        for url in product_url:
            resp=scrapy.Request(url=url,callback=self.parse_items,dont_filter=True)
            resp.meta['Dir-Name']=response.meta['Dir-Name']
            if counter==self.Limit:
               break
            if not resp != None:
                counter+=1
            yield resp
    def parse_items(self,response):
        print("Inside parse_items")
        item_name=response.css('.v-pro-ttl::text').extract()
        item_price=response.css('.v-offer-price-amt::text').extract()
        items_savings=response.css('.total_saving::text').extract()[0].strip()
        item_description=response.css('.v-pro-ttl::text').extract()
        item_detail_key=response.xpath('//div[@id=itemDetails]/p/b/text()').extract()
        item_detail_values=response.xpath('//div[@id=itemDetails]/p/text()').extract()
        brand=response.xpath('//span[@itemprop="brand"]/text()').extract()
        item_detail_values[0]=brand[0]
        stop_words= ["(all dimensions in inches)","(all dimensions in inches)","(all dimenstions in inches)"]
        item_detail_values=[words.strip() for words in item_detail_values if words not in stop_words]
        a=len(item_detail_key)
        b=len(item_detail_values)
        idetail={}
        for i in range(min(a,b)):
            idetail[item_detail_key[i]]=item_detail_values[i]
        stop_items=['pepperfry.com','We also offer you a','So go ahead and buy with confidence','Brand will upfront contact you for assembly']
        item_description=filter(lambda x:all([not y.lower() in x.lower() for y in stop_items]),item_description)
        item_description='\n'.join(item_description)
        image_url_list=response.xpath('//li[aclass="vip-option-slideeach"]/a/@data-img').extract()
        if (len(image_url_list)>3):
            d={
                'Item-title':item_name,
                'Item-description':item_description,
                "Item-Price":item_price,
                "Savings":items_savings,
                "Details":idetail}
            CATEGORY_NAME=response.meta['dir_name']
            ITEM_DIR_URL=os.path.join(self.BASE_DIR,os.path.join(CATEGORY_NAME,item_name))
            if not os.path.exists:
                os.makedirs(ITEM_DIR_URL)
            with open (os.path.join(ITEM_DIR_URL,"metaData.txt"),'w') as f:
                json.dump(d,f)
            for i, image_url in enumerate(image_url_list):
                r=requests.get(image_url)
                with open(os.path.join(ITEM_DIR_URL,"image_{}.jpg".format(i)),'wb') as f:
                    f.write(r.content)
            print("Successfully saved"+item_name+"data at:"+ITEM_DIR_URL)
            yield d
        yield None