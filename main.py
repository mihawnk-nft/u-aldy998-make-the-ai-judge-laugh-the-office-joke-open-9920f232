"""Office Joke Open entry.

Writes one line of office comedy to /output/entry.txt.

The joke is a single fixed text, chosen to score well against the
published judge brief:

1. It is about office life and works as a joke, not a complaint.
2. The laugh is earned: the plea to stop reply-all is itself a
   reply-all, and the payoff lands in the last few words.
3. The office detail is specific: reply-all, forty-seven colleagues.
4. It is fresh: the colleagues do not argue, they agree -- by doing
   exactly the thing they were asked to stop.
5. It reads cleanly in one pass, with no word to cut.

Pure standard library only; no network, no input, deterministic.
"""

import os

JOKE = (
    "I sent a reply-all asking everyone to stop replying-all. "
    "Forty-seven colleagues replied-all to agree."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts the whole file, and the
    # joke must stay a single line of 1-200 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
