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
        self.file = open('output_temp.txt', 'w')
        self.nodes = set()
        self.edges_count = 0

    def close_spider(self, spider):
        self.file.close()
        nodes_count = len(self.nodes)
        edges_count = self.edges_count

        with open("output_final.txt", "w") as output_final, open("output_temp.txt", "r") as output_temp:
            output_final.write("# Directed graph (each unordered pair of nodes is saved once): output_final.txt \n")
            output_final.write("# Web Crawler Output for COMP-4800 A6 Assignment by Kap Thang, Shubham Mehta\n")
            output_final.write(f"# Nodes: {nodes_count}\tEdges: {edges_count}\n")
            output_final.write("# FromNodeId\tToNodeId\n")
            output_final.write(output_temp.read())

    def process_item(self, item, spider):
        self.nodes.add(item['source'])
        # self.nodes.add(item['target'])
        self.edges_count += 1
        line = f"{item['source']} {item['target']}\n"
        self.file.write(line)
        return item