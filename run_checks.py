#!/usr/bin/env python3
"""Run all project checks: lint, type check, and tests.

Usage:
    python -m pytest --strict-config tests/  # Run tests
    ruff check .                              # Lint with Ruff
    ty check .                                # Type check with Ty
"""


def main() -> None:
    import subprocess
    import sys

    results = {"test": True, "lint": True, "typecheck": True}

    # Run tests
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "--strict-config", "tests/", "-v"],
        capture_output=True, text=True,
    )
    results["test"] = result.returncode == 0
    if not results["test"]:
        print("\n--- Test failures ---")
        print(result.stdout)

    # Run linting with Ruff
    result = subprocess.run(
        ["ruff", "check", "."],
        capture_output=True, text=True,
    )
    results["lint"] = result.returncode == 0
    if not results["lint"]:
        print("\n--- Lint failures ---")
        print(result.stdout)

    # Run type checking with Ty
    result = subprocess.run(
        ["ty", "check"],
        capture_output=True, text=True,
    )
    results["typecheck"] = result.returncode == 0
    if not results["typecheck"]:
        print("\n--- Type check failures ---")
        print(result.stdout)

    # Summary
    failed = [name for name, ok in results.items() if not ok]
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()
