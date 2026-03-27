import sys
import requests

if len(sys.argv) < 2:
    print("Error: Please provide a company name.")
    sys.exit(1)

company_name = sys.argv[1]
print(f"--- Starting Employee Search for: {company_name} ---")

# You will need to sign up for a free API key from a provider like Apollo.io
API_KEY = "YOUR_FREE_API_KEY"

def search_company_employees(name):
    # Step 1: Query the API to find the company and its employees
    url = "https://api.apollo.io/v1/mixed_people/search"
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    }
    
    # We ask the API to find people at the inputted company name
    payload = {
        "api_key": API_KEY,
        "q_organization_name": name,
        # You can uncomment the line below to filter strictly by job titles
        # "person_titles":,
        "per_page": 5 # Limit results to save free credits
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
                
                # Only print if an email was successfully verified by the provider
                if email:
                    print(f"Name: {full_name}")
                    print(f"Title: {title}")
                    print(f"Verified Email: {email}")
                    print("-" * 40)
        else:
            print("No contacts found for this company.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the search
search_company_employees(company_name)
