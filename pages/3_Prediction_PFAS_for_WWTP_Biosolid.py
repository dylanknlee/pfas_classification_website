import streamlit as st
import numpy as np
import pickle

# Specify the path to the model's .pkl file
file_path = 'models/CatBoost_model_bio.pkl'

# Open the file in binary read mode and load the model
with open(file_path, 'rb') as file:
    bio_classifier = pickle.load(file)

st.title("Risk Prediction of Total PFAS in Biosolids")

st.write("""This ML model classifies PFAS levels in WWTP biosolids as high risk (1) if they are detected and low risk (0) if 
         they are not detected. The model utilizes commonly monitored standard operational parameters of WWTPs as inputs, including: 
         year, month, influent/effluent volumes, industrial wastewater intake, total organic carbon (TOC), ammonia, biochemical oxygen 
         demand (BOD), carbonaceous biochemical oxygen demand (CBOD), flow rate, pH, total dissolved solids (TDS), and total suspended 
         solids (TSS).""")

st.write("""When using the model, please ensure that all inputs are in the correct format. Input values should strictly be numerical 
         floats; avoid using letters or non-numeric characters. The default values visible upon loading the website are set to median 
         values derived from the dataset used during model training. These defaults serve as starting points for predictions and can 
         be adjusted based on your specific input data.
         """)

# if detected - PFAS is at high risk for detection in biosolids.
# if detected - PFAS is at low risk for detection in biosolids.

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

# INPUT - Influent Volume
influent_volume = st.text_input("Influent Volume (acre-feet/month)", "387")

inputs["Influent Volume"] = check_input(influent_volume, "Influent Volume")

#--------------------------------------------------------------------------------------------------

# INPUT - Discharge Volume
discharge_volume = st.text_input("Discharge Volume in Influent (acre-feet/month)", "169.25")

inputs["Discharge Volume"] = check_input(discharge_volume, "Discharge Volume (Influent)")

#--------------------------------------------------------------------------------------------------

# INPUT - Industrial Total
industrial_total = st.text_input("Industrial Total in Influent (Percentage of total industrial inflow in all inflow) (%)", "0.625")

inputs["Industrial Total"] = check_input(industrial_total, "Industrial Total (Influent)")

#--------------------------------------------------------------------------------------------------

# INPUT - Total Ammonia (Influent)
total_ammonia = st.text_input("Total Ammonia in Influent (NH4 + NH3 (ng/L))", "22300000")

inputs["Total Ammonia (Influent)"] = check_input(total_ammonia, "Total Ammonia (Influent)")

#--------------------------------------------------------------------------------------------------

# INPUT - Biochemical Oxygen Demand (Influent)
biochemical_oxygen_demand = st.text_input("Biochemical Oxygen Demand in Influent (BOD was measured in 5 days at 20 deg. C (ng/L))", "255668102.2")

inputs["Biochemical Oxygen Demand (Influent)"] = check_input(biochemical_oxygen_demand, 
                                                    "Biochemical Oxygen Demand (Influent)")

#--------------------------------------------------------------------------------------------------

# INPUT - Carbonaceous Biochemical Oxygen Demand (Influent)
carbonaceous_biochemical_oxygen_demand = st.text_input("Carbonaceous Biochemical Oxygen Demand in Influent (CBOD was measured in 5 days at 20 deg. C (ng/L))", 
                                                       "645000000")

inputs["Carbonaceous Biochemical Oxygen Demand (Influent)"] = check_input(
                                                        carbonaceous_biochemical_oxygen_demand,
                                                        "Carbonaceous Biochemical Oxygen Demand (Influent)"
                                                        )
#--------------------------------------------------------------------------------------------------

# INPUT - Total Dissolved Solids (Influent)
total_dissolved_solids = st.text_input("Total Dissolved Solids in Influent (TDS (ng/L))", "507170067")

inputs["Total Dissolved Solids (Influent)"] = check_input(total_dissolved_solids,
                                               "Total Dissolved Solids (Influent)")

#--------------------------------------------------------------------------------------------------

# INPUT - Total Organic Carbon (Influent)
total_organic_carbon = st.text_input("Total Organic Carbon in Influent (TOC (ng/L))", "16043614")

inputs["Total Organic Carbon (Influent)"] = check_input(total_organic_carbon,
                                             "Total Organic Carbon (Influent)")

#--------------------------------------------------------------------------------------------------

# INPUT - Total Suspended Solids (Influent)
total_suspended_solids = st.text_input("Total Suspended Solids in Influent (TSS (ng/L))", "240900372.8")

inputs["Total Suspended Solids (Influent)"] = check_input(total_suspended_solids,
                                               "Total Suspended Solids (Influent)")

#--------------------------------------------------------------------------------------------------

# INPUT - pH (Influent)
ph = st.text_input("pH of Influent", "7.0")

# custom pH error checking function
try:
    converted_input = np.float64(ph)
    if 0 <= converted_input <= 14:
        inputs["pH (Influent)"] = converted_input
    else:
        st.error("The {0} value must be between 0 and 14".format('influent pH.'))
        inputs["pH (Influent)"] = False
except ValueError:
    st.error("Please enter a valid number for the {0}".format("influent pH."))
    inputs["pH (Influent)"] = False

#--------------------------------------------------------------------------------------------------

# INPUT 14 - Total Ammonia (Effluent)
total_ammonia_eff = st.text_input("Total Ammonia in Effluent", "176526.7692")

inputs["Total Ammonia (Effluent)"] = check_input(total_ammonia_eff, "Total Ammonia (Effluent)")

#--------------------------------------------------------------------------------------------------

# INPUT 15 - Biochemical Oxygen Demand, Percent Removal (Effluent)
bod_pr_eff = st.text_input("Biochemical Oxygen Demand, Percent Removal in Effluent", "0")

inputs["Biochemical Oxygen Demand, Percent Removal (Effluent)"] = check_input(bod_pr_eff, 
                                                          "Biochemical Oxygen Demand, Percent Removal (Effluent)")

#--------------------------------------------------------------------------------------------------

# INPUT 16 - Biochemical Oxygen Demand (Effluent)
biochemical_oxygen_demand_eff = st.text_input("Biochemical Oxygen Demand in Effluent", "2873391.258")

inputs["Biochemical Oxygen Demand (Effluent)"] = check_input(biochemical_oxygen_demand_eff, 
                                                    "Biochemical Oxygen Demand (Effluent)")

#--------------------------------------------------------------------------------------------------

# INPUT 17 - Carbonaceous Biochemical Oxygen Demand (Effluent)
carbonaceous_biochemical_oxygen_demand_eff = st.text_input("Carbonaceous Biochemical Oxygen Demand in Effluent", 
                                                       "2372284.641")

inputs["Carbonaceous Biochemical Oxygen Demand (Effluent)"] = check_input(
                                                        carbonaceous_biochemical_oxygen_demand_eff,
                                                        "Carbonaceous Biochemical Oxygen Demand (Effluent)"
                                                        )

#--------------------------------------------------------------------------------------------------

# INPUT 18 - Total Nitrate

total_nitrate = st.text_input("Total Nitrate in Effluent", "0")

inputs["Total Nitrate"] = check_input(total_nitrate, "Total Nitrate")

#--------------------------------------------------------------------------------------------------

# INPUT 19 - Total Nitrite

total_nitrite = st.text_input("Total Nitrite in Effluent", "0")

inputs["Total Nitrite"] = check_input(total_nitrite, "Total Nitrite")

#--------------------------------------------------------------------------------------------------

# INPUT 20 - Total Nitrogen

total_nitrogen = st.text_input("Total Nitrogen in Effluent", "0")

inputs["Total Nitrogen"] = check_input(total_nitrogen, "Total Nitrogen")

#--------------------------------------------------------------------------------------------------

# INPUT 21 - Total Dissolved Solids (Effluent)
total_dissolved_solids_eff = st.text_input("Total Dissolved Solids in Effluent", "507170067.4")

inputs["Total Dissolved Solids (Effluent)"] = check_input(total_dissolved_solids_eff,
                                               "Total Dissolved Solids (Effluent)")

#--------------------------------------------------------------------------------------------------

# INPUT 22 - Total Organic Carbon (Effluent)
total_organic_carbon_eff = st.text_input("Total Organic Carbon in Effluent", "16000000")

inputs["Total Organic Carbon (Effluent)"] = check_input(total_organic_carbon_eff,
                                             "Total Organic Carbon (Effluent)")

#--------------------------------------------------------------------------------------------------

# INPUT 23 - Total Suspended Solids (Effluent)
total_suspended_solids_eff = st.text_input("Total Suspended Solids in Effluent", "2336653.964")

inputs["Total Suspended Solids (Effluent)"] = check_input(total_suspended_solids_eff,
                                               "Total Suspended Solids (Effluent)")

#--------------------------------------------------------------------------------------------------

# INPUT 24 - Total Suspended Solids, Percent Removal (Effluent)
total_suspended_solids_pr_eff = st.text_input("Total Suspended Solids, Percent Removal in Effluent", 
                                           "0")

inputs["Total Suspended Solids, Percent Removal (Effluent)"] = check_input(total_suspended_solids_pr_eff,
                                               "Total Suspended Solids, Percent Removal (Effluent)")

#--------------------------------------------------------------------------------------------------

# INPUT 25 - pH (Influent)
ph_eff = st.text_input("pH of Effluent", "7.0")

# custom pH error checking function
try:
    converted_ph_eff = np.float64(ph_eff)
    if 0 <= converted_ph_eff <= 14:
        inputs["pH (Effluent)"] = converted_ph_eff
    else:
        st.error("The {0} value must be between 0 and 14".format('effluent pH.'))
        inputs["pH (Effluent)"] = False
except ValueError:
    st.error("Please enter a valid number for the {0}".format("effluent pH."))
    inputs["pH (Effluent)"] = False

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
        prediction = bio_classifier.predict(list(inputs.values()))

        if prediction == 0:
            st.write("PFAS is at low risk for detection in biosolids.")
        else:
            st.write("PFAS is at high risk for detection in biosolids.")