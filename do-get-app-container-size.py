#!/usr/bin/env python3

import requests
import getpass  # For securely inputting the API token

# Prompt for the Personal Access Token (PAT)
api_token = getpass.getpass("Enter your DigitalOcean API token: ")

# Define the DigitalOcean Apps API endpoint to list all apps
url = 'https://api.digitalocean.com/v2/apps'

# Define the headers with the API token for authentication
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

# Make the API request to list all apps
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    apps = response.json()['apps']

    # Extract and print information about each app and service
    for app in apps:
        app_name = app['spec']['name']

        # Retrieve information about services
        services = app['spec']['services']

        for service in services:
            service_name = service['name']
            instance_size_slug = service['instance_size_slug']
            print(f'App Name: {app_name}, Service Name: {service_name}, Instance Size Slug: {instance_size_slug}')

else:
    print(f'Failed to retrieve app information. Status code: {response.status_code}')
