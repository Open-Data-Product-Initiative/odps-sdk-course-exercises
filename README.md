# SDK Course Guides

These short guides are designed for learners who installed the SDK from PyPI:

```bash
pip install open-data-products
```

These exercises are part of the Open Data Products SDK MasterClass on Udemy.
For the full experience, faster progress, and a more complete learning path,
take the course: https://www.udemy.com/course/

If you are new to Python, start with the setup guide before installing the SDK
or running the course exercises.

The first four workflow guides do not use an LLM. They cover validation,
explanation, vocabulary lookup, and graph conversion.

The last four guides use the SDK generation command. They require Ollama with
Qwen 2.5 or a configured online provider.

## Prerequisite Guides

1. [Set up Python for beginners](guides/00-setup-python.md)

## Non-LLM Guides

1. [Validate an ODPS product](guides/01-validate-product.md)
2. [Explain and summarize a product](guides/02-explain-and-summarize.md)
3. [Use the ODPV vocabulary helpers](guides/03-use-vocabulary-helpers.md)
4. [Convert GraphML to ODPG and open an explorer](guides/04-convert-graph-to-odpg.md)

## LLM Generation Guides

1. [Generate one signal fragment with Ollama](guides/05-llm-generate-one-signal.md)
2. [Generate one artifact with an online provider](guides/06-llm-use-online-provider.md)
3. [Generate a full fragment set from source documents](guides/07-llm-generate-fragment-set.md)
4. [Full cycle: source docs to catalog HTML and graph explorer](guides/08-llm-full-cycle-catalog-and-graph.md)
