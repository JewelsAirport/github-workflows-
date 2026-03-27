import sys
import os
import requests

if len(sys.argv) < 2:
    print("Error: Please provide a company name.")
    sys.exit(1)

company_name = sys.argv[1]
print(f"--- Starting Employee Search for: {company_name} ---")

# Securely grab the API key from GitHub Secrets
API_KEY = os.environ.get("APOLLO_API_KEY")

def search_company_employees(name):
    if not API_KEY:
        print("Error: APOLLO_API_KEY is not set in GitHub Secrets.")
        return

    url = "https://api.apollo.io/v1/mixed_people/search"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    }
    
    payload = {
        "api_key": API_KEY,
        "q_organization_name": name,
        "per_page": 5 
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        
        if "people" in data and len(data["people"]) > 0:
            print(f"\nFound {len(data['people'])} verified contacts:\n")
            for person in data["people"]:
                full_name = person.get("name", "Unknown")
                title = person.get("title", "Unknown Title")
                email = person.get("email", "No email found")
                
                if email:
                    print(f"Name: {full_name}")
                    print(f"Title: {title}")
                    print(f"Verified Email: {email}")
                    print("-" * 40)
        else:
            print("No contacts found for this company.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

search_company_employees(company_name)
