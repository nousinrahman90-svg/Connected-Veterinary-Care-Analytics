"""
Connected Veterinary Care & Interoperability Economic Impact Analysis (Percentage-Normalized)
Author: Nousin Rahman
Affiliation: Zicklin School of Business, Baruch College, CUNY
Description:
    Models clinical record fragmentation across multi-clinic veterinary networks,
    normalizing all financial waste and friction metrics into clear percentage distributions 
    for accessible executive and stakeholder reporting.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

def simulate_veterinary_ecosystem_normalized(n_patients=20000, random_state=42):
    """
    Simulates multi-clinic veterinary visits and normalizes output metrics into percentages.
    """
    np.random.seed(random_state)
    
    data = {
        'previous_clinics_visited': np.random.poisson(lam=1.8, size=n_patients),
        'days_since_last_lab': np.random.exponential(scale=150, size=n_patients),
        'emergency_case_flag': np.random.binomial(n=1, p=0.18, size=n_patients),
        'has_centralized_emr': np.random.binomial(n=1, p=0.22, size=n_patients), 
    }
    df = pd.DataFrame(data)
    
    friction_score = (
        (df['previous_clinics_visited'] * 0.40) +
        (df['emergency_case_flag'] * 0.45) -
        (df['has_centralized_emr'] * 0.90) +
        np.random.normal(0, 0.25, size=n_patients)
    )
    df['diagnostic_delay_or_redundancy'] = (friction_score > 0.45).astype(int)
    
    base_redundant_cost = np.random.uniform(300, 650, size=n_patients)
    df['redundant_diagnostic_cost_usd'] = df['diagnostic_delay_or_redundancy'] * (
        base_redundant_cost * (1 - df['has_centralized_emr'])
    )
    
    return df

def run_percentage_analysis():
    print("=" * 80)
    print("VETERINARY CARE FRAGMENTATION & ECONOMIC IMPACT ANALYSIS (PERCENTAGE FORMAT)")
    print("Author: Nousin Rahman | Zicklin School of Business, Baruch College")
    print("=" * 80)

    df = simulate_veterinary_ecosystem_normalized(n_patients=20000, random_state=42)
    
    feature_cols = ['previous_clinics_visited', 'days_since_last_lab', 'emergency_case_flag', 'has_centralized_emr']
    X = df[feature_cols]
    y = df['diagnostic_delay_or_redundancy']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    clf = RandomForestClassifier(n_estimators=150, max_depth=6, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    total_patients = len(df)
    friction_cases = y.sum()
    friction_pct = (friction_cases / total_patients) * 100.0
    
    total_waste_usd = df['redundant_diagnostic_cost_usd'].sum()
    max_possible_waste = total_patients * 650.0 # Upper bound reference
    waste_share_pct = (total_waste_usd / (max_possible_waste * 0.5)) * 100.0 # Normalized scale

    print(f"\n[*] Total Patient Encounters Analyzed : {total_patients:,}")
    print(f"[*] Encounters Impacted by Friction   : {friction_pct:.2f}% of total visits")
    print(f"[*] Estimated Financial Waste Share   : {min(waste_share_pct, 100.0):.2f}% of baseline diagnostic spend\n")
    
    print("--- Predictive Model Accuracy Evaluation ---")
    print(f"Model Accuracy Rate: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
    
    print("--- Feature Importance Breakdown (Normalized Relative Impact %) ---")
    importances = clf.feature_importances_
    total_imp = sum(importances)
    for col, imp in sorted(zip(feature_cols, importances), key=lambda x: x[1], reverse=True):
        pct_share = (imp / total_imp) * 100.0
        print(f"  {col:<26} : {pct_share:6.2f}%")
    
    print("\n[✓] Percentage-normalized veterinary analysis completed successfully.")

if __name__ == "__main__":
    run_percentage_analysis()
