import csv
import os

import requests

ACTOR = "data_factory_nerd~sam-gov-contract-opportunities"
URL = f"https://api.apify.com/v2/acts/{ACTOR}/run-sync-get-dataset-items"

run_input = {
    "naicsCodes": ["541511", "541512", "541519"],  # IT services
    "noticeTypes": ["o", "k", "p", "r"],           # solicitations, combined, presolicitations, sources sought
    "openForResponseOnly": True,                   # skip notices whose deadline has passed
    "includeAttachments": True,                    # direct links to the SOW / RFP documents
    "maxItems": 50,
}

resp = requests.post(
    URL,
    headers={"Authorization": f"Bearer {os.environ['APIFY_TOKEN']}"},
    json=run_input,
    timeout=300,
)
resp.raise_for_status()
notices = resp.json()

with open("sam_bids.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["deadline", "title", "agency", "naics", "set_aside", "url", "first_attachment"])
    for n in sorted(notices, key=lambda n: n.get("responseDeadline") or "9999"):
        att = (n.get("attachments") or [{}])[0].get("url")
        w.writerow([n.get("responseDeadline"), n["title"], n.get("subTier") or n.get("department"),
                    n.get("naicsCode"), n.get("setAside"), n["url"], att])

print(f"Saved {len(notices)} open opportunities to sam_bids.csv")
