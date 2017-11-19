#!/bin/bash


DIR_THERE="/notebook"
DIR_HOST="$(dirname $(realpath $0))/notebook"

docker run \
    -it \
    --rm \
    --name notebook \
    -v $DIR_HOST:$DIR_THERE \
    -w $DIR_THERE \
    -p 8888:8888 \
    notebook
