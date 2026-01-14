def generate_reply(reply_type):
    if reply_type == "price":
       return("""Hello, \n
        Thank you for your inquiry about our pricing.\n
        Our prices start from Rs.5,000.\n
        Best regards,\n
        Support Team
        """)
    elif reply_type == "contact":
        return("""Hello, \n
        You can contact us via phone or whatsapp +94771234567\n
        Best regards,\n
        Support Team
        """)
    elif reply_type == "help":
        return("""Hello,\n
        We are happy to help you. Please describe your issue.\n
        Best regards,\n
        Support Team
        """)
    else:
        return("""
        Hello,\n
        Thank you for contacting us. We will get back to you shortly.\n
        Best regards,\n
        Support Team
        """)