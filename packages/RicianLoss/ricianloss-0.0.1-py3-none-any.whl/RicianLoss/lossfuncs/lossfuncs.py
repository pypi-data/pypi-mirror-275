import numpy as np
import scipy
import torch
import importlib.util
if importlib.util.find_spec("tensorflow"):
    import tensorflow as tf
    from tensorflow import keras

if importlib.util.find_spec("tensorflow_probability"):
    import tensorflow_probability as tfp


# Python function
def ricianloss_py(predictions, inputs, sigma):
    term1 = np.log(inputs / (sigma ** 2))
    term2 = -(inputs ** 2 + predictions ** 2) / (2 * (sigma ** 2))
    z = (inputs * predictions) / (sigma ** 2)
    I0e = scipy.special.i0e(z)
    lI0e = np.log(I0e)
    term3 = lI0e + z
    log_pdf = term1 + term2 + term3
    n_batch = inputs.shape[0]
    loss = -np.sum(log_pdf) / n_batch
    return loss


# PyTorch function
def ricianloss_pt(predictions, inputs, sigma):
    term1 = torch.log(inputs / (sigma ** 2))
    term2 = -(inputs ** 2 + predictions ** 2) / (2 * (sigma ** 2))
    z = (inputs * predictions) / (sigma ** 2)
    I0e = torch.special.i0e(z)
    lI0e = torch.log(I0e)
    term3 = lI0e + z
    log_pdf = term1 + term2 + term3
    n_batch = inputs.shape[0]
    loss = -torch.sum(log_pdf) / n_batch
    return loss


# PyTorch class
class ricianloss_ptcl(torch.nn.Module):
    def __init__(self, sigma=0.05):
        super(ricianloss_ptcl, self).__init__()
        self.sigma = sigma
    #
    def forward(self, predictions, inputs):
        loss = ricianloss_pt(predictions, inputs, self.sigma)
        return loss


if importlib.util.find_spec("tensorflow"):
    # Tensorflow function
    def ricianloss_tf(predictions, inputs, sigma):
        term1 = tf.math.log(inputs / (sigma ** 2))
        term2 = -(inputs ** 2 + predictions ** 2) / (2 * (sigma ** 2))
        z = (inputs * predictions) / (sigma ** 2)
        I0e = tfp.math.bessel_ive(0,z)
        lI0e = tf.math.log(I0e)
        term3 = lI0e + z
        log_pdf = term1 + term2 + term3
        n_batch = inputs.shape[0]
        loss = -tf.sum(log_pdf) / n_batch
        return loss
    #
    # Tensorflow class (but advised to use Keras in TF2)
    class ricianloss_tfcl(tf.compat.v1.losses):
        def __init__(self, sigma=0.05, **kwargs):
            super().__init__(**kwargs)
            self.sigma = sigma
        #
        def call(self, predictions, inputs):
            loss = ricianloss_tf(predictions, inputs, self.sigma)
            return loss
        #
        def get_config(self):
            config = { 'sigma' : self.sigma }
            # base_config = super().get_config()
            return { **config }
    #
    # Keras function (same as tensorflow)
    def ricianloss_ks(predictions, inputs, sigma):
        term1 = tf.math.log(inputs / (sigma ** 2))
        term2 = -(inputs ** 2 + predictions ** 2) / (2 * (sigma ** 2))
        z = (inputs * predictions) / (sigma ** 2)
        I0e = tfp.math.bessel_ive(0,z)
        lI0e = tf.math.log(I0e)
        term3 = lI0e + z
        log_pdf = term1 + term2 + term3
        n_batch = inputs.shape[0]
        loss = -tf.sum(log_pdf) / n_batch
        return loss
    #
    # Keras class
    class ricianloss_kscl(tf.keras.losses.Loss):
        def __init__(self, sigma=0.05, name='Rician', **kwargs):
            super().__init__(name=name, **kwargs)
            self.sigma = sigma
        #
        def call(self, predictions, inputs):
            loss = ricianloss_ks(predictions, inputs, self.sigma)
            return loss
        #
        def get_config(self):
            config = { 'sigma' : self.sigma }
            base_config = super().get_config()
            return { **base_config, **config }


