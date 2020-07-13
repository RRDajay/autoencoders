# Autoencoders

Autoencoders are an unsupervised learning technique used for representation learning. 

## Applications of autoencoders
1. Anomaly Detection
2. Data Denoising
3. Image inpainting
4. Information retrieval 
5. Dimension Reduction

## Network Architecture
![image](https://user-images.githubusercontent.com/65759544/87288555-1766c500-c52e-11ea-916d-0a92c28ff703.png)

From the image above, the goal is to create a compressed knowledge representation of the input data by imposing a "bottleneck". 

## Important note
The ideal autoencoder balances the following:

1. Sensitive enough to accurately build a representation of the input data
2. Insensitive enough to avoid overfitting. 

# Simple Autoencoder
In a simple autoencoder, the most common approach is to constrain the number of nodes in the network's hidden layer. This makes our network learn the most important attributes of our input data.

The main disadvantage of using a simple autoencoder is that it has no explicit regularization term. In other words, the only way to avoid overfitting is to sufficiently restrict the number of nodes in the hidden layer. 

## Simple Autoencoder output
![image](https://user-images.githubusercontent.com/65759544/87286487-82fb6300-c52b-11ea-8b66-7f658f8af543.png)

Image above is a sample output of an autoencoder neural network. 

However, the main disadvatage of using simple autoencoders

# Sparse Autoencoders
WIP
# Variational Autoencoders
WIP

## Reference 
* [Introduction to autoencoders](https://www.jeremyjordan.me/autoencoders/)
* [Sparse, Stacked and Variational Autoencoder](https://medium.com/@venkatakrishna.jonnalagadda/sparse-stacked-and-variational-autoencoder-efe5bfe73b64)


