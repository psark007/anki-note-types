# Anki note types

Custom Anki note types for technical study. Each folder contains its front and back templates, styling, and a short README.

- **Markdown + KaTeX (Basic)** — standard question and answer fields: `Front`, `Back`.
- **Markdown + KaTeX (Cloze)** — native cloze fields: `Text`, `Back Extra`.
- **Markdown + KaTeX (Programming)** — question and answer fields: `Front`, `Back`; includes a scratchpad on the question side.

## Install

These are template source files, not an `.apkg` package. In Anki, open **Tools → Manage Note Types** and add a note type. Add the fields in the order shown above, then open **Cards…** and copy `front.html` and `back.html` into the matching template boxes and `style.css` into Styling. For the Cloze model, start with Anki's built-in **Cloze** note type so cloze deletions work correctly, then apply the supplied fields and templates.

The templates load Markdown-it, KaTeX, highlight.js, markdown-it-mark, and KaTeX mhchem from their configured local-media paths or CDN fallbacks. Rendering may need an internet connection when local copies are not installed. Compatibility has only been inspected in Anki 26.09.3 on Linux; other versions and mobile clients have not been verified.
