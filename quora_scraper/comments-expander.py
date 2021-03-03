#!/usr/bin/env python
import argparse

DEBUG = 1
import time

from shared import \
    scrolldown, \
    show_more_of_articles, \
    view_more_comments, \
    view_collapsed_comments, \
    expand_hidden_comments, \
    view_more_replies, \
    show_more_of_comments, \
    try_again, \
    connectchrome

###############################################################

def msg(name=None):
    return ''' -i comments-expander.py
         
         Be sure to execute this script by passing the '-i' flag so that it starts in interactive mode
        '''
parser=argparse.ArgumentParser(description='Python (--interactive) Quora comments extractor tool', usage=msg())
parser.add_argument("user", help="The user ID you want to visit, e.g. 'Artem-Boytsov'")
parser.add_argument("-m", "--manual", action="store_true", help="skip all automatic processing and execute commands manually")
args=parser.parse_args()

user = args.user
url = "https://www.quora.com/profile/" + user
print("opening", url)
browser = connectchrome()
browser.get(url)
time.sleep(2)

nbanswers = browser.find_element_by_xpath("//div[text()[contains(.,'Answers')]]")
nbanswers = nbanswers.text.strip('Answers').strip().replace(',', '')
print('user has ', nbanswers, ' answers')

###############################################################

def print_method_name(name):
    print()
    print(name + "()")
    print()

def do_scrolldown():
    print_method_name(do_scrolldown.__name__)
    scrolldown(browser)

def do_show_more_of_articles():
    print_method_name(do_show_more_of_articles.__name__)
    show_more_of_articles(browser)

def do_view_more_comments():
    print_method_name(do_view_more_comments.__name__)
    view_more_comments(browser)

def do_view_collapsed_comments():
    print_method_name(do_view_collapsed_comments.__name__)
    view_collapsed_comments(browser)

def do_expand_hidden_comments():
    print_method_name(do_expand_hidden_comments.__name__)
    expand_hidden_comments(browser)

def do_view_more_replies():
    print_method_name(do_view_more_replies.__name__)
    view_more_replies(browser)

def do_show_more_of_comments():
    print_method_name(do_show_more_of_comments.__name__)
    show_more_of_comments(browser)

def do_try_again():
    print_method_name(do_try_again.__name__)
    try_again(browser)

def do_all():
    print_method_name(do_all.__name__)
    print("executing all commands in sequence...")
    do_scrolldown()
    do_show_more_of_articles()
    do_view_more_comments()
    do_view_collapsed_comments()
    do_expand_hidden_comments()
    do_view_more_replies()
    do_show_more_of_comments()
    do_try_again()

def print_manual_instructions():
    print()
    print("To see which commands you can execute manually, type 'do_' and then Tab (twice) to see the list of commands "
          "you can use to automatically expand the articles and comments. Type the rest of the command "
          "you want to call, close the parenthesis and hit Enter.")
    print()
    print("E.g. you could type 'do_all()' and Enter to run all the other commands in sequence.")
    print()
    print("to exit (the interactive shell), press Ctrl-D")
    print()

###############################################################

if(args.manual):
    print_manual_instructions()
else:
    do_all()
    do_all()
    do_all()
    do_all()
    do_all()
    do_all()
    # if saving as PDF, remove fixed position CSS of search bar to prevent it from being printed on each page
