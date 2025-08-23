from archetypes.healthcare_db.healthcare_db import create_dataset

# Load your dataset
dataset = create_dataset()
print(f"Dataset size: {len(dataset)} records")

def checkUsers():
    listOfUsers = []
    # Access data with simple dot notation
    for patient in dataset:
        print(f"Patient: {patient.patient.diagnosis}")
        print(f"Patient ID: {patient.patient.patient_id}")
        listOfUsers.append(patient)
        # Access nested data easily
        if patient.patient.vitals.stable:
            print(f"Heart rate: {patient.patient.vitals.heart_rate} BPM")

    return listOfUsers
