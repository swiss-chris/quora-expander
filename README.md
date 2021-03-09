# Quora-expander

Quora-expander is a command-line application written in Python that can automatically expand collapsed answers and comments for any given Quora user.

To run `quora-expander`:

1. Download `quora-expander.py` to your local machine, either manually or using `git clone`
1. Set up python to be run inside a terminal on your local machine
1. Make sure you have Google Chrome installed on your local machine
1. Download a version of `chromedriver` that is compatible with your machine and the installed version of Google Chrome and put the chromedriver binary inside the same directory as the `quora-expander.py` script, possibly replacing any one that was there before.
1. Run the `quora-expander` with the following command

```shell
$ python -i quora-expander.py [profile_id]
```

e.g. 

```shell
$ python -i quora-expander.py Artem-Boytsov
```

Optinally, you can pass the additional argument `-m` or `--manual` to skip the automatic execution of commands and drop immediately into the interactive shell, letting you pick and choose from the procession commands.

```shell
$ python -i quora-expander.py Artem-Boytsov -m
```

Once you are in the interactive shell, you can type `do_` and the Tab key (twice) to get the list of commands at your disposal:

```shell
>>> do_
do_all(                        do_show_more_of_comments(
do_expand_hidden_comments(     do_try_again(
do_print_manual_instructions(  do_view_collapsed_comments(
do_scrolldown(                 do_view_more_comments(
do_show_more_of_answers(       do_view_more_replies(
```

Finish typing the command you want, close the parenthesis, and hit Enter. 

E.g. the following command:

```shell
>>> do_view_more_comments()
```

will click on all "View More Comments" buttons it can find on the page, and once it has finished, will start over again until there are either no more "View More Comments" buttons on the page or until it determines that the number of buttons on the page isn't changing after clicking on all of them.

It will print out how many instances of that button it has found on the page each time it checks:

```shell

do_view_more_comments()
clicking on 141 instances of "//div[text()[contains(., 'View More Comments')]]"
clicking on 23 instances of "//div[text()[contains(., 'View More Comments')]]"
clicking on 5 instances of "//div[text()[contains(., 'View More Comments')]]"
clicking on 0 instances of "//div[text()[contains(., 'View More Comments')]]"
```

Whereas this command:

```shell
>>> do_all()
```

will call each of the individual commands once, in the appropriate order.

Finally,

```shell
do_print_manual_instructions()
```

will print a brief instruction message mentioning how to use the other commands.

---

**Disclaimer**: If you're an experienced python coder, you'll probably find all kinds of things that are wrong with this script. 
Feel free to propose improvements :) !

---

This project uses the following license: [MIT]

[MIT]: https://opensource.org/licenses/MIT
[article]: https://swiss-chris.medium.com/how-to-expand-all-answers-and-comments-on-quora-with-python-and-selenium-df6fdd86906c
