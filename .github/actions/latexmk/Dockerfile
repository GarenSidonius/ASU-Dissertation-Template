FROM blang/latex:ubuntu AS asudis

# install additional software
RUN apt-get update \
    ## Add system dependencies
    && apt-get -y install xzdec wget \
    ## Add biber for references
    && apt-get -y install biber

# download the very latest latexmk
RUN apt-get update \
    && wget -P /usr/local/bin http://mirrors.ctan.org/support/latexmk.zip \
    && unzip /usr/local/bin/latexmk.zip -d /usr/local/bin/ \
    ## Clean up cache to reduce size
    && apt-get -qq clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

# all submitted command arguments are prefixed with
ENTRYPOINT ["perl", "/usr/local/bin/latexmk/latexmk.pl"]

# with no command arguments, build a PDF off the template
CMD ["-cd", \
  "-interaction=batchmode", \
  "-pdf", \
  "-xelatex", \
  "dissertation_template_latex.tex" \
]
