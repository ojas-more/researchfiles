import mwclient
import time
from datetime import datetime

class CryptoWikiFetcher:
    def __init__(self, crypto_name: str):
        self.crypto_name = crypto_name
        self.site = mwclient.Site('en.wikipedia.org')
        self.page = self.site.pages[crypto_name]

    def get_intro_text(self, char_limit=500) -> str:
        return self.page.text()[:char_limit]

    def get_sorted_revisions(self) -> list:
        revisions = list(self.page.revisions())
        return sorted(revisions, key=lambda rev: rev["timestamp"])

    def print_revision_timestamps(self):
        revisions = self.get_sorted_revisions()
        for rev in revisions:
            ts_struct = rev["timestamp"]
            ts_datetime = datetime.fromtimestamp(time.mktime(ts_struct))
            print(ts_datetime)

    def print_first_and_last_revision(self):
        revisions = self.get_sorted_revisions()
        if not revisions:
            print("No revisions found.")
            return

        first = revisions[0]
        last = revisions[-1]

        first_time = datetime.fromtimestamp(time.mktime(first["timestamp"]))
        last_time = datetime.fromtimestamp(time.mktime(last["timestamp"]))

        print(f"\nFirst revision by {first['user']} at {first_time}")
        print(f"Comment: {first.get('comment', 'No comment')}\n")

        print(f"Last revision by {last['user']} at {last_time}")
        print(f"Comment: {last.get('comment', 'No comment')}")

if __name__ == "__main__":
    crypto_name = input("Enter the name of the cryptocurrency: ").strip()
    fetcher = CryptoWikiFetcher(crypto_name)

    print("\n--- Intro Text ---")
    print(fetcher.get_intro_text())

    print("\n--- First and Last Revisions ---")
    fetcher.print_first_and_last_revision()
