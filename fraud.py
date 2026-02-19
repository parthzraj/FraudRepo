import requests
from requests.auth import HTTPBasicAuth

def get_bearer_token(client_id, client_secret):
    """Authenticate with the API and return a bearer token."""
    token_url = "https://epaycop.xpectro-solutions.com/o/token/"
    data = {
        "grant_type": "client_credentials",
        "scope": "read write"
    }
    try:
        response = requests.post(token_url, data=data, auth=HTTPBasicAuth(client_id, client_secret))
        response.raise_for_status()
        token = response.json().get("access_token")
        print("Authentication successful!")
        return token
    except requests.exceptions.RequestException as e:
        raise Exception(f"Authentication failed: {e}")

def detect_phishing(file_obj, date_time, sender, receiver, locale, token):
    """Upload the audio file to the API and get the phishing detection result."""
    api_url = "https://epaycop.xpectro-solutions.com/api/fraud-detection/call/phishing"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "date_time": date_time,
        "sender": sender,
        "receiver": receiver,
        "locale": locale
    }
    try:
        # Prepare the file for upload
        files = {"file": (file_obj.filename, file_obj, "audio/wav")}
        print(f"Uploading file: {file_obj.filename}")
        response = requests.post(api_url, headers=headers, data=data, files=files)
        response.raise_for_status()
        print("File uploaded successfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")


def get_user_input():
    """Prompt the user for input parameters (CLI version)."""
    print("\nPlease enter the following details:")
    file_path = input("Audio file path (e.g., path/to/audio.wav): ")
    date_time = input("Date and time (e.g., 2024-10-27T13:18:00): ")
    sender = input("Sender phone number (e.g., +9122222222): ")
    receiver = input("Receiver phone number (e.g., +9199999999): ")
    locale = input("Locale (e.g., EN-IN for English-India): ")
    return file_path, date_time, sender, receiver, locale

def display_output(response):
    """Display the API's response in a clear format (CLI version)."""
    print("\n--- Phishing Detection Result ---")
    print(f"ID: {response.get('id')}")
    print(f"File Name: {response.get('file_name')}")
    print(f"Category: {response.get('category')}")  
    print(f"Reason: {response.get('reason')}")
    print("--------------------------------\n")

def main():
    """Main function to run the phishing detection process (CLI version)."""
    
    print("First, let’s authenticate with the API.")
    client_id = input("Enter your Client ID: ")
    client_secret = input("Enter your Client Secret: ")
    token = get_bearer_token(client_id, client_secret)
    
    
    while True:
        
        file_path, date_time, sender, receiver, locale = get_user_input()
        
        response = detect_phishing(file_path, date_time, sender, receiver, locale, token)
        
        display_output(response)
        
        again = input("Do you want to analyze another audio file? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using the phishing detector!")
            break

if __name__ == "__main__":
    main()