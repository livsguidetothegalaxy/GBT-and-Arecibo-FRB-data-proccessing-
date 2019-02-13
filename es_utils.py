#!/usr/bin/env python3

__author__ = 'Devansh Agarwal'
__email__ = 'da0017@mix.wvu.edu'

import logging

import elasticsearch

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)

if __name__ == '__main__':

    es_config = {'host': '10.1.0.125', 'port': 9200}
    es = elasticsearch.Elasticsearch(es_config)
    if es:
        logging.info(f'Connection successful')
