from sec_edgar_downloader import Downloader
import os
import requests
import argparse
import datetime

def check_filings_available(ticker, start_year, end_year):
    """
    Check if there are any 10-K filings available for the given ticker and year range.
    """
    # Construct the base URL for querying EDGAR
    base_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ticker}&type=10-K&dateb={start_year}1231&owner=exclude&count=40"
    
    # Query the first page to check for filings
    response = requests.get(base_url)
    if "No matching Ticker Symbol." in response.text or "No filings available." in response.text:
        return False
    return True

def download_data(name, ticker, email, start, end):
    """
    Download 10-K filings for the given ticker and year range.
    
    """
    data_dir = f"10-k_data"
    os.makedirs(data_dir, exist_ok=True)
    dl = Downloader(name, email, os.path.join(os.getcwd(), data_dir))
    
    start_date = datetime.date(start, 1, 1)
    end_date = datetime.date(end + 1, 1, 1) if end else None
    
    # Check if filings are available from the start year
    if not check_filings_available(ticker, start, end):
        raise ValueError(f"No 10-K filings available for {ticker} from {start} to {end}")
    
    try:
        num_filings = dl.get("10-K", ticker, limit=None, after=start_date, before=end_date, include_amends=False, download_details=True)
        print(f"Downloaded {num_filings} 10-K filings for {ticker} from {start_date} to {end_date}")
    except Exception as e:
        print(f"Error downloading or cleaning 10-K filings for {ticker}: {e}")
    
def main():
    parser = argparse.ArgumentParser(description="Download 10-K filings for a company")
    parser.add_argument("--name", type=str, help="Your company name")
    parser.add_argument("--ticker", type=str, help="The company ticker")
    parser.add_argument("--email", type=str, help="Your email address")
    parser.add_argument("--start", type=int, help="The start year")
    parser.add_argument("--end", type=int, help="The end year")
    args = parser.parse_args()
    
    download_data(args.name, args.ticker, args.email, args.start, args.end)
    return 0

if __name__ == "__main__":
    main()
