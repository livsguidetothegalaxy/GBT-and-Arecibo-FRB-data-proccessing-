#!/usr/bin/env python3

__author__ = 'Devansh Agarwal'
__email__ = 'da0017@mix.wvu.edu'

import glob
import logging

import elasticsearch
import h5py
import numpy as np

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format)


def dump_cand(es, cand_name, index='test', doc_type='test_type'):
    """
    Dump the candidate info to elasticsearch
    :param es: Elasticsearch instance
    :param cand_name: candidate h5
    :param index: index on ES
    :param doc_type: doc_type on ES
    :return: result of the dump
    """
    empty_dict = {}
    with h5py.File(cand_name, 'r') as h5:
        for keys in h5.attrs:
            print(keys, type(h5.attrs[keys]))
            if isinstance(h5.attrs[keys], bytes):
                pass
            elif isinstance(h5.attrs[keys], np.int64):
                empty_dict[keys] = int(h5.attrs[keys])
            elif isinstance(h5.attrs[keys], np.float64):
                empty_dict[keys] = float(h5.attrs[keys])
            else:
                empty_dict[keys] = str(h5.attrs[keys])
    r = es.index(index=index, doc_type=doc_type, id=empty_dict['cand_id'], body=empty_dict)
    return r


if __name__ == '__main__':

    es_config = ['10.1.0.125']
    es = elasticsearch.Elasticsearch(es_config)
    if es:
        logging.info(f'Connection successful')

    cands = glob.glob('/20m/FRB121102/21_cands/*h5')

    for cand in cands:
        print(dump_cand(es, cand))
