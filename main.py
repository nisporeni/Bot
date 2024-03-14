from stellar_sdk import Server
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sheet-parse-417019-e0be24b77bd5.json', scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet (replace 'Your Spreadsheet Name' with your actual spreadsheet name)
spreadsheet = client.open('DCG')
sheet = spreadsheet.sheet1

server = Server(horizon_url="https://horizon.stellar.org")
account_id = "GDLOECLBYEQXT4QGNGK4QZAK4YFCDR6K2CNLRJWDBLB3OVMAOFBCJB3Z"

def balance_handler(account_response):
    balance = account_response["balances"][1]  # Assuming XLM is the first asset in the list
    xlm_balance = balance['balance'].split('.')[0]  # Extract the part before the dot
    print(f"XLM balance: {xlm_balance}")

    # Update Google Spreadsheet cell B2 with the XLM balance
    sheet.update_cell(2, 2, xlm_balance)

# Fetch initial account balance
account = server.accounts().account_id(account_id).call()
balance_handler(account)
