# Autoencoders

Autoencoders are an unsupervised learning technique used for representation learning. 

![image](https://user-images.githubusercontent.com/65759544/87304275-24dc7900-c547-11ea-973c-8ef9cb311e80.png)


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

Common loss functions used for autoencoders are MSELoss and BCELoss. 

The main disadvantage of using a simple autoencoder is that it has no explicit regularization term. In other words, the only way to avoid overfitting is to sufficiently restrict the number of nodes in the hidden layer. 

## Simple Autoencoder Output
![image](https://user-images.githubusercontent.com/65759544/87286487-82fb6300-c52b-11ea-8b66-7f658f8af543.png)

# Sparse Autoencoders

Overfitting can be mitigated by adding a sparsity penalty to the existing training criterion of the neural network as seen by the formula below. This encourages fewer nodes to be activated when a sample is feeded into the network. 

![image](https://user-images.githubusercontent.com/65759544/87304460-6e2cc880-c547-11ea-91d0-1e0ba8735a58.png)

## Sparse Autoencoder Output

Common regularizers are:
1. L1 Regularization
2. KL-Divergence


# Variational Autoencoders
WIP

## References
* [Introduction to autoencoders](https://www.jeremyjordan.me/autoencoders/)
* [Sparse, Stacked and Variational Autoencoder](https://medium.com/@venkatakrishna.jonnalagadda/sparse-stacked-and-variational-autoencoder-efe5bfe73b64)
* [Sparse-Autoencoder](https://mc.ai/what-happens-in-sparse-autencoder/)


