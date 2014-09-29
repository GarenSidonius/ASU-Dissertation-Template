ASU Dissertation Template
=========================

This is a LaTeX template for typesetting Arizona State University dissertations and theses 
following the guidelines in the July 2013 format manual (the latest version at the 
time of posting). The template file is 'dissertation_template_latex.tex'. 

## Features 

Arizona State University already offers a LaTeX dissertation template, but this new 
template offers several new features: 

* Includes all required and optional sections, including a copyright page, dedication, 
acknowledgements, preface, endnotes, and biographical sketch
* Correct formatting for main matter (chapters) and back matter (appendices), which 
makes it easy to organize your entire document
* For the typesetting engine, works with either pdftex or xetex (xetex makes it easy to 
use any of the approved fonts)
* For references, works with natbib and biblatex (biblatex makes it easy to use Chicago, 
MLA, and APA style references)
* Better separation of content and formatting (e.g., write your table captions however 
you want and they will appear correctly in the list of tables). This arrangement makes 
it much easier to produce another (much better looking version) of your 
dissertation/thesis in case you want to share a better-looking version with colleagues. 
* Internal document references work (e.g., clicking on an in-text citation jumps down 
to that citation in the references list) 
* Bookmarks work, so there is a navigation side menu in the PDF that contains the 
major document elements (table of contents, each chapter heading, etc.), which makes 
the PDF easier to navigate
* Write PDF metadata (including title, name, keywords, etc.) automatically
* Uses 'memoir' documentclass, which makes it easier to change formatting and create a 
book-length work in general

## Making the sample file 

You can create a sample using 'dissertation_template_latex_sample.tex' and the various 
sample files. The sample file is already set up to pull in the sample chapter and 
appendix, so you can just run 'pdflatex' or 'xelatex' on the sample file itself to 
get a sample PDF based on this template. (See how to use latexmk to easily make the 
sample file below.) 

## Notations in template

This template is organized so that the code you need to change is indicated 
with '%<'. For example: 

    \newcommand*{\pointsize}{12pt}          %<Set the font size

Optional changes are indicated with '%~'. For example: 

    \chapter*{Acknowledgements}             %~Acknowledgements are optional

Important warnings are indicated with '%!'  

## Including other files

Make sure that LaTeX can find any external files that are called in this document 
(e.g., chapters and bibliography files). The easiest way to achieve that is to put them 
in the same folder as this file.

## Making with latexmk

I recommend using 'latexmk' to typeset your document. It's an excellent command line 
tool that will run and re-run TeX, BibTeX, biber, etc. until the document is completely
typeset. So you don't need to manually run pdftex, then biber, then pdftex to format
citations for example. 'latexmk' is usually bundled with TeX distributions, but you 
can also get it here: http://users.phys.psu.edu/~collins/software/latexmk-jcc/

### Making your dissertation/thesis with the template

To use 'latexmk' to process this document with pdftex, open a terminal and do: 

    latexmk -pdf dissertaton_template_latex.tex

To use 'latexmk' to process this document with xetex, open a terminal and do: 

    latexmk -pdf -xelatex dissertaton_template_latex.tex

### Making the sample file

To use 'latexmk' to process the sample file with pdftex, open a terminal and do: 

    latexmk -pdf dissertation_template_latex_sample.tex

To use 'latexmk' to process the sample file with xetex, open a terminal and do: 

    latexmk -pdf -xelatex dissertation_template_latex_sample.tex

### Continuous preview mode

'latexmk' also has a continuous preview mode (-pvc), which watches a .tex file for 
changes and re-runs TeX whenever it's updated. It's a great tool for checking 
formatting, e.g.: 

    latexmk -pdf -xelatex -pvc dissertaton_template_latex.tex

## TeX engines

This template will run with either pdftex or xetex. You will probably want to use
xetex in order to use fonts such as Garamond, Century, etc. (Make sure these fonts are 
installed on your system before trying to use them with xetex.) But pdftex sometimes 
runs much faster than xetex , so for drafting, you may want to use pdftex and then 
check the output periodically with xetex. 

## Memoir documentclass

This template uses the 'memoir' document class which has excellent documentation: 
www.tex.ac.uk/ctan/macros/latex/contrib/memoir/memman.pdf
If you need to change the formatting for some reason or if you need to understand 
what this code is doing, start by checking the 'memoir' documentation. 'memoir' also 
offers a lot of features and customization if you need to do something not already
included in the template (e.g., numbering equations consistently). And of course, CTAN
(http://www.ctan.org/) has documentation for all the packages used in this template. 

## Currently no style or class

I have intentionally not created a style file. All the code appears in this 
document. (I have found that troubleshooting formatting and other issues when a custom
style file is being used can be a headache.) As a result, the document includes a 
lengthy preamble, but it also means that you have all the relevant code in one document. 
If there is enough interest in either a style file or packaging everything in a class, 
I will create them. 

## Pandoc

I have adapted some code from the default pandoc latex template for this template. 
Pandoc is a great utility, and you can learn about pandoc 
here: http://johnmacfarlane.net/pandoc/

## Contact

Feel free to contact me with questions or suggestions: 
Robert Kutter (robert@kutterconsulting.com)

Find out more about me and my work here: http://kutterconsulting.com