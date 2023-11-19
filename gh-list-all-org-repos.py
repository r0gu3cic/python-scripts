#!/usr/bin/env python3

# List all repos in the org and spit out how many repos there is 

import requests
import getpass  # For securely inputting the PAT

# Replace these variables with your organization
organization = "<organization_name>"

# Prompt for the Personal Access Token (PAT)
pat = getpass.getpass("Enter your GitHub Personal Access Token: ")

# Define the API endpoint URL to list organization repositories
org_repos_url = f"https://api.github.com/orgs/{organization}/repos"

# Set up headers for the API request
headers = {
    "Authorization": f"token {pat}",
    "Accept": "application/vnd.github.v3+json"
}

# Initialize a list to store all repositories
all_repos = []

# Define a function to fetch repositories and handle pagination
def fetch_repositories(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        all_repos.extend(repos)
        # Check if there are more pages
        if "next" in response.links:
            fetch_repositories(response.links["next"]["url"])
    else:
        print(f"Failed to retrieve organization repositories. Status code: {response.status_code}")

# Fetch all repositories
fetch_repositories(org_repos_url)

# Print the total count and names of all repositories
total_count = len(all_repos)
print(f"Total number of organization repositories: {total_count}")
print("List of organization repositories:")
for repo in all_repos:
    print(repo["name"])