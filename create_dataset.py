# Import the necessary packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
import urllib.request

# Read the .txt file with the categories/classes
with open('classes.txt') as f:
    classes = f.read().splitlines()

# Define Chrome options to open the window in maximized mode
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize the Chrome webdriver
driver = webdriver.Chrome(options=options)

for category in classes:
    # Go to Yandex Images
    driver.get('https://yandex.com/images')
    # Search Yandex Images
    search_bar = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/form/div[1]/span/span/input')
    search_bar.send_keys(category)
    search_bar.send_keys(Keys.ENTER)
    
    # Get the URL corresponding to the search made
    url = driver.current_url
    
    # Navigate to this URL
    driver.get(url)
    
    # Define a pause time in between scrolls
    pause_time = 5
    
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    # Record the starting time
    start = datetime.datetime.now()
    
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(pause_time)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height: # which means end of page
            break
        # Update the last height
        last_height = new_height
    
    # Record the end time, then calculate and print the total time
    end = datetime.datetime.now()
    delta = end-start
    print("[INFO] Total time taken to scroll till the end {}".format(delta))
    
    # Extract all images
    images = driver.find_elements_by_tag_name('img')
    
    # Create the directory after checking if it already exists or not
    dir_name = category
    if not os.path.exists(dir_name):
        try:
            os.mkdir(dir_name)
        except OSError:
            print ("[INFO] Creation of the directory {} failed".format(os.path.abspath(dir_name)))
        else:
            print ("[INFO] Successfully created the directory {} ".format(os.path.abspath(dir_name)))
    
    # Extract the URLs of images and download them to the folder previously created
    for index, image in enumerate(images):
        src = image.get_attribute('src')
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            urllib.request.urlretrieve(src, './' + str(category) + '/' + str(index) + '.jpg')
        except ValueError:
            continue