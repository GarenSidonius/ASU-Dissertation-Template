FROM blang/latex:ubuntu AS asudis

# install additional software
RUN apt-get update \
    ## add system dependencies
    && apt-get -y install xzdec wget \
    ## add biber for references
    && apt-get -y install biber \
    ## clean up cache to reduce size
    && apt-get -qq clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

# download the very latest latexmk
RUN wget -P /usr/local/bin http://mirrors.ctan.org/support/latexmk.zip \
    && unzip /usr/local/bin/latexmk.zip -d /usr/local/bin/

# all submitted command arguments are prefixed with
ENTRYPOINT ["perl", "/usr/local/bin/latexmk/latexmk.pl"]

# with no command arguments, build a PDF off the template
CMD ["-cd", \
  "-interaction=batchmode", \
  "-pdf", \
  "-xelatex", \
  "dissertation_template_latex.tex" \
]
