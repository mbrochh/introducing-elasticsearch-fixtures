import pytest
from elasticsearch_fixtures.es_mixer import ESMixer

index = 'testindex'
es_mixer = ESMixer('http://localhost:9200/')


@pytest.fixture(scope='session', autouse=True)
def setup_elasticsearch():
    es_mixer.wipe_index(index)
