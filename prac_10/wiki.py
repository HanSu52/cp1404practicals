"""
Author: Han Su
Date: 05/06/2020
https://github.com/HanSu52/cp1404practicals
"""
import wikipedia


def get_search_results():
    search_input = input("Search: ")
    while search_input != "":
        print(wikipedia.search(search_input))
        search_input = input("Search: ")
    else:
        pass


get_search_results()
