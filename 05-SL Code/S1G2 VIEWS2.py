import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import data

# Load the data
df = data.ProcessData.load_data()

# Filter Philippine data
ph_data = data.ProcessData.filter_data(df)

# Create new data frame with filtered no_accounts column
ph_no_account = ph_data[ph_data['no_accounts'] != 0]

# Filter those who do neet financial services
ph_no_acc_no_needFS = data.ProcessData.no_need_for_fs(ph_no_account)

# Setting general format to the graphs
sns.set_theme(style="white", font="sans-serif")

class pages:
    #Page1 - Overview
    def Overview():
        st.title()
