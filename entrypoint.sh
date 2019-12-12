#!/bin/bash

set -e

SCRIPT_DIR=/ghidra

for file in /bin/*
do
  echo "### Analyzing file $file ###"
  for script in /script/*
  do
    echo "Executing $script"
    exec "${SCRIPT_DIR}"/support/analyzeHeadless . -import $file -postscript $script
  done
done