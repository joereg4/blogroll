""" from flask import Flask
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    # Parse the RSS feed
    feed = feedparser.parse('http://jregenstein.com/feed')

    # Build the HTML response
    html = '<h1>{}</h1>'.format(feed.feed.title)
    html += '<ul>'
    for entry in feed.entries:
        html += '<li><a href="{}">{}</a></li>'.format(entry.link, entry.title)
    html += '</ul>'

    return html

if __name__ == '__main__':
    app.run() """

from flask import Flask
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    base_url = 'http://jregenstein.com/feed'
    page = 1
    max_pages = 5  # Set the maximum number of pages you want to fetch
    entries = []

    while page <= max_pages:
        feed = feedparser.parse(f'{base_url}?page={page}')

        if not feed.entries:
            break

        entries.extend(feed.entries)
        page += 1

    # Build the HTML response
    html = '<h1>{}</h1>'.format(feed.feed.title)
    html += '<ul>'
    for entry in entries:
        html += '<li><a href="{}">{}</a></li>'.format(entry.link, entry.title)
    html += '</ul>'

    return html

if __name__ == '__main__':
    app.run()
