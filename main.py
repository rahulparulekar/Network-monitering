# Import necessary libraries
import os
import socket

# Function to print a welcome message
def netCheck():
    print('Welcome to NetCheck.')
    print('NetCheck is where you can utilize network tools.')
    print()

netCheck()

# Define functions for network operations

# Function to perform telnet
def telnet(ip, port):
    command = f"telnet {ip} {port}"  # Construct the telnet command
    os.system(command)  # Execute the telnet command using the os.system function

# Function to perform netcat
def netcat(ip, port, protocol='TCP'):
    if protocol == 'TCP':
        command = f"nc -vz {ip} {port}"  # Construct the netcat TCP command
    elif protocol == 'UDP':
        command = f"nc -vzu {ip} {port}"  # Construct the netcat UDP command
    os.system(command)  # Execute the netcat command using the os.system function

# Function to perform traceroute
def traceroute(ip):
    command = f"traceroute {ip}"  # Construct the traceroute command
    os.system(command)  # Execute the traceroute command using the os.system function

# Function to display the menu
def menu():
    print('Which tool would you like to use?')
    print('1. Telnet')
    print('2. Netcat (TCP)')
    print('3. Netcat (UDP)')
    print('4. Traceroute')

menu()

# Main loop for user interaction

while True:
    choice = input("Enter the number of the tool you want to use (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print('Invalid Input')
        continue

    target_ip = input('Enter Target IP Address: ')

    # Check if the entered IP address is valid
    if not socket.inet_aton(target_ip):
        print('Invalid IP address. Please enter a valid IP address.')
        continue

    target_port = input('Enter Target Port: ')

    # Check if the entered port is a number
    if not target_port.isdigit():
        print('Port must be a number.')
        continue

    if choice == '1':
        telnet(target_ip, target_port)  # Call the telnet function
    elif choice == '2':
        netcat(target_ip, target_port, protocol='TCP')  # Call the netcat function for TCP
    elif choice == '3':
        netcat(target_ip, target_port, protocol='UDP')  # Call the netcat function for UDP
    elif choice == '4':
        traceroute(target_ip)  # Call the traceroute function

    repeat_net_check = input('Would you like to make another NetCheck? (Y/n)').strip().lower()

    # Check if the user wants to repeat the NetCheck
    if repeat_net_check != "y":
        break
