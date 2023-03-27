# This script is for processing the data
import pandas as pd

class ProcessData:
    # Loading the data
    def load_data():            
        data = pd.read_csv('0-Data/micro_world.csv', encoding='ISO-8859-1')
        

        return data
    
    def filter_data(data):
        # Filter Philippine Data
        ph_data = data.query('economy == "Philippines"')

        return ph_data
    
    def cluster_data():
        data = pd.read_csv('0-Data/micro_world.csv', encoding='ISO-8859-1')
        data['SOA'] = [ 1 if x == 1 else 0 for x in data['fin16']]

        # Define the age bin edges and labels
        age_bins = [0, 18, 25, 35, 50, 65, 120]
        age_labels = ['below 18', '18-24', '25-34', '35-49', '50-64', '65 and over']

        # Convert the age column into age groups using pd.cut()
        data['age_group'] = pd.cut(data['age'], bins=age_bins, labels=age_labels, include_lowest=True)  

        ph_data = data.query('economy == "Philippines"')
        ph_data = ph_data.query('fin44a == 1 or fin44a == 2')
        
        cluster = ['age_group', 'emp_in', 'inc_q', 'account_fin', 'account_mob', 'saved', 'fin16', 'SOA', 'saved']
        cluster_data = ph_data[cluster]

        return cluster_data

        
        



    