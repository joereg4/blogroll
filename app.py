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

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
