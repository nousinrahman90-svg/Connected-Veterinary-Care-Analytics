"""
Connected Veterinary Care & Interoperability Economic Impact Analysis
Author: Nousin Rahman
Affiliation: Zicklin School of Business, Baruch College, CUNY
Description:
    Models clinical record fragmentation across multi-clinic veterinary networks,
    quantifying classification risk for diagnostic delays and calculating explicit 
    financial waste ($) from redundant bloodwork, imaging, and lab testing.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

def simulate_veterinary_ecosystem(n_patients=15000, random_state=42):
    """
    Simulates multi-clinic veterinary visits modeling:
      - previous_clinics_visited : Number of prior independent clinics visited
      - days_since_last_lab      : Elapsed time since last blood panel or diagnostic check
      - emergency_case_flag      : Binary flag for acute trauma / emergency presentation
      - has_centralized_emr      : Access status to a connected, distributed veterinary record ledger
    """
    np.random.seed(random_state)
    
    data = {
        'previous_clinics_visited': np.random.poisson(lam=1.8, size=n_patients),
        'days_since_last_lab': np.random.exponential(scale=150, size=n_patients),
        'emergency_case_flag': np.random.binomial(n=1, p=0.18, size=n_patients),
        'has_centralized_emr': np.random.binomial(n=1, p=0.22, size=n_patients), # Low interoperability baseline
    }
    df = pd.DataFrame(data)
    
    # Calculate operational friction score leading to redundant testing or clinical delay
    friction_score = (
        (df['previous_clinics_visited'] * 0.40) +
        (df['emergency_case_flag'] * 0.45) -
        (df['has_centralized_emr'] * 0.90) +
        np.random.normal(0, 0.25, size=n_patients)
    )
    df['diagnostic_delay_or_redundancy'] = (friction_score > 0.45).astype(int)
    
    # Financial Cost Model ($) for redundant diagnostics when EMR is absent
    # Average redundant blood panel + digital radiograph cost (~$350 - $600 per occurrence)
    base_redundant_cost = np.random.uniform(300, 650, size=n_patients)
    df['redundant_diagnostic_cost_usd'] = df['diagnostic_delay_or_redundancy'] * (
        base_redundant_cost * (1 - df['has_centralized_emr'])
    )
    
    return df

def run_analysis():
    print("=" * 80)
    print("VETERINARY CARE FRAGMENTATION & ECONOMIC IMPACT ANALYSIS")
    print("Author: Nousin Rahman | Zicklin School of Business, Baruch College")
    print("=" * 80)

    df = simulate_veterinary_ecosystem(n_patients=20000, random_state=42)
    
    feature_cols = ['previous_clinics_visited', 'days_since_last_lab', 'emergency_case_flag', 'has_centralized_emr']
    X = df[feature_cols]
    y = df['diagnostic_delay_or_redundancy']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    clf = RandomForestClassifier(n_estimators=150, max_depth=6, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print(f"\n[*] Total Patient Encounters Simulated : {len(df):,}")
    print(f"[*] Cases Incurring Diagnostic Friction: {y.sum():,} ({y.mean()*100:.1f}% imbalanced share)")
    print(f"[*] Total Estimated Redundant Waste  : ${df['redundant_diagnostic_cost_usd'].sum():,.2f}\n")
    
    print("--- Predictive Model Evaluation (Diagnostic Friction Classifier) ---")
    print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred, target_names=['Optimal Flow', 'Redundant/Delayed']))
    
    print("--- Feature Importance (Primary Drivers of Veterinary Inefficiency) ---")
    importances = clf.feature_importances_
    for col, imp in sorted(zip(feature_cols, importances), key=lambda x: x[1], reverse=True):
        print(f"  {col:<26} : {imp:.4f}")
    
    print("\n[✓] Veterinary economic and interoperability analysis completed successfully.")

if __name__ == "__main__":
    run_analysis()
