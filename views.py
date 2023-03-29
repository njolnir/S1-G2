import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import data
import plotly.express as px

# Load the data
df = data.ProcessData.load_data()

# Filter Philippine data
ph_data = data.ProcessData.filter_data(df)

#Filter Cluster data
cluster_data = data.ProcessData.cluster_data()

# Setting general format to the graphs
#sns.set_theme(style="white", font="sans-serif")

class pages:
    #Page1 - Overview
    def Overview():
        # Write the title and the subheader
        st.image('01-Images/Pandas.Raks/Ready Na Ba.png')
    
        st.write(
            '''
            Financial inclusion means ensuring that financial services truly enhance the well-being of their users not just now but across the lifespan. 
            Filipinos often joke about retirement and growing old but…ready na ba talaga tayong tumanda?

            '''
        )   

        st.write(
            '''We used the Global Financial Inclusion (Findex) Database 2021 from the World Bank to learn more about Filipinos’ saving behavior for old age. 
            The Global Findex Database has been the definitive source of data on the ways in which adults around the world use financial services–from use of cards to mobile accounts, from payments to saving–to offer insights about financial resilience and gaps in financial inclusion.
'''
        )

        st.write(
            '''We found that  9 in 10 Filipinos are worried about not having enough money for old age.'''
        )

        # Load Photo
        st.image('01-Images/Pandas.Raks/9in10.png')
        st.write(
            '''
            However, 61% of these people who are worried have not saved for old age. 

            '''
            )
        
        st.image('01-Images/61.png')
        st.write(
            '''Our analysis zooms in on people who are worried about having enough money for old age and we aimed to:'''
        )
        st.write("* Describe Filipinos who are saving and not saving for old age")
        st.write("* Identify groups of Filipinos who do not save for old ag")
        st.write("* Recommend action steps to help Filipinos save for old age")

        #show ph_data
        expander = st.expander("Show PH_Data")
        expander.dataframe(ph_data)

    def demog():
        # Write the title
        st.title("Demographics of Filipinos who Saved for Old Age")
            
        st.subheader("This shows a quick overview of the Age Group, Employment, Income Bracket and Account Ownership of Filipinos Who Saved for Old Age")

        tab_age, tab_emp, tab_inc, tab_accf, tab_accm, tab_save = st.tabs(["Age Group", "Employment", "Income Bracket", "Traditional Banking", "Mobile Banking", "Saved"])

        with tab_age:
            #demog by age group
            st.subheader("In terms of Age Group")
            st.markdown("""
            ##### The rise up until the middle age groups (25 to 34 and 35 to 49) may be because of more earning capacity and the need for saving for old age becoming more apparent. 
            The dip after the middle age groups may be because of being in the age that saving for old age is meant for.

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
            ##### The proportion of those who saved for old age among those who have accounts in financial institutions is more than twice the proportion of those who saved for old age among those who do not have accounts in financial institutions.  
            ##### """)
            Demographics.show_accf()

        with tab_accm:
            #demog by mobile banking
            st.subheader("By Mobile Banking")
            st.markdown("""
            ##### Similarly, the proportion of those who saved for old age among those who have mobile accounts is a lot higher than that of those who do not have mobile bank accounts.  
            ##### """)
            Demographics.show_accm()

        with tab_save:
            #demog by saved
            st.subheader("Who Saved in the Past Year?")
            st.markdown(""" 
            ##### Majority (559 respondents) of Filipinos who worried for old age have saved the past year. \
                Of which, there are 343 (61.3%) have been saving for old age. 
            ##### """)

            Demographics.show_saved()

    def clustering():
        # Write the title
#        st.title("Clustering")
#        st.subheader("Clustering Criteria")
        st.write("We used K-Modes clustering to group Filipinos and understand their characteristics related to saving for old age. K-Modes clustering is an unsupervised machine learning technique that finds patterns in a dataset and groups observations based on their similarities in terms of different variables. ")
        st.image('01-Images/Pandas.Raks/Clustering.png')
        
        st.write('We used the following variables for clustering:')
        st.write("   * Age, employment and income level are used because of the variations observed in terms of saving for old age across the levels of each variable as shown in the previous section.")
        st.write("   * Account ownership in financial institutions and mobile banks are used because having an account is a gateway to other financial services such as saving. We also saw in the previous section that saving for old age varies depending on whether people have accounts or not.")
        st.write("   * The variable indicating saving in the past year is used since it is the action for the variable we are mainly interested in.")
        st.write("   * The variable indicating saving for old age is our main variable of interest.")
        st.subheader("Clustering Result")
        st.write("After testing different numbers of clusters, we arrived at these five clusters.")
        st.image('01-Images/Pandas.Raks/Cluster Table.png')
    
    def wansoa():
        st.image('01-Images/Pandas.Raks/Not Saving.png')

        tab_dep, tab_wp, tab_mc = st.tabs(["Dependents", "Working Poor", "Middle-Class Earners"])

        with tab_dep:
            st.image('01-Images/Pandas.Raks/Dependents.png')
        
        with tab_wp:
            st.image('01-Images/Pandas.Raks/Working Poor.png')

        with tab_mc:
            st.image('01-Images/Pandas.Raks/Middle Class Earners.png')    
    
    def conclusion():
        #Write the title
        st.title("Conclusion")
        st.write("1.) A majority of Filipinos are not saving for old age")
        st.write("2.) There are different groups of Filipinos who did not save for old age yet:")
        st.write("* Employed")
        st.write("* Middle-income and below")
        st.write("* Limited account ownership")
        st.write("* Limited saving")
        st.write("* Aged 18 to 49")
        st.write("3.) Different groups need different types of support to be able to save for old age")
    
    def recommendation():
        st.title("Recommendations")
    
#       tab_FL, tab_BUSA, tab_RSP = st.tabs(["Financial Literacy Initiatives",
#                                           "Boosting Underserved Savings Access",
#                                           "Retirement Savings Plan"])
                                            
#        with tab_FL:
        st.write("1.) Advocating financial literacy as early as senior high school and providing practical advice and guidance on retirement planning can help \
                         Filipinos save and invest effectively for their retirement, leading to greater financial security over the long term.")

#        with tab_BUSA:
        st.write("2.) Introducing low-cost and accessible savings mechanisms, enables more Filipinos even in underserved/rural areas to save for retirement.\
                 This increase in accessibility creates opportunities for Underserved Filipinos to achieve financial security in their retirement.")

#        with tab_RSP:
        st.write("3.) Making retirement savings programs more accessible and increasing public awareness about them can encourage Filipinos to save for their old age.\
                 By providing easier access and greater knowledge about these programs, more people can take advantage of them and start saving for their future.")
            

    def the_team():
        #Write the title
        st.title("Team PANDAS.RAKS")

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

        def show_saved():
            st.image('03-Codes/by save.png')
                        





            
            