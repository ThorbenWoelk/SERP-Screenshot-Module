"""
This Python module uses Chromedriver (get it on
https://sites.google.com/a/chromium.org/chromedriver/) to make screenshots of
the first Google SERP for a specific range of keywords defined below.

The following Python package will have to be installed in order to run:
- selenium (see http://selenium-python.readthedocs.io/installation.html)
"""

# import packages needed
import os
import datetime
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from depot.manager import DepotManager

# define constants and settings
CHROME_ARGS = [
'--headless', # comment out if you want chromedriver to use the GUI
'--lang=de-de', # choose your language settings (e.g. --lang=de-de, --lang=en-GB, --lang=fr-fr)
'--disable-gpu' # a workaround for known bug of chromedriver on Windows. Do not comment out.
]
SCREENSHOT_SIZE = (1280, 3000)
IN_FILE = 'keyword_data.tsv'
ENGINES = [
'Google', # comment out if no screenshot is needed for the respective engine
'Bing'
]

def get_keywords(in_file):
    """define search terms to make screenshots for"""
    list_of_keywords = []
    with open(in_file) as csvfile:
         reader = csv.DictReader(csvfile, delimiter='\t')
         for row in reader:
         # append your lists
            list_of_keywords.append(row['keyword'])
    return list_of_keywords

def create_file_location(for_engines):
    """create new folder labeled by date and subfolder for search engine"""
    now = datetime.datetime.now()
    directory = now.strftime("%Y-%m-%d_%H-%M")
    if not os.path.exists(directory):
        os.makedirs(directory)
        if 'Google' in for_engines:
            os.makedirs(directory+'\\Google')
        if 'Bing' in for_engines:
            os.makedirs(directory+'\\Bing')
    return (directory, now)

def make_screenshot(keyword_data, chrome_args, size, engines):
    """make screenshots for a set of input keywords"""
    # get keywords
    keywords = get_keywords(keyword_data)
    # create folders to save screenshots in and get path and date
    path, date = create_file_location(engines)
    # configure Chromedriver options
    chrome_options = Options()
    for argument in chrome_args:
        chrome_options.add_argument(argument)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_window_size(size[0], size[1]) # set the window size that you need
    # make screenshots
    for keyword in keywords:
        if 'Google' in engines:
            driver.get('https://www.google.de/search?q='+keyword)
            driver.save_screenshot('{}{}.png'.format(path+'\\'+'Google'+'\\', date.strftime("%Y-%m-%d ")+keyword))
        if 'Bing' in engines:
            driver.get('https://www.bing.com/search?q='+keyword)
            driver.save_screenshot('{}{}.png'.format(path+'\\'+'Bing'+'\\', date.strftime("%Y-%m-%d ")+keyword))

make_screenshot(IN_FILE, CHROME_ARGS, SCREENSHOT_SIZE, ENGINES)
