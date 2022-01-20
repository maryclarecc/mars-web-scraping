def scrape():
    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd
    import requests
    import pymongo
    # # NASA Mars News
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    # # Mars Space Images - Featured Image
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    href = soup.find('img', class_='headerimage')['src']
    featured_image_url = 'https://spaceimages-mars.com/' + href
    featured_image_url
    # # Mars Facts
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    df = tables[0]
    # # Mars Hemispheres
    # ## Cerberus
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    href = soup.find_all('a')[4]['href']
    cerebrus = 'https://marshemispheres.com/' + href
    cerebrustitle = soup.find('h2', class_='title').text
    # ## Schiaparelli
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    href = soup.find_all('a')[4]['href']
    schiaparelli = 'https://marshemispheres.com/' + href
    schiaparellititle = soup.find('h2', class_='title').text
    # ## Syrtis Major
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    href = soup.find_all('a')[4]['href']
    syrtis = 'https://marshemispheres.com/' + href
    syrtistitle = soup.find('h2', class_='title').text
    # ## Valles Marineris
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/valles.html'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    href = soup.find_all('a')[4]['href']
    valles = 'https://marshemispheres.com/' + href
    vallestitle = soup.find('h2', class_='title').text
    # ### Save as a dictionary
    marsdata = [
        {'NewsTitle': news_title, 
        "NewsText": news_p, 
        "FeaturedImage": featured_image_url,
        "MarsFacts": df,
        "Valles_title": "Valles Marineris Hemisphere", 
        "Valles_img_url": valles,
        "Cerberus_title": "Cerberus Hemisphere", 
        "Cerberus_img_url": cerebrus,
        "Schiaparelli_title": "Schiaparelli Hemisphere", 
        "Schiaparelli_img_url": schiaparelli,
        "Syrtis_title": "Syrtis Major Hemisphere", 
        "Syrtis_img_url": syrtis},
    ]
    print(marsdata)
    browser.quit()
    return(marsdata)