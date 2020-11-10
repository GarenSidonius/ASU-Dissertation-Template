#!/bin/sh

# Before running this script, create the Docker container by running:
#
# $ ./build.sh
#
# It forwards arguments to `pytest` inside the Docker container, which checks
# the PDF against ASU formatting guidelines.
#
# Provide the name of the PDF that should be checked:
#
# $ ./check.sh dissertation_template_latex_sample.pdf
#
# Additional options allowed by `pytest` can also be provided after the
# name of the PDF file.
#
IMAGE=pdfcheck:latest
exec docker run --rm \
    --net=none \
    -v "$PWD":/data \
    -v "$PWD/.github/actions/pdfcheck":/usr/src/app \
    "$IMAGE" \
    pytest -s -r w --tb=line --verbosity=1 -W ignore::DeprecationWarning \
    --pdf data "$@"
# provide a directory inside the container that holds the pdf
#
# mount the code directory so that the image does not need to be rebuilt
# after making small code changes (i.e., for easier development flow)
#
# include `--pdf data` based on the mount provided above
