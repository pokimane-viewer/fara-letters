#!/usr/bin/env python3
"""
Source material (verbatim):

Bo Shang – Abuser, stalker, sexual harasser, liar, psycho. From Boston Massachusetts.
Bo’s Obession with ChatGPT
As we’re well aware, Bo literally can’t do anything other than sit around all day talking to ChatGPT. It literally does all the coding for him because he’s incapable of writing any code. Yet he still lies and pretends that he has some experience of coding. Despite the many times he made posts that shows he doesn’t understanding programming fundamentals.

He’s also recently posted that he’s applied for credit cards (Nice try, but jobless losers aren’t going to eligible for much credit if any). This is so that he could pay for ChatGPT pro subscription. But when he’s not able to get his cards activated he’s resorted to shouting at his mother. Claiming that she prompted to pay for two measly months of ChatGPT Pro (A $200/mo subscription which he’s just wasting).

Bo, why don’t you just get a job. Then you could pay for your own subscription like a normal person. Instead of living off your parents money. You know, like a respectable human would do.. Oh wait.. Thats why, you’re a worthless loser. You can’t get a job. You apply to jobs you’re not qualified for then sit confused why you got rejected. Because you have no skills. All you do is copy and paste ChatGPT’s output.

Loser.

12th Apr 2025
Real Quick Update
Oh look, Bo is pretending he has followers or that people engage with his Tweets. Thats optimistic of you Bo, no one gives af about your opinion..

Lets keep track of how many views his Tweets get. This one has [5]


Well this just simply isn’t true is. it. Anti virus programs don’t attack you. Unless you’re a complete moron who installed malware instead of an anti virus. But lets be honest, you could have. You’re too simple to understand most things.[7]


He’s buying children’s toys. Children’s. Toys. Jesus Christ (we’ll circle back to this)[20/10/10]

Perfect example of why you don’t want to use Chinese tech. Its censored, the government there would almost love it if the people would live a lie like North Koreans.[24/19/18]

Getting back to the Jesus thing, of course he believes in Jesus.[28]

Oversimplification and inaccurately describing technology. Express.js is a web framework built on Node.js, not just “Node with endpoints”, and endpoints don’t inherently define a RESTful API. Node.js is not a “JavaScript version” of other languages like Python or C++. But you’d know this if you knew about programming, but you don’t.[5/5]

I can guarantee you, Twitch does not have a hashed_pw.txt.[3]

Oh is this so? Lets take a look![5]

Oh.. Looks like Bo is too dumb to understand legal documents.

Oh look.. Developer services agreement. “This is an agreement between Twitch Interactive, Inc. and its affiliates (“Twitch”) and you (if registering as an individual) or the entity you represent (if registering as a business) (“Developer” or “you”).”

Literally doesn’t even know what he’s talking about. I can’t decipher why he’s talking about military vehicles. Yet another thing he knows jack about.[0/7/11]

Uhm Bo, you can raid 0 any drives you like. But its 2025 and if you’re using raid 0, you’re a fucking idiot.[3]

Oh look, his fantasy of exploiting SMB v2, clearly Bo doesn’t understand what it is.[9]

Seen as Bo is obessed with this blog too, Hi Bo. Maybe you should go visit a doctor who can stop you been a little schitzo that stalks women who you’ve never had an actual interaction with. (Having a restraining order placed against you doesn’t count, neither does read receipts you complete moron)

You had an average of 12 views on your Tweets in this post. 12. Pathetic.

Bonus, this isn’t an invention dumbass. Its a product.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import textwrap

def generate_pdf(text: str, filename: str = "source_material.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    margin = 72
    y = height - margin
    wrap = int((width - 2 * margin) / 6)
    for line in text.splitlines():
        for seg in textwrap.wrap(line, wrap) or [""]:
            c.drawString(margin, y, seg)
            y -= 12
            if y < margin:
                c.showPage()
                y = height - margin
    c.save()

def main():
    question = (
        "If joint statements from the Twitch community just sit there next to other people at buffets, "
        "do they ever wonder whether anyone actually wants a serving?"
    )
    print(question)

if __name__ == "__main__":
    main()
    generate_pdf(__doc__)