from crawl import DataCrawler
from plot import Plot

if __name__ == '__main__':
    DataCrawler().start(store=True)
    Plot().start()
