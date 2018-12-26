#!/bin/sh
BASEDIR=$(dirname "$0")

cd $BASEDIR
pwd
pushd .
if [ -d ./ ]
then
python pathCreate.py
else
echo "Error: Directory path does not exists."
fi

read -p "Press Return to Close..."