import scrapy


class NovelSpiderSpider(scrapy.Spider):
    name = "novel_spider"
    allowed_domains = ["www.worldnovel.online"]
    start_urls = ["http://www.worldnovel.online/"]

    def start_requests(self):
        urls = [
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2958-seeing-he-qianqian-again",
            "https://www.worldnovel.online/rkr/chapter-445",
            "https://www.worldnovel.online/archean-eon-art/chapter-753-treatment",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-626-dark-great-teacher",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-204",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        judul = response.url.split("/")[-3]
        chapter = response.url.split("/")[-2]
        filename = f"Novel-{judul}-{chapter}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
