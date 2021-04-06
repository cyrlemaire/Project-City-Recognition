# src.infrastructure package

## Submodules

## src.infrastructure.data_generator module


### src.infrastructure.data_generator.load_test_data()
Loads test data.


### src.infrastructure.data_generator.train_validation_data_generator()
Loads generators for train and validation data.

## src.infrastructure.data_scraping module


### src.infrastructure.data_scraping.fetch_image_urls(query: str, max_links_to_fetch: int, wd: <module 'selenium.webdriver' from '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/selenium/webdriver/__init__.py'>, sleep_between_interactions: int = 1)
Allows the webdriver to look for a query in Google Image and fetches a number of image links
corresponding to the query.


### src.infrastructure.data_scraping.persist_image(folder_path: str, file_name: str, url: str)
Downloads all the images from a set of urls and save them in a dedicated folder.

## src.infrastructure.remove_duplicates module

## Module contents
