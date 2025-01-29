# Google Sheets Data Processor

This project provides functionality to interact with a Google Sheet, perform data analysis, and update scores.

## Features

- **Get Top Individuals:** Retrieve the top K individuals based on their score.
- **Get Top Places:** Retrieve the top K places based on the average score.
- **Add New User:** Add new users to the Google Sheet.
- **Increase Score:** Increase the score of a specific user.

## Setup

1.  **Clone the repository**
2.  **Create a .env file** in the root directory and add your Google Sheet ID:
    ```
    SHEET_ID=your_google_sheet_id
    ```
3.  **Download your Google Service Account credentials** as `credentials.json` and place it in the root directory. This file is necessary for authenticating with the Google Sheets API.
4.  **Install the necessary packages:**
    ```
    pip install gspread pandas python-dotenv google-auth-oauthlib google-auth-httplib2
    ```

## Usage

Refer to the `sheet/sheet_operations.py` file for the functions and their usage. This file contains the core logic for interacting with Google Sheets, including reading data, adding new users, and updating scores.

## File Structure

-   `.env`: Contains environment variables, specifically the Google Sheet ID.
-   `credentials.json`: Contains Google Service Account credentials for authenticating with the Google Sheets API.
-   `sheet/config.py`: Configures the connection to Google Sheets using the provided credentials. It handles the authentication process.
-   `sheet/sheet_operations.py`: Contains functions for interacting with the Google Sheet, such as getting top individuals, top places, adding new users, and increasing scores.

## Google API Setup

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new project or select an existing one.
3.  Enable the **Google Sheets API** for your project.
4.  Create a service account and download the credentials as a JSON file (`credentials.json`).
5.  Share your Google Sheet with the service account's email address.
