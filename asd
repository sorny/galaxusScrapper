Dockerized scrapper for discounted articles over at galaxus.ch

build it:
docker build -t galaxusscrapper .

run it:
docker run -d \
  --name galaxusscrapper \
  -p 9080:9080 \
  galaxusscrapper:latest

query it:
curl "http://localhost:9080/crawl.json?start_requests=true&spider_name=galaxus"