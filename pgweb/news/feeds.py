from django.contrib.syndication.feeds import Feed

from models import NewsArticle

from datetime import datetime, time

class NewsFeed(Feed):
	title = description = "PostgreSQL news"
	link = "http://www.postgresql.org/"

	description_template = 'news/rss_description.html'
	title_template = 'news/rss_title.html'

	def items(self):
		return NewsArticle.objects.filter(approved=True)[:10]

	def item_link(self, obj):
		return "http://www.postgresql.org/about/news/%s/" % obj.id

	def item_pubdate(self, obj):
		return datetime.combine(obj.date,time.min)

