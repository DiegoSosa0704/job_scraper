# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Job(Item):
    title = Field()
    company = Field()
    location = Field()
    url = Field()
    salary = Field()
    tags = Field()
    date_posted = Field()
    crawl_timestamp = Field()
    job_board = Field()
    pass
