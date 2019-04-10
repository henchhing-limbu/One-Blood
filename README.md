# One-Blood
## Introduction ##
In the field of Blood-based disease diagnosis, identifying blood cells subtypes
of patients is significant. Human have been doing the job of identifying blood 
cells subtypes. One Blood aims to devise to automate this job by introducing a 
machine learning model that does the classification job.

## Goal ##
We aim to develop a machine learning model that can predict the blood cell subtype
of a blood cell image.

## Architecture ##

#### Input ####
A blood cell iamge

### Convolutional Neural Network ###
* Pretrained CNN (Inception v3 or VGG 19)
* Custom CNN

## Dense Network ##
### Number of hidden layers ###
Work in progress

### Number of hidden units per layer
Work in progress

### Dropout value ###
Work in progress

### Final Layer ###
* Loss function: Categorical Cross-Entropy
* Number of hidden units: 4

## Output Labels ##
* Eosinophil
* Lymphocyte
* Monocyte
* Neutrophil

## Model Optimizer ##
Adam or RMSprop

## Expected Result ##
The model will be used to aid in prediction of the subtype of blood cells as a
supplement to or in place of medical experts. We expect the model to predict 
blood cell subtypes at an accuracy higher than 80%.

## Expected Challenges ##
We expect that naturally there is human error within the data already because 
the images of the blood cells are originally labeled by human doctors, but 
seeing as how they are the best-versed in the topic, we are willing to accept 
this level of accuracy. 

## References ##
[1] https://www.kaggle.com/paultimothymooney/blood-cells