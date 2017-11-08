
def create_input_ops(
          dataset,
          batch_size,
          num_threads,
          is_train
          ):
          
  input_ops = {}
  with tf.device("/cpu:0"), tf.name_scope(scope):
    def load_fn(...):
      data = dataset.get_data()
      return data
      
    input_ops['image'], input_ops['label'] = tf.py_func(
            load_fn, inp=...,
            Tout=[tf.float32, tf.int],
            name='func_hp'
    )

  batch_ops = tf.train.shuffle_batch(
            input_ops,
            batch_size=batch_size,
            num_threads=num_threads,
            capacity=capacity,
            min_after_dequeue=min_capacity,
        )
  
  return input_ops, batch_ops
