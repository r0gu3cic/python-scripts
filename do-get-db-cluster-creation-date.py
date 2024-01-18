#!/usr/bin/env python3

import requests
import getpass  # For securely inputting the API token
from datetime import datetime

# Prompt for the Personal Access Token (PAT)
api_token = getpass.getpass("Enter your DigitalOcean API token: ")

# DigitalOcean API endpoint for listing all databases
url = "https://api.digitalocean.com/v2/databases"

# Define the headers with the API token for authentication
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json",
}

# Make a GET request to the DigitalOcean API to get information about all databases
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Loop through each database cluster
    for database in data["databases"]:
        # Extract information about each database cluster
        cluster_id = database["id"]
        cluster_name = database["name"]
        creation_timestamp = database["created_at"]

        # Convert the timestamp to a datetime object
        creation_date = datetime.strptime(creation_timestamp, "%Y-%m-%dT%H:%M:%SZ")

        # Calculate the age of the database cluster
        current_date = datetime.now()
        database_age = current_date - creation_date

        # Format the creation date
        formatted_creation_date = creation_date.strftime("%d.%m.%Y at %H:%M")

        print(f"Cluster '{cluster_name}' (ID: {cluster_id}) is {database_age.days} days old. It was created on {formatted_creation_date}h.")
else:
    print(f"Error: {response.status_code} - {response.text}")