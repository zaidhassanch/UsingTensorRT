# UsingTensorRT
A simple method for using TensorRT. Please provide feedback.

I recommend using nvidia docker which gives TensorRT and drivers pre-installed. The following could be a useful link for pulling the code:
https://marmelab.com/blog/2018/03/21/using-nvidia-gpu-within-docker-container.html
(Let me know if there is any way of using nvidia-docker inside google colab)

Personally I used the DLAMI image from AWS was used. 

At the time of writing the tensorflow version 1.8 was compatible with this TensorRT version.

Save the existing Keras graph into a pb file:
The code has been shared. The model files will be shared soon.

Read the graph back in: 

Identify the required input and output nodes:
Input node is easily identified by printing the first couple of nodes. Output nodes are easy to identify in Keras and the code can be seen in the loadGraph file.
Output node once identified can be used in tensorflow using the sess.run call.

Use the script by calling its infer function:
The code will be made available in the near future
