#!/usr/bin/env python3

import requests
import getpass

def add_branch_protection(organization_name, repository_name, branch_name, pat):
    # Define the branch protection rule data
    branch_protection_url = f"https://api.github.com/repos/{organization_name}/{repository_name}/branches/{branch_name}/protection"
    branch_protection_data = {
        "required_status_checks": None,
        "enforce_admins": None,
        "required_pull_request_reviews": {
            "require_code_owner_reviews": False,  # Adjust as needed
            "required_approving_review_count": 1,
            "dismiss_stale_reviews": True,
            "require_linear_history": True,  # Require linear history
        },
        "restrictions": None,
        "required_linear_history": True,  # Require linear history
        "allow_force_pushes": False,
        "allow_deletions": False,
    }

    # Set up the headers with the personal access token
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Make a PUT request to add branch protection
    response = requests.put(branch_protection_url, json=branch_protection_data, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print(f"Branch protection added to the '{branch_name}' branch of '{repository_name}'.")
    else:
        print(f"Failed to add branch protection. Status code: {response.status_code}")
        print(response.text)

# Replace these variables with your organization and repository
organization_name = "<organization_name>"
repository_name = "<repo_name>"
branch_name = "develop"

# Prompt for the Personal Access Token (PAT)
pat = getpass.getpass("Enter your GitHub Personal Access Token: ")

# Add branch protection to the GitHub repository with the specified criteria
add_branch_protection(organization_name, repository_name, branch_name, pat)
