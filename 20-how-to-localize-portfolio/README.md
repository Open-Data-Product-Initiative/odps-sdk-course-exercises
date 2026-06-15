# Lecture 20: How to Localize a Portfolio

Portfolio localization creates translated static HTML review pages for regional
stakeholders. It does not change the canonical ODPC, ODPS, or ODPG YAML files.

Use this lesson after you have a working portfolio workspace from the previous
lessons.

## 1. Start From A Rendered Portfolio

You need a portfolio workspace with a current `index.html`:

```bash
ls portfolio/index.html
```

If the page does not exist yet, render it from the current YAML artifacts:

```bash
open-data-products portfolio render portfolio/
```

## 2. Choose Target Languages

`portfolio localize` accepts BCP 47 language tags. Start with one or two
languages while learning the workflow:

```text
fi   Finnish
sv   Swedish
ar   Arabic
vi   Vietnamese
```

Arabic is useful for checking right-to-left page rendering. Finnish and Swedish
are useful for Nordic stakeholder review examples.

## 3. Run Localization

Use a configured LLM provider to translate the visible HTML strings:

```bash
open-data-products portfolio localize portfolio/ \
  --languages "fi,sv" \
  --provider claude \
  --model claude-sonnet-4-5
```

The command reads the existing portfolio HTML, translates human-facing text,
and writes localized pages beside the main `index.html`.

## 4. Review The Outputs

Check that the localized pages and translation file exist:

```bash
ls portfolio/index.fi.html
ls portfolio/index.sv.html
ls portfolio/portfolio-i18n.yaml
```

The common outputs are:

- `portfolio/index.fi.html`
- `portfolio/index.sv.html`
- `portfolio/index.ar.html`
- `portfolio/index.vi.html`
- `portfolio/portfolio-i18n.yaml`

`portfolio-i18n.yaml` stores the translated strings used to render localized
HTML pages. It is generated from the portfolio view, not from editing the
canonical YAML artifacts.

## 5. Open The Localized Pages

Open the localized HTML files in a browser:

```text
portfolio/index.fi.html
portfolio/index.sv.html
```

Review the overview, artifact panels, product cards, graph labels, and about
section. The goal is not only translation quality; reviewers should confirm
that the page still works as a portfolio review artifact.

## 6. Keep YAML As The Source Of Truth

Localization is for human-facing review pages. The canonical files remain:

```text
portfolio/portfolio.yaml
portfolio/odpc/catalog.yaml
portfolio/odpc/fragments/*.yaml
portfolio/odpg/graph.yaml
portfolio/odps/products/*.yaml
```

Agents, scripts, validation commands, and version control should keep using
those YAML files as the source of truth.

## 7. Troubleshooting

If localization takes too long with a local model, try fewer languages first:

```bash
open-data-products portfolio localize portfolio/ \
  --languages "fi" \
  --provider ollama \
  --model qwen2.5
```

If a command pasted into `zsh` behaves strangely, check that every line
continuation backslash is the final character on its line. A space after `\`
breaks the command.

If automation should fail on validation issues, add `--strict-validation`:

```bash
open-data-products portfolio localize portfolio/ \
  --languages "fi,sv" \
  --provider claude \
  --model claude-sonnet-4-5 \
  --strict-validation
```

## What You Learned

- `portfolio localize` creates translated static HTML review pages.
- Localization leaves ODPC, ODPS, and ODPG YAML artifacts unchanged.
- `portfolio-i18n.yaml` stores translated page strings.
- BCP 47 tags such as `fi`, `sv`, `ar`, and `vi` select target languages.
- Local models can work, but hosted providers are often better for longer
  multilingual review pages.

## Next Lesson

Continue to
[Lecture 21: Final review: human view and agent-ready YAML](../21-final-review-human-view-and-agent-ready-yaml/).
