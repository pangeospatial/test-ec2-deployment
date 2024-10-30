import argparse
import requests

def send_email(message, subject):
    data = {
        "message": message,
        "subject": subject
    }
    response = requests.post("https://hook.us1.make.com/o6w7cj9fw9gjzxog1y21q8fwnntupc6o", data=data)
    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email. Status code: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send an email via webhook")
    parser.add_argument("-m", "--message", required=True, help="The body of the email message")
    parser.add_argument("-s", "--subject", required=True, help="The subject of the email")

    args = parser.parse_args()
    send_email(args.message, args.subject)
