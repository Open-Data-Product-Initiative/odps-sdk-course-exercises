# Guide 0: Set Up Python for Beginners

This guide helps you install Python, create a clean project environment, and
install the Open Data Products SDK before starting the course exercises.

## 1. Check whether Python is already installed

Open Terminal, PowerShell, or Command Prompt and run:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

You should see a version number such as:

```text
Python 3.12.4
```

If you see an error, install Python in the next step.

## 2. Install Python

Use one of these options:

- Windows: install Python from https://www.python.org/downloads/windows/
- macOS: install Python from https://www.python.org/downloads/macos/
- Linux: use your package manager, such as `apt`, `dnf`, or `brew`

On Windows, enable the option that adds Python to `PATH` during installation.
This makes the `python` command available in your terminal.

## 3. Create a course folder

```bash
mkdir odps-sdk-course
cd odps-sdk-course
```

This dedicated folder keeps the SDK work separate from your other Python
projects. You will use it for the installation, test commands, and later
course exercises.

## 4. Create a virtual environment

```bash
python3 -m venv .venv-sdk
```

If your computer uses `python`, run:

```bash
python -m venv .venv-sdk
```

A virtual environment gives this project its own Python package space. That
means SDK packages and dependencies do not interfere with other projects on
your machine.

## 5. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv-sdk\Scripts\Activate.ps1
```

On Windows Command Prompt:

```bat
.\.venv-sdk\Scripts\activate.bat
```

On macOS or Linux:

```bash
source .venv-sdk/bin/activate
```

After activation, your terminal prompt usually starts with `(.venv-sdk)`.

## 6. Upgrade `pip`

```bash
python -m pip install --upgrade pip
```

`pip` is Python's package installer. Keeping it current avoids many beginner
installation problems.

## 7. Install the SDK

```bash
pip install open-data-products
```

## 8. Run a smoke test

```bash
open-data-products --help
```

You should see the SDK command help. If you do, Python and the SDK are ready for
the course exercises.

## What You Learned

- How to check whether Python is installed.
- How to install Python if it is missing.
- How to create and activate a virtual environment.
- How to install the Open Data Products SDK.
- How to confirm the SDK command works.

## Next Lesson

Continue to [Lecture 8: Validate, Explain, and Summarize an ODPS Product](../Lecture-08-validate-product/).
