from selenium import webdriver
import time
import requests
import os
from PIL import Image
import io
import hashlib

# TODO: object oriented

# TODO: add a config file for paths and parameters

# Path for your ChromeDriver here:
DRIVER_PATH = '/Users/cyrillemaire/Documents/Yotta/Project/Project_2/Chrome_drivers/chromedriver'

# Path for your images folder
IMAGES_PATH = '/Users/cyrillemaire/Documents/Yotta/Project/Project_2/pictures'

# Number of imagees per query:
n_images = 100

# Change your set of queries here:
queries = ['facade paris',
               'building front paris',
               'rue Paris',
               'street Paris',
               'logement Paris',
               'housing Paris',
               'batiment Paris',
               'building Paris',
               'house Paris',
               'maison Paris',
               'rue Monge Paris',
               'boulevard saint germain Paris',
               'rue des saint Peres Paris',
               'Facade Londres',
               'building front London',
               'rue Londres',
               'street London',
               'logement Londres',
               'housing London',
               'batiment Londres',
               'building London',
               'house London',
               'maison Londres',
               'chelsea house London',
               'brick house London',
               'oxford street london']


def fetch_image_urls(query: str, max_links_to_fetch: int, wd: webdriver, sleep_between_interactions: int = 1):
    def scroll_to_end(wd):
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

    wd = webdriver.Chrome(executable_path=DRIVER_PATH)

    for query in queries:
        wd.get('https://google.com')
        search_box = wd.find_element_by_css_selector('input.gLFyf')
        search_box.send_keys(query)
        links = fetch_image_urls(query, n_images, wd)
        for i in links:
            persist_image(IMAGES_PATH, query, i)
    wd.quit()
