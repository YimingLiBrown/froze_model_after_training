# froze_model_after_training
I learnt two ways to froze a tensorflow model during my internship: froze a tf.saver() model and froze a tf.saved_model model

I was not familiar with TensorFlow so at beginning I thought only the model is saved as Save_Model format can be frozen and the frozen process can only be excuted during training.
The Uber Ludwig saves the model as tf.saver(), so I add some code to Ludwig source code to save the model as Saved_model. The code is provided in modify_ludwig folder.

At the end of my internship, I'm getting familiar with tensorflow and I find out that the frozen process can be excuted separately from training and both saver and saved_model format can be frozen.
The steps can be found in froze_models folder.