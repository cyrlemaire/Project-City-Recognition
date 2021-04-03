import hashlib
import io
from PIL import Image
import requests
from selenium import webdriver
import time

from src.config.config import *

# Data scrapping (only if you want to scrap new images from google image)
DRIVER_PATH = "path/to/google chrome/drivers"
IMAGES_PATH = "path/to/download/folder"
N_IMAGES = 100 #number of image downloaded per query
QUERIES = ['facade paris',
           'building front paris',
           'maison typique Paris',
           'typical house Paris',
           'logement Paris',
           'housing Paris',
           'batiment Paris',
           'building Paris',
           'house Paris',
           'maison Paris'] #exemple of queries for Paris

def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 1):
    """Allows the webdriver to look for a query in google image and fetch a number of image links
    corresponding to the query"""

    def scroll_to_end(wd):
        """ Scroll to the end of the loaded page"""
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    if actual_image.get_attribute('src') is not None:
                        image_urls.add(actual_image.get_attribute('src'))
                    else:
                        pass
            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls


def persist_image(folder_path: str, file_name: str, url: str):
    """ Download all the images from a set of urls and save them in a deedicated folder"""
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        folder_path = os.path.join(folder_path, file_name)
        if os.path.exists(folder_path):
            file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        else:
            os.mkdir(folder_path)
            file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")


if __name__ == '__main__':

    # instantiate the webdriver
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)

    # Go through each query and download corresponding images
    for query in QUERIES:
        wd.get('https://google.com')
        search_box = wd.find_element_by_css_selector('input.gLFyf')
        search_box.send_keys(query)
        links = fetch_image_urls(query, N_IMAGES, wd)
        for i in links:
            persist_image(IMAGES_PATH, query, i)
    wd.quit()
