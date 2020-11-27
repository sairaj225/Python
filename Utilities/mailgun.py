
import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd58f6d278f5f45799467aa38681f7c46.mailgun.org/messages",
        auth=("api", "d16f419795311d8ed9e2852ed8758c07-a83a87a9-cdfb81d3"),
        data={"from": "mailgun@sandboxd58f6d278f5f45799467aa38681f7c46.mailgun.org",
              "to": ["sairaju.atukuri123@gmail.com", "sai raju@sandboxd58f6d278f5f45799467aa38681f7c46.mailgun.org"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
            
r=send_simple_message()
print(r)