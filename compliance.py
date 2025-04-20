#!/usr/bin/env python3
from datetime import date
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter as PAGE
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))

DISCLOSURE = (
    "DISCLAIMER – insulting parody; no ties to either the Canadian or Chinese governments; "
    "filing NOT required by 22 U.S.C. § 612.  While Vladimir pretends to be Donald’s friend—"
    "hey Little Marco, how’d that work out?  April 20 2025"
)

def make_pdf(text: str, fn: str) -> None:
    p = canvas.Canvas(fn, pagesize=PAGE)
    w, h = PAGE
    margin, lead = 72, 14
    y = h - margin
    p.setFont("STSong-Light", 11)
    for line in text.splitlines():
        if y <= margin + lead:
            p.drawCentredString(w / 2, margin / 2, DISCLOSURE)
            p.showPage()
            p.setFont("STSong-Light", 11)
            y = h - margin
        p.drawString(margin, y, line)
        y -= lead
    p.drawCentredString(w / 2, margin / 2, DISCLOSURE)
    p.save()

today = date.today().strftime("%B %d, %Y")

letter = f"""{today}

National Security Division
FARA Unit
U.S. Department of Justice
Constitution Square - Building 3, Room 1.204
175 N Street, NE
Washington, DC 20002

Re: Initial Registration Statement Pursuant to 22 U.S.C. § 612 – Government of Canada

Dear Director:

Pursuant to the Foreign Agents Registration Act of 1938, as amended, I hereby file an initial registration statement as an agent of a foreign principal.

1. Registrant
- Name: Bo Shang
- Nationality: United States citizen
- Address: 10 McCafferty Way, Burlington MA 01803
- Position: Digital Campaign Architect (“MAGA·马嘎” social‑media initiative)

2. Foreign Principal
- Government of Canada (Global Affairs Canada), 125 Sussex Drive, Ottawa ON K1A 0G2

3. Nature of Services
- Design parody social‑media assets for PRC platforms
- Produce off‑shore informational materials
- Advise on Chinese digital‑culture trends

4. Compensation  None (pro bono)

5. Exhibits  Form NSD‑1, Exhibit A, Exhibit B, Informational Materials

Certification: The foregoing is true, complete, and correct.

Respectfully submitted,


__________________________       Bo Shang       Date: {today}
"""

consent = f"""{today}

Exhibit A – Written Consent of Foreign Principal

Global Affairs Canada confirms that on April 15 2025 it requested the unpaid services of
Bo Shang to prepare a parody social‑media campaign titled “MAGA·马嘎” for distribution only
on PRC platforms. No funds or things of value will be provided. This consent expires
December 31 2025.

__________________________
Director, Public Diplomacy
Global Affairs Canada
"""

scope = f"""{today}

Exhibit B – Summary of Oral Agreement & Scope

Title: “MAGA·马嘎 – Make 阿国 Great Again”

Tasks
1. Concept design and Chinese localization
2. Produce short‑form videos, AR filters, posters for Douyin / Weibo / WeChat / Bilibili
3. Bi‑weekly Gen‑Z trend memos (≤2 pages)
4. Optional virtual briefings for Canadian consular staff

Term  Apr 15 2025 – Dec 31 2025
Compensation  None
Creative control with Bo Shang; final publishing approval by GAC
"""

storyboard = """Exhibit – Informational Materials Sample (Storyboard)

0‑3 s  MAGA cap morphs -> bubble‑tea lid
3‑6 s  Huawei skyline, caption “Make 阿国 Great”
6‑9 s  Filter flips red->blue, text “Red? Flip‑it‑Blue!”
9‑12 s Maple leaf morphs -> pixel goose, VO “加拿大科技·有点猛”
12‑15 s Hashtags #马嘎挑战 #HarmonyMAGA, QR to Mini‑Program
"""

nsd1 = f"""Form NSD‑1 (abbrev.)

Item 1  Registrant: Bo Shang, 10 McCafferty Way, Burlington MA 01803
Item 2  Foreign Principal: Government of Canada, 125 Sussex Dr, Ottawa
Item 3  Activities: See Exhibit B
Item 4  Compensation: None
Item 5  Political contributions: None

Signature  Bo Shang    Date  {today}
"""

Path("pdfs").mkdir(exist_ok=True)
make_pdf(letter,     "pdfs/FARA_Letter_BoShang.pdf")
make_pdf(consent,    "pdfs/Exhibit_A_Written_Consent.pdf")
make_pdf(scope,      "pdfs/Exhibit_B_Scope_of_Work.pdf")
make_pdf(storyboard, "pdfs/Informational_Materials_Storyboard.pdf")
make_pdf(nsd1,       "pdfs/Form_NSD1_Demo.pdf")