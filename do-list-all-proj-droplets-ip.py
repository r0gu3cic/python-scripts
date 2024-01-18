#!/usr/bin/env python3

import requests
import getpass  # For securely inputting the API token

# Prompt for the Personal Access Token (PAT)
api_token = getpass.getpass("Enter your DigitalOcean API token: ")

# Define the DigitalOcean API endpoint to list all droplets
url = 'https://api.digitalocean.com/v2/droplets'

# Define the headers with the API token for authentication
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

# Make the API request to list all droplets
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    droplets = response.json()['droplets']
    
    # Extract and print the IP addresses of all droplets
    for droplet in droplets:
        droplet_name = droplet['name']
        droplet_ip = droplet['networks']['v4'][0]['ip_address']
        print(f'Droplet Name: {droplet_name}, IP Address: {droplet_ip}')
else:
    print(f'Failed to retrieve droplet information. Status code: {response.status_code}')