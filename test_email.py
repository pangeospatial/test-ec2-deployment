import requests

data = {
    "message": "Hello, this is the body.",
    "subject": "Test Email Subject"
}
response = requests.post("https://hook.us1.make.com/o6w7cj9fw9gjzxog1y21q8fwnntupc6o", data=data)
