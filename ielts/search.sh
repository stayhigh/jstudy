#!/bin/bash
# usage: ./search.sh arm > arm.out

query=$1
wget -U "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" -e robots=off --output-document ${query}.html -c https://www.ldoceonline.com/dictionary/${query} 
/usr/local/bin/python3 parse.py ${query}.html
