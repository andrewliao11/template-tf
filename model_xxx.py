
class Model(object):
  def __init__(config, is_train, ...):
    # create placeholder
    image = tf.placeholder(...)
    label = tf.placeholder(...)
    with tf.variable_scope(model_name):
      self.build(is_train)
    
  def get_feed_dict(batch_data):
    feed_dict = {
                image: batch_data[0],
                label: batch_data[1]
                 }
    return feed_dict
    
  def build():
    # suppose your model is quite complicated
    def sub_model1():
      with tf.variable_scope("sub_model1"):
      ...
      return output
    
    def sub_model2():
      with tf.variable_scope("sub_model2"):
      ...
      return output
      
    def sub_model3():
      with tf.variable_scope("sub_model3"):
      ...
      return output
    
    # build graph
    xxx1 = sub_model1(input)
    xxx2 = sub_model2(xxx2)
    xxx = tf.concat([xxx1, xxx2], axis=-1)
    xxx = sub_model3(xxx)
    
    # build loss
    loss = tf.reduce_mean(tf.cross_entropy(xxx, label))
    
    # build summary
    xxx_summary = tf.summar.image(xxx)
    ...
    self.summary_op = tf.merge_summary([xxx1_summary, xxx2_summary, xxx3_summary])
    
    
