from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='RicianLoss',
   version='0.0.1',
   description='Rician likelihood loss for self-supervised deep learning from MRI',
   license="MIT",
   long_description=long_description,
   author='Christopher S. Parker',
   author_email='christopher.parker@ucl.ac.uk',
   url="http://github.com/csparker/",
   packages=['RicianLoss'],  #same as name
   install_requires=['numpy', 'torch', 'tqdm', 'SimpleITK'], #external packages as dependencies
   scripts=[
            'examples/example_qmri',
            'examples/example_autoencoder',
            'lossfuncs/lossfuncs',
            'modelfuncs/modelfuncs',
            'nnfuncs/nnfuncs',
            'sigma/sigma',
            'tests/test_1',
            'tests/test_2',
            'tests/test_3',
            'tests/test_4',
            'utils/utils'
           ]
)