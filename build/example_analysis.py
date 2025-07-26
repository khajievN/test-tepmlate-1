from archetypes.healthcare_db.healthcare_db import create_dataset

# Load your dataset
dataset = create_dataset()
print(f"Dataset size: {len(dataset)} records")

# Access data with simple dot notation
for patient in dataset:
    print(f"Patient {patient.patient.patient_id}: {patient.patient.diagnosis}")
    
    # Access nested data easily
    if patient.patient.vitals.stable:
        print(f"Heart rate: {patient.patient.vitals.heart_rate} BPM")
