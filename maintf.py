#For TensorFlow:

import tensorflow as tf

# Set device for computations
with tf.device('/GPU:0'):
    model = YourModel()
    data = tf.convert_to_tensor(data, dtype=tf.float32)
    labels = tf.convert_to_tensor(labels, dtype=tf.float32)
    
    # Forward pass
    with tf.GradientTape() as tape:
        predictions = model(data)
        loss = loss_function(labels, predictions)

    # Backward pass
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
