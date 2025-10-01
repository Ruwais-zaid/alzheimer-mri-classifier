#!/bin/bash

git lfs install

if [ -d "/tmp/alzheimer-mri-classifier" ]; then
    cd /tmp/alzheimer-mri-classifier
    git pull
else
    git clone https://github.com/Ruwais-zaid/alzheimer-mri-classifier.git /tmp/alzheimer-mri-classifier
fi

cd /tmp/alzheimer-mri-classifier
git lfs pull
cp alheimers/resnetmodel.pt /opt/models/model.pt
