# TensorFlow Inference:
with tf.device('/GPU:0'):
    predictions = model(data)  # Perform inference

