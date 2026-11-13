# Data Factory examples

Small, runnable scripts that use the Data Factory scrapers on the Apify Store.

| Script | What it does | Scraper |
|---|---|---|
| `sam_bids.py` | Exports open SAM.gov IT-services opportunities (NAICS 541511/541512/541519) to `sam_bids.csv`, sorted by response deadline, with a link to the first attachment. | [SAM.gov Contract Opportunities Scraper](https://apify.com/data_factory_nerd/sam-gov-contract-opportunities) |

## Run it

```bash
pip install requests
export APIFY_TOKEN=...   # your Apify API token
python sam_bids.py
```

No SAM.gov account or API key needed. You pay Apify per result (see the scraper's Store page for current pricing).

## More scrapers

- [Greenhouse Jobs Scraper](https://apify.com/data_factory_nerd/greenhouse-jobs-scraper)
- [ATS Jobs Scraper](https://apify.com/data_factory_nerd/ats-jobs-scraper)

MIT licensed.
