import requests

print("=" * 40)
print("🔗 URL Shortener")
print("=" * 40)

url = input("Enter your long URL: ")

api = f"https://tinyurl.com/api-create.php?url={url}"

try:
    response = requests.get(api)

    if response.status_code == 200:
        print("\n✅ Short URL:")
        print(response.text)
    else:
        print("\n❌ Failed to shorten the URL.")

except Exception as e:
    print("\nError:", e)
