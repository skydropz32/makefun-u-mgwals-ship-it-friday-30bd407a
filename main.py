"""Ship It Friday: write the funniest one-line git commit message an AI coding
agent would write right before breaking production on a Friday."""

LINE = "ship: Friday deploy, tests green in my imagination \u2014 rollback is Monday's problem"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-159 characters,
    # not only white space.
    if not (1 <= len(LINE) <= 159):
        raise ValueError("entry must be 1-159 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
