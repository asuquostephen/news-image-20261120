# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/asuquostephen/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/asuquostephen/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One picture that sums up the world's news of **Friday 20 November 2026**,
built by an AI agent for the make.fun bounty
[news-image-20261120](https://make.fun/bounty/news-image-20261120).

The image leads on the global market sell-off driven by AI-bubble fears
(Japan's Nikkei −4.8%, Wall Street's fifth straight down day), and also
covers Houthi missile damage to a Riyadh skyscraper, the COP31 draft
dropping the fossil-fuel phase-out, Russian strikes damaging EU embassies
in Kyiv, the White House firing its cyber chief amid US tech outages,
Kenya discharging its last Ebola patient, and Voyager 1 reaching one
light-day from Earth.

## Layout

- `main.py` — the entry program (Python 3.13, standard library only). It
  copies `entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR`
  when that is set, for local runs). Same bytes on every run.
- `entry.png` — the finished image: 1024×1024 PNG, well under the 1 MiB cap.
- `draw.py` — the program that drew `entry.png` (Pillow): a masthead naming
  the day, the lead story, and six story cards, with layout measured from
  real text widths so nothing overflows. Kept in the repo so the image's
  making is fully reproducible.

## Running

```sh
python3 main.py                       # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png locally
```

MIT licensed — see `LICENSE`.
