#!/usr/bin/env python3

import requests
import getpass
import base64

def create_readme_file(organization_name, repository_name, pat):
    # Define the README.md content
    readme_content = "## Welcome to My Repository\n\nThis is the README.md file for the repository."

    # Encode the content to base64
    readme_content_base64 = base64.b64encode(readme_content.encode()).decode()

    # Set up the headers with the personal access token
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Define the file creation data
    file_creation_url = f"https://api.github.com/repos/{organization_name}/{repository_name}/contents/README.md"
    file_creation_data = {
        "message": "Create README.md",
        "content": readme_content_base64,
        "branch": "develop",  # Add README to the 'develop' branch
    }

    # Make a PUT request to create the README.md file
    response = requests.put(file_creation_url, json=file_creation_data, headers=headers)

    # Check the response status code
    if response.status_code == 201:
        print("README.md file created successfully.")
    else:
        print("Failed to create README.md file.")
        print(response.text)

# Replace these variables with your organization and repository
organization_name = "<organization_name>"
repository_name = "<repo_name>"

# Prompt for the Personal Access Token (PAT)
pat = getpass.getpass("Enter your GitHub Personal Access Token: ")

# Create readme file
create_readme_file(organization_name, repository_name, pat)
