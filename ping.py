import csv
import time
import ping3

def ping_ip(ip_address, duration_seconds):
    responses = []
    start_time = time.time()
    while (time.time() - start_time) < duration_seconds:
        response = ping3.ping(ip_address)
        if response is not None:
            responses.append(response * 1000)  # Convert to milliseconds
        else:
            print(f"Failed to ping {ip_address}")
            return None  # Abort if ping fails
    return responses

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Response Time (ms)'])
        for response_time in data:
            writer.writerow([response_time])

if __name__ == "__main__":
    ip_address = "192.168.2.199"  # Change this to the IP address you want to ping
    duration_seconds = 60  # Change this to the duration you want to ping in seconds

    responses = ping_ip(ip_address, duration_seconds)
    if responses is not None:
        if len(responses) > 0:
            filename = "XXm.csv"
            save_to_csv(responses, filename)
            print(f"Response times saved to {filename}")
        else:
            print("No responses received.")
    else:
        print("Aborted. Failed to ping the IP address or took too long to respond.")