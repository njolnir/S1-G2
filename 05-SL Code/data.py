# This script is for processing the data
import pandas as pd

class ProcessData:
    # Loading the data
    def load_data():            
        data = pd.read_csv('0-Data/micro_world.csv')
        
        return data
    
     # Filter Philippine Data
    def filter_data(data):
        ph_data = data.query('economy == "Philippines"')

        return ph_data
    