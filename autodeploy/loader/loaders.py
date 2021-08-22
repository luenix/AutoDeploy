import pickle


class PickleLoader:
  def __init__(self, model_path, multi_model = False):
    self.model_path = model_path
    self.multi_model = multi_model

  def load(self):
    # TODO: do handling
    try:
      if not self.multi_model:
        self.model_path = [self.model_path]
      models = []
      for model in self.model_path:
        with open(model, 'rb') as reader:
          models.append(pickle.load(reader))
      return models
    except FileNotFoundError as fnfe:
      logger.error('model file not found...')
      raise FileNotFoundError('model file not found ...')
