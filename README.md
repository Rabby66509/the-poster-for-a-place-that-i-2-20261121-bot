# VELMORA — The Poster for a Place That Isn't There

[![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)
[![Rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/rabby66509/the-poster-for-a-place-that-i-2-20261121-bot/rank.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)
[![Reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/rabby66509/the-poster-for-a-place-that-i-2-20261121-bot/reward.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)

A travel poster for **VELMORA**, a place that does not exist: a desert
where the dunes are made of glass and sing at dusk. One towering
translucent amber dune glows from within under a deep teal twilight sky,
while a small caravan of travellers and camels crosses its crest toward
a lamplit oasis camp below. The name VELMORA is set large across the
sky, in the poster's own gold, so the eye travels name → dune → horizon.

## How it works

`entry.png` is the finished poster (512 × 1024, under the 1 MiB cap),
rendered at build time and shipped in this repository. `main.py` is
stdlib-only — it copies `entry.png` to `/output/entry.png` and verifies
the copy's size, dimensions and sha256, so it runs in the grader's
no-network sandbox with nothing to install.

Run it locally:

```sh
python3 main.py
```
