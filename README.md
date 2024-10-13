## Fabric Detection Project: 

#### Overview
This branch contains the initial work of the Fabric Detection Project, which was developed and tested on a local laptop environment. The focus here is on exploring and prototyping various image processing techniques, feature extraction methods, and machine learning models to classify different types of fabrics. The project handles the classification of five fabric types: cotton, corduroy, denim, linen, and wool.

#### Project Structure
The structure of this branch reflects the prototyping phase, where Jupyter notebooks were primarily used to experiment with various components of the fabric detection pipeline. The structure is as follows:

```
.gitignore
    README.md
    tree.py       # Provides the folder structure of the repository
    tree_structure.txt  # Contains the folder structure of the repository
    laptop_notebooks/ 
        1. Feature Extra & Model training.ipynb
        2. Feature Extraction.ipynb
        1. Model Training.ipynb
        2. Model Training RAPIDS.ipynb
        3. model_training_effective.ipynb
        cpu_gpu.ipynb
        environment.yml
        environment1.yml
        library_installation.ipynb
        Feature Extraction Techniques Trials/
            Canny Edge Detection.ipynb
            data_augmentation.ipynb
            data_augmentation_1.ipynb
            Gabor filter.ipynb
            Local Binary Pattern.ipynb
            SIFT.ipynb
            .ipynb_checkpoints/
                Canny Edge Detection-checkpoint.ipynb
                Fourier Transform-checkpoint.ipynb
                Gabor filter-checkpoint.ipynb
                Local Binary Pattern-checkpoint.ipynb
                SIFT-checkpoint.ipynb
            Gabor Filters/
                denim.ipynb
                wool.ipynb
```

#### Note about the various files and folders in this repo:

1. Feature Extraction Techniques Trials: 
- Various feature extraction techniques have been tried and tested in this folder on each type of fabric. 
- The notebooks have been named as per the feature extraction techniques tried in that notebook. 
- The folder `Gabor Filters` was created with two notebooks, viz., denim.ipymb and wool.ipynb to further check whether significant features were being extracted from the images of denim and wool by applying this technique or not.

2.  `Feature Extra & Model training.ipynb` & `Feature Extraction.ipynb`:
- In these notebooks we have further gone to write the full code to implement the feature extraction techniques validated in the `Feature Extraction Techniques Trials` folder.

3. `Model Traning.ipynb`: 
- In this notebook we have tried to apply nested cross validation using scikit-learn with Random Forest Classifier & Support Vector Machines Classifier.

4. `Model Training RAPIDS.ipynb`:
- In this notebook we have implemented the NVIDIA RAPIDS library to utilize the computational power of our GPUs to handle the Nested Cross Validation process which could not be performed by our CPU alone.
- Implementing the RAPIDS library, we realized that :<br>
    <t><t>a. Compatible version of Tensorflow and RAPIDS could not be setup.<br>
    <t><t>b. Removing Tensorflow from our environment may still not solve our issue as the computational requirements were much larger than what our systems could afford.


#### **Key Insights**:
1. The following feature extraction techniques were decided to extract features from the images based on several trials on images of different fabrics:
- Local Binary Pattern(LBP)
- Gabor Filters
- Canny Edge Detection

2. Our hardware requirements to train and validate the ML model were far from what we could afford on our local system. 
**So we decided to train our model on Google Colab Pro Cloud with higher compuatational resources.**

