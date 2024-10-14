### Fabric Detection Model Performance Analysis

The results of the nested cross validation that we ran in our notebook `Memory_optimzd_Model_Training.ipynb` have been analyzed here.

The avg. accuracy  = 52.16 %
The avg. macro average F! score = 51%

**In our problem, we will be focusing on improving the macro average F! score,  emphasizing the tradeoff between precision and recall. We want to reduce both the false positives and false negatives.**

**Why we want to reduce both False Positives & False Negatives?**
----

#### Model Wise Peformance Analysis
1. SVM Model Performance
- Best Parameters and Scores:
  - The optimal C parameter varies significantly across runs, indicating sensitivity to this hyperparameter.
  - The number of PCA components also varies (1000, 2000, 3000), affecting the model's performance.
  - The best F1 scores for the SVM model range from approximately 0.44 to 0.48.
- Classification Metrics:
  - Accuracy ranges from 47% to 52%.
  - The SVM model shows high precision but lower recall for certain classes, particularly Class 3.
  - Macro and weighted average F1-scores hover around 0.45 to 0.53.

2. Random Forest Model Performance
- Best Parameters and Scores:
  - The max_depth parameter remains consistent at 20 across all runs, suggesting a stable optimal depth.
  - The number of estimators (n_estimators) and PCA components vary slightly.
  - The best F1 scores for the RF model range from approximately 0.50 to 0.52.
- Classification Metrics:
  - Accuracy ranges from 53% to 56%, consistently higher than the SVM model.
  - The RF model demonstrates a better balance between precision and recall across all classes.
  - Macro and weighted average F1-scores are higher, ranging from 0.51 to 0.54.


#### Class-wise Performance Analysis
1. Class 1 (Corduroy):
- SVM: High recall but low precision, indicating many false positives.
- RF: High precision but lower recall, suggesting fewer predictions but more accurate ones.

2. Class 2(Cotton) and 3(Denim):
- RF outperforms SVM with higher recall and F1-scores, indicating better identification of these classes.

3. Classes 4(Linen) and 5(Wool):
- Both models struggle, but RF maintains slightly better performance.




To analyze the **reasons** behind the poor performance of our models(both SVM & Random Forest) we went through the following approaches:
1. Validated our feature extraction methods again by visually analyzing the features extracted from each class of fabric by each method over a large number of images:
    - Our feature extraction technqiues were able to identify significant features from the fabric images.
      
2. Checked the amount of explained variance of our data at different values of PCA components(`n_components`):
   - Created a new notebook `PCA_explained_variance.ipynb` to understand the explained variance at different levels of `n_components`.
   - n_components=1000 & n_components=2000 had a cumulative variance of only 44% & 60% respectively.
   - n_components=3000 & n_components=4000 had a cumulative variance of 70% & 78% respectively.
   - Decided to go with at least n_components = 3000 and maximum n_components=4000 so that maximum information can be captured from our data.
    
3. Validated whether our choice of fabric categories is correct or not:
   - We are originally using the following fabric categories for classification: cotton, corduroy, denim, wool & linen.
   - On reiterating through our literature review, we realized that corduroy can be made from cotton, wool 
