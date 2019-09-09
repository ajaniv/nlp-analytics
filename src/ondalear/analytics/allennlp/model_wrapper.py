"""
.. module:: ondalear.analytics.allenlnp.model_wrapper
   :synopsis: allennlp model wrapper module
"""
import logging
import json
from overrides import overrides
from allennlp.predictors import Predictor
from allennlp.models.archival import load_archive
from ondalear.analytics.models import AbstractModelWrapper, AbstractModelConfig, register


_logger = logging.getLogger(__name__)

class AllenNLPModelWrapper(AbstractModelWrapper):
    """AllenNLP Model Wrapper"""

    @overrides
    def model_name(self):
        return self.config.model_name

    @overrides
    def config_name(self):
        return self.config.config_name

    @overrides
    def log_blob(self):
        return dict(config_name=self.config_name(),
                    model_name=self.model_name())

    @overrides
    def load(self):
        blob = super().log_blob()
        _logger.info('loading model: %s', blob)

        archive = load_archive(self.config.archive_file)

        _logger.info('loaded model: %s', blob)
        return archive

    @overrides
    def from_archive(self):
        blob = self.log_blob()
        _logger.info('creating model: %s', blob)

        archive = self.load()
        self.model = Predictor.from_archive(archive, self.model_name())

        _logger.info('created model: %s', blob)
        return self.model

    @overrides
    def analyze(self, model_input, model_params=None):
        blob = self.log_blob()
        _logger.info('begin model analysis: %s', blob)

        model_output = self.model.predict_json(model_input)

        _logger.info('end model analysis: %s', blob)
        return model_output



class AllenNLPModelConfig(AbstractModelConfig):
    """AllenNLP model configuration class"""


def model_cofiguration(config_file_path):
    """build model configuration"""

    with open(config_file_path) as config_file:
        blob = json.load(config_file)

    return {config_name: AllenNLPModelConfig(config_name=config_name, **config)
            for config_name, config in blob.items()}

FAMILY_NAME = 'allennlp'

def initialize(config_file_path):
    """initialize allennlp models"""
    # load configuration
    configs = model_cofiguration(config_file_path)

    # register
    for model_name, config in configs.items():
        model_wrapper = AllenNLPModelWrapper(config)
        # instantiate underlying model from archive
        model_wrapper.from_archive()
        register(FAMILY_NAME, model_name, model_wrapper)
