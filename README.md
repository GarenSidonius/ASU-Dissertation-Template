[![PDF Status](https://www.sharelatex.com/github/repos/GarenSidonius/ASU-Dissertation-Template/builds/latest/badge.svg)](https://www.sharelatex.com/github/repos/GarenSidonius/ASU-Dissertation-Template/builds/latest/output.pdf)

ASU Dissertation Template
=========================

This is a LaTeX template for typesetting Arizona State University dissertations and theses following the guidelines in the September 2014 format manual (the latest version at the time of posting). 
The template file is `dissertation_template_latex.tex`. 

## Features 

Arizona State University already offers a LaTeX dissertation template, but this new 
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
You will probably want to use `xetex` in order to use one of the required fonts, such as Garamond or Century. 
(If you are running the template on your own computer, make sure these fonts are installed on your system before trying to use them with `xetex`.) 
But `pdftex` sometimes runs much faster than `xetex`, so for drafting, you may want to use `pdftex` and then check the output periodically with `xetex`. 

## Making PDFs with the template

### On ShareLaTeX 

This template also exists as a [template on ShareLaTeX](https://www.sharelatex.com/templates/55124898eee6edb00c043cf2). 
By using ShareLaTeX, you avoid having to get a TeX distribution running on your own computer, something that several people have struggled with. 
To use the version of this template on ShareLaTeX: 

1. [Create a ShareLaTeX account](https://www.sharelatex.com/register).

2. Start a new project based on this template: 
    a. Visit [the template page](https://www.sharelatex.com/templates/55124898eee6edb00c043cf2).
    b. Click the "`Open in ShareLaTeX`" button.

3. Update the template with your own dissertation information (e.g., author name) and content. (This README file and the template file itself walks you through where and how to update the template.)  

4. Click the "`Compile`" or "`Recompile`" button to make your document. 

### On your own computer

#### Requirements 

I recommend that Windows users download and install the latest version of [MiKTeX](http://miktex.org/), and I recommend that Mac users download and install the latest version of [MacTeX](https://tug.org/mactex/). 
Both of these are large TeX distributions that are (1) easy to install, (2) contain all the packages used in the template, and (3) probably contain any additional packages that you will want to use. 

Linux users beware: The LaTeX packages in default repositories are often out of date and may not work with this template, so make sure your packages are up to date. 
You may need to download packages manually or customize your setup. 
If you're a Linux user, I trust you can get TeX working on your own. 

#### Making with latexmk

I recommend using `latexmk` to typeset your document. 
`latexmk` is an excellent command line tool that will run and re-run TeX, BibTeX, biber, etc. until the document is completely typeset. 
If you use `latexmk`, you will not need to manually run `pdftex`, then `biber`, then `pdftex` to format citations, for example. 
`latexmk` is usually bundled with TeX distributions, but you can also get it [here](http://users.phys.psu.edu/~collins/software/latexmk-jcc/). 

#### Step-by-step: Making the sample file 

To preview the formatting in the full template, you can create a sample using `dissertation_template_latex_sample.tex`. 

First, make sure that you have an up-to-date TeX distribution on your system. 
(See the "Requirements" section above.) 
Second, download the template and supporting files to your computer. 
A couple ways to get these files on your computer are: 

1. Click the ["Download ZIP" button](https://github.com/GarenSidonius/ASU-Dissertation-Template/archive/master.zip) on this page, and then unzip the downloaded file. 
2. If your computer has `git` installed, open a terminal and enter: 
    
    git clone https://github.com/GarenSidonius/ASU-Dissertation-Template 

Third, open a terminal (if you have not already), and navigate into the directory with the template files. 
For example, enter the following command in the terminal: 

    cd ~/Downloads/ASU-Dissertation-Template

Finally, use `latexmk` to process the sample file with `xetex` by entering the following in the terminal: 

    latexmk -pdf -xelatex dissertation_template_latex_sample.tex

Or use `latexmk` to process the sample file with `pdftex` by entering the following in the terminal: 

    latexmk -pdf dissertation_template_latex_sample.tex

Both of these commands should produce a PDF called `dissertation_template_latex_sample.pdf`, which is the sample document. 
Click [here](https://www.sharelatex.com/github/repos/GarenSidonius/ASU-Dissertation-Template/builds/latest/output.pdf) to view the sample document built with `pdftex`. 

#### Step-by-step: Making your dissertation/thesis with the template

Follow the same steps for making the sample file in the previous section, but change the name of the `*.tex` file from `dissertation_template_latex_sample.tex` to `dissertation_template_latex.tex`. 
For example, use `latexmk` to process the template file with `xetex` by entering the following in the terminal: 

    latexmk -pdf -xelatex dissertation_template_latex.tex

#### Continuous preview mode

`latexmk` also has a continuous preview mode (initiated with the flag `-pvc`), which watches a `*.tex` file and all supporting files (including separate chapter files) for changes. 
When any of these files are changed, `latexmk` automatically re-runs TeX and produces a new PDF. 
It's a great tool for checking formatting. 
For example, to use `latexmk` to process the template file with `xetex` in continuous preview mode, open a terminal and enter the following: 

    latexmk -pdf -xelatex -pvc dissertation_template_latex.tex

## Editing the template

To use the template to create *your* dissertation or thesis, you'll obviously need to edit the template file. 

### Notations in template

This template is organized so that the code you need to change is indicated with `%<`. For example, one line in the template that needs to be edited is the following: 

    \newcommand*{\pointsize}{12pt}          %<Set the font size

Optional changes are indicated with `%~`, for example, 

    \chapter*{Acknowledgements}             %~Acknowledgements are optional

Important warnings are indicated with `%!`.  

### Including other files

Make sure that LaTeX can find any external files that are called in this document (typically, individual chapter files and the bibliography files). 
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

Feel free to contact me with questions or suggestions: Robert Kutter (robert@kutterconsulting.com)

Find out more about me and my work here: <http://kutterconsulting.com>

Copyright 2015 Robert W. Kutter