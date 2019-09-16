"""
.. module:: ondalear.analytics.models
   :synopsis: models package

"""
from ondalear.analytics.models.constants import MODEL_PRIMARY_OUTPUT_KEY
from ondalear.analytics.models.base import AbstractModelWrapper, AbstractModelConfig
from ondalear.analytics.models.registry import register, find
