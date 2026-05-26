# Guide 1: Validate an ODPS Product

This is the first useful SDK workflow: validate a product YAML file and get a
machine-readable result.

## 1. Open the guide folder

```bash
cd guides/01-validate-product
```

This folder already contains:

- `product.yaml`: a valid ODPS product.
- `invalid-product.yaml`: an intentionally invalid ODPS product.

If you want to create the file yourself, replace `product.yaml` with:

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

## 2. Validate the file

```bash
open-data-products validate product.yaml
```

Expected result:

```text
Validation successful!
```

## 3. Validate an invalid file

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

## 4. Get JSON output

```bash
open-data-products validate product.yaml --json
```

Use `--json` when the result is consumed by CI, scripts, or another tool.

## What You Learned

- `open-data-products validate` detects the document type.
- The SDK validates ODPS 4.x product files.
- Invalid files produce validation errors learners can fix.
- Human-readable output is useful while learning.
- JSON output is better for automation.
