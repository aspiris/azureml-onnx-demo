# azureml-onnx-demo

A project to demo the training of a model on Iris dataset, export to ONNX format, and deploy it to Azure ML for inferencing.

Companion code to the blog post: https://www.aspiris.io/blog/inference-with-onnx-and-azure-ml

[ONNX](https://onnx.ai/) provides several benefits as a Machine Learning model representation, and as a runtime. Namely:
1. Interoperability - develop your models using any of the popular ML frameworks (PyTorch, TensorFlow, SciKit-Learn)
2. Inference Performance - ONNX runtime optimizes for the best performance, regardless of the hardware being used
3. Deployment Flexibility - deploy the models on different hardware and cloud environments.

[Azure ML](https://ml.azure.com/) is a great choice for the whole Machine Learning workflow, from model development, to deployment.


