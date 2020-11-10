#!/usr/bin/env bash

# It is allowed to provide a custom tag, but the
# convenience script for `latexmk` (`latexmk.sh`)
# assumes that the "latest" tag is used.
if [ $# -eq 0 ]
  then
    tag='latest'
  else
    tag=$1
fi

docker build --no-cache -t asudis:$tag .github/actions/latexmk

docker build --no-cache -t pdfcheck:$tag .github/actions/pdfcheck
