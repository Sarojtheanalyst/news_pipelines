import pandas as pd
from scraper import NewsScraper
from sheets import GoogleSheetManager


def run_pipeline():
    scraper = NewsScraper()
    gs = GoogleSheetManager()

    ws = gs.get_worksheet("News_Data")

    # existing data
    existing_titles = gs.get_existing_titles(ws)

    # SCRAPE DATA
    bajar = scraper.scrape_bajar()
    nepali = scraper.scrape_nepali_paisa()

    scraper.close()

    all_news = bajar + nepali

    # FILTER ONLY NEW NEWS
    new_rows = []

    for item in all_news:
        if item["title"] not in existing_titles:
            new_rows.append([
                item["title"],
                item["news"],
                item["source"],
                item["timestamp"]
            ])

    # UPLOAD
    if new_rows:
        ws.append_rows(new_rows)
        print(f"✅ {len(new_rows)} new news added!")
    else:
        print("⚡ No new news found!")


if __name__ == "__main__":
    run_pipeline()