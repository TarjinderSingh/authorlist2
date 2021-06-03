#!/usr/bin/env python3
"""
Parse Authors 0.1 (24 Jan 2020)
This is a basic Python Script for generating authorship lists

example:
    $ ./parse-authors.py -i test/sample-authorship-table.tsv

Source: www.github.com/tarjindersingh/
"""

__author__ = "Tarjinder Singh"
__license__ = "MIT"

import os
import sys
import argparse
import subprocess

import pandas as pd
import numpy as np


def main(args):
    df = pd.read_table(args['input'], encoding='utf-8')
    df['Middle Initial'] = df['Middle Initial'] + '.'
    df['Middle Initial'] = df['Middle Initial'].str.replace(' ', '')
    df['Middle Initial'] = df['Middle Initial'].replace(np.nan, '')
    df['Name'] = df['First Name'] + ' ' + \
        df['Middle Initial'] + ' ' + df['Last Name']

    adict = {}
    counter = 1
    authorlist = []

    for index, row in df[['Name', 'Affiliation']].iterrows():
        affiliation = row.Affiliation.split(
            '\n') if row.Affiliation is not np.nan else ['NA']
        numbers = []
        for a in affiliation:
            if a in adict:
                numbers.append(adict[a])
            elif a is not 'NA':
                adict[a] = counter
                counter += 1
                numbers.append(adict[a])
        if numbers != []:
            numbers.sort()
            authorlist.append('{0}^'.format(row.Name) +
                              ','.join([str(n) for n in numbers]) + '^')
        else:
            authorlist.append(row.Name)

    address_list = []
    for address, index in sorted(adict.items(), key=lambda x: x[1]):
        address_list.append('^' + str(index) + '^' +
                            '{1}'.format(index, address))

    print((len(authorlist), len(address_list)))

    author_string = ', '.join(authorlist)
    address_string = ' '.join(address_list)

    email_string = ', '.join(
        [e for e in df['Email'].tolist() if e is not np.nan])

    str_write = """---
title: "Authorship"
output: word_document
---

""" + author_string + "\n\n" + address_string + "\n\n\n" + email_string

    f = open("author-list.Rmd", 'w')
    f.write(str_write)

    os.system('''R -e "rmarkdown::render('author-list.Rmd')"''')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input file", dest="input")
    args = parser.parse_args()
    args = args.__dict__
    main(args)
