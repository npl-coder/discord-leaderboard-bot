import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Scope
scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

#
creds = Credentials.from_service_account_file(
    "credentials.json", scopes=scopes)

client = gspread.authorize(creds)
sheets_id = os.getenv("SHEET_ID")
sheet = client.open_by_url(sheets_id)
worksheet_list = sheet.worksheets()
worksheet = sheet.sheet1

