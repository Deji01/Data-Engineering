#!/usr/bin/bash

cd shoes/

scrapy crawl solesupplier

cd ..

python3 clean_db.py