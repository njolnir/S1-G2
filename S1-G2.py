import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns

def load_data():
    # Load the data
    data = pd.read_csv('0-Data/micro_world.csv', encoding='ISO-8859-1')
    return data


def Overview():
    # Write the title and the subheader
    # Load Title Photo
    st.image('01-Images/00-Title.png')

    st.write(
        '''
        Financial inclusion means ensuring that financial services truly enhance the well-being of their users 
        not just now but across the lifespan. 
        Filipinos often joke about retirement and growing old but…ready na ba talaga tayong tumanda?
        '''
    )

    st.write(
        '''
    
        '''
    )
    # Load Photo
    st.image('01-Images/00-Worry.png')
    st.write(
        '''
        Using the Global Findex 2021, we saw that 9 in 10 Filipinos are worried about not having enough money for old age. 

        '''
    )

    # Load data
    data = load_data()
    ph_data = data.query('economy == "Philippines"')

    #show ph_data
    expander = st.expander("Show PH_Data")
    expander.dataframe(ph_data)
    
    

    
def demo():
    # Write the title
    st.title(
        "Filipinos who Saved for Old Age"
    )
    st.subheader("This shows ")

    # Load the data
    data = pd.read_csv('micro_world.csv', encoding='ISO-8859-1')
    data['SOA'] = [ 1 if x == 1 else 0 for x in data['fin16']]


    # Define the age bin edges and labels
    age_bins = [0, 18, 25, 35, 50, 65, 120]
    age_labels = ['below 18', '18-24', '25-34', '35-49', '50-64', '65 and over']

    # Convert the age column into age groups using pd.cut()
    data['age_group'] = pd.cut(data['age'], bins=age_bins, labels=age_labels, include_lowest=True)

    ph_data = data.query('economy == "Philippines"')

def findings():
    # Write the title and the subheader
    st.title(
        "This page is for the analysis and findings(clustering)"
    )

def conclusion():
    # Write the title
    st.title(
        "What We Can Do"
    ) 

def recommendation():
    # Write the title
    st.title(
        "What We Can Do"
    )


def the_team():
    # Write the title
    st.title(
        "The Team"
    )


list_of_pages = [
    "Overview",
    "Demographics",
    "Findings",
    "Conclusion",
    "Recommendation",
    "Pandas.RAKS"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Overview":
    Overview()

elif selection == "Demographics":
    demo()

elif selection == "Findings":
    findings()

elif selection == "Conclusion":
    conclusion()

elif selection == "Recommendation":
    recommendation()

elif selection == "Pandas.RAKS":
    the_team()
