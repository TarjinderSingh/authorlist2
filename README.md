# authorlist2

Contains a basic script for generating authorship lists.
Uses pandas and pandoc to generate appropriate list. 
Needs installation of `rmarkdown` in R and pandas in Python.

Give permission to run if needed.

## Setup

Clone from Github:

```bash
git clone --depth=1 https://www.github.com/TarjinderSingh/authorlist2
```

Give permission to run:

```bash
chmod 777 /path/to/parse-authors.py
PATH=$PATH:/path/to/authorlist2
```

## Running

Note: requires an input tsv in a very specific format and heading
See `test/` for ensuring compatable format.

Running in directory:

```bash
./parse-authors.py -i test/sample-authorship-table.tsv
```

Running outside of directory with appropriate PATH and permissions:

```bash
parse-authors.py -i /path/to/test/sample-authorship-table.tsv
```
