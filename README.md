# Fabric Detection Model - Development Branch

## Overview

This is the **development** branch of the Fabric Detection Model project. The branch contains ongoing development work, including the folder structure setup and initial versions of the training pipeline. This branch is actively being updated with new features, improvements, and experimental code.

The goal of this project is to create a machine learning model capable of detecting and classifying **corduroy** and **denim** fabrics from images, using a modular pipeline for training and deployment.

## Features in Development

- **Training Pipeline**: In-progress implementation of the pipeline for training the fabric classification model.
- **Deployment Pipeline**: Code for deploying the model, under active development.

## Branch Purpose

The **development** branch is a workspace for integrating, testing, and refining new features before they are merged into the stable **main** branch. It is used for:
- Implementing new functionalities (e.g., pipelines, utilities).
- Integrating different components like image processing, feature extraction, and model training.
- Testing and validating code before moving it to the **main** branch.

## Feature Branches

1. `final_train_pipeline` : Contains the training pipeline code. Merges into this `development_branch`
2. `deployment_pipeline`: Contains the deployment pipeline code. Merges its sub-branch `ebs_deployment` into this `development_branch`
This branch may contain incomplete or experimental code and should not be used for production purposes.

## Project Structure

- **`artifacts/`**: Temporary storage for intermediate outputs such as models and processed images.
- **`common/`**: Utility scripts like configuration management.
- **`deployment/`**: Code for deploying the model, including configurations for AWS Elastic Beanstalk.
- **`training/`**: Code for the training pipeline.
- **`final_train_pipeline/`**: Contains final, stable training pipeline code before merging into the development branch.
- **`deployment_pipeline/`**: Contains the deployment pipeline code under development.
- **`requirements.txt`**: Lists dependencies for development and testing purposes.


