import scrapy


class NovelSpiderSpider(scrapy.Spider):
    name = "novel_spider"
    allowed_domains = ["www.worldnovel.online"]
    start_urls = ["http://www.worldnovel.online/"]

    def start_requests(self):
        urls = [
            # Absolute Great Teacher
            "https://www.worldnovel.online/absolute-great-teacher/chapter-626-dark-great-teacher",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-625-sliding-into-the-dark-abyss",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-624-transforming-into-wind-ceremony-of-death",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-623-im-fighting-for-my-teacher",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-622-sorry-i-didnt-hold-back-enough-and-injured-you/",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-621-mysterious-species-of-darkness-strange-ability/",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-620-life-tutor-chicken-soup-for-the-soul/",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-619-xuanyuan-po-your-acting-skills-are-so-exaggerated/",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-618-gathering-of-geniuses/",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-617-sun-mos-on-the-spot-guidance/",
            "https://www.worldnovel.online/absolute-great-teacher/chapter-616-appreciation-of-a-major-character/",
            # Archean Eon Art
            "https://www.worldnovel.online/archean-eon-art/chapter-753-treatment/",
            "https://www.worldnovel.online/archean-eon-art/chapter-752-essence-soul-eighth-tribulation-lifeform/",
            "https://www.worldnovel.online/archean-eon-art/chapter-751-natural-accomplishment/",
            "https://www.worldnovel.online/archean-eon-art/chapter-750-more-than-ten-thousand-years-later/",
            "https://www.worldnovel.online/archean-eon-art/chapter-749-tenacity-of-life/",
            "https://www.worldnovel.online/archean-eon-art/chapter-748-the-fate-of-celestial-thearch-myriad-star-final-chapter-of-volume/",
            "https://www.worldnovel.online/archean-eon-art/chapter-747-first-meeting-with-fiend-mountains-owner/",
            "https://www.worldnovel.online/archean-eon-art/chapter-746-the-sound-on-the-mountaintop/",
            "https://www.worldnovel.online/archean-eon-art/chapter-744-half-step-eighth-eminence-meng-chuan/",
            "https://www.worldnovel.online/archean-eon-art/chapter-743-epiphany/",
            # Chaotic Sword God
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2958-seeing-he-qianqian-again",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2957-proceeding-to-the-heavenly-crane-clan/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2956-the-trade-association-of-five-regions/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2955-the-saint-monarch-passes/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2954-the-lightning-god-clan-retreats/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2953-reaching-the-ice-pole-plane/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2952-someone-to-run-errands/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2951-hitchhiking/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2950-grand-exalt/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2949-manifestation-of-the-ways/",
            "https://www.worldnovel.online/chaotic-sword-god/chapter-2948-l-ei-shiguang/",
            # Ranker’s Return
            "https://www.worldnovel.online/rkr/chapter-445",
            "https://www.worldnovel.online/rkr/chapter-444/",
            "https://www.worldnovel.online/rkr/chapter-443/",
            "https://www.worldnovel.online/rkr/chapter-442/",
            "https://www.worldnovel.online/rkr/chapter-441/",
            "https://www.worldnovel.online/rkr/chapter-440/",
            "https://www.worldnovel.online/rkr/chapter-439/",
            "https://www.worldnovel.online/rkr/chapter-438/",
            "https://www.worldnovel.online/rkr/chapter-437/",
            "https://www.worldnovel.online/rkr/chapter-436/",
            "https://www.worldnovel.online/rkr/chapter-435/",
            # The Rise of Phoenixes
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-204",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-203/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-202/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-201/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-200/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-199/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-198/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-197/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-196/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-195/",
            "https://www.worldnovel.online/the-rise-of-phoenixes/chapter-194/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        judul = response.url.split("/")[-3]
        chapter = response.url.split("/")[-2]
        filename = f"{judul}-{chapter}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
