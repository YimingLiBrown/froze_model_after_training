import tensorflow as tf
import os

dir = os.path.dirname(os.path.realpath(__file__))
print(dir)
checkpoint = tf.train.get_checkpoint_state(dir + '/model')
print(checkpoint)
input_checkpoint = checkpoint.model_checkpoint_path
print(input_checkpoint)

absolute_model = '/'.join(input_checkpoint.split('/')[:-1])
print(absolute_model)

output_grap = absolute_model + "/frozen_model.pb"
with tf.Session(graph=tf.Graph()) as sess:
    saver = tf.train.import_meta_graph(input_checkpoint + '.meta',
                                       clear_devices=True)

    saver.restore(sess, input_checkpoint)
    for op in tf.get_default_graph().get_operations():
        print(op.name, op.values())

    output_grap_def = tf.graph_util.convert_variables_to_constants(sess,tf.get_default_graph().as_graph_def(),output_node_names=['temperature/predictions_temperature/Reshape'])
    with tf.gfile.GFile(output_grap, 'wb') as f:
        f.write(output_grap_def.SerializeToString())
    print("%d ops in the final graph." % len(output_grap_def.node))