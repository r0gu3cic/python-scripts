#!/usr/bin/env python3

# Add all the organization repos to the team 

import requests
import getpass  # For securely inputting the PAT

# Replace these variables with your organization and team
organization = "<organization_name>"
team_slug = "<team_slug>"

# Prompt for the Personal Access Token (PAT)
pat = getpass.getpass("Enter your GitHub Personal Access Token: ")

# Define the API endpoint URLs
org_repos_url = f"https://api.github.com/orgs/{organization}/repos"
team_url = f"https://api.github.com/orgs/{organization}/teams/{team_slug}/repos"

# Get a list of all organization repositories
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

# Add each repository to the team
for repo in all_repos:
    repo_name = repo["name"]
    repo_full_name = repo["full_name"]
    response = requests.put(f"{team_url}/{repo_full_name}", headers=headers)

    if response.status_code == 204:
        print(f"Added repository {repo_name} to team {team_slug}")
    else:
        print(f"Failed to add repository {repo_name} to team {team_slug}. Status code: {response.status_code}")

