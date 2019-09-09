"""
.. module:: ondalear.analytics.models.registry
   :synopsis: model registry
"""
import logging
from collections import defaultdict

_logger = logging.getLogger(__name__)

_model_cache = defaultdict(dict)


def register(family, name, model_wrapper):
    """register model data"""
    _model_cache[family][name] = model_wrapper


def find(family, name):
    """find model data"""
    try:
        return _model_cache[family][name]
    except KeyError:
        _logger.error('model %s of family %s not found', name, family)

