import streamlit as st

st.markdown("""
    <h1>Prediction Tool for PFAS in California WWTPs</h1>
    """, unsafe_allow_html=True)

st.markdown("""
    <h2>Machine Learning for Monitoring Per- and Polyfluoroalkyl Substance (PFAS) in California's Wastewater Treatment Plants: An Assessment of Occurrence and Fate</h2>
    """, unsafe_allow_html=True)

# list authors and their respective departments
st.markdown("""
    <h4>Jialin Dong<sup>1</sup>, Seungjun Kim<sup>2</sup>, Sean D. Young<sup>2,3</sup>, Chengxi Li<sup>1</sup>, Zhichao Jin<sup>4</sup>, Dylan Lee <sup>5</sup>, and Christopher I. Olivares<sup>1</sup></h4>
    """, unsafe_allow_html = True)

departments = """
<sup>1</sup> Department of Civil and Environmental Engineering, University of California, Irvine, CA  
<sup>2</sup> Department of Informatics, University of California, Irvine, CA  
<sup>3</sup> Department of Emergency Medicine, University of California, Irvine, CA  
<sup>4</sup> Department of Physics and Astronomy, University of California, Irvine, CA  
<sup>5</sup> Department of Computer Science, University of California, Irvine, CA  
"""

st.markdown(departments, unsafe_allow_html=True)

st.markdown("""
            <b>Correspondance:</b> <u>chris.olivares@uci.edu</u>
            """, unsafe_allow_html = True)

paper_url = ...
github_url = "https://github.com/JialinDong/Machine-Learning-for-Monitoring-Per--and-Polyfluoroalkyl-Substance-PFAS-in-California-s-Wastewater"
lab_website_url = "https://olivareslab.org/research/"
data_url = "https://github.com/JialinDong/ML-Monitoring-PFAS-Californias-WWTP/tree/main/Data"

# Create buttons in the container
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    
    # Paper button
    with col1:
        st.markdown(f"[![Paper](https://img.shields.io/badge/Paper-Link-blue.svg)]({paper_url})")
    
    # GitHub button
    with col2:
        st.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-Link-blue.svg)]({github_url})")
    
    # Lab website button
    with col3:
        st.markdown(f"[![Lab Website](https://img.shields.io/badge/Lab%20Website-Link-blue.svg)]({lab_website_url})")

    # Data button
    with col4:
        st.markdown(f"[![Data](https://img.shields.io/badge/Data-Link-blue.svg)]({data_url})")

st.header("Abstract")

abstract = """
Although wastewater treatment plants (WWTPs) are considerable sources of Per- and Polyfluoroalkyl Substances (PFAS) pollution, comprehensive monitoring, and management outlining PFAS contamination in WWTPs remain insufficient. 

This study introduced two advanced approaches to address the issue: 
- a statewide database, WWTP-PFAS-CA, for PFAS tracking in WWTPs
- machine learning (ML) models to predict PFAS risk.

To facilitate the establishment of an effective, data-driven monitoring framework, we developed the public WWTP-PFAS-CA statewide database (2020-2023), which encompasses information from over 200 WWTPs across California. This database detailed PFAS concentrations in influent, effluent, and biosolids and included data on sampling dates, wastewater sources, and treatment processes.

Our analysis revealed that more than 80% of WWTPs exhibit increased total PFAS concentrations in the effluent, with over half of these facilities facing a significant risk of surpassing the 70 ng/L threshold for PFAS levels in wastewater. Individual PFAS were positively correlated with each other within the same wastewater matrix.

Additionally, we developed a data-driven and precise ML tool for comprehensive PFAS monitoring (assessing total PFAS risk, individual PFAS occurrences, and predicting specific PFAS concentrations) in WWTPs. The AUROC/accuracy for the prediction of total PFAS risks were ~80%.

Our machine learning models achieved ~80% accuracy in predicting total PFAS risk in WWTPs and identified key influencers of PFAS fate in influent, effluent, and biosolids, including WWTP size, wastewater source, county population, and GDP. Our research provides a data-driven perspective on PFAS behavior and offers a novel strategy for monitoring possibilities for WWTPs.
"""

st.write(abstract)

st.image("figures/Figure1.jpg", caption = """Figure 1: Graphical Abstract for Machine Learning for Monitoring Per- and Polyfluoroalkyl Substance (PFAS) in California's Wastewater Treatment 
                                            Plants: An Assessment of Occurrence and Fate""")
st.image("figures/Figure2.jpg", caption = """Figure 2: PFAS occurrence in California WWTPs. Panel A:  Mean concentrations and standard deviations (divided by 10) of total PFASs in 
         influent, effluent, and biosolids. Panel B: Mean concentrations of 39 PFASs in influent, effluent, and biosolids. Insert: SC-PFCA represents short-chain (C4-C6) PFCAs; 
         LC-PFCA represents long-chain (C7+) PFCAs; SC-PFSA represents short-chain PFSAs; LC-PFSA represents long-chain PFSAs; FT represents fluorotelomers; FASA represents 
         perfluoroalkane sulfonamide; Other represents other PFAS (ADONA, HFPO-DA (GenX), 11ClPF3OUDS, 9ClPF3ONS). Panel C: Detection frequency of 39 PFASs across California WWTPs, 
         represented in a radar chart. Panel D: Percent of California WWTPs exhibiting higher PFAS concentrations in effluent compared to influent.""")
st.image("figures/Figure3.jpg", caption = """Figure 3: Geographic distribution and Risk Assessment of PFAS Contaminants in California WWTPs. Panel A: Total PFAS risk in WWTP influent (INF). 
         Panel B: Total PFAS risk in WWTP effluent (EFF). Panel C: Total PFAS risk in WWTP biosolids (BIO). Panel D: County-wise distribution of total PFAS average concentrations in 
         INF/EFF/BIO.""")

# buttons and/or caption to move to different models
st.write("""Our website serves as an interactive platform embedded with five classification models designed specifically for Task 1 of our study: predicting total PFAS risk in influent, effluent, 
         and biosolids. Among these five models, three are developed to predict PFAS concentrations using a limited set of non-PFAS input features, allowing for estimations in influent, effluent, 
         and biosolids. The remaining two models utilize PFAS values from influent alone to predict PFAS levels in effluent and biosolids. Collectively, these models provide a comprehensive approach 
         to assessing PFAS risk, supporting informed decision-making in wastewater treatment and environmental monitoring.
         """)

st.write("""The five classification models introduced above are available in the left sidebar of this website. Click on the corresponding link to visit each model and explore its predictions based 
         on the specific wastewater treatment stage you are interested in.
        """)

# Contact Section
st.markdown("""
    <h2>Contact</h2>
    """, unsafe_allow_html=True)

st.markdown("If you want to discover more, then please contact the <a href=https://olivareslab.org/join-the-lab/)>Olivares Lab</a>.", unsafe_allow_html=True)


