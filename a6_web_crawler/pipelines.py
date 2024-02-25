# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class A6WebCrawlerPipeline:
    def process_item(self, item, spider):
        return item

class TxtExportPipeline:

    def open_spider(self, spider):
        self.file = open('temp_output.txt', 'w')
        self.nodes = set()
        self.edges_count = 0

    def close_spider(self, spider):
        self.file.close()
        nodes_count = len(self.nodes)
        edges_count = self.edges_count

        with open("web-crawler-output.txt", "w") as final_output, open("temp_output.txt", "r") as temp_output:
            final_output.write("# Directed graph (each unordered pair of nodes is saved once): web-crawler-output.txt \n")
            final_output.write("# Web Crawler Output for COMP-4800 A6 Assignment by Kap Thang, Shubham Mehta\n")
            final_output.write(f"# Nodes: {nodes_count}\tEdges: {edges_count}\n")
            final_output.write("# FromNodeId\tToNodeId\n")
            final_output.write(temp_output.read())

    def process_item(self, item, spider):
        self.nodes.add(item['source'])
        # self.nodes.add(item['target'])
        self.edges_count += 1
        line = f"{item['source']} {item['target']}\n"
        self.file.write(line)
        return item