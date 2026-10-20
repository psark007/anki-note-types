#!/usr/bin/env python3
"""Build example .apkg files from the note type templates in this repository."""

from pathlib import Path

import genanki


ROOT = Path(__file__).resolve().parents[1]
NOTE_TYPES = ROOT / "note-types"
OUTPUT = ROOT / "dist"


def model(slug, model_id, name, fields, *, cloze=False):
    directory = NOTE_TYPES / slug
    return genanki.Model(
        model_id,
        name,
        fields=[{"name": field} for field in fields],
        templates=[{
            "name": "Card 1",
            "qfmt": (directory / "front.html").read_text(encoding="utf-8"),
            "afmt": (directory / "back.html").read_text(encoding="utf-8"),
        }],
        css=(directory / "style.css").read_text(encoding="utf-8"),
        **({"model_type": genanki.Model.CLOZE} if cloze else {}),
    )


def main():
    OUTPUT.mkdir(exist_ok=True)

    basic = model(
        "markdown-katex-basic", 2071834101,
        "Markdown + KaTeX (Basic)", ["Front", "Back"],
    )
    cloze = model(
        "markdown-katex-cloze", 2071834103,
        "Markdown + KaTeX (Cloze)", ["Text", "Back Extra"], cloze=True,
    )
    deck = genanki.Deck(2071834102, "Markdown + KaTeX — Basic and Cloze")
    deck.add_note(genanki.Note(basic, [
        "## Pythagorean theorem\n\nWhat is the length of the hypotenuse if the legs are 3 and 4?",
        "By $a^2+b^2=c^2$, the hypotenuse is $c=5$.\n\n- Square each leg\n- Add the results\n- Take the square root",
    ]))
    deck.add_note(genanki.Note(cloze, [
        "The derivative of $x^2$ is {{c1::$2x$}}.",
        "Apply the power rule: $\\frac{d}{dx}x^n=nx^{n-1}$.",
    ]))
    genanki.Package(deck).write_to_file(OUTPUT / "markdown-katex-basic-cloze.apkg")

    programming = model(
        "markdown-katex-programming", 2071834105,
        "Markdown + KaTeX (Programming)", ["Front", "Back"],
    )
    deck = genanki.Deck(2071834106, "Markdown + KaTeX — Programming")
    deck.add_note(genanki.Note(programming, [
        "## Sum a list\n\nWrite a Python function that returns the sum of a list of numbers.",
        "```python\ndef total(values):\n    return sum(values)\n```\n\nFor $[1,2,3]$, the result is $6$.",
    ]))
    genanki.Package(deck).write_to_file(OUTPUT / "markdown-katex-programming.apkg")


if __name__ == "__main__":
    main()
