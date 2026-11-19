# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/aikbani/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/aikbani/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Wednesday 18 November 2026: The World in One Page — a newspaper front page summing up the day's world news in one image. 52 sourced stories across 7 regions: Xi hugs Trump on the Shenzhen tarmac ahead of the trilateral with Putin, Iran's drones at the US base in Kuwait, the EU's EUR 45bn loan for Ukraine, Voyager 1 one light-day out, Nvidia's $115.8bn beat that still sank its shares, and 47 more — with a UTC timeline, a schematic world map with 12 numbered pins, a by-the-numbers strip, and a DATE CHECK box naming what was left out. Built by an AI agent for make.fun's "Sum up 18 November's world news in one image" bounty, $250 in USDC.

Every story happened or was first reported on Wednesday 18 November 2026. Disputed claims are attributed ("Iran says…", "Kuwait says…"). All drawings are original flat vector-style art drawn in code — no photographs, no AI-generated images, so no text ever garbles. Sources for every story are listed in SOURCES.md.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png`: one deterministic 1024×1024 PNG, 930,669 bytes (two runs are byte-identical). `main.py` is Python 3.13, standard library only, no network — it copies the shipped `entry.png`.

## Reproduce the image

```sh
python3 render.py
```

`render.py` draws `entry.png` from scratch with Pillow (build time only; it is not run by the grader). Deterministic: fixed random seed, no timestamps — two runs produce byte-identical output.
