# Simple Expert System in Python

def diagnose():
    print("=== Simple Medical Expert System ===")
    print("Answer with 'yes' or 'no'\n")

    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    headache = input("Do you have a headache? ").lower()
    sore_throat = input("Do you have a sore throat? ").lower()
    runny_nose = input("Do you have a runny nose? ").lower()
    body_pain = input("Do you have body pain? ").lower()

    # Rule-based logic
    if fever == "yes" and cough == "yes" and body_pain == "yes":
        print("\n🤒 You may have the Flu.")
    elif sore_throat == "yes" and runny_nose == "yes":
        print("\n🤧 You may have the Common Cold.")
    elif headache == "yes" and fever == "yes":
        print("\n🥵 You may have a Viral Infection.")
    elif cough == "yes" and sore_throat == "yes":
        print("\n😷 You may have Throat Infection.")
    else:
        print("\n🙂 You seem healthy, but stay hydrated and take care!")

# Run the expert system
diagnose()
