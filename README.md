# GalaxusScrapper
### Version 0.1

Galaxusscrapper is web-scrapping spider based on scrapy.
Its dockerized and offers a REST api based on scrapyrt for convenience :)


# Main Features:

  - Get the latest 250 discounted products on galaxus.ch, their current price and other metadata
Example response:
```
{
	"status": "ok",
	"items": [
		{
			"name": <name of the product>,
			"product_type": <product category or type>,
			"price": <current price>,
			"orig_price": <original price>,
			"discount": <discount in %>,
			"image_src": <image src>,
			"link": <link to article>
		},
        ...
	],
	"items_dropped": [
	],
	"stats": {
	},
	"spider_name": "galaxus"
}
```


### Tech

GalaxusScrapper uses open source libs and open data to work properly:

* [scrapy](https://github.com/scrapy/scrapy) - a fast high-level web crawling & scraping framework for Python
* [scrapyrt](https://github.com/scrapinghub/scrapyrt) - Scrapy realtime
* [Unidecode](https://pypi.org/project/Unidecode/) - ASCII transliterations of Unicode text


# Installation
1) Build the docker container
```sh
docker build -t galaxusscrapper .
```
2) Run the container
```sh
docker run -d \
  --name galaxusscrapper \
  -p 9080:9080 \
  galaxusscrapper:latest
```
3) Enjoy scrapping and gettin the latest discounted products :)
```sh
curl "http://localhost:9080/crawl.json?start_requests=true&spider_name=galaxus"
```


Have fun and use with care, don't flood galaxus with price polls every second! Pretty please!

License
----

MIT

**Free Software, Hell Yeah!**
