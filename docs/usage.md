# Usage

The README covers the basics. This page collects the
longer examples and the notes that did not fit up front.

## Basic

```bash
chatsh explain this error < error.log
cat diff.patch | chatsh review this diff
```

## Notes

- Streams tokens as they arrive
- Model and system prompt via flags or env
