import sys
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


class ESSearch:

    def __init__(self, index):
        self.client = Elasticsearch()
        self.index = index

    def search(self, search_term):
        s = Search(using=self.client, index=self.index)
        s = s.query("match", name=search_term)
        response = s.execute()
        return response


if __name__ == '__main__':
    search_term = sys.argv[1]
    es_search = ESSearch('testindex')
    response = es_search.search(search_term)
    print(response)
