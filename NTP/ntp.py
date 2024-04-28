# Import necessary libraries
import ntplib
from time import ctime

# NTP server to query
ntp_server = 'pool.ntp.org'

# Function to get current time from NTP server
def get_ntp_time(server):
    try:
        # Create NTP client
        client = ntplib.NTPClient()

        # Query NTP server for time
        response = client.request(server)

        # Extract and return the current time from the response
        return ctime(response.tx_time)

    except Exception as e:
        # Handle any errors that may occur during the process
        print("Error:", e)
        return None

# Main function to demonstrate NTP time retrieval
def main():
    # Get current time from NTP server
    ntp_time = get_ntp_time(ntp_server)

    # Display the retrieved time
    if ntp_time:
        print("Current time (from NTP server):", ntp_time)
    else:
        print("Failed to retrieve current time from NTP server.")

# Execute the main function
if __name__ == "__main__":
    main()
