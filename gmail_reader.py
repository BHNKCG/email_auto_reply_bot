import base64

def get_unread_emails(service, max_results=5):
    results = service.users().messages().list(
        userId = "me",
        labelIds = ["INBOX", "UNREAD"],
        maxResults = max_results
    ).execute()

    messages = results.get("messages", [])
    emails = []

    for msg in messages:
        msg_data  = service.users().messages().get(
            userId = "me",
            id = msg["id"],
            format = "full"
        ).execute()

        headers = msg_data["payload"]["headers"]

        subject = ""
        sender = ""

        for header in headers:
            if header["name"] == "Subject":
                subject = header["value"]
            if header["name"] == "From":
                sender = header["value"]
        
        body = ""

        parts = msg_data["payload"].get("parts")
        if parts:
            for part in parts:
                if part["mimeType"] == "text/plain":
                    data = part["body"].get("data")
                    if data:
                        body = base64.urlsafe_b64decode(data).decode("utf-8")
        else:
            data = msg_data["payload"]["body"].get("data")
            if data:
                body = base64.urlsafe_b64decode(data).decode("utf-8")

        emails.append({
            "id": msg["id"],
            "from": sender,
            "subject": subject,
            "body": body
        })

    return emails

def mark_as_read(service, message_id):
    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={"removeLabelIds": ["UNREAD"]}
    ).execute()
