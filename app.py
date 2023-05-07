from flask import Flask, render_template
import feedparser

app = Flask(__name__, static_url_path='/blog/static')

@app.route('/blog/')
def index():
    # Parse the RSS feed
    feed = feedparser.parse('http://jregenstein.com/feed')

    # Build the HTML response
    html = '<h1>{}</h1>'.format(feed.feed.title)
    html += '<ul>'
    for entry in feed.entries:
        html += '<li><a href="{}">{}</a></li>'.format(entry.link, entry.title)
    html += '</ul>'

    return render_template('index.html', content=html)

if __name__ == '__main__':
    app.run(port=8000)
