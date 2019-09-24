# Introducing elasticsearch-fixtures

This repo contains a demo-package that I used to present a little talk at the
Python User Group Singapore September 2019 meetup.

You can try this code like this:

```
cd ~/Projects
git clone git@github.com:mbrochh/introducing-elasticsearch-fixtures.git
cd introducing-elasticsearch-fixtures
mkvirtualenv es-fixtures
pip install -r requirements.txt
cd demo_package
# make sure you have elasticsearch and kibana installed and running
python search_es.py Alice
py.test
```

Notes: `search_es.py` is a fictional program that somehow uses Elasticsearch
under the hood. We would like to develop that program in a test driven manner.
`test_search_es.py` contains the test cases for our fictional program.
