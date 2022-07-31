![CI](https://github.com/GarenSidonius/ASU-Dissertation-Template/workflows/CI/badge.svg)

ASU Dissertation Template
=========================

This is a LaTeX template for typesetting Arizona State University (ASU) dissertations and theses following ASU's format manual.
The template file is `dissertation_template_latex.tex`.

## Features

Arizona State University already offers a LaTeX dissertation template, but this
template offers several new features:

* Includes all required and optional sections, including a copyright page, dedication, acknowledgements, preface, endnotes, and biographical sketch.
* Correct formatting for main matter (chapters) and back matter (appendices), which makes it easy to organize your entire document.
* For the typesetting engine, works with either `pdftex` or `xetex`. (`xetex` makes it easy to use any of the approved fonts.)
* For references, works with `natbib` and `biblatex`. (`biblatex` makes it easy to use Chicago, MLA, and APA style references.)
* Better separation of content and formatting. For example, write your table captions however you want and they will appear correctly in the list of tables. This arrangement makes it much easier to produce another (much better-looking version) of your dissertation/thesis in case you want to share a better-looking version with colleagues.
* Internal document references work. For example, clicking on an in-text citation jumps down to that citation in the references list.
* Bookmarks work, so there is a navigation side menu in the PDF that contains the major document elements (e.g., table of contents and each chapter heading), so the PDF is easier to navigate.
* Writes PDF metadata (including the title, name, and keywords) automatically.
* Uses the `memoir` document class, so it is easier to change formatting and create a book-length work in general.

## TeX engines

This template will run with either `pdftex` or `xetex`.
You should probably use `xetex` in order to use one of the required fonts, such as Garamond or Century.
(If you are running the template on your own computer, make sure these fonts are located where the TeX engine can find and use them.)
But `pdftex` sometimes runs much faster than `xetex`, so for drafting, you may want to use `pdftex` and then check the output periodically with `xetex`.

## Making PDFs with the template

There are a variety of ways to convert a LaTeX document to a PDF (e.g., [MiKTeX](http://miktex.org/) and [MacTeX](https://tug.org/mactex/)).
But help with using the template from its author is only available for the Docker workflow described below because there are too many LaTeX platforms to be able to support them all.

### Requirements

Install Docker.
Follow instructions [here](https://docs.docker.com/get-docker/).

### Overview

    ./build.sh
    ./latexmk.sh [ latexmk options ] [ target file ]
    ./check.sh [ target file ]

For example,

    ./build.sh
    ./latexmk.sh -pdf dissertation_template_latex_sample.tex
    ./check.sh dissertation_template_latex_sample.pdf

### Step-by-step: Making the sample file

To preview the formatting in the full template, you can create a sample using `dissertation_template_latex_sample.tex`.

Download the template and supporting files to your computer.
A couple ways to get these files on your computer are:

1. Click the ["Download ZIP" button](https://github.com/GarenSidonius/ASU-Dissertation-Template/archive/master.zip) on this page, and then unzip the downloaded file.
2. If your computer has `git` installed, open a terminal and enter:

    git clone https://github.com/GarenSidonius/ASU-Dissertation-Template

Third, open a terminal (if you have not already), and navigate into the directory with the template files.
For example, enter the following command in the terminal:

    cd ~/Downloads/ASU-Dissertation-Template

Create a local Docker image by entering the following in the terminal:

    ./build.sh

Process the sample file with `xetex` by entering the following in the terminal:

    ./latexmk.sh -f -cd -interaction=batchmode -pdf -xelatex \
    dissertation_template_latex_sample.tex

Or process the sample file with `pdftex` by entering the following in the terminal:

    ./latexmk.sh -f -cd -interaction=batchmode -pdf \
    dissertation_template_latex_sample.tex

Both of these commands should produce a PDF called `dissertation_template_latex_sample.pdf`, which is the sample document.
(Don't use the `-f` option all the time; it seems to be necessary to get the first run to complete successfully at the moment.)

### Step-by-step: Making your dissertation/thesis with the template

Follow the same steps for making the sample file in the previous section, but change the name of the `*.tex` file from `dissertation_template_latex_sample.tex` to `dissertation_template_latex.tex`.
For example, process the template file with `xetex` by entering the following in the terminal:

    ./latexmk.sh -cd -interaction=batchmode -pdf -xelatex \
    dissertation_template_latex.tex

### More options for latexmk

Documentation for `latexmk` is available [here](http://personal.psu.edu/jcc8//software/latexmk-jcc/).

One of the more useful options is continuous preview mode (initiated with the flag `-pvc`).
In this mode, `latexmk` watches a `*.tex` file and all supporting files (including separate chapter files) for changes.
When any of these files are changed, `latexmk` automatically re-runs TeX and produces a new PDF.
It's a great tool for checking formatting.
For example, to use `latexmk` to process the template file with `xetex` in continuous preview mode, open a terminal and enter the following:

    ./latexmk.sh -pdf -xelatex -pvc dissertation_template_latex.tex

### Test PDF Formatting

Run cursory tests for PDF formatting with `check.sh`, for example,

    ./check.sh dissertation_template_latex_sample.pdf

Currently these tests are not comprehensive, and do not guarantee passing format review by the Graduate College.
They just check some aspects of the title page, margins, and fonts.
To send a signal to me that it is worth spending time expanding this part of the project, please open issues for more comprehensive testing.

## Editing the template

To use the template to create *your* dissertation or thesis, you'll obviously need to edit the template file.

### Notations in template

This template is organized so that the code you need to change is indicated with `%<`. For example, one line in the template that needs to be edited is the following:

    \newcommand*{\pointsize}{12pt}          %<Set the font size

Optional changes are indicated with `%~`, for example,

    \chapter*{Acknowledgements}             %~Acknowledgements are optional

Important warnings are indicated with `%!`.

### Including other files

Make sure that LaTeX can find any external files that are called in this document (typically, individual chapter files and bibliography files and sometimes font files).
The easiest way to make sure LaTeX can find all the external files is to put them in the same folder as the template file.

### Supporting documentation

This template uses the `memoir` document class.
The `memoir` document class has excellent [documentation](http://www.tex.ac.uk/ctan/macros/latex/contrib/memoir/memman.pdf), so if you need to change the formatting for some reason or if you need to understand what this code is doing, start by checking the `memoir` documentation.
`memoir` also offers a lot of features if you need to do something not already included in the template (e.g., numbering equations consistently).
And of course, [CTAN](http://www.ctan.org/) has documentation for all the packages used in this template.
ShareLaTeX also has [excellent documentation](https://www.sharelatex.com/learn/Main_Page) both on LaTeX in general and using ShareLaTeX.

## Currently no style or class

I have intentionally not created a style file.
All the code appears in the template file itself because, in my experience, using custom style files can make it difficult to find and fix issues.
The disadvantage of this approach is a lengthy preamble in the template file, but the advantage is having all the relevant code in one document.
If there is enough interest in either a style file or packaging everything in a class, I will create them.

## Pandoc

I have adapted some code from the default Pandoc latex template.
Pandoc is a great utility, and you can learn about it [here](http://johnmacfarlane.net/pandoc/).

## Contact

The best way to get a response to any questions about the template or errors is to open a new issue in GitHub.
This is the preferred way to ask questions because issues are public and available to other users who might have the same or similar questions.
Otherwise, I can be contacted by email: Robert Kutter (robert@kutterconsulting.com)

Find out more about me and my work here: <http://kutterconsulting.com>

Copyright 2022 Robert W. Kutter
