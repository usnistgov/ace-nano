#!/bin/bash
docker kill $(docker ps -q)

# Run Yolo Container
YOLO_HOME="$PWD"
docker run \
	--rm \
	--gpus all \
	--runtime nvidia \
	--network host \
	-v $YOLO_HOME/code:/code  \
	-v $YOLO_HOME/data:/data \
	-it yolo bash
