### Fabric Detection Model Performance Analysis

The results of the nested cross validation that we ran in our notebook `Memory_optimzd_Model_Training.ipynb` have been analyzed here.

The avg. accuracy  = 52.16 %
The avg. macro average F! score = 51%

**In our problem, we will be focusing on improving the macro average F! score,  emphasizing the tradeoff between precision and recall. We want to reduce both the false positives and false negatives.**

**Why we want to reduce both False Positives & False Negatives?**
1. False Positives (FP) 

A false positive occurs when the model incorrectly classifies a fabric as belonging to a different category than it actually does. For instance, a model might classify cotton as polyester when it is actually cotton. Reducing false positives is important because:

  - Incorrect Fabric Usage: Misclassifying fabric types can lead to the wrong materials being used in production processes. Each fabric type has distinct properties, such as breathability, texture, or elasticity, that may be required for specific applications. For example, using polyester in place of cotton can result in products that do not meet the desired performance or quality standards.

  - Customer Dissatisfaction: When fabrics are misclassified, end users or customers relying on the classification system may receive materials that do not match their expectations. This can lead to dissatisfaction if the received fabric does not meet the required properties for a particular use case, such as softness, durability, or appearance.


2. False Negatives (FN)
A false negative occurs when the model fails to correctly identify a fabric type, classifying it as a different fabric or missing it entirely. For example, the model may classify wool as nylon. Reducing false negatives is equally critical for the following reasons:

  - Missed Opportunities for Appropriate Use: Each fabric type has specific properties that make it suitable for certain applications. If a fabric like wool is misclassified, its specific benefits (such as insulation properties in wool) may not be utilized in contexts where they are needed, leading to suboptimal product design or manufacturing choices.

  - Incorrect Product Matching: In applications where specific fabric properties are critical (such as clothing, upholstery, or industrial fabrics), failing to correctly identify a fabric type could result in products that do not perform as expected. This can lead to further production issues and potential customer returns.

  - Inventory and Supply Chain Confusion: Misclassifications within inventory systems can lead to errors in stock management. For instance, if fabric types are incorrectly categorized, this can create confusion in stock-keeping units (SKUs) and disrupt supply chain processes, leading to inefficiencies and increased operational costs.


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




#### To analyze the **reasons** behind the poor performance of our models(both SVM & Random Forest) we went through the following approaches:
1. Validated our feature extraction methods again by visually analyzing the features extracted from each class of fabric by each method over a large number of images:
    - Our feature extraction technqiues were able to identify significant features from the fabric images.
      
2. Validated whether our choice of fabric categories is correct or not:
   - We are originally using the following fabric categories for classification: cotton, corduroy, denim, wool & linen.
   - On reiterating through our literature review, we came to know that corduroy can be made from  cotton,wool and linen.
   - This means that an image of corduroy fabric may be classified as cotton, corduroy ,wool and linen at the same time since the material used to make corduroy is cotton, wool, or linen. This may arise confusion in our model and may be responsible for the poor performance of our model.
   - Through our literature review we also came to know that denim can be made from cotton & linen, thus again confusing our model between the fabrics.
   - **Taking all these discrepancies into consideration we now decided to only go with two fabric categories, viz., corduroy and denim**
  
3. Checked the amount of explained variance of our data at different values of PCA components(`n_components`) :
   - Created a new notebook `PCA_explained_variance.ipynb` to understand the explained variance at different levels of `n_components`.
   - n_components=1000 & n_components=2000 had a cumulative variance of only 44% & 60% respectively.
   - n_components=3000 & n_components=4000 had a cumulative variance of 70% & 78% respectively.
   -  Decided to go with the maximum number of principal components by taking `n_components=None`.
  

**References**

[1] Fabricsight, "Corduroy: A versatile fabric with history," Accessed: Sept. 20, 2024. [Online]. Available: https://www.fabricsight.com/blogs/posts/corduroy-a-versatile-fabric-with-history

[2] Sewport, "Corduroy fabric," Accessed: Sept. 20, 2024. [Online]. Available: https://sewport.com/fabrics-directory/corduroy-fabric#:~:text=While%20it%20is%20usually%20made,corduroy%20made%20with%20other%20materials

[3] Wikipedia, "Corduroy," Oct. 2024. [Online]. Available: https://en.wikipedia.org/wiki/Corduroy

[4] Sino Comfort, "What is corduroy fabric made of?," May 2024. Accessed: Sept. 20, 2024. [Online]. Available: https://sinocomfort.com/blog/what-is-corduroy-fabric-made-of

[5] A Hand Tailored Suit, "What is corduroy?", Dec. 2022. Accessed: Sept. 20, 2024. [Online]. Available: https://ahandtailoredsuit.com/blogs/off-the-cuff/what-is-corduroy

[6] Britannica, "Denim," Accessed: Sept. 20, 2024. [Online]. Available: https://www.britannica.com/topic/denim

[7] Hockerty, "What are jeans made of?" Accessed: Sept. 20, 2024. [Online]. Available: https://www.hockerty.com/en/blog/what-are-jeans-made-of#:~:text=Denim%20is%20a%20sturdy%2C%20100,material%20using%20plain%20single%20weave.&text=The%20yarn%20we%20get%20from,to%20have%20a%20different%20color

[8] Wikipedia, "Denim," May 2023. [Online]. Available: https://en.wikipedia.org/wiki/Denim

[9] Sewport, "Denim fabric," Accessed: Sept. 20, 2024. [Online]. Available: https://sewport.com/fabrics-directory/denim-fabric
