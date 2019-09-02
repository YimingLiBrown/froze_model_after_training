#Save the model as ProtoBuf Type
In order to deploy a tensorflow model, the model can only be in pb format.\

If you have saved your model as tf.saver() structure, the model is saved in a checkpoint file and a meta file. You can frozen your model with ```frozen.py``` which I've provided in this repo. You need to modify the the checkpoint path, output_grap and output_node_names.

If you saved your model as Saved_Model structure, python has provided a ```freeze_graph.py``` file to do so:
```
python freeze_graph.py
--input_saved_model_dir=your_path/saved_model
--output_node_names=your_output_node_name --output_graph=model.pb
```
