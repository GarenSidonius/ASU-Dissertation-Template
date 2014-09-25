ASU Dissertation Template
=========================

This is a LaTeX template for typesetting Arizona State University dissertations and theses 
following the guidelines in the July 2013 format manual. 

The template file is 'dissertation_template_latex.tex'. You can create a sample using 
'dissertation_template_latex_sample.tex' and the various sample files. 

[1] This template is organized so that the code you need to change is indicated 
with '%<'. For example: 

    \newcommand*{\pointsize}{12pt}          %<Set the font size

Optional changes are indicated with '%~'. For example: 

    \chapter*{Acknowledgements}             %~Acknowledgements are optional

Important warnings are indicated with '%!'  

[2] Make sure that LaTeX can find any external files that are called in this document 
(e.g., chapters and bibliography files). The easiest way to achieve that is to put them 
in the same folder as this file.

[3] I recommend using 'latexmk' to typeset your document. It's an excellent command line 
tool that will run and re-run TeX, BibTeX, biber, etc. until the document is completely
typeset. So you don't need to manually run pdftex, then biber, then pdftex to format
citations for example. 'latexmk' is usually bundled with TeX distributions, but you 
can also get it here: http://users.phys.psu.edu/~collins/software/latexmk-jcc/
To use 'latexmk' to process this document with pdftex, open a terminal and do: 

    latexmk -pdf dissertaton_template_latex.tex

To use 'latexmk' to process this document with xetex, open a terminal and do: 

    latexmk -pdf -xelatex dissertaton_template_latex.tex

'latexmk' also has a continuous preview mode (-pvc), which watches a .tex file for 
changes and re-runs TeX whenever it's updated. It's a great tool for checking 
formatting, e.g.: 

    latexmk -pdf -xelatex -pvc dissertaton_template_latex.tex

[4] This template will run with either pdftex or xetex. You will probably want to use
xetex in order to use fonts such as Garamond, Century, etc. (Make sure these fonts are 
installed on your system before trying to use them with xetex.) But pdftex sometimes  
runs much faster than xetex , so for drafting, you may want to use pdftex and then 
check the output periodically with xetex. 

[5] This template uses the 'memoir' document class which has excellent documentation: 
www.tex.ac.uk/ctan/macros/latex/contrib/memoir/memman.pdf
If you need to change the formatting for some reason or if you need to understand 
what this code is doing, start by checking the 'memoir' documentation. 'memoir' also 
offers a lot of features and customization if you need to do something not already
included in the template (e.g., numbering equations consistently). And of course, CTAN
(http://www.ctan.org/) has documentation for all the packages used in this template. 

[6] I have intentionally not created a style file. All the code appears in this 
document. (I have found that troubleshooting formatting and other issues when a custom
style file is being used can be a headache.) As a result, the document includes a 
lengthy preamble, but it also means that you have all the relevant code in one document.  

[7] I have adapted some code from the default pandoc latex template for this template,
learn about pandoc here: http://johnmacfarlane.net/pandoc/

Feel free to contact me with questions or suggestions: 
Robert Kutter (robert@kutterconsulting.com)