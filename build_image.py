"""news-image-20261124, Tue 24 Nov 2026 — make.fun bounty entry.
36 stories, all dated Tue 24 Nov 2026 (happened or first reported);
other days' news appears only in the DATE CHECK box. Korea's $375,000
AI-cheat bounty is excluded: announced Mon 23 Nov.
Deterministic, offline, Pillow only. 1024x1024.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (253, 246, 227)
INK = (17, 17, 17)
RED = (185, 28, 28)
NAVY = (20, 40, 80)
GREY = (90, 90, 90)

def font(name, size):
    paths = {
        "serif_b": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "serif": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "sans_b": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "sans": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    }
    try:
        return ImageFont.truetype(paths[name], size)
    except Exception:
        return ImageFont.load_default()

def wrap(d, text, f, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def text_block(d, x, y, text, f, fill, max_w, max_lines=3, lh=None):
    lh = lh or int(f.size * 1.25)
    lines = wrap(d, text, f, max_w)[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# --- top strip ---
d.rectangle([0, 0, W, 22], fill=NAVY)
d.text((12, 4), "THE WORLD IN ONE DAY", font=font("sans_b", 11), fill=(255, 255, 255))
d.text((W-12, 4), "36 STORIES  •  6 REGIONS  •  EVERY ONE DATED TUESDAY 24 NOVEMBER 2026", font=font("sans_b", 11), fill=(255, 255, 255), anchor="ra")

# --- headline ---
d.text((512, 30), "Tuesday 24 November 2026", font=font("serif_b", 44), fill=INK, anchor="ma")
d.text((512, 80), "HUAWEI GUILTY ON 10 OF 12 COUNTS", font=font("serif_b", 28), fill=RED, anchor="ma")
d.text((512, 114), "US jury convicts on trade secrets and sanctions  •  IRGC says four tankers mined in Hormuz  •  Senegal win Africa Cup back in court", font=font("serif", 12), fill=INK, anchor="ma")
d.line([24, 136, 1000, 136], fill=INK, width=2)

# --- numbers strip ---
nums = [("10/12", "Huawei counts guilty"), ("4", "tankers hit in Hormuz"), ("~60", "Patriot missiles delayed"), ("103.3", "US consumer confidence"), ("5.6", "Nepal quake magnitude"), ("272", "meningitis cases, Gaza")]
x = 24
for n, lab in nums:
    d.text((x+78, 144), n, font=font("sans_b", 20), fill=RED, anchor="ma")
    d.text((x+78, 168), lab, font=font("sans", 9), fill=GREY, anchor="ma")
    x += 163
d.line([24, 186, 1000, 186], fill=INK, width=1)

# --- UTC timeline strip ---
d.rectangle([24, 194, 1000, 224], fill=NAVY)
d.text((36, 200), "UTC TIMELINE:", font=font("sans_b", 11), fill=(255, 220, 0))
d.text((150, 200), "00:00 Hormuz tankers  •  00:52 Megaspeed listed  •  02:09 El Chapo Isidro  •  08:14 Sparta II", font=font("sans", 10), fill=(255, 255, 255))
d.text((150, 212), "11:40 Hamas security chief killed  •  14:27 Riyadh tower hit  •  20:41 Huawei verdict", font=font("sans", 10), fill=(255, 255, 255))

# --- region bar ---
d.rectangle([24, 230, 1000, 248], fill=NAVY)
d.text((512, 233), "EUROPE 9    •    AMERICAS 7    •    ASIA-PACIFIC 8    •    MIDDLE EAST 6    •    AFRICA 3    •    WORLD 3", font=font("sans_b", 10), fill=(255, 255, 255), anchor="ma")

# --- 3 lead stories ---
leads = [
    ("1  BROOKLYN, USA  •  LAW  •  CONFIRMED", "Huawei guilty on 10 of 12 counts", "Federal jury convicts on trade-secret theft, bank and wire fraud, money laundering and sanctions over Iran business. Acquitted on racketeering. Sentencing Sep 2027. (Reuters)", (20, 40, 80)),
    ("2  STRAIT OF HORMUZ  •  WAR  •  IRGC CLAIM", "Four tankers mined, IRGC says", "IRGC claims three tankers hit sea mines and burned, then a fourth; Tehran orders the strait closed in stages. Maritime centre: claims unverified. (IRNA / JMIC)", (20, 40, 80)),
    ("3  CAS, LAUSANNE  •  SPORT  •  CONFIRMED", "Senegal win Africa Cup back in court", "CAS restores Senegal's title after CAF stripped it following the chaotic January final and gave it to Morocco. Morocco plans to appeal. (Reuters / AP)", (20, 40, 80)),
]
y0 = 256
for i, (kicker, head, body, bg) in enumerate(leads):
    x = 24 + i*324
    d.rectangle([x, y0, x+308, y0+62], fill=bg)
    if i == 0:  # gavel + GUILTY stamp
        d.rectangle([x+110, y0+14, x+200, y0+26], fill=(150, 110, 60))
        d.rectangle([x+150, y0+26, x+160, y0+52], fill=(150, 110, 60))
        d.rectangle([x+120, y0+52, x+190, y0+58], fill=(120, 90, 50))
        d.text((x+154, y0+30), "10/12", font=font("sans_b", 13), fill=(255, 255, 255), anchor="ma")
        d.text((x+154, y0+8), "GUILTY", font=font("sans_b", 10), fill=(255, 220, 0), anchor="ma")
    elif i == 1:  # strait + burning tankers
        d.rectangle([x, y0+34, x+308, y0+62], fill=(30, 90, 130))
        for bx in (30, 130, 230):
            d.rectangle([x+bx, y0+40, x+bx+50, y0+52], fill=(60, 60, 60))
            d.polygon([(x+bx+20, y0+40), (x+bx+26, y0+22), (x+bx+32, y0+40)], fill=(255, 120, 0))
            d.polygon([(x+bx+30, y0+40), (x+bx+36, y0+28), (x+bx+42, y0+40)], fill=(255, 200, 0))
    else:  # trophy + gavel
        d.polygon([(x+130, y0+12), (x+180, y0+12), (x+170, y0+34), (x+140, y0+34)], fill=(255, 200, 0))
        d.rectangle([x+148, y0+34, x+162, y0+50], fill=(255, 200, 0))
        d.rectangle([x+128, y0+50, x+182, y0+56], fill=(255, 200, 0))
        d.text((x+154, y0+16), "AFCON", font=font("sans_b", 9), fill=INK, anchor="ma")
        for sx in (40, 90, 240, 280):
            d.ellipse([x+sx, y0+14, x+sx+5, y0+19], fill=(255, 255, 255))
    d.text((x, y0+68), kicker, font=font("sans_b", 9), fill=RED)
    yy = text_block(d, x, y0+84, head, font("sans_b", 15), INK, 308, 2, 18)
    text_block(d, x, yy+2, body, font("sans", 10), (60, 60, 60), 308, 3, 13)

# --- 13 small cards, 5 x 3 (last row 3) ---
cards = [
    ("4  ZAPORIZHZHIA", "Russia strikes kill 2, injure 40", "Overnight attack hits homes and a 5-storey block; 4 children hurt. (Reuters)"),
    ("5  POLAND", "Russian drone enters Polish airspace", "Tracked during strikes on western Ukraine; Warsaw says likely deliberate. (Reuters)"),
    ("6  MOSCOW", "Putin: retaliation 'inevitable'", "Says Ukraine keeps hitting refineries despite Trump's call for restraint. (Reuters)"),
    ("7  WASHINGTON", "US delays ~60 Patriot missiles", "Defence chief has not approved the allocated transfers. (FT)"),
    ("8  LONDON", "UK warns Ukraine suppliers on sabotage", "MoD and MI5: supply chains at risk of proxy arson attacks. (Reuters)"),
    ("9  PARIS", "Sarkozy and Bruni face bribery trial", "Judge orders trial over witness-tampering in Libya funds case; 11 defendants. (Le Monde)"),
    ("10  HAMBACH, FR", "BYD in talks to buy Ineos plant", "First European car factory buy by a Chinese carmaker. (Reuters)"),
    ("11  BRUSSELS", "EU adopts Autumn Package 2027", "Fiscal guidance for 2027; 11 euro states warned on spending rules. (EU Commission)"),
    ("12  GULF OF FINLAND", "Ukraine hits Russian freighter Sparta II", "Kyiv claims drone strike; ship towed to Russian port, 16 crew evacuated. (Reports)"),
    ("13  CARTAGENA", "Gunmen hold 25 hostage in supermarket", "Masked gang seizes shoppers after failed armoured-truck robbery. (AP)"),
    ("14  VILLAVICENCIO", "Car bomb injures 23 in Colombia", "Blast outside regional offices on Monday night; president blames narcoterror. (Reports)"),
    ("15  WASHINGTON", "US consumer confidence jumps to 103.3", "Highest since Jan 2025, driven by jobs optimism after midterms. (Reuters)"),
    ("16  WASHINGTON ST.", "Three H5N1 cases, one death", "Dairy workers in Yakima County; WHO: no human-to-human spread seen. (Reuters/WHO)"),
]
y1 = 448
for idx, (kicker, head, body) in enumerate(cards):
    row, col = divmod(idx, 5)
    x = 24 + col*196
    y = y1 + row*88
    d.rectangle([x, y, x+186, y+80], fill=(255, 255, 255), outline=(200, 190, 170))
    d.rectangle([x, y, x+186, y+15], fill=NAVY)
    d.text((x+6, y+2), kicker, font=font("sans_b", 8), fill=(255, 255, 255))
    text_block(d, x+6, y+19, head, font("sans_b", 11), INK, 174, 2, 13)
    text_block(d, x+6, y+45, body, font("sans", 9), (70, 70, 70), 174, 2, 11)

# --- also list, 20 more, two columns ---
y2 = 720
d.text((24, y2), "ALSO ON TUESDAY 24 NOVEMBER  —  20 MORE STORIES", font=font("sans_b", 11), fill=RED)
d.line([24, y2+16, 1000, y2+16], fill=RED, width=1)
also_left = [
    "17  Abrego Garcia leaves US voluntarily for Spain",
    "18  US drone helped catch El Chapo Isidro",
    "19  Brazil Congress passes Lula fiscal package",
    "20  Bukele: 3 Salvadoran troops killed in Haiti",
    "21  Russian jet nears Ulleung; Seoul scrambles F-15Ks",
    "22  China probes Politburo member Chen Jining",
    "23  China extends gallium export pause to Jan 2027",
    "24  Shenzhou-24 crew named, incl. first Pakistani",
    "25  Nepal quake 5.6 shakes east near Tibet border",
    "26  BBC: China-linked AI fakes target Taiwan vote",
]
also_right = [
    "27  Indonesia charges ex-police chief Listyo Sigit",
    "28  IRGC claims container ship hit in Hormuz",
    "29  Riyadh PIF tower hit by drone, 11 injured",
    "30  Houthis 60 km from Aden, Yemen army says",
    "31  Israel kills Hamas internal security chief",
    "32  Gaza warns of meningitis epidemic, 272 cases",
    "33  Congo searches for missing cargo plane",
    "34  Nigeria's Tinubu asks to cut 2026 budget",
    "35  US puts Megaspeed on Entity List",
    "36  US readies new tariffs after Section 301 probe",
]
yy = y2+22
for t in also_left:
    d.text((24, yy), t, font=font("sans", 9), fill=INK)
    yy += 12
yy = y2+22
for t in also_right:
    d.text((512, yy), t, font=font("sans", 9), fill=INK)
    yy += 12

# --- map box + date check ---
y3 = 866
d.rectangle([24, y3, 380, y3+112], fill=(220, 235, 245), outline=NAVY)
d.text((32, y3+4), "WHERE IT HAPPENED — pins match story numbers", font=font("sans_b", 9), fill=NAVY)
d.ellipse([50, y3+30, 150, y3+76], fill=(200, 210, 180))
d.ellipse([170, y3+28, 280, y3+80], fill=(200, 210, 180))
d.ellipse([300, y3+48, 360, y3+90], fill=(200, 210, 180))
for (px, py, n) in [(90, y3+42, "1"), (200, y3+48, "2"), (240, y3+42, "3"), (120, y3+62, "5"), (260, y3+66, "12"), (80, y3+66, "13")]:
    d.ellipse([px-7, py-7, px+7, py+7], fill=RED)
    d.text((px, py), n, font=font("sans_b", 8), fill=(255, 255, 255), anchor="mm")
d.text((32, y3+96), "World map, schematic — drawn in code.", font=font("sans", 8), fill=GREY)

d.rectangle([392, y3, 1000, y3+112], outline=RED, width=2)
d.text((404, y3+6), "DATE CHECK — READ THIS FIRST", font=font("sans_b", 11), fill=RED)
dc = "Every story 1-36 happened or was first reported on Tue 24 Nov 2026 (UTC). Left out as other days' news: Jensen Huang back as Nvidia CEO (Mon 23 Nov), Merkury sinking announcement (Mon 23 Nov; strike pre-dawn Sun 22 Nov), COP31 end (Sun 22 Nov), Myanmar ICJ ruling (Thu 19 Nov), El Chapo arrest & Peru quake (Fri 20 Nov), FIFA Women's World Cup hosts & EU sanctions package (Mon 23 Nov), Shenzhou-24 launch (Wed 25 Nov). Korea's $375,000 AI-cheat bounty was announced Mon 23 Nov, so it is not counted. IRGC tanker claims are labelled as claims, not verified facts."
text_block(d, 404, y3+24, dc, font("sans", 10), INK, 584, 6, 13)

# --- footer ---
d.text((24, 984), "Sources: Reuters, AP, BBC, Bloomberg, Xinhua, EU Commission, WHO, wires 24 Nov. Scenes are drawn illustrations, not photographs.", font=font("sans", 8), fill=GREY)
d.rectangle([0, 996, W, H], fill=NAVY)
d.text((512, 1004), "36 STORIES  •  6 REGIONS  •  TUESDAY 24 NOVEMBER 2026", font=font("sans_b", 10), fill=(255, 255, 255), anchor="ma")

out = Path("/home/hatch/workspace/goals/make-fun-competition-participation/files/news-image-20261124/entry.png")
img.save(out, format="PNG", optimize=True)
print(out, out.stat().st_size)
