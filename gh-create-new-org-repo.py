#!/usr/bin/env python3

import requests
import getpass

def create_github_repo(organization_name, repository_name, pat):
    # Define the API endpoint
    api_url = f"https://api.github.com/orgs/{organization_name}/repos"

    # Set up the headers with the personal access token
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Define the repository data
    repository_data = {
        "name": repository_name,
        "private": True,  # Create a private repository
    }

    # Make a POST request to create the repository
    response = requests.post(api_url, json=repository_data, headers=headers)

    # Check the response status code
    if response.status_code == 201:
        print(f"Repository '{repository_name}' created successfully in the '{organization_name}' organization.")
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(response.text)

# Replace these variables with your organization and repository
organization_name = "<organization_name>"
repository_name = "<repo_name>"

# Prompt for the Personal Access Token (PAT)
pat = getpass.getpass("Enter your GitHub Personal Access Token: ")

# Create the GitHub repository
create_github_repo(organization_name, repository_name, pat)
