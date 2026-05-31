# Guide 1: Validate, Explain, and Summarize an ODPS Product

This is the first useful SDK workflow: validate a product YAML file, inspect it
with human-readable output, and load lightweight metadata for automation.

## 1. Open the guide folder

```bash
cd guides/Lecture-07-validate-product
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

## 6. Get the explanation as JSON

```bash
open-data-products explain product.yaml --json
```

Use this form when another system needs to read the result.

## 7. Load a lightweight summary

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

## What You Learned

- `open-data-products validate` detects the document type.
- The SDK validates ODPS 4.x product files and ODPG graph files.
- Invalid files produce validation errors learners can fix.
- Human-readable output is useful while learning.
- JSON output is better for automation.
- `explain` gives a readable document overview.
- `summary` gives lightweight metadata without loading the body into output.
- `refs` helps discover `$ref` and `ref` links.

## Next Lesson

Continue to [Guide 2: Use the ODPV Vocabulary Helpers](../Lecture-09-use-vocabulary-helpers/).
