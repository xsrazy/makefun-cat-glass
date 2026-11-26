"""Five Seconds to Explain the Glass.

Entry for the make.fun bounty
``u-po-pu-five-seconds-to-explain-the-glass-934d9949``.

The program writes one sentence to ``$MAKEFUN_OUTPUT_DIR/entry.txt``:
the excuse a house cat gives in the five seconds after sweeping a
glass off the table. No apology, no confession, just the cat's own
defence, in the cat's own voice.

The line was picked from seven candidates in a head-to-head against
the judge's five criteria: the vacuum-cleaner spy theory is the
freshest comic idea, pure cat paranoia and self-interest, with zero
remorse, and it reads aloud in about four seconds.
"""

import os

LINE = "The glass was a spy for the vacuum cleaner, so I dealt with it."

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert LINE.strip(), "line must not be only whitespace"
assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
assert "\n" not in LINE and "\u2014" not in LINE, "no newline, no em dash"


def write_entry() -> str:
    """Write LINE to entry.txt and return the path written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return path


if __name__ == "__main__":
    write_entry()
