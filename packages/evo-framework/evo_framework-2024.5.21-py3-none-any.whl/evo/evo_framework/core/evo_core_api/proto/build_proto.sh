#!/bin/bash

DIRECTORY_BASE=$(dirname "$(realpath "$0")")

CURRENT_DIRECTORY=$(pwd)
echo "Current directory: $CURRENT_DIRECTORY"

cd $DIRECTORY_BASE
pwd
echo "RUN Proto"
protoc --proto_path="." --python_out="../entity/" *.proto
mkdir -p "./entity/cs/"
protoc --proto_path="." --csharp_out="./entity/cs/" *.proto

cd "$CURRENT_DIRECTORY"