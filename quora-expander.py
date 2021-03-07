#!/usr/bin/env python
import argparse
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def connectchrome():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('log-level=3')
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver_path= Path.cwd() / "chromedriver"
    browser = webdriver.Chrome(executable_path=driver_path, options=options)
    browser.maximize_window()
    browser.set_window_position(70, 0, windowHandle ='current')
    time.sleep(2)
    return browser

def scrolldown(self):
    print('scrolling down to get all answers...')
    last_height = self.page_source
    loop_scroll=True
    attempt = 0
    # scroll down loop until page not changing
    while loop_scroll:
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height=self.page_source
        if new_height == last_height:
            # in case of not change, we increase the waiting time
            attempt += 1
            if attempt==3:# in the n-th attempt we end the scrolling
                loop_scroll=False
        else:
            attempt=0
        last_height=new_height

def click_on_all(browser, find_by, selector):
    last_nb_buttons = -1
    last_nb_buttons_repeated = 0
    while True:
        buttons = find_by(selector)
        nb_buttons = len(buttons)

        print('clicking on', nb_buttons, 'instances of', '"' + selector + '"')
        for button in buttons:
            ActionChains(browser).move_to_element(button).click(button).perform()
            time.sleep(0.5)

        # know when to exit the loop
        if nb_buttons == 0:
            break
        elif nb_buttons == last_nb_buttons:
            last_nb_buttons_repeated += 1
            # if we keep seeing the same number of buttons, the buttons are probably broken
            if last_nb_buttons_repeated == 10:
                print("aborting. it looks like the remaining", nb_buttons, "buttons may not be responding to clicks.")
                break
        else:
            last_nb_buttons = nb_buttons
            last_nb_buttons_repeated = 0


def show_more_of_articles(browser):
    click_on_all(browser, browser.find_elements_by_xpath, "//div[contains(text(), '(more)')]")

def view_more_comments(browser):
    click_on_all(browser, browser.find_elements_by_xpath, "//div[text()[contains(., 'View More Comments')]]")

def view_collapsed_comments(browser):
    click_on_all(browser, browser.find_elements_by_xpath, "//div[text()[contains(., 'View Collapsed Comments')]]")

def expand_hidden_comments(browser):
    click_on_all(browser, browser.find_elements_by_css_selector, ".qu-tapHighlight--white .qu-pb--tiny")

def view_more_replies(browser):
    click_on_all(browser, browser.find_elements_by_xpath, "//div[text()[contains(., 'View More Replies')]]")

def show_more_of_comments(browser):
    click_on_all(browser, browser.find_elements_by_xpath, "//span[contains(text(), '(more)')]")

def try_again(browser):
    click_on_all(browser, browser.find_elements_by_xpath, "//div[text()[contains(., 'Try again')]]")

def print_method_name(name):
    print()
    print(name + "()")

###############################################################

def msg(name=None):
    return '''  
         python -i quora-expander.py [profile_id]
         
         Be sure to execute this script by calling 'python' and passing in the '-i' flag so that it starts in interactive mode.
         
         Use -h or --help for the full help output.
        '''
parser=argparse.ArgumentParser(description='Python (interactive) Quora article and comments expander script', usage=msg())
parser.add_argument("profile_id", help="The Quora Profile ID you want to visit, e.g. 'Artem-Boytsov'")
parser.add_argument("-m", "--manual", action="store_true", help="skip all automatic processing and execute commands manually")
args=parser.parse_args()

url = "https://www.quora.com/profile/" + args.profile_id
print("opening", url)
browser = connectchrome()
browser.get(url)
time.sleep(2)

nbanswers = browser.find_element_by_xpath("//div[text()[contains(.,'Answers')]]")
nbanswers = nbanswers.text.strip('Answers').strip().replace(',', '')
print('Quora Profile has ', nbanswers, ' answers')

###############################################################

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

def iterate_do_all(iteration_nb, total_nb):
    print()
    print("iteration", iteration_nb + 1, "of", total_nb)
    do_all()

def do_print_manual_instructions():
    print()
    print("To see which commands you can execute manually, type 'do_' and then Tab (twice) to see the list of commands "
          "you can use to automatically expand the articles and comments. Type the rest of the command "
          "you want to call, close the parenthesis and hit Enter.")
    print()
    print("E.g. you could type 'do_all()' and Enter to run all the other commands in sequence.")
    print()
    print("to exit (the interactive shell), press Ctrl-D")
    print()
    print("PS: In order for manual command execution to work, make sure you are running this script in interactive mode "
          "by explicitly calling the 'python' command and passing in the '-i' flag. See the --help output for an example.")
    print()

###############################################################

if(not args.manual):
    nb_iterations = 6
    for i in range(nb_iterations):
        iterate_do_all(i, nb_iterations)

do_print_manual_instructions()

# if saving as PDF, remove fixed position CSS of search bar to prevent it from being printed on each page
