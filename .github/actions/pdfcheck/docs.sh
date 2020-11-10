#!/bin/sh

# build documentation
#
# Build the docker container with the following command from
# the root of the project:
#
#   ./build.sh
#
# Build documentation (no arguments):
#
#   ./docs.sh
#
IMAGE=pdfcheck:latest
docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/usr/src/app "$IMAGE" sphinx-apidoc -o docs/source pdfcheck && \
docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/usr/src/app "$IMAGE" sphinx-build -b html docs/source docs/build
