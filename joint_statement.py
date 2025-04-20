# -*- coding: utf-8 -*-
import requests, pdfkit, tempfile, os

url = "https://www.state.gov/joint-statement-on-the-united-states-ukraine-meeting-in-jeddah/"
headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get(url, headers=headers, timeout=30).text

with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
    f.write(html.encode())
    temp_html = f.name

pdf_name = "US_Ukraine_Jeddah_Statement.pdf"
pdfkit.from_file(temp_html, pdf_name)
os.remove(temp_html)