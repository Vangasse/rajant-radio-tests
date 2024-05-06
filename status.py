#!/usr/bin/env python3

import os
import pandas as pd
from rajant_api import Breadcrumb

if __name__ == '__main__':
    bc = Breadcrumb(host="10.98.78.1",
                    port=2300,
                    role="ADMIN",
                    password="breadcrumb-admin")
    
    n_requests = 100
    data = []

    if bc.authenticate():
        for _ in range(n_requests):
            msg = str(bc.get_state_filter("wireless.peer"))
            index = msg.find("signal: ")
            dbm = int(msg[index+8:index+11])
            index = msg.find("rssi: ")
            rssi = int(msg[index+6:index+9])
            data.append({'DBM': dbm, 'RSSI': rssi})
            print("DBM:", dbm, "RSSI:", rssi)
    
    df = pd.DataFrame(data)
    
    # Create the 'experiment' directory if it doesn't exist
    experiment_dir = 'experiment'
    if not os.path.exists(experiment_dir):
        os.makedirs(experiment_dir)
    
    # Check existing numbered directories and add another numbered folder
    numbered_folders = [d for d in os.listdir(experiment_dir) if os.path.isdir(os.path.join(experiment_dir, d))]
    if numbered_folders:
        new_folder_num = max([int(d) for d in numbered_folders]) + 1
    else:
        new_folder_num = 1
    
    new_folder_path = os.path.join(experiment_dir, str(new_folder_num))
    os.makedirs(new_folder_path)
    
    # Save the DataFrame to a CSV file inside the numbered folder
    csv_filename = os.path.join(new_folder_path, 'parameters.csv')
    df.to_csv(csv_filename, index=False)
