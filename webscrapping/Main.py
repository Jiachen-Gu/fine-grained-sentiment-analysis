"""
This is written by Kuok Hong, Chan
All the code written to: Scrape the data from trustpilot and airbnb
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
import re
from classObj import def_dictionary
import TrustpilotSource
from classObj import pre_process
from selenium.webdriver.support.ui import WebDriverWait as wait

BOOL_TRUSTPILOT = False
BOOL_AIRBNB = False
TOTAL_COUNT = 55
# INITIAL_COUNTER = 1
URL = "https://www.trustpilot.com/review/www.airbnb.com?page="


def getting_url(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    return soup


def scraping_airbnb():
    header = ['user_id', 'user_name', 'review_text', 'word_count']
    with open('scraped_text_air_bnb.csv', mode='a', newline='') as file_header:
        head_writer = csv.writer(file_header, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        head_writer.writerow(header)

    url_airbnb = ["147929067","34877961","160107678","54411627","284481242","50931972",
                    "159690663","285551649","13756773","80234878","57307805","2372163",
                    "124405171","258279865","206634285","46621870","40932533","278047812",
                    "18842252","23011433","108946977","17136448","207456806","11145548",
                    "41135342","6567091","11803471","124947088","277283479","9536549",
                    "134838188","226995111","104838996","107874877","215209779",
                    "133852923","154754796","222920493","156006487","9861758","189718559"]

    patterns = ['Government ID', 'Selfie', 'Email address', 'Phone number', 'Work email']

    chrome_path = r"C:\Users\RexPC\Desktop\chromedriver.exe"

    for url in url_airbnb:
        driver = webdriver.Chrome(chrome_path)
        driver.get("https://www.airbnb.com/users/show/" + url)
        btnLearnMore = driver.find_elements_by_class_name("_b0ybw8s")
        for x in range(len(btnLearnMore)):
            driver.execute_script("arguments[0].click();", btnLearnMore[x])
            time.sleep(3)
        new_page_source = driver.page_source
        extended_soup = BeautifulSoup(new_page_source, "lxml")
        comment = []
        name = extended_soup.find('div', {'class': "_1ekkhy94"}).text[
               8:len(extended_soup.find('div', {'class': "_1ekkhy94"}).text)]

        for index, val in enumerate(extended_soup.find_all('div', {'class': "_czm8crp"})):
            comment.append(val.text)

        j = 0
        for index, value in enumerate(comment):
            if comment[index] == patterns[3] and comment[index + 1] != patterns[4]:
                del comment[0:index + 1]
            elif comment[index] == patterns[4] and comment[index + 1] != patterns[3]:
                del comment[0:index + 1]
            elif comment[index] == patterns[2] and comment[index + 1] != patterns[3] and comment[index + 1] != patterns[
                4]:
                del comment[0:index + 1]

        for text in comment:
            if len(text.split(" ")) > 10:
                list_review = []
                list_review.append(text)
                prep = pre_process(name, list_review[0])
                prep.__remove_whitespcace__()
                prep.expandContractions()
                prep.replace_numbers_to_char()
                prep.toLowerCase()
                prep.replace_and_symbol()
                prep.removeNewLine()
                prep.removeCarriageChar()
                prep.removePuntuation()
                prep.removeNumber()
                prep.removeEmptySpace()
                prep.deleteDigits()

                list_review2 = []
                list_review2.append(prep.Review)
                print(list_review2)
                with open('scraped_text_air_bnb.csv', mode='a', newline='', encoding='utf-8-sig') as airbnb_file:
                    scrape_writer = csv.writer(airbnb_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    scrape_writer.writerow([url.split("/")[-1], name, list_review2, len(text.split(" "))])


def scraping_trust_pilot():
    INITIAL_COUNTER = 1
    header = ['user_id', 'review_id', 'user_name', 'num_of_stars', 'review_category', 'review_text', 'word_count']
    with open('scraped_text_trust_pilot.csv', mode='a', newline='') as file_header:
        head_writer = csv.writer(file_header, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        head_writer.writerow(header)

    for count in range(TOTAL_COUNT):
        print(INITIAL_COUNTER)

        with open('scraped_text_trust_pilot.csv', mode='a', newline='') as trust_pilot_file:
            scrape_writer = csv.writer(trust_pilot_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            url_links = URL + str(INITIAL_COUNTER)
            soup = getting_url(url_links)

            dict_inst = TrustpilotSource.get_review_and_user_list(soup, href=True)
            print(dict_inst)
            for val in TrustpilotSource.get_dictionary_value(dict_inst):
                content = []
                soup_instance = getting_url("https://www.trustpilot.com/reviews/" + val)
                reviews_text = soup_instance.find_all('p', {'class': "review-content__text"})
                user_name = soup_instance.find_all('div', {'class': "consumer-information__name"})
                num_of_star = soup_instance.find_all('img')[2]['alt']
                user_id = list(dict_inst.keys())[list(dict_inst.values()).index(val)]

                if reviews_text:
                    if len(reviews_text[0].text.split(" ")) > 50:
                        patterns = ['helpline number']

                        prep = pre_process(user_name[0].text, reviews_text[0].text)
                        prep.__remove_whitespcace__()
                        prep.expandContractions()
                        prep.replace_numbers_to_char()
                        prep.toLowerCase()
                        prep.removePuntuation()
                        prep.removeNumber()
                        prep.replace_and_symbol()
                        prep.reformat_airbnb()
                        prep.removeEmptySpace()

                        if val != "5d3ca0fbf01869069cc4287f" and val != "5d38c142f018690bd04332cb" and val != "5d2f3e5accd70b06a869cfd7":
                            if TrustpilotSource.checkForSimilarPatterns(patterns, prep.Review):  # remove spam reviews
                                content.append(user_id)  # user id
                                content.append(val)  # review id
                                content.append(prep.Name)  # user name
                                content.append(re.findall(r'\d+', num_of_star)[0])  # number of stars
                                content.append(num_of_star.split(":")[1].strip())
                                content.append(prep.Review) # review text
                                content.append(len(prep.Review)) # word count
                                print(content)
                                scrape_writer.writerow(content)
        INITIAL_COUNTER += 1


def main():
    scraping_trust_pilot() #Perform Trust pilot Scraping
    scraping_airbnb()      # Perform Airbnb Scraping


if __name__ == "__main__":
    main()
