# Simple Page Analyzer

This is a relatively simple Python script that analyzes the content of a hosted web page. It does the following:

- Captures the page URL and page title.
- Parses the page content.
- Finds the overall content sentiment.
- Finds the top 10 keywords. (For each keyword, shows the part of speech, number of occurrences, and the overall density.)
- Finds all links with fully-formed URLs (internal and external).
- Exports the page analysis in either HTML or Markdown format.

I created the script to demonstrate how a few Python packages can quickly introduce some powerful NLP processing features without a lot of extra coding. (I'm not a great programmer; if I can create a script like this, then any technically oriented person should be able to follow my example and write a similar script.) This doesn't break any ground or show best cases usage. It's just to show some simple features in a single script. (I showed this script to an engineer at an AI-focused company, and his response was, "*Oh. This is an old school NLP approach.*")

I had a twofold guideline while creating the analyzer script.

1. Use only common Python packages that could introduce powerful NLP capabilities.
2. Do not bloat my local system or requiring a large dependency chain. (If you've ever installed [rake-nlkt](https://pypi.org/project/rake-nltk/), then you know what I mean. It's powerful, handles sentences, and is more customizable, but it comes with a lot of dependencies.)

I used the following packages to get these features:

| Package Name                                                | Description
|:---                                                         |:---
| [requests](https://pypi.org/project/requests/)              | Requesting a valid web page (by specific URL).
| [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)  | Parsing and extracting HTML content, including named elements like links.
| [TextBlob](https://pypi.org/project/textblob/)              | Analyzing page sentiment and tagging parts of speech (POS).
| [NLTK](https://pypi.org/project/nltk/)                      | Tokenizes text, remove common words from analysis, tag the parts of speech, and calculates keyword frequency.


## Run the Page Analyzer Script

1. Install the requirements. (This step is necessary only if you do not have the packages installed already.)

   ```
   pip install -r requirements.txt
   ```

2. If this is the first time using the NLTK, you might need to enter the following commands. Otherwise, skip this step.
   ```
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

3. Run the script.
   ```
   python simple_analyzer.py
   ```

4. When prompted, enter a fully-formed HTTP or HTTPS web page address. For example, enter something like the following:
   ```
   https://bfro.net/ 
   ```

5. Enter an output format: `html` or `md`.

## Script Output

The script generates a page analysis report in either HTML or Markdown format.

|HTML Example Output | Markdown Example Output
|--|--
|![html.png](html.png "HMTL version") |![md.png](md.png "HMTL version")

The output file name appends a clean version of page title to `page_analysis_` and adds the appropriate file extension. For example, for the https://bfro.net/, the page title is *Bigfoot Field Researchers Organization*, or it was at the time of the last update to the page. If you opted for markdown format, then the resulting file name would be something like `page_analysis_Bigfoot_Field_Researchers_Organization.md`.

Here are some suggested pages to use for the script:

**Positive Sentiment**

- https://www.intel.com/content/www/us/en/developer/articles/technical/3-ways-to-get-started-with-oneapi-code-samples.html
- https://code.visualstudio.com/docs
- https://bfro.net/
   
**Negative Sentiment**
- https://www.microsoft.com/en-us/windows/business/c/windows-11-pro-intel-vpro


## Clean Up

When you are done, you can remove the installed packages installed for this example by entering the following command:
```
pip uninstall -y -r requirements.txt
```
Enjoy!