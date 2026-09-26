# Email Analyzer – Python

A Python project that analyzes email data from a text file.

## What it does

* Counts total messages
* Counts messages from each email
* Counts messages by day
* Counts messages by hour
* Finds the top sender
* Finds the top 10 senders

## Python concepts used

* File handling
* `open()`
* `try` / `except`
* `for` loops
* `if` statements
* Strings
* `split()`
* Dictionaries
* Tuples
* Lists
* `.items()`
* Sorting
* List slicing

## What I learned

I practiced working with data from a text file and organizing it using dictionaries, lists, and tuples. I also practiced sorting data to find the most frequent senders.

## Data

The sample email data is from Python for Everybody.

## Output

Enter a file name:mbox-short.txt
========== EMAIL ANALYZER ==========

Total messages: 27

Messages from each email: [(5, 'cwen@iupui.edu'), (4, 'zqian@umich.edu'), (4, 'david.horwitz@uct.ac.za'), (3, 'louis@media.berkeley.edu'), (3, 'gsilver@umich.edu'), (2, 'stephen.marquard@uct.ac.za'), (2, 'rjlowe@iupui.edu'), (1, 'wagnermr@iupui.edu'), (1, 'ray@media.berkeley.edu'), (1, 'gopal.ramasammycook@gmail.com'), (1, 'antranig@caret.cam.ac.uk')]

Top sender: (5, 'cwen@iupui.edu')

Messages by day: {'Sat': 1, 'Fri': 20, 'Thu': 6}

Messages by hour: [('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6), ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]

Top 10 senders: [(5, 'cwen@iupui.edu'), (4, 'zqian@umich.edu'), (4, 'david.horwitz@uct.ac.za'), (3, 'louis@media.berkeley.edu'), (3, 'gsilver@umich.edu'), (2, 'stephen.marquard@uct.ac.za'), (2, 'rjlowe@iupui.edu'), (1, 'wagnermr@iupui.edu'), (1, 'ray@media.berkeley.edu'), (1, 'gopal.ramasammycook@gmail.com')]
