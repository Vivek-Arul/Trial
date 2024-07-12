import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import string

# Set up the Google Sheets API client
def get_gsheet_client(creds_path='credentials.json'):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    return client

# Generate random data
def generate_random_data(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def main():
    sheet_name = 'testing'  # Update this to the name of your Google Sheet
    cell = 'A1'  # Update this to the cell where you want to write the data

    client = get_gsheet_client()
    sheet = client.open(sheet_name).sheet1

    random_data = generate_random_data()
    sheet.update_acell(cell, random_data)
    print(f"Written random data to Google Sheet: {random_data}")

if __name__ == "__main__":
    main()
