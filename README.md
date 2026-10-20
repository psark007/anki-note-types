# Anki note types

A collection of Anki note types that I use for technical (or otherwise) study. Each folder contains its front and back templates, styling, and a short README.

- **Markdown + KaTeX (Basic)** — standard question and answer fields: `Front`, `Back`.
- **Markdown + KaTeX (Cloze)** — native cloze fields: `Text`, `Back Extra`.
- **Markdown + KaTeX (Programming)** — question and answer fields: `Front`, `Back`; includes a scratchpad on the question side.

## Install

### Build and install `.apkg` packages

Install the build dependency and run the script:

```sh
python -m pip install -r requirements.txt
python scripts/build_packages.py
```

The two example packages are written to `dist/` and contain only synthetic demo cards. To install one, choose **File → Import** in Anki and select the `.apkg`; its note type and example cards are imported together.

### Manual installation

Alternatively, create the note type in Anki and copy in the template files:

1. Open **Tools → Manage Note Types** and add a note type. For Cloze, choose Anki's built-in **Cloze** type.
2. Add the fields in the order listed above.
3. Select the type, click **Cards…**, and paste `front.html` into Front Template, `back.html` into Back Template, and `style.css` into Styling. Find these files in the matching `note-types/` folder.

The templates load Markdown-it, KaTeX, highlight.js, markdown-it-mark, and KaTeX mhchem from their configured local-media paths or CDN fallbacks. Rendering may need an internet connection when local copies are not installed.

These work for me with Anki installed as a FlatPak on Fedora. Also seems to work just fine on AnkiDroid.
