GitHub Webhook Telegram Notification
This project is a simple Flask application that receives GitHub webhook events and sends notifications to a specified Telegram chat. When a commit is pushed to a GitHub repository, this application extracts the commit message and the author's details, and then sends them to a Telegram chat using a bot.

Features
Receives webhook events from GitHub
Sends commit messages and author details to a Telegram chat
Supports asynchronous message sending
Prerequisites
Python 3.10+
GitHub account and repository
Telegram bot and chat setup
python-telegram-bot library
Flask library
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Create a virtual environment and activate it:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Set up your GitHub webhook. In your GitHub repository, go to Settings -> Webhooks -> Add webhook and configure it with the following details:

Payload URL: http://your-server-url/webhook
Content type: application/json
Events: Select Push events or any other event you want to receive
Configuration
You need to configure the Telegram bot token and chat ID. These are hardcoded in app.py:

python
Copy code
TOKEN = 'your-telegram-bot-token'
CHAT_ID = 'your-chat-id'
Replace 'your-telegram-bot-token' and 'your-chat-id' with your bot's token and your Telegram chat ID.

Running the Application
To run the Flask application, use the following command:

bash
Copy code
python app.py
The server will start on localhost:5000. Ensure that your server is publicly accessible if you are deploying it for production use.

How It Works
When the GitHub repository receives a push event, it sends a webhook to the /webhook endpoint of this Flask application.
The application processes the webhook data, extracts the commit messages and author information, and sends the data to a specified Telegram chat using a bot.
Example of a Telegram Message
sql
Copy code
Commit message: Fixed a bug in the login logic
Author: John Doe <johndoe@example.com>
Troubleshooting
If messages aren't sent to the Telegram chat, ensure that the bot has permission to send messages to the chat.
Check the logs in the terminal for any errors.
Ensure that the webhook is correctly set up in your GitHub repository.
