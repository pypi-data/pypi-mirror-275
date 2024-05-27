# Python Gmail Summary Bot

> [!WARNING]
> I recommend forking the repo and using it as a GitHub Action

## Creating credentials for accessing Google APIs.

### Step 1: Create a Service Account

1. **Go to the Google Cloud Console**: [Google Cloud Console](https://console.cloud.google.com/).
2. **Select your project** or create a new one.
3. Search for **APIs & Services** in the search bar.
4. Click on **Credentials** in the left sidebar.
5. Click on **Create Credentials** and select **OAuth client ID**.
6. Select **Desktop app** as the application type.
7. Add the generated credentials as environment variables in your project. 

### Step 2: Enable the Gmail API

1. **Go to the API & Services page**: [API & Services](https://console.cloud.google.com/apis/dashboard).
2. **Enable the Gmail API**:
    - Click on "Enable APIs and Services".
    - Search for "Gmail API" and enable it for your project.

## Local usage

```shell
cp .env.example .env
```

```shell
python3 -m venv .
python3 -m pip install -r requirements.txt
python3 main.py
```