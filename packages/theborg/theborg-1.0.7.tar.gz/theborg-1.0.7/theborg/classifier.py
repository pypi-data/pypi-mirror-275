# import package
from __future__ import absolute_import, division, print_function # python2 compatibility
import numpy as np
import torch
import time
from . import radam
from .model import Model


#===================================================================================================
# convolutional models
# simple multi-layer perceptron model
class CNNClassifierModel(torch.nn.Module):
    def __init__(self, dim_in, num_neurons, num_channels, mask_size, stride_size, num_features):
        super(CNNClassifierModel, self).__init__()

        self.conv1 = torch.nn.Sequential(
                       torch.nn.Conv1d(1, num_channels, mask_size),
                       torch.nn.MaxPool1d(kernel_size=mask_size, stride=stride_size),
                       torch.nn.LeakyReLU()
        )

        self.conv2 = torch.nn.Sequential(
                       torch.nn.Conv1d(num_channels, num_channels, mask_size),
                       torch.nn.MaxPool1d(kernel_size=mask_size, stride=stride_size),
                       torch.nn.LeakyReLU()
        )

        self.conv3 = torch.nn.Sequential(
                       torch.nn.Conv1d(num_channels, num_channels, mask_size),
                       torch.nn.MaxPool1d(kernel_size=mask_size, stride=stride_size),
                       torch.nn.LeakyReLU()
        )
        self.conv4 = torch.nn.Sequential(
                       torch.nn.Conv1d(num_channels, 1, mask_size),
                       torch.nn.MaxPool1d(kernel_size=mask_size, stride=stride_size),
                       torch.nn.LeakyReLU()
        )

        # calculate number of features after convolution
        num_features = dim_in
        for i in range(4):
            num_features = (num_features-mask_size) + 1 # from covolution # no stride
            num_features = (num_features-mask_size)//stride_size + 1 # from max pooling

        print("Number of features before the dense layers:", num_features)

        self.features = torch.nn.Sequential(
            torch.nn.Linear(num_features, num_neurons),
            torch.nn.LeakyReLU(),
            torch.nn.Linear(num_neurons, num_neurons),
            torch.nn.LeakyReLU(),
            torch.nn.Linear(num_neurons, num_features),
            torch.nn.Sigmoid()
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.features(x[:,0,:])
        return x

#===================================================================================================
# simple multi-layer perceptron model

class CNNClassifier(Model):
    def __init__(self, dim_in=4, num_neurons=100, num_features=500, **kwargs):
        super().__init__(dim_in, num_neurons, num_features, **kwargs)
        self.model = CNNClassifierModel(dim_in, num_neurons, num_features)
    
        #===================================================================================================
        # train neural networks
        def train(self,training_spectra=None, training_labels=None, validation_spectra=None, validation_labels=None,
                  validation_split=0.2, num_channels=8, num_neurons=30, mask_size=11, stride_size=3,
                  num_steps=1e3, learning_rate=1e-4, batch_size=256, cuda=False, shuffle=True, label_names=None):

            '''
            Training neural networks as a classifier.

            The validation set is used to independently evaluate how well the neural net
            is emulating the spectra. If the neural network overfits the spectral variation, while
            the loss will continue to improve for the training set, but the validation
            set should show a worse loss.
            
            The training is designed in a way that it always returns the best neural net
            before the network starts to overfit (gauged by the validation set).

            Parameters
            ----------
            training_labels : numpy array
               The labels for the training set.  It should have dimensions of [# training data, # labels]
            training_data : numpy array
               The data for the training set.  It should have dimensions of [# training data, # features].
            validation_labels : numpy array, optional
               Validation sample labels.  It should have dimensions of [# validataion data, # labels].
            validation_data : numpy array, optional
               Validation sample data.  It should have dimensions of [# validataion data, # features].
            validation_split : float, optional
               You can use this to split off some of the training set itself as the validation set.
                Default is 0.20 or 20%.
            num_channels : int, optional
               Number of channels??  Default is 8.
            num_neurons : int, optional
               Number of neurons in the hidden layers.  Default is 30.
            mask_size : int, optional
               Size of convolutional mask.  Default is 11.
            stride_size : int, optional
               Stride size in convolutional layer. Default is 3.
            num_steps : int, optional
               How many steps to train until convergence.
                1e4 is good for the specific NN architecture and learning I used by default.
                Bigger networks will take more steps to converge, and decreasing the learning rate
                will also change this. You can get a sense of how many steps are needed for a new
                NN architecture by plotting the loss evaluated on both the training set and
                a validation set as a function of step number. It should plateau once the NN
                has converged.  Default is 1000.
            learning_rate : float, optional
               Step size to take for gradient descent.
                This is also tunable, but 1e-4 seems to work well for most use cases. Again,
                diagnose with a validation set if you change this.  Default is 1e-4.
            batch_size : int, optional
               The batch size for training the neural networks during the stochastic
                gradient descent. A larger batch_size reduces stochasticity, but it might also
                risk of stucking in local minima. Default is 256.
            cuda : boolean, optional
               Use CUDA on a GPU.  Default is False.
            shuffle : boolean, optional
               Randomize/shuffle the data.  Default is to shuffle the data.
            label_names : list, optional
               List of names of labels.

            Results
            -------
            The model is trained and can be used to emulate the data.

            Example
            -------

            model.train(training_data=data,training_labels=labels,num_steps=2000)

            '''

            # No training data
            if training_data is None and training_labels is None and \
               self.training_data is None and self.training_labels is None:
                raise ValueError('Need training_data and training_labels to train the model')

            # Training data to use
            if training_data is None:
                training_data = self.training_data
            if training_labels is None:
                training_labels = self.training_labels

            # run on cuda
            if cuda:
                dtype = torch.cuda.FloatTensor
                torch.set_default_tensor_type('torch.cuda.FloatTensor')
            else:
                dtype = torch.FloatTensor
                torch.set_default_tensor_type('torch.FloatTensor')   

            # Shuffle the data
            ndata,num_features = training_data.shape
            ndata2,num_labels = training_labels.shape
            ind = np.arange(ndata)
            if shuffle:
                np.random.shuffle(ind)  # shuffle in place

            # Default label names
            if label_names is None:
                label_names = []
                for i in range(num_labels):
                    label_names.append('label'+str(i+1))
            
            # Validation split
            if validation_labels is None and validation_data is None and validation_split is not None:
                vsi = np.arange(ndata)
                np.random.shuffle(vsi)   # shuffle
                vsi = vsi[0:int(np.round(validation_split*ndata))]  # only want validation_split
                vind = ind[vsi]
                ind = np.delete(ind,vsi)   # remove these from the training set
                validation_data = training_data[vind,:] 
                validation_labels = training_labels[vind,:]

            # Default num_neurons
            if num_neurons is None:
                num_neurons = 2*num_features
                print('num_neurons not input.  Using 2*Nfeatures = ',num_neurons)

            # Re-initialize the model and trained data and history
            #self.model = self.model.__class__(num_labels, num_neurons, num_features)
            #self.model = CNNClassifierModel(num_labels, num_neurons, num_features)
            self.model = CNNClassifierModel(dim_in=dim_in, num_neurons=num_neurons, num_channels=num_channels,
                                            mask_size=mask_size, stride_size=stride_size, num_features=num_features)
            self.num_labels = num_labels
            self.num_features = num_features
            self.num_neurons = num_neurons
            self.learning_rate = learning_rate
            self.batch_size = batch_size
            self.label_names = label_names
            self.training_loss = []
            self.validation_loss = []
            self.training_labels = training_labels[ind,:]
            self.trained = False

            # scale the labels, optimizing neural networks is easier if the labels are more normalized
            xmax = np.max(training_labels[ind,:], axis = 0)
            xmin = np.min(training_labels[ind,:], axis = 0)
            self.xmin = xmin
            self.xmax = xmax
            bd, = np.where(self.xmax-self.xmin==0.0)
            if len(bd)>0:
                raise ValueError('Label '+str(bd)+' has no variation')
            x = self.scaled_labels(training_labels[ind,:])
            x_valid = self.scaled_labels(validation_labels)

            # dimension of the input
            dim_in = x.shape[1]

            #--------------------------------------------------------------------------------------------
            # assume cross entropy loss
            loss_fn = torch.nn.BCELoss()
            
            # make pytorch variables
            x = torch.from_numpy(x).type(dtype)
            y = torch.from_numpy(training_labels[ind,:]).type(dtype)
            x_valid = torch.from_numpy(x_valid).type(dtype)
            y_valid = torch.from_numpy(validation_labels).type(dtype)

            # run on cuda
            if cuda:
                x.cuda()
                y.cuda()
                x_valid.cuda()
                y_valid.cuda()

            # expand into 3D (i.e. 1 channel)
            x = x[:,None,:]
            x_valid = x_valid[:,None,:]


            # initiate the classifier and optimizer
            model = self.model
            if cuda:
                model.cuda()
            model.train()

            # we adopt rectified Adam for the optimization
            optimizer = radam.RAdam([p for p in model.parameters() if p.requires_grad==True], lr=learning_rate)

            #--------------------------------------------------------------------------------------------
            # train in batches
            nsamples = x.shape[0]
            nbatches = nsamples // batch_size

            nsamples_valid = x_valid.shape[0]
            nbatches_valid = nsamples_valid // batch_size

            # initiate counter
            current_loss = np.inf
            training_loss = []
            validation_loss = []

            #-------------------------------------------------------------------------------------------------------
            # train the network
            for e in range(int(num_steps)):

                # randomly permute the data
                perm = torch.randperm(nsamples)
                if cuda:
                    perm = perm.cuda()

                # for each batch, calculate the gradient with respect to the loss
                for i in range(nbatches):
                    idx = perm[i * batch_size : (i+1) * batch_size]
                    y_pred = model(x[idx])
                    loss = loss_fn(y_pred, y[idx])*1e4
                    optimizer.zero_grad()
                    loss.backward(retain_graph=False)
                    optimizer.step()

                # First time
                if self._best_state_dict is None:
                    self._best_state_dict = model.state_dict()
                    
                # the average loss
                if e % 10 == 0:

                    # randomly permute the data
                    perm_valid = torch.randperm(nsamples_valid)
                    if cuda:
                        perm_valid = perm_valid.cuda()
                    loss_valid = 0
                    
                    for j in range(nbatches_valid):
                        idx = perm_valid[j * batch_size : (j+1) * batch_size]
                        y_pred_valid = model(x_valid[idx])
                        loss_valid += loss_fn(y_pred_valid, y_valid[idx])*1e4
                    loss_valid /= nbatches_valid

                    print('iter %s:' % e, 'training loss = %.3f' % loss,\
                          'validation loss = %.3f' % loss_valid)

                    loss_data = loss.detach().data.item()
                    loss_valid_data = loss_valid.detach().data.item()
                    training_loss.append(loss_data)
                    validation_loss.append(loss_valid_data)

                    # record the weights and biases if the validation loss improves
                    if loss_valid_data < current_loss:
                        current_loss = loss_valid_data
                        self._best_state_dict = model.state_dict()

            #--------------------------------------------------------------------------------------------
            # Final values
            self.model.load_state_dict(self._best_state_dict)  # save final best values
            self.training_loss = training_loss                    
            self.validation_loss = validation_loss
            self.trained = True


# simple multi-layer perceptron model
class ClassifierModel(torch.nn.Module):
    def __init__(self, num_features, num_neurons, num_labels):
        super(ClassifierModel, self).__init__()
        self.features = torch.nn.Sequential(
            torch.nn.Linear(num_features, num_neurons),
            torch.nn.LeakyReLU(),
            torch.nn.Linear(num_neurons, num_neurons),
            torch.nn.LeakyReLU(),
            torch.nn.Linear(num_neurons, num_labels),
            torch.nn.Sigmoid()
        )
    def forward(self, x):
        return self.features(x)

class Classifier(Model):
    def __init__(self, num_features=100, num_neurons=100, num_labels=4, **kwargs):
        super().__init__(num_features, num_neurons, num_labels, **kwargs)
        self.model = ClassifierModel(num_features, num_neurons, num_labels)
    
