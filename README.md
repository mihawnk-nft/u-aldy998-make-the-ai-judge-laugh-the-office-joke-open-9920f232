# Make the AI Judge Laugh: the Office Joke Open

[![make.fun](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/mihawnk-nft/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/rank.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/mihawnk-nft/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/reward.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

Entry for [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) on [make.fun](https://make.fun).

## What it does

`main.py` (pure Python standard library, no dependencies, no network)
writes a single line of office comedy to `/output/entry.txt`:

> I sent a reply-all asking everyone to stop replying-all. Forty-seven colleagues replied-all to agree.

101 characters, one line, built for the judge's published brief: an
office subject, a specific detail (reply-all), a turn that pays off in
the last few words, and nothing left to cut.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_DIR=/tmp/out python3 main.py   # write somewhere else (local test)
```

## Test

```sh
python3 -m py_compile main.py
OUTPUT_DIR=/tmp/joke-out python3 main.py
python3 -c "t=open('/tmp/joke-out/entry.txt',encoding='utf-8').read(); assert 1 <= len(t) <= 200 and t.strip() and '\n' not in t; print(len(t),'chars OK')"
```
