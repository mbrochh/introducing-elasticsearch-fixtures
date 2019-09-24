from elasticsearch_fixtures.es_mixer import ESMixer

from ..search_es import ESSearch

es_mixer = ESMixer('http://localhost:9200/')


class TestESSearch:

    def test_search(self):
        # adding fixtures to our DB
        es_mixer.blend('testindex', name='Alice')
        es_mixer.blend('testindex', name='Bob')

        # running tests on the fixtures
        es_search = ESSearch('testindex')
        result = es_search.search('Foobar')
        assert len(result) == 0, (
            'Returns no results if bad search term is given')

        result = es_search.search('Alice')
        assert len(result) == 1, (
            'Returns corrent number of results for given search term')
        assert result[0].name == 'Alice', (
            'Returns correct results matching the search term')