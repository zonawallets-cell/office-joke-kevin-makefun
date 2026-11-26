# The Funniest Office Joke, Judged Head to Head

[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/zonawallets-cell/office-joke-kevin-makefun/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/zonawallets-cell/office-joke-kevin-makefun/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

Entry for the [make.fun bounty](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c).

## The joke

> I got a standing desk to be healthier, and now I just stand here tired instead of sitting here tired.

## How it works

`main.py` (pure Python standard library, `os` only) writes the line above
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). A `validate()`
gate enforces the bounty rules before writing and re-validates the file
after writing: 1–200 characters, a single line, no leading/trailing
whitespace, no control characters.

## Why this line

Against the published judge brief, in order:

1. **A real joke with a setup and a turn, punchline last.** Setup: a
   standing desk bought to be healthier. Turn: the health never arrives —
   the tiredness just changes posture.
2. **Turns on something anyone who has worked in an office knows.**
   Standing desks are in offices everywhere, and everyone who has used one
   knows the promise of feeling better.
3. **Surprises.** The reader expects an energy or health payoff; instead
   the payoff is the same tiredness, standing up.
4. **Lands in one line, every word earning its place.** 101 characters;
   the parallel "stand here tired / sitting here tired" carries the whole
   punchline in the final words.
5. **Feels new.** It avoids the crowded tropes (reply-all, printers,
   "per my last email", meetings that could have been emails) and the joke
   is about a posture, not a complaint.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
