SERP Screenshot Module
======================

This Python module uses Chromedriver as headless browser to make screenshots of
the first SERP on Google and/or Bing engine for a set of keywords which can be specified by the user.


## Installation guide

You will need to have a running Python distribution as well as Chromedriver installed (get it on https://sites.google.com/a/chromium.org/chromedriver/).

The following Python package will have to be installed in order to run:  
- selenium (see http://selenium-python.readthedocs.io/installation.html)

## How to run

Running the module is simple. The only thing you need to add to the folder is a file named "keyword_data.tsv" holding all the relevant keywords in a column named "keyword". (It doesn't matter if there are any other columns in the table. The code will just look for all the keywords in the keyword column.)

1. Open your preferred terminal and navigate to the folder where the module is saved. (On Windows, you can use Powershell and type ``cd "path/to/file"``)
2.  Run it by typing ``python .\screenshot.py``.

A new folder should then appear in your directory, labeled by the current date and time. It holds one subfolder per engine in which you should be able to find the screenshots.

## Advances settings

There are a few more settings you can change directly in the PY file (in the "change settings here" section).

1. Exclude engines: Commenting out either Bing or Google in the ENGINES list excludes them from screenshot making.
2. Language settings: The default is set to English ("-lang=en-GB") but you can change it according to the target search language.
3. Change window size: If you don't need the whole SERP page, you can specify the window size the screenshots will have by adjusting the numbers (width, height in pixels) in SCREENSHOT_SIZE.
4. Additionally to the 'keyword_data' file, you might want to add a file labeled 'manually_added_keywords.tsv' which holds additional keywords you want to scrape. This is particularly useful if you get a set of currently trending keywords directly from a database and still want to have some additional keywords to be always taken into consideration.  
