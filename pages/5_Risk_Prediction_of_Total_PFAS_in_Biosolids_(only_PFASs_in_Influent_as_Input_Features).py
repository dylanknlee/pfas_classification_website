import streamlit as st
import pickle
import numpy as np

st.title("Risk Prediction of Total PFAS in Biosolid (only PFASs in Influent as Input Features)")

# model description
st.write("""This ML model classifies Total PFAS levels in WWTP biosolids as high risk if they are detected and low risk if 
         they are not detected. The model utilizes 39 PFAS's measured in influent as inputs.""")

st.write("""When using the model, please ensure that all inputs are in the correct format. Input values should strictly be numerical 
         floats; avoid using letters or non-numeric characters. The default values visible upon loading the website are set to median 
         values derived from the dataset used during model training. These defaults serve as starting points for predictions and can 
         be adjusted based on your specific input data.
         """)

# Specify the path to the model's .pkl file
file_path = 'models/AdaBoost_model_BIO_web.pkl'

# Open the file in binary read mode and load the model
with open(file_path, 'rb') as file:
    bio_classifier = pickle.load(file)

def check_input(input, title):
    try:
        converted_input = np.float64(input)
        return converted_input
    except ValueError:
        st.error("Please enter a valid number for {0}".format(title))
        return False

inputs = dict()

chemicals = [
    "PFBA (ng/L)", "PFPeA (ng/L)", "PFHxA (ng/L)", "PFHpA (ng/L)", "PFOA (ng/L)", 
    "PFNA (ng/L)", "PFDA (ng/L)", "PFUnA (ng/L)", "PFDoA (ng/L)", "PFTrDA (ng/L)", 
    "PFTA (ng/L)", "PFHxDA (ng/L)", "PFODA (ng/L)", "3:3 FTCA (ng/L)", "5:3 FTCA (ng/L)", 
    "7:3 FTCA (ng/L)", "4:2 FTS (ng/L)", "6:2 FTS (ng/L)", "8:2 FTS (ng/L)", "10:2 FTS (ng/L)", 
    "PFBS (ng/L)", "PFPeS (ng/L)", "PFHxS (ng/L)", "PFHpS (ng/L)", "PFOS (ng/L)", 
    "PFNS (ng/L)", "PFDS (ng/L)", "PFDoS (ng/L)", "FOSA (ng/L)", "MeFOSA (ng/L)", 
    "EtFOSA (ng/L)", "MeFOSE (ng/L)", "EtFOSE (ng/L)", "NMeFOSAA (ng/L)", "NEtFOSAA (ng/L)", 
    "ADONA (ng/L)", "HFPO_DA (GenX) (ng/L)", "11ClPF3OUDS (ng/L)", "9ClPF3ONS (ng/L)"
]

for chemical in chemicals:
    value = st.text_input(chemical, "0")
    inputs[chemical.lower().replace(" ", "_")] = check_input(value, chemical)

# User Prediction
if st.button("Make Prediction"):
    # obtain any invalid inputs
    invalid_inputs = [key for key, value in inputs.items() if value is False]

    # find all invalid inputs, if any
    if invalid_inputs:
        # print an error message if any inputs are invalid
        st.error("The following inputs are invalid: " + ", ".join(invalid_inputs))
    else:
        # inputs are all valid, make prediction
        inputs = list(inputs.values())
        inputs = [inputs]
        prediction = bio_classifier.predict(inputs)
        if prediction == 0:
            st.write("PFAS is at low risk for detection in biosolids.")
        else:
            st.write("PFAS is at high risk for detection in biosolids.")