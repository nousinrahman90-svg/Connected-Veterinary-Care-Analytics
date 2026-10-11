# Connected-Veterinary-Care-Analytics
Professional documentation detailing veterinary interoperability challenges, missing clinical history, and financial loss metrics.


VETERINARY CARE FRAGMENTATION & ECONOMIC IMPACT ANALYSIS
Author: Nousin Rahman | Zicklin School of Business, Baruch College
================================================================================

[*] Total Patient Encounters Simulated : 20,000
[*] Cases Incurring Diagnostic Friction: 11,504 (57.5% imbalanced share)
[*] Total Estimated Redundant Waste  : $5,109,394.52

--- Predictive Model Evaluation (Diagnostic Friction Classifier) ---
Accuracy Score: 0.8780
                   precision    recall  f1-score   support

     Optimal Flow       0.80      0.95      0.87      2549
Redundant/Delayed       0.96      0.83      0.89      3451

         accuracy                           0.88      6000
        macro avg       0.88      0.89      0.88      6000
     weighted avg       0.89      0.88      0.88      6000

--- Feature Importance (Primary Drivers of Veterinary Inefficiency) ---
  previous_clinics_visited   : 0.6014
  has_centralized_emr        : 0.3054
  emergency_case_flag        : 0.0798
  days_since_last_lab        : 0.0135

[✓] Veterinary economic and interoperability analysis completed successfully.

