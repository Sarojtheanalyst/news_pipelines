import gspread
from google.oauth2.service_account import Credentials
from config import SCOPES, SPREADSHEET_ID

class GoogleSheetManager:
    def __init__(self, creds_file="service_account.json"):
        creds = Credentials.from_service_account_file(
            creds_file,
            scopes=SCOPES
        )
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_key(SPREADSHEET_ID)

    def get_worksheet(self, name="News_Data"):
        try:
            return self.sheet.worksheet(name)
        except:
            return self.sheet.add_worksheet(name, rows=5000, cols=20)

    def get_existing_titles(self, ws):
        records = ws.get_all_records()
        return set([r.get("title") for r in records if r.get("title")]) 