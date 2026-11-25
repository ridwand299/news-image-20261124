# Sum up 24 November's world news in one image

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/ridwand299/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/ridwand299/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A one-page newspaper front page summing up Tuesday 24 November 2026 in
36 stories, drawn entirely in code with Pillow. No photographs: every
scene is a drawn illustration.

## The image

`entry.png` (1024x1024, RGB) is rendered by `build_image.py` and copied
to `/output/entry.png` by `main.py`. Two runs produce byte-identical
output.

- **Lead stories:** a US jury convicts Huawei on 10 of 12 counts;
  the IRGC says four tankers were mined in the Strait of Hormuz
  (labelled as a claim, not a verified fact); CAS restores Senegal's
  Africa Cup title.
- **Format:** numbers strip, UTC timeline, 13 small cards, 20 more
  stories in the "Also on Tuesday" list, a schematic world map with
  numbered pins, and a DATE CHECK box.
- **Date discipline:** every story 1–36 happened or was first reported
  on Tue 24 Nov 2026 (UTC). Stories from other days are named in the
  DATE CHECK box and kept out of the count — including Jensen Huang's
  return as Nvidia CEO (Mon 23 Nov), the Merkury sinking announcement
  (Mon 23 Nov), the COP31 end (Sun 22 Nov), the Myanmar ICJ ruling
  (Thu 19 Nov), and Korea's $375,000 AI-cheat bounty (announced Mon
  23 Nov).

## Run it

```sh
python3 build_image.py   # renders entry.png
python3 main.py          # copies entry.png to /output/entry.png
```

Requires Python 3.13 and Pillow (`pip install pillow`).

## Sources

Reuters, AP, BBC, Bloomberg, Xinhua, European Commission, WHO, and
wire reports dated 24 Nov 2026.

## License

MIT — see `LICENSE`.
