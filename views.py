import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import data

# Load the data
df = data.ProcessData.load_data()

# Filter Philippine data
ph_data = data.ProcessData.filter_data(df)

#Filter Cluster data
cluster_data = data.ProcessData.cluster_data()

# Setting general format to the graphs
sns.set_theme(style="white", font="sans-serif")

class pages:
    #Page1 - Overview
    def Overview():
        # Write the title and the subheader
        st.image('01-Images/00-Title.png')
    
        st.write(
            '''
            Financial inclusion means ensuring that financial services truly enhance the well-being of their users 
            not just now but across the lifespan. 
            Filipinos often joke about retirement and growing old but…ready na ba talaga tayong tumanda?
            '''
        )   

        # Load Photo
        st.image('01-Images/00-Worry.png')
        st.write(
            '''
            Using the Global Findex 2021, we saw that 9 in 10 Filipinos are worried about not having enough money for old age. 

            '''
            )
        

        #show ph_data
        expander = st.expander("Show PH_Data")
        expander.dataframe(ph_data)

    def demog():
        # Write the title
        st.title("Demographics of Filipinos Saved for Old Age")
            
        st.subheader("This shows a quick overview of the Age Group, Employment, Income Bracket and Account Ownership of Filipinos Who Saved for Old Age")

        tab_age, tab_emp, tab_inc, tab_accf, tab_accm = st.tabs(["Age Group", "Employment", "Income Bracket", "Traditional Banking", "Mobile Banking"])

        with tab_age:
            #demog by age group
            st.subheader("In terms of Age Group")
            st.markdown("""
            ##### The older Filipinos get, the more likely they are to save for old age up until middle age. After middle age, saving for old age dips and rises again as they get older.
            ##### """)
            Demographics.show_age()

        with tab_emp:
            #demog by employment
            st.subheader("In terms of Employment")
            st.markdown("""
            ##### In the survey, 43.00 %  in the Workforce  have savings prepared for when they get older, 15% higher than those who are out of the Workforce respondents.
            This may suggest that having a regular source of income encourages individuals to save more for their future retirement needs.  
            ##### """)
            Demographics.show_emp()

        with tab_inc:
            #demog by Income Bracket
            st.subheader("By Income Bracket")
            st.markdown("""
            ##### In the survey, 60.6% for the top 20% have savings prepared for when they get older this is around three times higher than the 21.8% for the bottom 20% of respondents.
            This shows the huge discrepancy between High Income vs Low Income earners here in the Philippines.  
            ##### """)
            Demographics.show_inc()

        with tab_accf:
            #demog by Traditional banking
            st.subheader("By Traditional Banking")
            st.markdown("""
            #####  
            ##### """)
            Demographics.show_accf()

        with tab_accm:
            #demog by mobile banking
            st.subheader("By Mobile Banking")
            st.markdown("""
            #####  
            ##### """)
            Demographics.show_accm()

class Demographics:
        def show_age():
            ##### Group the data and apply aggregations ####
            #### When using Aggregations you retain talbe (data frame)###
            
            age = cluster_data.groupby(['age_group']).agg(
                POP=('SOA', 'count'),
                SOA=('SOA', 'sum')
            ).reset_index()

            #since acct_fin is already table format i just performed column computations#
            age['~SOA']=age['POP']-age['SOA']
            age['SOA%']=round((age['SOA']/age['POP'])*100,2)
            age['~SOA%']=round((age['~SOA']/age['POP'])*100,2)

            ### Stacked Bar chart ####
            # Create bar plot with stacked bars
            fig, ax = plt.subplots(figsize=(9, 5), dpi=400)
            sns.barplot(x='age_group', y='SOA%', data=age, color='b', ax=ax)
            sns.barplot(x='age_group', y='~SOA%', data=age, color='grey', ax=ax, bottom=age['SOA%'])
            ax.set_title('By Age Group')
            ax.set_xlabel('Age Group')
            ax.set_ylabel('% Saved for Old Age')

            # Function to add value labels to the bars
            def addlabels(ax):
                for p in ax.containers:
                    ax.bar_label(p, label_type='edge', fontsize=8)

            # Add value labels to the bars  
            addlabels(ax)

            # Show plot on Streamlit
            st.pyplot(fig)
        
        def show_emp():
             ##### Group the data and apply aggregations ####
            #### When using Aggregations you retain talbe (data frame)###

            emp = cluster_data.groupby(['emp_in']).agg(
                POP=('SOA', 'count'),
                SOA=('SOA', 'sum')
            ).reset_index()

            emp_mapping = {
                1: 'Employed',
                2: 'Unemployed'
            }

            emp = emp.replace({'emp_in': emp_mapping})

            #since acct_fin is already table format i just performed column computations#
            emp['~SOA']=emp['POP'] - emp['SOA']
            emp['SOA%']=round((emp['SOA']/emp['POP'])*100,2)
            emp['~SOA%']=round((emp['~SOA']/emp['POP'])*100,2)
            
            ### Stacked Bar chart ####
            # Create bar plot with stacked bars
            fig, ax = plt.subplots(figsize=(9, 5), dpi=400)
            sns.barplot(x='emp_in', y='SOA%', data=emp, color='b', ax=ax)
            sns.barplot(x='emp_in', y='~SOA%', data=emp, color='grey', ax=ax, bottom=emp['SOA%'])
            ax.set_title('By Employment')
            ax.set_xlabel('Employment')
            ax.set_ylabel('% Saved for Old Age')

            # Function to add value labels to the bars
            def addlabels(ax):
                for p in ax.containers:
                    ax.bar_label(p, label_type='edge', fontsize=8)

            # Add value labels to the bars  
            addlabels(ax)

            # Show plot on Streamlit
            st.pyplot(fig)

        def show_inc():
             ##### Group the data and apply aggregations ####
            #### When using Aggregations you retain talbe (data frame)###

            inc = cluster_data.groupby(['inc_q']).agg(
                POP=('SOA', 'count'),
                SOA=('SOA', 'sum')
            ).reset_index()

            inc_mapping = {
                1: 'Poorest',
                2: 'Next Poorest',
                3: 'Middle',
                4: 'Next Richest',
                5: 'Richest'
            }

            inc = inc.replace({'inc_q': inc_mapping})

            #since acct_fin is already table format i just performed column computations#
            inc['~SOA']=inc['POP'] - inc['SOA']
            inc['SOA%']=round((inc['SOA']/inc['POP'])*100,2)
            inc['~SOA%']=round((inc['~SOA']/inc['POP'])*100,2)
            
            ### Stacked Bar chart ####
            # Create bar plot with stacked bars
            fig, ax = plt.subplots(figsize=(9, 5), dpi=400)
            sns.barplot(x='inc_q', y='SOA%', data=inc, color='b', ax=ax)
            sns.barplot(x='inc_q', y='~SOA%', data=inc, color='grey', ax=ax, bottom=inc['SOA%'])
            ax.set_title('By Income Bracket')
            ax.set_xlabel('Income Bracket')
            ax.set_ylabel('% Saved for Old Age')

            # Function to add value labels to the bars
            def addlabels(ax):
                for p in ax.containers:
                    ax.bar_label(p, label_type='edge', fontsize=8)

            # Add value labels to the bars  
            addlabels(ax)

            # Show plot on Streamlit
            st.pyplot(fig)

        def show_accf():
             ##### Group the data and apply aggregations ####
            #### When using Aggregations you retain talbe (data frame)###

            accf = cluster_data.groupby(['account_fin']).agg(
                POP=('SOA', 'count'),
                SOA=('SOA', 'sum')
            ).reset_index()

            accf_mapping = {
                1: 'Yes',
                0: 'No'
            }

            accf = accf.replace({'acount_fin': accf_mapping})

            #since acct_fin is already table format i just performed column computations#
            accf['~SOA']=accf['POP'] - accf['SOA']
            accf['SOA%']=round((accf['SOA']/accf['POP'])*100,2)
            accf['~SOA%']=round((accf['~SOA']/accf['POP'])*100,2)
            
            ### Stacked Bar chart ####
            # Create bar plot with stacked bars
            fig, ax = plt.subplots(figsize=(9, 5), dpi=400)
            sns.barplot(x='account_fin', y='SOA%', data=accf, color='b', ax=ax)
            sns.barplot(x='account_fin', y='~SOA%', data=accf, color='grey', ax=ax, bottom=accf['SOA%'])
            ax.set_title('By Traditional Banking')
            ax.set_xlabel('Account Ownership')
            ax.set_ylabel('% Saved for Old Age')

            # Function to add value labels to the bars
            def addlabels(ax):
                for p in ax.containers:
                    ax.bar_label(p, label_type='edge', fontsize=8)

            # Add value labels to the bars  
            addlabels(ax)

            # Show plot on Streamlit
            st.pyplot(fig)

        def show_accm():
             ##### Group the data and apply aggregations ####
            #### When using Aggregations you retain talbe (data frame)###

            accm = cluster_data.groupby(['account_mob']).agg(
                POP=('SOA', 'count'),
                SOA=('SOA', 'sum')
            ).reset_index()

            accm_mapping = {
                1: 'Yes',
                0: 'No'
            }

            accm = accm.replace({'acount_mob': accm_mapping})

            #since acct_fin is already table format i just performed column computations#
            accm['~SOA']=accm['POP'] - accm['SOA']
            accm['SOA%']=round((accm['SOA']/accm['POP'])*100,2)
            accm['~SOA%']=round((accm['~SOA']/accm['POP'])*100,2)
            
            ### Stacked Bar chart ####
            # Create bar plot with stacked bars
            fig, ax = plt.subplots(figsize=(9, 5), dpi=400)
            sns.barplot(x='account_mob', y='SOA%', data=accm, color='b', ax=ax)
            sns.barplot(x='account_mob', y='~SOA%', data=accm, color='grey', ax=ax, bottom=accm['SOA%'])
            ax.set_title('By Mobile Banking')
            ax.set_xlabel('Account Ownership')
            ax.set_ylabel('% Saved for Old Age')

            # Function to add value labels to the bars
            def addlabels(ax):
                for p in ax.containers:
                    ax.bar_label(p, label_type='edge', fontsize=8)

            # Add value labels to the bars  
            addlabels(ax)

            # Show plot on Streamlit
            st.pyplot(fig)



            
            