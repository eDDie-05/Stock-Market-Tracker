import feedparser

feed = feedparser.parse(
    "https://finance.yahoo.com/rss/topstories"
)

for item in feed.entries[:10]:
    print(item.title)