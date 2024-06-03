import os
import pandas as pd
import matplotlib.pyplot as plt

def draw_boxplots(n, m):
    # Create a directory to save the plots if it does not exist
    if not os.path.exists('boxplots/times'):
        os.makedirs('boxplots/times')
    
    # Dictionary to store data for each IP
    ip_data = {}

    # Loop through the specified range of folders
    for i in range(n, m + 1):
        folder_name = f'experiment/{i}'
        
        # Read the 'ping_data.csv' file
        ping_data_path = os.path.join(folder_name, 'ping_data.csv')
        if os.path.exists(ping_data_path):
            ping_data = pd.read_csv(ping_data_path)
            
            # Append the Time values to the corresponding IP in ip_data dictionary
            for _, row in ping_data.iterrows():
                ip = row['IP']
                time = row['Time']
                
                if ip not in ip_data:
                    ip_data[ip] = []
                ip_data[ip].append((i, time))
    
    # Plot boxplots for each IP
    for ip, values in ip_data.items():
        # Create a dataframe for the current IP
        df = pd.DataFrame(values, columns=['Folder', 'Time'])
        
        # Create a boxplot
        plt.figure(figsize=(10, 6))
        boxplot = df.boxplot(by='Folder', column='Time', grid=False)
        plt.title(f'Boxplot do Tempo de Resposta do IP: {ip}')
        plt.suptitle('')
        plt.xlabel('Leitura')
        plt.ylabel('Tempo de Resposta (ms)')
        
        # Save the plot as an image
        plt.savefig(f'boxplots/times/{ip}_boxplot.png')
        plt.close()

# Specify the range of folders
n = 1
m = 20

# Call the function to draw boxplots
draw_boxplots(n, m)