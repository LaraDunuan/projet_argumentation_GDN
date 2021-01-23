#!/bin/bash
#  Lara DUNUAN et Siyu WANG
#  Projet Argumentation Grand Débat National, Mai 2019 

/Applications/treetagger/tree-tagger-french |
perl -pe "s#^(.*)\t(([^:]*)(:.*)?)\t(.*)\$#\1/\5/\3#" |
tr '\n' ' ' |
perl -pe 's/SENT /SENT\n/g'
