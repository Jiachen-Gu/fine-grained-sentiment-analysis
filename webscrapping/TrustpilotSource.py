def getting_data_from_trustPilot():
    url = "https://www.trustpilot.com/review/www.airbnb.com?languages=en"

def getting_web_pages():
    return True

import re
from classObj import def_dictionary

def get_dictionary_value(dict):
    return dict.values()

def get_review_and_user_list(soup, href):
    review_list = []
    user_list = []

    for a in soup.find_all('a', href=True):
        if a['href'][0:7] == '/users/' and a['href'][7].isdigit():
            user_list.append(a['href'][7:len(a['href'])])

        if a['href'][0:9] == '/reviews/':
            review_list.append(a['href'][9:len(a['href'])])

    dict_obj = def_dictionary()
    if len(user_list) == len(review_list):
        for i in range(len(user_list)):
            dict_obj.add(user_list[i], review_list[i])

    return dict_obj

def checkForSimilarPatterns(patterns, text):
    boolReview = True
    for pattern in patterns:
        if re.search(pattern, text):
            boolReview = False
    return boolReview