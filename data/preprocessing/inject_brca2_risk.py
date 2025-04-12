# ✅ FILE: data/preprocessing/inject_brca2_risk.py
import pandas as pd

metadata_path = "data/metadata/patient_metadata.csv"  # Adjust if your path is different
output_path = "data/metadata/mirai_patient_metadata_brca2.csv"

# Patients with known BRCA2 pathogenic variants (example list)
brca2_positive_patients = [1, 5, 8]  # You can update based on real data

# Load and inject
df = pd.read_csv(metadata_path)
df['BRCA2_pathogenic_status'] = df['patient_id'].apply(
    lambda pid: 1 if pid in brca2_positive_patients else 0
)

df.to_csv(output_path, index=False)
print(f"✅ Injected BRCA2 into metadata → saved to {output_path}")
