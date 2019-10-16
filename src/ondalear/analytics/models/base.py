"""
.. module:: ondalear.analytics.models.model_wrapper
   :synopsis: model wrapper module
"""
import logging

from abc import abstractmethod, ABC

_logger = logging.getLogger(__name__)

class AbstractModelConfig(ABC):
    """base model configuration class"""
    def __init__(self, **kwargs):
        """Initialize the instance"""
        for key, value in kwargs.items():
            setattr(self, key, value)

class AbstractModelWrapper(ABC):
    """base class model wrapper"""
    def __init__(self, config, model=None):
        self.config = config
        self.model = model

    @abstractmethod
    def load(self):
        """load archive file"""

    @abstractmethod
    def from_archive(self):
        """create the model from archive"""

    @abstractmethod
    def convert_model_input(self, model_input):
        """convert model input to native format"""

    @abstractmethod
    def analyze(self, model_input, model_params=None):
        """perform model analysis on the model input using run time parameters"""

    @abstractmethod
    def model_name(self):
        """model name"""

    @abstractmethod
    def config_name(self):
        """configuration name"""

    def log_blob(self):
        """create log blob"""
        return dict(archive_file=self.config.archive_file,
                    config_name=self.config_name(),
                    model_name=self.model_name())
