import os
import pandas as pd
import matplotlib.pyplot as plt

def draw_dbm_boxplots(n, m):
    # Create a directory to save the plots if it does not exist
    if not os.path.exists('boxplots/dbm'):
        os.makedirs('boxplots/dbm')
    
    # Dictionary to store data for each IP
    ip_data = {}

    # Loop through the specified range of folders
    for i in range(n, m + 1):
        folder_name = f'experiment/{i}'
        
        # Read the 'parameters.csv' file
        parameters_data_path = os.path.join(folder_name, 'parameters.csv')
        if os.path.exists(parameters_data_path):
            parameters_data = pd.read_csv(parameters_data_path)
            
            # Append the DBM values to the corresponding IP in ip_data dictionary
            for _, row in parameters_data.iterrows():
                ip = row['IP']
                dbm = row['DBM']
                
                if ip not in ip_data:
                    ip_data[ip] = []
                ip_data[ip].append((i, dbm))
    
    # Plot boxplots for each IP
    for ip, values in ip_data.items():
        # Create a dataframe for the current IP
        df = pd.DataFrame(values, columns=['Folder', 'DBM'])
        
        # Create a boxplot
        plt.figure(figsize=(10, 6))
        boxplot = df.boxplot(by='Folder', column='DBM', grid=False)
        plt.title(f'Boxplot da Potência de Sinal do IP: {ip}')
        plt.suptitle('')
        plt.xlabel('Leitura')
        plt.ylabel('Potência do Sinal (dBm)')
        
        # Save the plot as an image
        plt.savefig(f'boxplots/dbm/{ip}_dbm_boxplot.png')
        plt.close()

# Specify the range of folders
n = 1
m = 20

# Call the function to draw DBM boxplots
draw_dbm_boxplots(n, m)
