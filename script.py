from email.utils import format_datetime
from datetime import datetime


pubdate = format_datetime(datetime.now())
output = f"<rss><channel><pubDate>{pubdate}</pubDate>"

endpoints = [
    "https://invertebase.org/portal/content/dwca/DMNH-Mollusk_DwC-A.zip",
    "https://invertebase.org/portal/content/dwca/ANSP-MAL_DwC-A.zip"
]

for endpoint in endpoints:
    output = output + f"<item><title>{endpoint}</title><link>{endpoint}</link><ipt:dwca>{endpoint}</ipt:dwca><pubDate>{pubdate}</pubDate></item>"

output = output + "</channel></rss>"

file = open("feed.rss", "w")
file.write(output)
file.close()
