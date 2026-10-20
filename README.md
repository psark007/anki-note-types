# Anki note types

A collection of Anki note types that I use for technical (or otherwise) study. Each folder contains its front and back templates, styling, and a short README.

- **Markdown + KaTeX (Basic)** — standard question and answer fields: `Front`, `Back`.
- **Markdown + KaTeX (Cloze)** — native cloze fields: `Text`, `Back Extra`.
- **Markdown + KaTeX (Programming)** — question and answer fields: `Front`, `Back`; includes a scratchpad on the question side.

## Install

These are template source files, not an `.apkg` package. In Anki, open **Tools → Manage Note Types** and add a note type. Add the fields in the order shown above, then open **Cards…** and copy `front.html` and `back.html` into the matching template boxes and `style.css` into Styling. For the Cloze model, start with Anki's built-in **Cloze** note type so cloze deletions work correctly, then apply the supplied fields and templates.

## Create and install an `.apkg`

To make a package, create a deck with notes using the desired note type, then choose **File → Export**, select that deck, and export as an **Anki Deck Package (`.apkg`)**. Include only cards you intend to share. To install a package, open **File → Import** in Anki and select the `.apkg`; its note type is imported along with its cards.

The templates load Markdown-it, KaTeX, highlight.js, markdown-it-mark, and KaTeX mhchem from their configured local-media paths or CDN fallbacks. Rendering may need an internet connection when local copies are not installed.

These work for me with Anki installed as a FlatPak on Fedora. Also seems to work just fine on AnkiDroid.
