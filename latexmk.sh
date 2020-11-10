#!/bin/sh

# Before running this script, create the Docker container by runnning:
#
# $ ./build.sh
#
# This script is based on
# https://github.com/blang/latex-docker/blob/master/latexdockercmd.sh
#
# It forwards arguments to `latexmk` inside the Docker container, e.g.,
#
# $ ./latexmk.sh -cd -interaction=batchmode -pdf -xelatex dissertation_template_latex_sample.tex
#
IMAGE=asudis:latest
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" "$@"
