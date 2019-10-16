## Models
* Integrate additional models into the framework

## AllenNLP 
* Fetching of model data over the network is taking a significant amount of time
  for some archive files (i.e. AllenNLP 1GB arhives)
* AllenNLP untars model file per invocation of python main.  Review approach,
  keep persistent untared archive files for improved performance.
* Log is verbose.  Change log level to warning to reduce verbocity when comfortable with
  the implementation.