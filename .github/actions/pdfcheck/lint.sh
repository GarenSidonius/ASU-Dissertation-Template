#!/bin/sh

# lint code in this part of the project with `black`
#
# Build the docker container with the following command from
# the root of the project:
#
#   ./build.sh
#
# Run the linter from this directory (no arguments):
#
#   ./lint.sh

IMAGE=pdfcheck:latest
docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/usr/src/app "$IMAGE" black .
