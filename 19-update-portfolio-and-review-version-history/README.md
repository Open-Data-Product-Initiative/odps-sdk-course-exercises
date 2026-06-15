# Lecture 19: Update the Portfolio and Review Version History

A portfolio is a living artifact. Source material changes, new signals appear,
and product drafts improve over time. This lesson shows how to refresh a
workspace and review previous versions.

## 1. Add Or Change Source Material

Add a new file to one saved source lane:

```bash
cat > source_docs/signals/support-pressure-signal.txt <<'TXT'
Support operations note from April 19, 2026 at 10:15.

Priority accounts with unresolved tickets are waiting longer for first response.
Customer success teams want this signal linked to retention review workflows.
TXT
```

## 2. Refresh Changed Sources

```bash
open-data-products portfolio refresh portfolio/ \
  --provider claude \
  --model claude-sonnet-4-5
```

Refresh scans saved source lanes and sends changed or new source files to the
LLM. Existing unchanged artifacts are preserved where possible.

## 3. Force Full Reprocessing

```bash
open-data-products portfolio refresh portfolio/ \
  --all-sources \
  --provider claude \
  --model claude-sonnet-4-5
```

Use `--all-sources` when the full evidence set should be reprocessed.

## 4. Sync Edited YAML Without An LLM

```bash
open-data-products portfolio sync portfolio/
```

Use sync after directly editing ODPC fragments, ODPS products, or graph YAML.

## 5. Review Version History

```bash
find portfolio/versions -maxdepth 2 -type f | sort
```

Successful builds and refreshes snapshot previous portfolio outputs. The latest
`index.html` includes links to available versions so reviewers can compare
current and previous portfolio pages.

## What You Learned

- Refresh processes changed and new source documents by default.
- `--all-sources` forces full reprocessing.
- `portfolio sync` rebuilds browser output from edited YAML without an LLM.
- Version snapshots support review and governance over time.

## Next Lesson

Continue to
[Lecture 20: How to localize a portfolio](../20-how-to-localize-portfolio/).
