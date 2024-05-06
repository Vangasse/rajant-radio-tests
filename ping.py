import csv
import os
import time
import ping3

def ping_ip(ip_address, num_attempts):
    responses = []
    for _ in range(num_attempts):
        response = ping3.ping(ip_address)
        if response is not None:
            responses.append(response * 1000)  # Convert to milliseconds
        else:
            print(f"Failed to ping {ip_address}")
    return responses

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Response Time (ms)'])
        for response_time in data:
            writer.writerow([response_time])

def find_next_folder(experiments_dir):
    numbered_folders = sorted([int(d) for d in os.listdir(experiments_dir) if os.path.isdir(os.path.join(experiments_dir, d))])
    for folder_num in numbered_folders:
        folder_path = os.path.join(experiments_dir, str(folder_num))
        if not os.path.exists(os.path.join(folder_path, "ping_data.csv")):
            return folder_path
    
    # If all existing folders contain "ping_data.csv", create a new numbered folder
    if numbered_folders:
        new_folder_num = max(numbered_folders) + 1
    else:
        new_folder_num = 1
    new_folder_path = os.path.join(experiments_dir, str(new_folder_num))
    os.makedirs(new_folder_path)
    return new_folder_path

if __name__ == "__main__":
    ip_address = "10.110.37.1"  # Change this to the IP address you want to ping
    num_attempts = 100  # Change this to the number of attempts you want to make
    experiments_dir = "experiment"

    responses = ping_ip(ip_address, num_attempts)
    if responses:
        filename = "ping_data.csv"
        folder_path = find_next_folder(experiments_dir)
        file_path = os.path.join(folder_path, filename)
        save_to_csv(responses, file_path)
        print(f"Response times saved to {file_path}")
    else:
        print("Aborted. Failed to ping the IP address.")
