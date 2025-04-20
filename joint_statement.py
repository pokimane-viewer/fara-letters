#!/usr/bin/env python3
# joint_statement.py
# std‑lib + pip install requests==2.32.2 beautifulsoup4==4.12.3 reportlab==4.2.0

import textwrap, requests, sys
from pathlib import Path
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

URL = "https://www.state.gov/joint-statement-on-the-united-states-ukraine-meeting-in-jeddah/"
OUT = "US_Ukraine_Jeddah_Statement.pdf"

def fetch_text(url: str) -> list[str]:
    html = requests.get(url, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1") or soup.title
    yield (title.get_text(strip=True) if title else "Joint Statement")
    for p in soup.select("article p"):
        txt = p.get_text(separator=" ", strip=True)
        if txt:
            yield txt

def write_pdf(lines: list[str], path: str) -> None:
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    c = canvas.Canvas(path, pagesize=letter)
    w, h = letter
    margin, leading = 72, 14
    x, y = margin, h - margin
    c.setFont("STSong-Light", 11)
    wrap = textwrap.TextWrapper(width=90, break_long_words=False)
    for raw in lines:
        for line in wrap.wrap(raw):
            if y <= margin:
                c.showPage()
                c.setFont("STSong-Light", 11)
                y = h - margin
            c.drawString(x, y, line)
            y -= leading
        y -= leading
    c.save()

def main() -> None:
    lines = list(fetch_text(URL))
    write_pdf(lines, OUT)
    print(f"saved -> {OUT}")

if __name__ == "__main__":
    sys.exit(main())