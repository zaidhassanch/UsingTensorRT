# UsingTensorRT
A simple method for using TensorRT. Please provide feedback.

I recommend using nvidia docker which gives TensorRT and drivers pre-installed. The following could be a useful link for pulling the code:
https://marmelab.com/blog/2018/03/21/using-nvidia-gpu-within-docker-container.html
(Let me know if there is any way of using nvidia-docker inside google colab)

Personally I used the DLAMI image from AWS was used. 

At the time of writing the tensorflow version 1.8 was compatible with this TensorRT version.

Save the existing Keras graph into a pb file:

import keras
from keras import backend as K
from keras_retinanet import models

from tensorflow.python.framework import importer
from tensorflow.python.framework import ops
import tensorflow as tf
from tensorflow.python.framework import graph_io
from tensorflow.python.tools import freeze_graph
from tensorflow.core.protobuf import saver_pb2
from tensorflow.python.training import saver as saver_lib


from tensorflow.python.ops import data_flow_ops
from google.protobuf import text_format
from tensorflow.python.platform import gfile
from tensorflow.core.protobuf import saved_model_pb2
from tensorflow.python.summary import summary

from keras.models import load_model
filename = 'TD4.h5'



model_path = "..."

def get_session():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    config.gpu_options.per_process_gpu_memory_fraction = 0.5
    return tf.InteractiveSession(config=config)


os.environ["CUDA_VISIBLE_DEVICES"] = "0"
keras.backend.tensorflow_backend.set_session(get_session())



model = models.load_model(model_path, backbone_name='resnet50')
graph_z = tf.get_default_graph()


out_node_name = ""
for i in range(len(model.outputs)):
    output_name = model.outputs[i].name.split(':')[0]
    tf.identity(model.outputs[i],output_name)
    out_node_name = out_node_name +"," + output_name
    print(out_node_name)
out_node_name = out_node_name[1:]; # get rid of the comma
K.set_learning_phase(0)
model_dir = './'
model_filename = 'retinanet.pb'
sess = K.get_session()
saver = saver_lib.Saver(write_version=saver_pb2.SaverDef.V2)
checkpoint_path = saver.save(sess, '/home/ubuntu/orlink1/orlink/app/modules/orlink_module/saved_ckpt', global_step=0)
nodes = tf.get_default_graph().as_graph_def().node
graph_io.write_graph(sess.graph, '.', 'tmp1.pb')
freeze_graph.freeze_graph('./tmp1.pb', '',
                          	False, checkpoint_path, out_node_name,
                          	"save/restore_all", "save/Const:0",
                          	model_dir+model_filename, False, "")

print "saving"


Use the script by calling its infer function:
The code will be made available in the near future
