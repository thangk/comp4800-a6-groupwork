from scrapy import Spider, Request
from a6_web_crawler.items import LinkGraphItem
from scrapy.exceptions import CloseSpider

class ToscrapeCrawlerSpider(Spider):
    name = "toscrape-crawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_counter = 0
        self.url_to_id = {}
        self.nodes = set()
        self.nodes_with_children = set()  # Track nodes that have outgoing edges
        self.nodes_without_children = set()  # Track nodes without outgoing edges (leaf nodes)
        self.nodes_limit = 10  # -1 for no limit
        self.processed_links = set()

    def parse(self, response):
        if response.url not in self.url_to_id:
            self.url_to_id[response.url] = self.id_counter
            self.nodes.add(self.id_counter)
            self.id_counter += 1

        source_id = self.url_to_id[response.url]
        has_children = False  # Assume no children until found

        for href in response.css("a::attr(href)").extract():
            target_url = response.urljoin(href)
            if target_url not in self.url_to_id:
                self.url_to_id[target_url] = self.id_counter
                self.nodes.add(self.id_counter)
                self.id_counter += 1

            target_id = self.url_to_id[target_url]
            if (source_id, target_id) not in self.processed_links:
                self.processed_links.add((source_id, target_id))  # Mark this pair as processed
                yield LinkGraphItem(source=source_id, target=target_id)
                has_children = True  # Found a child node
                self.nodes_with_children.add(source_id)  # Mark source node as having outgoing edges

                if self.nodes_limit == -1 or len(self.nodes) <= self.nodes_limit:
                    yield Request(target_url, callback=self.parse)

        if not has_children:
            # If no children found for this node, it's a leaf node
            self.nodes_without_children.add(source_id)

    def close_spider(self, spider):
        pass
