# nlp-analytics
* A wrapper around underlying nlp model implementations, including AllenNLP
* Provides a high level interface abstracting model specifics.
* While it has been designed to be used as the analytics  layer for the project https://github.com/ajaniv/document-management,
  it may be integrated into other projects, or serve as a training tool.

# model requirements
* Model has to be wrapped by a layer which translates high level API requests to a native model implementation.
* This abstracting layer handles model file download and archiving, initialization, and input and output mappings.

# links
* [Development](./docs/develop.md)
* [Git](./docs/git.md)
* [Todo](./docs/todo.md)