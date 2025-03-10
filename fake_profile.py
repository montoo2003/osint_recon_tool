import requests

def detect_fake_profile(username):
    url = f"https://nitter.net/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        profile_data = response.text
        if "Joined February 2024" in profile_data:
            return "⚠️ This profile is likely fake (very new account)."
        return "✅ Profile appears legitimate."
    
    return "User not found."
