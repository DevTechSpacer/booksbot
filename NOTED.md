# **App info & Development notes**

🪐🌍🔹

## How to run and deploy

### **𝟣. Running**

Run with saving scraped data to json or csv file:

```

scrapy crawl mytespider -o my_scraped_data.json
# or
scrapy crawl chocolatespider -o my_scraped_data.csv
```

### **𝟤. Deployment**

App is deployed on [Scrapy Cloud](https://app.zyte.com/)

```
$ pip install shub
$ shub login API key: apiKey
$ shub deploy appId
```

---

### **How to extend**

Generate s spider

```
scrapy genspider NAME_OF_SPIDER https://url.toscrape.com/
```

item\["product_link\] = quote.css('#product_list > li:nth-child(1) > a::attr(href)).getall() # Link

item\["product_name\] = quote.css('#product_list > li:nth-child(1) > h2 > a::attr(href)).getall() # Name

item\["product_price\] = quote.css('#product_list > li:nth-child(1) > div.product-bottom-box > div > span::text).getall() # Price

item\["product_image\] = quote.css('#product_list > li:nth-child(1) > div.image-block > a > img::attr(src)).getall() # Image

item\["product_producer\] = quote.css('#product_list > li:nth-child(1) > a::text).getall() # Producer

item\["product_on_stock \] = quote.css('#product_list > li:nth-child(1) > span::text).getall() # Skladem

### **Pagination**

> **Options:**
>
> 1.  [CSS selector to a href](https://scrapeops.io/python-scrapy-playbook/scrapy-pagination-guide/#2-follow-next-page-url-from-response)
> 2.  [From generated Sitemap](https://scrapeops.io/python-scrapy-playbook/scrapy-pagination-guide/#3-using-a-websites-sitemap)
> 3.  [Machine learning recognition](https://scrapeops.io/python-scrapy-playbook/scrapy-pagination-guide/#6-use-machine-learning-with-autopager)
>
> ```
> import autopager
> import requests
> autopager.urls(requests.get('http://quotes.toscrape.com'))
> ['http://quotes.toscrape.com/tag/obvious/page/1/', 'http://quotes.toscrape.com/tag/simile/page/1/', 'http://quotes.toscrape.com/page/2/']
> ```
>
> 1.  Alternatively [Scrape all pages](https://scrapeops.io/python-scrapy-playbook/scrapy-pagination-guide/#4-using-crawlspider) (without pagination)

---

### **Hints**

#### Create PostgreSQL table for scraped data

```
CREATE TABLE IF NOT EXISTS chocolate_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price VARCHAR(255),
    url TEXT
);
```

#### List installed pip packages

```
pip list
```

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600&display=swap'); .viaxlsx p {border-bottom:1px solid #66ddff!important;font-family: 'Quicksand', sans-serif; font-weight: 500;} p {font-size: 14px; font-family:monospace;}
