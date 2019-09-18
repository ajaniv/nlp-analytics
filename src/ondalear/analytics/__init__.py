"""
.. module:: ondalear.analytics
   :synopsis: ondalear nlp analytics package

"""
from ondalear.analytics.allennlp import (ALLENNLP_MODEL_BDAF,
                                         ALLENNLP_MODEL_BDAF_NAQNAET,
                                         ALLENNLP_MODEL_FAMILY)
from ondalear.analytics.allennlp import initialize as initialize_allennlp
from ondalear.analytics.models import (MODEL_FAMILY,
                                       MODEL_PRIMARY_OUTPUT_KEY,
                                       MODEL_NAME)
from ondalear.analytics.models import find as find_model

__title__ = 'OndaLear NLP Analytics'
__version__ = '0.0.1'
__author__ = 'Amnon Janiv'
__license__ = 'BSD'
__copyright__ = 'Copyright 2019 OndaLear LLC'

# Version synonym
VERSION = __version__
