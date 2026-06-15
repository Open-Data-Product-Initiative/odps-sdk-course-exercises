# Lecture 7: Installing and Running the SDK

This lesson gets a clean local SDK workspace ready, creates a Python virtual
environment, installs the SDK, and runs the first simple command.

This is the local terminal setup path. The Colab workflow is handled separately
in the course notebooks.

## 1. Create The Course Workspace

```bash
mkdir odps-sdk-course
cd odps-sdk-course
python3 -m venv .venv-sdk
source .venv-sdk/bin/activate
```

On Windows PowerShell, activate the environment with:

```bash
.venv-sdk\Scripts\Activate.ps1
```

After activation, your terminal prompt should show that `.venv-sdk` is active.

## 2. Install The SDK

Install the SDK inside the virtual environment:

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade open-data-products
```

Using `python -m pip` keeps the install tied to the active virtual environment.

## 3. Check The SDK Command

```bash
open-data-products --help
```

You should see the main command groups for validation, generation, ODPC, ODPG,
ODPV, and portfolio workflows.

You can also check the installed version:

```bash
open-data-products --version
```

## 4. Run A Simple JSON Command

```bash
open-data-products manifest --json
```

The manifest output is a machine-readable description of the SDK surface.

## 5. Keep The Folder Shape

The rest of the course uses this practical structure:

```text
source_docs/
fragments/
catalogs/
graphs/
portfolio/
reports/
```

You can create a separate lesson folder later when you want to keep one
exercise isolated.

When you return to this course later, open the same folder and reactivate the
virtual environment before running SDK commands:

```bash
cd odps-sdk-course
source .venv-sdk/bin/activate
```

## What You Learned

- A virtual environment keeps the course install separate from other Python
  projects.
- The SDK package name is `open-data-products`.
- The SDK command is `open-data-products`.
- `--help` shows the available workflows.
- `manifest --json` proves the package imports and the CLI can render
  machine-readable output.
- The course workspace separates source material, generated fragments,
  catalogs, graphs, portfolio outputs, and reports.

## Next Lesson

Continue to
[Lecture 8: Validating and explaining standards files](../08-validating-and-explaining-standards-files/).
