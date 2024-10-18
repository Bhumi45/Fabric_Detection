# Fabric Detection Model - Deployment Pipeline Branch

## Overview

- This branch, **deployment_pipeline**, contains the final code for the machine learning model's Deployment pipeline.
- **To deploy it to ElasticBeanstalk environment you would need to refer to our `ebs_deployment` branch.**  
- The goal of this branch is to offer a stable and well-optimized pipeline for running fabric classification model as a Flask web application.

**_Note: This branch only contains the finalised code for Deployment pipeline not for Training pipeline. Also the code is not yet configured to be deployed in any cloud services. To deploy in ElasticBeanstalk environment check out our `ebs_deployment` branch._**
 
## Pipeline components:

#### 1. Image Processing
- Converts to grayscale and resizes the image before feature extraction

#### 2. Feature Extraction
- Extracts the features from the image using Canny Edge, Gabor Filters and Local Binary Pattern(LBP) Techniques

#### 3. Feature Engineering
- Transforms the features using the Feature Engineering pipeline saved from the Training Pipeline.

#### 4. Prediction
- Returns the predicted label for the image using the final model trained in the Training pipeline.


## Key Files

- **`deployment/prediction_pipeline.py`**: Executes the various components of the pipeline
- **`deployment/app.py`**: Run the model as a flask web application


## Installation

Follow the steps below to set up the environment:

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Parthsarthi-lab/Fabric_Detection.git
    cd Fabric_Detection
    git checkout deployment_pipeline
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Deployment Pipeline

To run flask web application, execute the following command:

```bash
python deployment/app.py
```
