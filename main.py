def check_email(text):
    if "price" in text:
        return "Send price reply"
    else:
        return "Send default reply"
    
email_text = "Hello, I need your price detail"
result = check_email(email_text)
print(result)