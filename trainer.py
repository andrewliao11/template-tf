
class Trainer(object):
  def get_model_class(model_name):
    if model_name == 'baseline':
      from model_xxx_xxx import Model
    else:
      raise ValueError(model_name)
    return Model
  
  def __init__(self, config, dataset, dataset_test):
  
    train_dir = '%s_%s_%s'% (
      config.learning_rate,
      config.model_name,
      config.prefix,
      # add whatever you want
      )
    
    # create input
    train_batch = create_input_ops(dataset, batch_size)
    test_batch = create_input_ops(dataset_test, batch_size)
    
    # create model
    Model = selg.get_model_class(config.model_name)
    self.model = Model(...)
    tensorflow.contrib.slim.model_analyzer.analyze_vars(all_vars, print_info=True)
    
    # optimizer, summary, saver, writer
    # for summary, if you're working on cv problem, please add image summary (visualization matters)
    
  def train(...):
    for i in range(max_steps):
      self.run_single_step(...)
      # periodically write_summary/save_checkpoint/evaluation
      # you're also encouraged to log the training speed (instance/sec, iter/sec, etc.)
      # if sometimes, the speed is quite low, you should check your hardware :(
      
  def rin_single_step(...):
    start_time = time.time()
    
    # to monitor your training process. e.g. learning rate, graident norm (or even for each layer you care about)
    general_output = [...]
    values = self.sess.run(
                general_output + [loss, output, ...],
                self.model.get_feed_dict(batch_data)
                )
                           
    # values that you want to record or reuse             
    loss, ... = values[3:]
    
    return loss, ...., time.time()-start_time
    
  def run_test(...):
    start_time = time.time()
    values = self.sess.run(
                  [loss, output, ...],
                  self.model_get_feed_dict(batch_data)
                  )
    return values, time.time()-start_time
    
def main(...):
  parser = argparse.ArgumentParser()
  ...
  config = parser.parse_args()
  if config.dataset == xxx:
    import xxx_dataset as dataset
  elif 
    ...
  else:
    raise ValueError(config.dataset)
  
  dataset_train, dataset_test = dataset.create_default_splits()
  trainer = Trainer(config, dataset_train, dataset_test)
  trainer.train()
  
if __name__ == '__main__':
    main()
