
__PATH__ = '\path\to\your\dataset'

class Dataset():

  def __init__(id, name, is_train):
    
    # read the data
    self.data = xxx.load(os.path.join(__PATH__, 'data.xxx'))
    
  def get_data():
    # can do teh preprocess here
    image = self.data['image'][xx:xx, :]
    label = self.data['label'][xx:xx]
    image = scipy.resize(image,[h, w])
    
    return image, label # return the data you need
  
def create_default_splits(n, is_train=True):
  ids_train, ids_test = all_ids()

  dataset_train = Dataset(ids_train, name='train', is_train=is_train)
  dataset_test = Dataset(ids_test, name='test', is_train=is_train)
  return dataset_train, dataset_test
  
def all_ids(...):
  # read_your txt file or npy
  # and return the ids or path 
