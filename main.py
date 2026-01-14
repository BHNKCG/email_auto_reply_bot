from keyword_rules import get_reply_type
from reply_templates import generate_reply

email_text = "Hello, I need your contact details"
reply_type = get_reply_type(email_text)
reply_message = generate_reply(reply_type)

print("Detected type:", reply_type)
print("\nAuto Reply Message:\n")
print(reply_message)