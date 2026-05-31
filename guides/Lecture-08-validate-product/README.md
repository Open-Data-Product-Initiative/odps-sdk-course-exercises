# Lecture 8: Validate, Explain, and Summarize an ODPS Product

This is the first useful SDK workflow: validate a product YAML file, inspect it
with human-readable output, and load lightweight metadata for automation.

## 1. Open the guide folder

```bash
cd guides/Lecture-08-validate-product
```

This folder already contains:

- `product.yaml`: a valid ODPS product.
- `invalid-product.yaml`: an intentionally invalid ODPS product.
- `graph.yaml`: a small ODPG graph you can validate as a second document type.

If you want to create the product file yourself, replace `product.yaml` with:

```bash
cat > product.yaml <<'YAML'
schema: https://opendataproducts.org/v4.0/schema/odps.json
version: "4.0"
product:
  name: Airport Operations Performance
  productID: airport-operations-performance
  visibility: public
  status: production
  type: dataset
  description: Operational data product for monitoring airport turnaround and departure performance.
  valueProposition: Helps operations teams reduce delays and coordinate airport resources.
YAML
```

## 2. Validate the product

```bash
open-data-products validate product.yaml
```

Expected result:

```text
Validation successful!
```

## 3. Validate an invalid product

Run validation against the intentionally broken example:

```bash
open-data-products validate invalid-product.yaml
```

Expected result:

```text
Validation failed
```

The file is valid YAML, but it is missing `productID`, which is required for
this product document.

## 4. Get validation as JSON

```bash
open-data-products validate product.yaml --json
```

Use `--json` when the result is consumed by CI, scripts, or another tool.

## 5. Explain the product

```bash
open-data-products explain product.yaml
```

The explanation is compact and intended for humans, agents, and automation
logs.

## 6. Load machine-readable product metadata

```bash
open-data-products summary product.yaml --json
```

Use `summary` when another system needs structured fields such as `spec`,
`kind`, file size, hash, and document id. Avoid using `explain --json` for
machine parsing because it stores the readable explanation as one prose string.

## 7. Load a lightweight product summary

```bash
open-data-products summary product.yaml
```

Summary output gives file-level metadata such as detected spec, kind, size,
and hash. It does not return the full document body.

## 8. List references

```bash
open-data-products refs product.yaml --json
```

For this simple product there may be no references. In larger ODPS, ODPC, and
ODPG files, this helps discover linked artifacts.

## 9. Validate the graph

```bash
open-data-products validate graph.yaml --json
```

The SDK detects this as an ODPG graph document and validates it separately from
the ODPS product file.

## 10. Explain the graph

```bash
open-data-products explain graph.yaml
```

This output includes the graph identity, node count, edge count, node types,
relationship types, and how many node references were discovered.

Expected result:

```text
File: graph.yaml
Schema: https://opendataproducts.org/odpg-v1.0/schema/odpg.yaml
ODPG version: 1.0
Graph id: GRAPH-AVIATION-001
Graph name: Aviation Data Product Value Graph
Kind: Graph
Nodes: 3
Edges: 2
Node types: BusinessObjective, DataProduct, UseCase
Relationship types: uses, supports
Node references: 3
```

Avoid `--json` for this step unless you are feeding the output into another
program. JSON output is machine-friendly, but the readable explanation is
stored as a string with escaped line breaks.

## 11. Load machine-readable graph metadata

```bash
open-data-products odpg-summary graph.yaml
```

Use this output for automation. It returns structured graph fields such as
`nodeCount`, `edgeCount`, `nodeTypes`, `edgeTypes`, and `confidenceValues`
without requiring another tool to parse the prose explanation.

## What You Learned

- `open-data-products validate` detects the document type.
- The SDK validates ODPS 4.x product files and ODPG graph files.
- Invalid files produce validation errors learners can fix.
- Human-readable output is useful while learning.
- Structured JSON commands are better for automation.
- `explain` gives a readable document overview for products and graphs.
- `summary` gives lightweight file metadata without loading the body into output.
- `odpg-summary` gives structured graph counts and type distributions.
- `refs` helps discover `$ref` and `ref` links.

## Next Lesson

Continue to [Guide 2: Use the ODPV Vocabulary Helpers](../Lecture-09-use-vocabulary-helpers/).
