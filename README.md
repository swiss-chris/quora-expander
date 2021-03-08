# Quora-expander

Quora-expander is a command-line application written in Python that can automatically expand collapsed articles and comments for any given Quora user.

To run `quora-expander`:

1. Download `quora-expander.py` to your local machine, either manually or using `git clone`
1. Set up python to be run inside a terminal on your local machine
1. Make sure you have Google Chrome installed on your local machine
1. Download a version of `chromedriver` that is compatible with your machine and the installed version of Google Chrome and put the chromedriver binary inside the same directory as the `quora-expander.py` script, possibly replacing any one that was there before.
1. Run the `quora-expander` with the following command

```sh
$ python -i quora-expander.py [profile_id]
```

e.g. 

```sh
$ python -i quora-expander.py Artem-Boytsov
```

**Disclaimer**: If you're an experienced python coder, you'll probably find all kinds of things that are wrong with this script. 
Feel free to propose improvements :) !

This project uses the following license: [MIT]

[MIT]: <https://opensource.org/licenses/MIT>
