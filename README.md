# authorlist2

Contains a basic script for generating authorship lists.
Uses pandas and pandoc to generate appropriate list. 
Needs installation of `rmarkdown` in R and pandas in Python.

Give permission to run if needed.

This was designed as a hack/one-of script for individual projects.
If there are useful changes you'd like to suggest, please use pull requests to hellp improve the code.

## Setup
****
Clone from Github:

```bash
git clone --depth=1 https://www.github.com/TarjinderSingh/authorlist2
```

Give permission to run:

```bash
chmod 777 /path/to/parse-authors.py
PATH=$PATH:/path/to/authorlist2
```

For some setups, you need to ensure that R is executable from the command line. You will see an error when running `R` on the command line. For MacOS, you can use:

```bash
PATH=$PATH:/Library/Frameworks/R.framework/Versions/4.0/Resources/
```

For some setups, you have to have to identify pandoc as an environment variable. In MacOS:

```bash
export RSTUDIO_PANDOC=/Applications/RStudio.app/Contents/MacOS/pandoc
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

Note, sometimes pandoc gets stuck when running in the command line. If a 
.docx is not generated and only the .Rmd file, run:

```bash
R -e "rmarkdown::render('author-list.Rmd')"
```