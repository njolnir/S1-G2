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

class Pages:
    # Page 1 - Introduction
    def introduction():
    # Write the title and the subheader
        st.title(
            "Project MabuhAI: Uncovering the Different Factors that Make up Unbanked Filipinos"
        )
        st.subheader(
            """
            Out of 872 adult Filipinos, 65.48% were found unbanked. Moreover, PH had the 5th highest percentage population of unbanked adults among the low-income SEA countries.
            """
        )

        # Load photo -> Update photo relevant to our topic
        st.image("sea_countries.png")
        st.markdown(""" 
        *In a global scale, the average percentage population of unbanked adults was 41.64%. Going beyond the benchmark, it could only mean that Philippines' banks and other formal financial institutions were not yet quite accessible in 2017.*
        """)

        # Objectives
        st.subheader("Our main objective is to create a profile of unbanked filipino adults across their income, employment, received domestic remittances, and status of having emergency funds.")
        st.subheader("Additionally, we want to look at the main reasons why Filipinos are unbanked and how they manage their money (borrowing, emergency funds).")

        # Display data
        #st.markdown("**A Look at the Philippine Data**")
        #st.dataframe(ph_data.reset_index(drop=True))
        #st.markdown("Source: Global Findex 2017 from World Bank.")
        expander = st.expander("A Look at the Philippine Data")
        expander.dataframe(ph_data.reset_index(drop=True))
        expander.write("Source: Global Findex 2017 from World Bank")

    # Page 2 - Demographics
    def demog():
        # Write the title
        st.title(
            "Demographics of Unbanked Filipinos"
        )
        st.subheader("This shows a quick overview of the educational attainment, employment status, and sex distribution of the unbanked adult Filipinos from the survey.")

        tab_educ, tab_emp, tab_sex = st.tabs(["Education", "Employment", "Sex"])
       
        with tab_educ:
            # Show in terms of educational attainment
            st.subheader("In terms of Educational Attainment")
            st.markdown("""
            ##### Among the unbanked Filipinos aged 21 and above, around 56% have finished up to secondary level or high school only.
            """)
            Demographics.show_educ()

        with tab_emp:
            # Show in terms of employment status
            st.subheader("In terms of Employment Status")
            st.markdown("""
            ##### 4 out of 6 unbanked adult Filipinos are unemployed.
            """)
            Demographics.show_emp()

        with tab_sex:
            # Show in terms of gender
            st.subheader("In terms of Sex")
            st.markdown("""
            ##### There are more adult _female_ Filipinos who are unbanked than males.
            """)
            Demographics.show_gender()

    # Page 3 - Factors and Profile
    def show_factors_and_profile():
        st.title(
            "Factors why Filipinos are Unbanked"
        )

        # Show the different factors
        st.subheader("Why are Filipinos unbanked?")
        Factors_and_Profile.show_factors()        
        st.markdown("""
        ##### Understanding the unbank status of Filipinos, top factors appeared to be the one's financial capacity, lack of documentation, and distance from banks. Interestingly, 39.93% of the unbanked respondents did not find bank financial services a need. We will dive deeper into those who said they have no need for financial services.
        """)

        # Show profile for those who said there is no ned for FS
        st.subheader("So why is there no need for a bank account?")
        st.markdown("""
        ##### With K-Modes clustering, we saw that those who did not need to have a bank account were _employed_, and the _Middle_ and _Richest_ income groups could come up with emergency funds when something unexpected happens.
        """)
        st.image("profile_noneedfs.PNG")
        st.markdown("""
        ##### Moreover, members of the middle income category were _receiving domestic remittances_. Thus, bank services were deemed unnecessary.
        """)

        st.markdown("""
        ##### From the adult Filipinos who said they do not have a bank account because they do not need it, 97% had an account at other financial institutions. Furthermore, 97% of the group also had mobile money accounts.
        """)

        col1, col2 = st.columns(2)

        with col1:
            Factors_and_Profile.show_mob_acc("Has an account at financial institution?")

        with col2:
            Factors_and_Profile.show_mob_acc("Has a mobile money account?")
        
        st.markdown("_Financial Institutions other than banks might be from insurance industries, investment companies, and money brokers, to name a few. Meanwhile, mobile money accounts or commonly known as e-wallets, are those like GCash, Maya, and Shopee wallets._")

        st.subheader("Looking at the bigger picture")
        st.markdown("""
        ##### Here we look at some aspects of the unbanked adult Filipinos in terms of their capacity to save and borrow, as well as their source fo emergency funds.
        """)

        tab1, tab2, tab3 = st.tabs(["Saving Capacity", "Borrowing Power", "Emergency Funds"])

        # Saving Capacity
        with tab1:
            st.markdown("""
            ##### For the last 12 months, 64 out of 228 respondents said they were saving up for retirement.

            ##### In this analysis, we looked into the different reasons our respondents took into consideration in terms of saving money.

            ##### Note that these are the same people who said they do not need financial services.
            """)
            Factors_and_Profile.show_save_capacity()
            
        # Borrowing Power
        with tab2:
            st.markdown("""
            ##### Some 106 people who were borrowing money said they do not need financial services.
            """)
            Factors_and_Profile.show_borrow_power()
        
        # Emergency Funds
        with tab3:
            st.markdown("""
            ##### 103 out of 228 unbanked Filipinos who had no need of financial services had a possible source of emergency funds. Among them, 43 Filipinos would rely on their money from working, while 39 Filipinos would rely on their friends or relatives.

            ##### This indicates that majority of Filipinos believe to be always capable in budgeting enough funds for savings. Many other Filipinos strongly trust their family and friends to back them up in case they have insufficient or no funds at all.
            """)
            Factors_and_Profile.show_emg_funds()

    # Page 4 - Insights & Reco
    def show_conclusion():
        # Write the title
        st.title(
            "Key Insights and Recommendations"
        )

        st.subheader("Financial Situation")
        st.markdown("""
        ##### _PH is still behind in terms of financial inclusivity as 65% of the adult Filipinos were unbanked, due to the lack of money and bank services were deemed too expensive._
        """)

        st.subheader("Distance")
        st.markdown("""
        ##### _One of the primary factors why Filipinos had no account was that banks were too far from their homes._
        """)

        st.subheader("Lack of Requirements")
        st.markdown("""
        ##### _It was found out that unbanked status partly stemmed from the rigorous process and documentation of banks._
        """)

        st.subheader("Providing these Filipinos some sources of financial assistance (e.g., cash assistance, pension) and making these financial services more accessible (i.e., locate communities where bank institutions are scarce, reduce steps on setting up accounts) can be the first steps for these Filipinos to improve their financial situation.")

        st.subheader("Education")
        st.markdown("""
        ##### _Many unbanked Filipinos had completed education up to the secondary level only._
        """)

        st.subheader("Mobile Accounts")
        st.markdown("""
        ##### _The rise of mobile wallets in the country was transitioning Filipinos to the fintech industry. Hence, the accessibility makes Filipinos favor mobile wallets over traditional bank accounts. To reiterate, 97% of the unbanked had mobile money accounts!_
        """)

        st.subheader("Trust")
        st.markdown("""
        ##### _Majority of Filipinos strongly rely on their family/friends when it comes to borrowing money or to receiving emergency funds. Exposing them to the benefits of savings accounts and/or mutual funds will enable them to secure their savings more effectively._
        """)

        st.subheader("Implementing mandatory financial literacy classes in high school, will raise Filipinos’ awareness of various available financial services, such as savings accounts, mobile accounts, and mutual funds.")

    # Page <insert No.>
    def the_team():
        # Write the title
        st.title(
            "The Team"
        )

        st.image("team_monty_python.jpg", caption='Meet the Team behind Project MabuhAI.')

# Demographics
class Demographics:
        def show_educ():
            ### EDUCATIONAL ATTAINMENT ###
            # Filter the data by educ
            ph_educ_no_acc = ph_no_account.groupby('educ')['no_accounts'].count().reset_index()

            educ_mapping = {
                1: 'Primary or Less',
                2: 'Secondary',
                3: 'Tertiary'
            }

            ph_educ_no_acc = ph_educ_no_acc.replace({'educ': educ_mapping})

            # Plot the data
            fig, ax = plt.subplots(figsize=(9,5), dpi=300)
            
            plot = sns.barplot(
                x = ph_educ_no_acc['educ'],
                y = ph_educ_no_acc['no_accounts'],
                color='#C0C0C0'
            )
            plot.bar([1], [322], color='#378078')

            plt.title('Educational Attainment of Unbanked Filipinos aged 21 and above', pad=10.0)
            ax.set_xlabel('Educational Attainment', labelpad=10.0)
            ax.set_ylabel('No. of Filipinos with no Accounts', labelpad=10.0)
            plt.bar_label(plot.containers[0], fmt='%.0f')
            #plt.xticks(rotation=45)
            plt.ylim(0, 400)

            # Show the data
            st.pyplot(fig)
        
        def show_gender():
            ### GENDER DISTRIBUTION ###
            # Filter the data by female
            ph_gen_no_acc = ph_no_account.groupby('female')['no_accounts'].count().reset_index()

            gen_mapping = {
                1: 'Male',
                2: 'Female'
            }

            ph_gen_no_acc = ph_gen_no_acc.replace({'female': gen_mapping})
            ph_gen_no_acc = ph_gen_no_acc.sort_values(by='no_accounts', ascending=False)

            # Plot the data
            fig, ax = plt.subplots(figsize=(9,5), dpi=200)

            plot = sns.barplot(
                x = ph_gen_no_acc['female'],
                y = ph_gen_no_acc['no_accounts'],
                color='#378078'
            )

            plt.title('Sex Distribution of Unbanked Adult Filipinos', pad=10.0)
            ax.set_xlabel('Biological Sex', labelpad=10.0)
            ax.set_ylabel('No. of Filipinos with no Accounts',labelpad=10.0)
            plt.bar_label(plot.containers[0], fmt='%.0f')
            plt.ylim(0, 350)

            st.pyplot(fig)
        
        def show_emp():
            ### EMPLOYMENT STATUS ###
            # Filter the data by emp_in
            ph_emp_no_acc = ph_no_account.groupby('emp_in')['no_accounts'].count().reset_index()

            emp_mapping = {
                0: 'Employed',
                1: 'Unemployed'
            }

            ph_emp_no_acc = ph_emp_no_acc.c

            # Plot the data
            fig, ax = plt.subplots(figsize=(9,5), dpi=200)

            plot = sns.barplot(
                x = ph_emp_no_acc['emp_in'],
                y = ph_emp_no_acc['no_accounts'],
                color='#C0C0C0'
            )
            plot.bar([1], [382], color='#378078')

            plt.title('Majority of Unbanked Filipinos aged 21 and above are Unemployed', pad=10.0)
            ax.set_xlabel('Employment Status', labelpad=10.0)
            ax.set_ylabel('No. of Filipinos with no Accounts', labelpad=10.0)
            plt.bar_label(plot.containers[0], fmt='%.0f')
            plt.ylim(0, 450)

            # Show the data
            st.pyplot(fig)

# Factors and Profiling
class Factors_and_Profile:
    
    def show_factors():
        new_ph_data = data.ProcessData.add_reason_col(ph_data)

        # Get the reasons why Filipinos are Unbanked
        r_ph_data = new_ph_data[
            [
                'r_too_far',
                'r_too_expensive',
                'r_lack_documentation',
                'r_trust',
                'r_religious_reasons',
                'r_lack_of_money',
                'r_family_already_have',
                'r_no_need_for_fs'
            ]
        ]
        
        r_labels = [
            'Too Far',
            'Too Expensive',
            'Lack of Documentation',
            'Lack of Trust',
            'Religious Regions',
            'Lack of Money',
            'Family Member Already Has Account',
            'No Need For Financial Services'
        ]

        # Get total for each reason
        sum_per_reason = r_ph_data.sum()
        sum_no_accounts = new_ph_data['no_accounts'].sum()
        percentage_reasons = (sum_per_reason*100)/sum_no_accounts

        # Assign label to percent value
        df = pd.DataFrame({"percentage_reasons":percentage_reasons, "r_labels":r_labels})
        df = df.sort_values('percentage_reasons', ascending=False).reset_index()

        # Plot the data
        fig, ax = plt.subplots(figsize=(9,8), dpi=300)
        plot = sns.barplot(
            x = df['percentage_reasons'],
            y = df['r_labels'],
            color='#C0C0C0'
        )
        ax.set_xlabel("% of Population", labelpad=10.0)
        ax.set_ylabel("Reasons", labelpad=10.0)
        plt.bar_label(plot.containers[0], fmt='%.2f', padding=7.0)
        plt.xlim(0, 80)

        # Plot the special bar separately
        plot.barh([4], [39.93], color='#378078')

        # Show the data
        st.pyplot(fig)
    
    def show_save_capacity():
        # Use a list to store columns for each saving reason
        list = ['fin15', 'fin16', 'fin17a', 'fin17b']

        # Use another list for proper naming convention each saving reason
        saving_reason = ['for_farm_business_purpose',
                        'for_old_age',
                        'using_an_account_at_a_financial_institution',
                        'using_an_informal_savings_club']
        
        # Create a loop to count respondents who said 'yes' and
        # create a new column for each reason based on the list created above
        for i in list:
            ph_no_acc_no_needFS[saving_reason[list.index(i)]] = ph_no_acc_no_needFS.apply(
                lambda x : 1 if x[i] == 1 else 0, axis=1
            )
        
        # Aggregate
        ph_no_acc_no_needFS.agg(
            business = ('for_farm_business_purpose', 'sum'),
            retirement = ('for_old_age','count'),
            used_at_a_financial_institution = ('using_an_account_at_a_financial_institution', 'sum'),
            informal_savings_club = ('using_an_informal_savings_club', 'sum'),
            population = ('wpid_random', 'count')
        )

        # Calculate % each reason
        business = round(ph_no_acc_no_needFS['for_farm_business_purpose'].sum() * 100.0 / ph_no_acc_no_needFS['wpid_random'].count(), 2)
        retirement = round(ph_no_acc_no_needFS['for_old_age'].sum() * 100.0 / ph_no_acc_no_needFS['wpid_random'].count(), 2)
        used_at_fi = round(ph_no_acc_no_needFS['using_an_account_at_a_financial_institution'].sum() * 100.0 / ph_no_acc_no_needFS['wpid_random'].count(), 2)
        informal_savings = round(ph_no_acc_no_needFS['using_an_informal_savings_club'].sum() * 100.0 / ph_no_acc_no_needFS['wpid_random'].count(), 2)

        # Store aggregated columns to a new DataFrame
        df = {'saving_reason' : ['Business Purposes', 'Retirement', 'Used in Financial Institution', 'Informal Savings Club'],
            'value' : [business, retirement, used_at_fi, informal_savings]}

        reasons = pd.DataFrame(df)

        # Sort values
        reasons = reasons.sort_values('value', ascending = False)

        # Plot the data
        fig, ax = plt.subplots(figsize=(6,4), dpi=300)
        plot = sns.barplot(
            x = reasons['value'],
            y = reasons['saving_reason'],
            color='#C0C0C0'
        )
        plot.barh([0], [28.07], color='#378078')
        plot.barh([1], [25.44], color='#C0C0C0')
        plot.barh([2], [7.46], color='#C0C0C0')
        plot.barh([3], [2.19], color='#C0C0C0')

        ax.set_xlabel("Saving Capacity % per Reason", labelpad=10.0)
        ax.set_ylabel("")
        plt.bar_label(plot.containers[0], fmt='%.2f', padding=7.0)
        plt.xlim(0, 35)

        # Show the data
        st.pyplot(fig)
    
    def show_borrow_power():

        # Filter for Filipinos who borrowed
        ph_no_acc_no_needFS['borrowed'] = ph_no_acc_no_needFS.apply(
            lambda x: 1 if x['fin22a'] == 1 or x['fin22b'] == 1 or x['fin22c'] == 1 else 0, axis = 1
        )

        # Filter for Filipinos who borrowed and have no bank account
        ph_no_acc_no_needFS['borrowed_no_bank'] = ph_no_acc_no_needFS.apply(
            lambda x: 1 if x['borrowed'] == 1 & x['no_accounts'] == 1 else 0, axis = 1
        )

        #Filter for where Filipinos borrow
        ph_no_acc_no_needFS['borrowed_from_fi'] = ph_no_acc_no_needFS.apply(
            lambda x: 1 if x['borrowed_no_bank'] == 1 & x['fin22a'] == 1 else 0, axis = 1
        )
        ph_no_acc_no_needFS['borrowed_from_family'] = ph_no_acc_no_needFS.apply(
            lambda x: 1 if x['borrowed_no_bank'] == 1 & x['fin22b'] == 1 else 0, axis = 1
        )
        ph_no_acc_no_needFS['borrowed_from_informal'] = ph_no_acc_no_needFS.apply(
            lambda x: 1 if x['borrowed_no_bank'] == 1 and x['fin22c'] == 1 else 0, axis = 1
        )

        # Get borrowed from data only
        borrowed_from = ph_no_acc_no_needFS[
            [
                'borrowed_from_fi',
                'borrowed_from_family',
                'borrowed_from_informal'
            ]
        ]

        # Total population that borrowed per where they borrowed from
        borrowed_from_sum = borrowed_from.sum()

        # Assigning labels
        borrowed_from_df = pd.DataFrame({
            'Borrowed From' : ['Financial Instituion', 'Family or Friends', 'Informal Savings Club'],
            'Number' : borrowed_from_sum
        })

        # Sorted values
        borrowed_from_df_sorted = borrowed_from_df.sort_values(by="Number", ascending=False)

        # Plot the data
        fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
        plot = sns.barplot(
            x = borrowed_from_df_sorted["Number"],
            y = borrowed_from_df_sorted["Borrowed From"],
            color='#C0C0C0'
        )

        ax.set_xlabel("Population", labelpad=10.0)
        ax.set_ylabel(" ")
        plt.bar_label(plot.containers[0], fmt='%.2f', padding=3.0)
        plt.xlim(0, 110)


        # Plot the special bar separately ...
        plot.barh([0], [98], color='#378078')


        # Show the data
        st.pyplot(fig)
    
    def show_emg_funds():

        #Clean data according to emergency sources
        new_ph_data = data.ProcessData.add_reason_col(ph_data)
        ph_esources_data = new_ph_data[(new_ph_data['no_accounts'] != 0) & new_ph_data['r_no_need_for_fs'] == 1]

        ph_esources_data = ph_esources_data.groupby(['no_accounts','fin25']).agg(total_pop=('wpid_random','count')).reset_index()
        #Add new percentage column
        ph_esources_data['%_of_total_pop'] = ph_esources_data['total_pop']*100/sum(ph_esources_data['total_pop'])

        e_reason = {
        1.0:'Savings',
        2.0:'Family or friends',
        3.0:'Money from working',
        4.0:"Borrowing from a bank, \n employer, or private fund",
        5.0:'Selling assets',
        6.0:'Some other source',
        7.0:'Don\'t know'
        }

        #Replace float values of 'fin25' into labels
        ph_esources_data = ph_esources_data.replace({'fin25': e_reason})
        ph_esources_data = ph_esources_data.sort_values('%_of_total_pop', ascending=False).reset_index()

        #Plot the data
        fig, ax = plt.subplots(figsize=(6,6), dpi=200)
        plot = sns.barplot(
            x = ph_esources_data['%_of_total_pop'],
            y = ph_esources_data['fin25'],
            color='#C0C0C0'
        )
        

        ax.set_xlabel('Source of Emergency Funds', labelpad=10.0)
        ax.set_ylabel('Number of Unbanked Filipinos', labelpad=10.0)
        # Remove clutter
        ax.set(ylabel=None)
        plt.bar_label(plot.containers[0], fmt='%.2f', padding=3.0)
        plt.xlim(0, 50)

        plot.barh([0], [41.75], color='#378078')
        plot.barh([1], [37.86], color='#378078')
        
        # Show the data
        st.pyplot(fig)

    def show_mob_acc(title):

        #Filter data for fin11h:  no need for financial services and has need for financial services
        no_accounts_fin11h = ph_data[(ph_data['fin11h']==1)]

        #create a df of no accounts and is fin11h
        am_fin11h = no_accounts_fin11h.groupby('account_mob')['fin11h'].count().reset_index()
    
        #change numerical label to words
        income_group_mapping = {
            1.0:'Yes',
            2.0:'No'
        }

        am_fin11h.replace({'account_mob':income_group_mapping})
    
        # Set figure size
        fig, ax = plt.subplots(figsize=(9,7)  , dpi=200)
    
        clrs = ['#C0C0C0' if (x < max(am_fin11h['fin11h'])) else '#378078' for x in am_fin11h['fin11h'] ]
    
        # Run bar plot
        plot = sns.barplot(
            x = am_fin11h['account_mob'],
            y = am_fin11h['fin11h'],
            palette= clrs
            
        )
        
        # Set labels
        ax.set_xlabel(title, labelpad=10.0)
        ax.set_ylabel('')
        
        plot.set(xticklabels=['Yes', 'No'])
        plot.set(yticklabels=[])
        plt.bar_label(plot.containers[0], fmt='%.0f', padding=3.0)
        plt.ylim(0, 250)
        
        # Show figure
        st.pyplot(fig)