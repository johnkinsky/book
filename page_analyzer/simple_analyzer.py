# Script to analyze a single page for content, sentiment, keywords, and links to resources.

# Install required packages:
# pip install -r requirements.txt
# Uninstall packages if needed:
# pip uninstall -y -r requirements.txt

import requests
import nltk
import re
from bs4 import BeautifulSoup
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from urllib.parse import urlparse

# Part of speech (POS) mapping to human-readable descriptions
POS_MAP = {
    'NN': 'Noun',
    'NNS': 'Plural Noun',
    'NNP': 'Proper Noun',
    'NNPS': 'Plural Proper Noun',
    'VB': 'Verb (base)',
    'VBD': 'Verb (past)',
    'VBG': 'Verb (gerund)',
    'VBN': 'Verb (past participle)',
    'VBP': 'Verb (present)',
    'VBZ': 'Verb (3rd person)',
    'JJ': 'Adjective',
    'JJR': 'Comparative Adjective',
    'JJS': 'Superlative Adjective',
    'RB': 'Adverb',
    'RBR': 'Comparative Adverb',
    'RBS': 'Superlative Adverb',
    'IN': 'Preposition',
    'DT': 'Determiner',
    'PRP': 'Pronoun',
    'PRP$': 'Possessive Pronoun',
    'CC': 'Coordinating Conjunction',
    'CD': 'Cardinal Number',
    'EX': 'Existential There',
    'FW': 'Foreign Word',
    'LS': 'List Item Marker',
    'MD': 'Modal',
    'PDT': 'Predeterminer',
    'POS': 'Possessive Ending',
    'RP': 'Particle',
    'SYM': 'Symbol',
    'TO': 'To',
    'UH': 'Interjection',
    'WDT': 'Wh-determiner',
    'WP': 'Wh-pronoun',
    'WP$': 'Possessive Wh-pronoun',
    'WRB': 'Wh-adverb'
}

def get_url():
    url = input("Enter a valid http or https URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with http:// or https://")
    return url

def sanitize_filename(text): # Clean up the URL to use for file naming
    return re.sub(r'[^\w\-_. ]', '', text).replace(' ', '_')

def scrape_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    # Get the page title to disambiguate page results
    title = soup.title.string.strip() if soup.title and soup.title.string else "untitled"

    base_netloc = urlparse(url).netloc
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        parsed_href = urlparse(href)
        if parsed_href.scheme in ['http', 'https'] and parsed_href.netloc and parsed_href.netloc != base_netloc:
            links.append(href)
    return text, links, title

def analyze_text(text):
    blob = TextBlob(text)
    tone = "Positive 😊" if blob.sentiment.polarity > 0 else "Negative 😞" if blob.sentiment.polarity < 0 else "Neutral 😐"
    words = word_tokenize(text.lower())
    filtered_words = [w for w in words if w.isalpha() and w not in stopwords.words('english')]
    total_words = len(filtered_words)
    freq = nltk.FreqDist(filtered_words)
    top_keywords = freq.most_common(10)
    tagged_words = dict(nltk.pos_tag(filtered_words))
    keyword_data = [
        (
            word,
            count,
            round((count / total_words) * 100, 1),
            POS_MAP.get(tagged_words.get(word, 'UNK'), 'Unknown')
        )
        for word, count in top_keywords
    ]
    return tone, keyword_data


def write_html(url, tone, keywords, links, title):
    keyword_list = ''.join(
        f"<tr><td><b>{word}</b></td><td>{pos}</td><td>{count}</td><td>{density}%</td></tr>"
        for word, count, density, pos in keywords
    )
    link_list = ''.join(f'<li><a href="{link}" target="_blank">{link}</a></li>' for link in links)

    html_content = f"""
    <html>
    <head>
    <title>Page Analysis of {title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sansation:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">
    <style>
    body {{margin: 50px 50px 50px 50px;}}
    h1, h2, p, a, ul, li, th, td {{font-family: 'Sansation', sans-serif;}}
    html {{background-image: linear-gradient(135deg, white 75%, blue);}}
    table, th, td, tr {{border: 1px solid black; text-align: center; border-collapse: collapse; padding: 5px;}}
    </style>
    </head>
    <body>
        <h1>Page Analysis</h1>
        <h2>URL</h2> 
        <p><a href="{url}" target="_blank">{url}</a></p>
        <h2>Page Title</h2>
        <p>{title}</p>
        <h2>Detected Tone</h2>
        <p>{tone}</p>
        <h2>Top Keywords (no more than 10)</h2>
        <table><tr><th>Keyword</th><th>Part of Speech (?)</th><th>Count</th><th>Density</th></tr>
        {keyword_list}</table>
        <h2>External Links Found</h2>
        <ul>{link_list}</ul>
    </body>
    </html>
    """

    safe_title = sanitize_filename(title)
    filename = f"page_analysis_{safe_title}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML formatted page analysis written to {filename}")

def write_markdown(url, tone, keywords, links, title):
    keyword_lines = '\n'.join(
        f"|**{word}**|{pos}|{count}|{density}%"
        for word, count, density, pos in keywords
    )
    link_lines = '\n'.join(f"- [{link}]({link})" for link in links)

    md_content = f"""# Page Analysis
## URL
{url}

## Page Title
{title}

## Detected Tone
{tone}

## Top Keywords (no more than 10)
|Keyword|Part of Speech (?)|Count|Density
|:--- |:--- |:--- |:---
{keyword_lines}

## External Links Found
{link_lines}
"""
    safe_title = sanitize_filename(title)
    filename = f"page_analysis_{safe_title}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Markdown formatted page analysis written to {filename}")

def main():
    try:
        url = get_url()
        text, links, title = scrape_content(url)
        tone, keywords = analyze_text(text)

        format_choice = input("Export format? (html/md): ").strip().lower()
        if format_choice == "html":
            write_html(url, tone, keywords, links, title)
        else:
            write_markdown(url, tone, keywords, links, title)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
