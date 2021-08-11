from pydantic import BaseModel, create_model
from utils import utils


""" Simple user input schema. """


class UserInput:
  def __init__(self, config, *args, **kwargs):
    self._model_attr = utils.annotator(dict(config.input_schema))
    self.UserInputSchema = create_model('UserInputSchema', **self._model_attr)


class UserOut:
  def __init__(self, config, *args, **kwargs):
    self._model_attr = utils.annotator(dict(config.out_schema))
    self.UserOutputSchema = create_model(
        'UserOutputSchema', **self._model_attr)


class ModelDetailSchema:
  def __init__(self, config, *args, **kwargs):
    self._model_attr = utils.annotator(dict(config.out_schema))
    self.ModelDetailSchema = create_model(
        'ModelDetailSchema', **self._model_attr)