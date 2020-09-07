import scrapy
import unidecode
from scrapy import Selector


def sanatize(subject, content):
    if content:
        content = unidecode.unidecode(
            content.strip().replace('\n', '').replace('\r', '').replace('statt ', '').replace('.–', '').replace(
                '"', '').replace('”', ''))
    else:
        content = 'unknown-' + subject
    return content


class GalaxusSpider(scrapy.Spider):
    name = "galaxus"
    base_url = "https://www.galaxus.ch/"

    def start_requests(self):
        # Take param is the amount of articles to load
        url = self.base_url + "/de/Sale?take=250&so=12"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.body)
        articles = response.xpath('//div[@class="products-wrapper"]//article').getall()
        for row in articles:
            # print(row)
            sel = Selector(text=row)
            try:
                brand = sanatize('brand',
                                 sel.xpath('//h5/span/text()').get())
                product = sanatize('product',
                                   sel.xpath('//h5/text()').getall()[
                                       1])
                name = brand + ' ' + product
            except Exception:
                name = sanatize('name',
                                sel.xpath('//h5/text()').get())

            product_type = sanatize('product_type', sel.xpath(
                '//span[@class="product-type"]/a/text()').get())

            price = float(sanatize('price', sel.xpath('//div[@class="product-price"]/text()').getall()[1]))

            orig_price = float(sanatize('orig_price', sel.xpath(
                '//div[@class="product-price"]/span[@class="product-price-appendix"]/text()').get()))

            discount = 100 - price / orig_price * 100

            image_src = sanatize('image_src', sel.xpath(
                '//noscript/img/@src').get())

            link = sanatize('link', self.base_url + sel.xpath(
                '//a[contains(@class, "product-overlay")]/@href').get())

            yield {
                'name': name,
                'product_type': product_type,
                'price': price,
                'orig_price': orig_price,
                'discount': discount,
                'image_src': image_src,
                'link': link
            }
