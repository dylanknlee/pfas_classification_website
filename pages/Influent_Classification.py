import streamlit as st
import pickle
import numpy as np

st.title("Risk Prediction of Total PFAS in Influent")

# model description
st.write("""This ML model classifies PFAS levels in WWTP influent as high risk (1) if they exceed 70 nanograms per liter (ng/L), and low risk (0) 
         if they fall below this threshold. The model utilizes commonly monitored standard operational parameters of WWTPs as inputs, including: 
         year, month, influent/effluent volumes, industrial wastewater intake, total organic carbon (TOC), ammonia, biochemical oxygen demand (BOD), 
         carbonaceous biochemical oxygen demand (CBOD), flow rate, pH, total dissolved solids (TDS), and total suspended solids (TSS).""")

st.write("""When using the model, please ensure that all inputs are in the correct format. Input values should strictly be numerical 
         floats; avoid using letters or non-numeric characters. The default values visible upon loading the website are set to median 
         values derived from the dataset used during model training. These defaults serve as starting points for predictions and can 
         be adjusted based on your specific input data.
         """)

# user instructions

# INFLUENT - influent wastewater treatment plant
# BIOSOLID - biosolid in wastewater treatment
# EFFLUENT - effluent in wastewater treament plant

# Specify the path to the model's .pkl file
file_path = 'models/CatBoost_model_inf.pkl'

# Open the file in binary read mode and load the model
with open(file_path, 'rb') as file:
    inf_classifier = pickle.load(file)

def check_input(input, title):
    try:
        converted_input = np.float64(input)
        return converted_input
    except ValueError:
        st.error("Please enter a valid number for {0}".format(title))
        return False

inputs = dict()

# INPUT 1 - Year
year = st.number_input("Select a Year", min_value=1900, max_value=2100, value=2024, step=1)
inputs["Year"] = year

#--------------------------------------------------------------------------------------------------

# INPUT 2 - Month
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Mapping of months to their corresponding integer values
month_to_int = {month: i+1 for i, month in enumerate(months)}

# Dropdown menu for selecting month
selected_month = st.selectbox("Select a Month", months)

# Get the corresponding integer value for the selected month
inputs["Month"] = month_to_int[selected_month]

#--------------------------------------------------------------------------------------------------

# INPUT 3 - Discharge Volume
discharge_volume = st.text_input("Discharge Volume", "169.25")

inputs["Discharge Volume"] = check_input(discharge_volume, "Discharge Volume")

#--------------------------------------------------------------------------------------------------

# INPUT 4 - Influent Volume
influent_volume = st.text_input("Influent Volume", "387")

inputs["Influent Volume"] = check_input(influent_volume, "Influent Volume")

#--------------------------------------------------------------------------------------------------

# INPUT 5 - Industrial Total
industrial_total = st.text_input("Industrial Total", "0.625")

inputs["Industrial Total"] = check_input(industrial_total, "Industrial Total")

#--------------------------------------------------------------------------------------------------

# INPUT 6 - Total ammonia
total_ammonia = st.text_input("Total Ammonia", "22300000")

inputs["Total Ammonia"] = check_input(total_ammonia, "Total Ammonia")

#--------------------------------------------------------------------------------------------------

# INPUT 7 - Biochemical Oxygen Demand
biochemical_oxygen_demand = st.text_input("Biochemical Oxygen Demand", "255668102.2")

inputs["Biochemical Oxygen Demand"] = check_input(biochemical_oxygen_demand, 
                                                    "Biochemical Oxygen Demand")

#--------------------------------------------------------------------------------------------------

# INPUT 8 - Carbonaceous Biochemical Oxygen Demand
carbonaceous_biochemical_oxygen_demand = st.text_input("Carbonaceous Biochemical Oxygen Demand", 
                                                       "645000000")

inputs["Carbonaceous Biochemical Oxygen Demand"] = check_input(
                                                        carbonaceous_biochemical_oxygen_demand,
                                                        "Carbonaceous Biochemical Oxygen Demand"
                                                        )

#--------------------------------------------------------------------------------------------------

# INPUT 9 - Flow
flow = st.text_input("Flow", "3.1334")

inputs["Flow"] = check_input(flow, "Flow")

#--------------------------------------------------------------------------------------------------

# INPUT 10 - Total Dissolved Solids
total_dissolved_solids = st.text_input("Total Dissolved Solids", "250000")

inputs["Total Dissolved Solids"] = check_input(total_dissolved_solids,
                                               "Total Dissolved Solids")

#--------------------------------------------------------------------------------------------------

# INPUT 11 - Total Organic Carbon
total_organic_carbon = st.text_input("Total Organic Carbon", "250000")

inputs["Total Organic Carbon"] = check_input(total_organic_carbon,
                                             "Total Organic Carbon")

#--------------------------------------------------------------------------------------------------

# INPUT 12 - Total Suspended Solids
total_suspended_solids = st.text_input("Total Suspended Solids", "240900372.8")

inputs["Total Suspended Solids"] = check_input(total_suspended_solids,
                                               "Total Suspended Solids")

#--------------------------------------------------------------------------------------------------

# INPUT 13 - pH
ph = st.text_input("pH", "7.0")

# custom pH error checking function
try:
    converted_input = np.float64(ph)
    if 0 <= converted_input <= 14:
        inputs["pH"] = converted_input
    else:
        st.error("The {0} value must be between 0 and 14".format('pH'))
        inputs["pH"] = False
except ValueError:
    st.error("Please enter a valid number for {0}".format("pH"))
    inputs["pH"] = False

#--------------------------------------------------------------------------------------------------

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
        prediction = inf_classifier.predict(list(inputs.values()))

        if prediction == 0:
            st.write("The PFAS risk is lower than 70 nanograms per liter (70 ng/L).")
        else:
            st.write("The PFAS risk is greater than 70 nanograms per liter (70 ng/L).")

