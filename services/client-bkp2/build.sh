#!/bin/bash
TAG="335777049998.dkr.ecr.us-east-1.amazonaws.com/dumpster-fire:nom-ui-demo"
echo $TAG
docker build -t $TAG . \
    && docker push $TAG
