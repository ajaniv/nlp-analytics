"""
.. module:: ondalear.analytics.tests.allennlp.test_reading_comprehension
   :synopsis: allennlp reading comprehension tests package

"""
import os
from ondalear.analytics.config.common.log import initialize as log_init
from ondalear.analytics.allennlp import (initialize,
                                         ALLENNLP_MODEL_FAMILY,
                                         ALLENNLP_MODEL_BDAF,
                                         ALLENNLP_MODEL_BDAF_NAQNAET)
from ondalear.analytics.models import find

# initialize logging
log_init()

def config_file_path(file_name):
    """Construct config file path"""
    this_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(this_dir, 'config')
    return os.path.join(data_dir, file_name)

PASSAGE = """
A reusable launch system (RLS, or reusable launch vehicle, RLV) is a launch system which is capable of launching a 
payload into space more than once. This contrasts with expendable launch systems, where each launch vehicle is 
launched once and then discarded. No completely reusable orbital launch system has ever been created. 
Two partially reusable launch systems were developed, the Space Shuttle and Falcon 9. The Space Shuttle was partially 
reusable: the orbiter (which included the Space Shuttle main engines and the Orbital Maneuvering System engines), 
and the two solid rocket boosters were reused after several months of refitting work for each launch. 
The external tank was discarded after each flight. 

"""
QUESTION = 'How many partially reusable launch systems were developed?'
MODEL_BIDAF = 'BiDAF (trained on SQuAD)'

# pylint: disable=no-self-use
class AbstractQuestionTest:
    """Base class for question answer test cases"""

    MODEL_INPUT = dict(passage=PASSAGE, question=QUESTION)
    CONFIG_FILE = None

    @classmethod
    def initialize(cls, config_file):
        """initialize the analytics environment for the model"""
        file_path = config_file_path(config_file)
        initialize(file_path)

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        cls.initialize(cls.CONFIG_FILE)

    def find_model(self, model_family, model_name):
        """initialize and find the model"""
        model = find(model_family, model_name)
        return model

    def assert_answer(self, model, model_input, output_key, expected_answer):
        """Verify question answer protocol"""

        output = model.analyze(model_input)
        output_key = model.config.primary_output_key
        assert output[output_key] == expected_answer

class TestBDAF(AbstractQuestionTest):
    """Test BDAF reading comphrension model"""
    EXPECTED_ANSWER = 'Two'
    CONFIG_FILE = 'config_bdaf.json'
    MODEL_NAME = ALLENNLP_MODEL_BDAF
    OUTPUT_KEY = 'best_span_str'

    def test_answer_question(self):
        """expect answer to question to be correct"""
        model = self.find_model(ALLENNLP_MODEL_FAMILY, self.MODEL_NAME)
        self.assert_answer(model, self.MODEL_INPUT,
                           self.OUTPUT_KEY, self.EXPECTED_ANSWER)

class TestNAQANET(AbstractQuestionTest):
    """Test NAWANET reading comphrension model"""
    EXPECTED_ANSWER = {'answer_type': 'count', 'count': 2}
    CONFIG_FILE = 'config_naqanet.json'
    MODEL_NAME = ALLENNLP_MODEL_BDAF_NAQNAET
    OUTPUT_KEY = 'answer'

    def test_answer_question(self):
        """expect answer to question to be correct"""
        model = self.find_model(ALLENNLP_MODEL_FAMILY, self.MODEL_NAME)
        self.assert_answer(model, self.MODEL_INPUT,
                           self.OUTPUT_KEY, self.EXPECTED_ANSWER)
