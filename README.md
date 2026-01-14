# Automated Email Reply Bot 
A python-based Gmail API automation system. It is a bot that automatically reads unread emails, identifies user intention, responds appropriately, and marks the emails as having been read all under the secure OAuth authentication.

## Features
- Read unread Gmail emails automatically
- Detect email intent using keyword-based logic
- Generate predefined reply messages
- Send replies automatically via Gmail API
- Mark emails as read after replying
- Secure OAuth 2.0 authentication
- Clean, modular Python project structure

## Tech Stack
- Python
- Gmail API
- Google OAuth 2.0
- Git & GitHub

## Project Structure
<<<<<<< HEAD
```
email_auto_reply_bot/
├── main.py
├── gmail_auth.py
├── gmail_reader.py
├── gmail_sender.py
├── keyword_rules.py
├── reply_templates.py
├── requirements.txt
├── .gitignore
└── README.md
=======
```text
email_auto_reply_bot/
     ├── main.py
     ├── keyword_rules.py
     ├── reply_templates.py
     ├── requirements.txt
     ├── .gitignore
     └── README.md
>>>>>>> 12dcdc6942bc5ef16776b5846bf4286139919aa5
```
## How to Run
1. Clone the repository:

       git clone https://github.com/BHNKCG/email_auto_reply_bot.git

2. Go to the project folder:

       cd email_auto_reply_bot

3. Install Dependencies
pip install -r requirements.txt

4. Enable Gmail API & Get Credentials
- Go to Google Cloud Console
- Create a new project
- Enable Gmail API
- Configure OAuth Consent Screen (External → Testing)
- Create OAuth Client ID (Desktop App)
- Download the credentials file and rename it:
     credentials.json
(DO NOT upload this .json file to GitHub)

5. Run the bot:
python main.py
- Browser will open for Google login (first run only)
- Allow access
- token.json will be generated automatically


## Security Notes
- Never commit credentials.json
- Never commit token.json
- .gitignore is configured to protect sensitive files

## Use Cases
- Customer support automation
- Small business email responders
- Freelancers handling client inquiries
