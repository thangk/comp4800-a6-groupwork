# COMP-4800 A6 Assignment

## Group memebers: Kap Thang, Shubham Mehta

---

### Install scrapy framework with pip

```
pip install scrapy
```

<br>

### To run, navigate inside project folder `a6_web_crawler` and run,

```
scrapy crawl toscrape-crawler
```

<br>

### Adjust nodes limit

In `a6_web_crawler/spiders/toscrape_crawler.py` by changing the `self.nodes_limit` value.
Note: `-1 = unlimited nodes`.
