from gmail_auth import get_gmail_service
from gmail_reader import get_unread_emails, mark_as_read
from gmail_sender import send_reply
from keyword_rules import get_reply_type
from reply_templates import generate_reply

service = get_gmail_service()

emails = get_unread_emails(service)

print(f"Processing {len(emails)} unread emails...\n")

for email in emails:
    reply_type = get_reply_type(email["body"])
    reply_message = generate_reply(reply_type)

    send_reply(
        service,
        to_email=email["from"],
        subject=email["subject"],
        message_text=reply_message
    )

    mark_as_read(service, email["id"])

    print("Replied to:", email["from"])
