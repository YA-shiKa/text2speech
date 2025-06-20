import requests

response = requests.post("http://127.0.0.1:8000/speak", json={"text": "Namaste, how are you?"})

if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("✅ Audio saved to output.mp3")
else:
    print(f"❌ Failed: {response.status_code} {response.text}")
