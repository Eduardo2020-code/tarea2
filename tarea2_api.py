import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


try:
    response = requests.get(f"{BASE_URL}/posts")
    response.raise_for_status()
    datos = response.json()

    print("✅ First 5 post titles from the API:\n")
    for post in datos[:5]:
        print(f"- {post['title'].capitalize()}")

except requests.exceptions.RequestException as e:
    print("❌ Error performing GET request:", e)


new_post = {
    "title": "Test post",
    "body": "This content was sent from a Python script.",
    "userId": 1
}

try:
    post_response = requests.post(f"{BASE_URL}/posts", json=new_post)
    post_response.raise_for_status()
    result = post_response.json()

    print("\n✅ POST successful. Server response:")
    for key, value in result.items():
        print(f"{key}: {value}")

except requests.exceptions.RequestException as e:
    print("❌ Error performing POST request:", e)
