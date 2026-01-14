def get_reply_type(email_text):

    email_text = email_text.lower()

    if "price" in email_text:
        return "price"
    elif "contact" in email_text:
        return "contact"
    elif "help" in email_text:
        return "help"
    else:
        "default"