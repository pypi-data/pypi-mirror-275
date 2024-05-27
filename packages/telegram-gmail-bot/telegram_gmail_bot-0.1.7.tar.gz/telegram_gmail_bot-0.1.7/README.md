# Python Gmail Summary Bot

[![PyPI version](https://badge.fury.io/py/telegram-gmail-bot.svg)](https://badge.fury.io/py/telegram-gmail-bot)

A bot to summarize your Gmail emails using the Gmail API and send summaries to Telegram.

## Features
- Summarizes Gmail emails.
- Sends email summaries to a specified Telegram chat.

## Installation

You can install the package via pip:

```shell
pip install telegram-gmail-bot
```

## Setup

### Creating credentials for accessing Google APIs

#### Step 1: Create a Service Account

1. **Go to the Google Cloud Console**: [Google Cloud Console](https://console.cloud.google.com/).
2. **Select your project** or create a new one.
3. Search for **APIs & Services** in the search bar.
4. Click on **Credentials** in the left sidebar.
5. Click on **Create Credentials** and select **OAuth client ID**.
6. Select **Desktop app** as the application type.
7. Add the generated credentials as environment variables in your project.

#### Step 2: Enable the Gmail API

1. **Go to the API & Services page**: [API & Services](https://console.cloud.google.com/apis/dashboard).
2. **Enable the Gmail API**:
   - Click on "Enable APIs and Services".
   - Search for "Gmail API" and enable it for your project.

## Local Usage

1. Copy the example environment file and fill in your credentials:
    ```shell
    cp .env.example .env
    ```

2. Create a virtual environment and install dependencies:
    ```shell
    python3 -m venv .
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the bot:
    ```shell
    python main.py
    ```
