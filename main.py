from keyword_rules import get_reply_type

email_text = "Hello, can you send me your contact details?"
reply_type = get_reply_type(email_text)

print("Detected reply type:", reply_type)