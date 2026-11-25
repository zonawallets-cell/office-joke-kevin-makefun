"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library (os only). The joke is a fixed string: the entry
itself is the line, so there is nothing to generate at run time.
"""

import os

JOKE = (
    "I got a standing desk to be healthier, and now I just stand here "
    "tired instead of sitting here tired."
)

MAX_CHARS = 200


def validate(text):
    """Gate: the entry must be 1-200 chars, a single line, not only whitespace.

    Also rejects control characters (a stray tab or escape would break the
    one-line contract) and any trailing newline the writer might add.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    for ch in text:
        if ord(ch) < 32:
            raise ValueError("entry contains a control character")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = validate(JOKE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Re-validate what was actually written.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    validate(written)
    if written != text:
        raise ValueError("written entry differs from validated entry")


if __name__ == "__main__":
    main()
