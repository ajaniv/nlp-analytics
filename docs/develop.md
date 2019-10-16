## pylint
### run pylint on a file from the project directory
`> pylint --rcfile=.pylintrc <file path>`


## vscode
### change terminal name on Mac
* launch vscode command mode: `cmd + shift + p`
* rename terminal command: `Terminal:Rename`


## Python path
`> export PYTHONPATH=<project path>/src`

`> export PYTHONPATH=~/projects/document_management_dev/nlp_analytics/src`

## coverage
### run the coverage command
`> coverage run --source ondalear setup.py test`
### run the coverage report
`> coverage report -m`

### sample output
``` bash
> coverage report -m
Name                                                                        Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------------------------------------
ondalear/__init__.py                                                              1      0   100%
ondalear/analytics/__init__.py                                                    6      0   100%
...
...
...
```

## check manifest
`> check-manifest -v`

## running all unit tests
`> pytest -s`
## running specific unit test
`> pytest -s tests/allennlp/test_reading_comprehension.py::TestBDAF::test_answer_question`