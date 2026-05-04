import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"


def main():
    if not PROBLEMS_DIR.exists():
        print("No problems directory found.")
        return

    files = sorted(PROBLEMS_DIR.glob("*.py"))

    if not files:
        print("No problem files found.")
        return

    passed = 0
    failed = 0

    for file in files:
        print(f"Running {file.name}...")
        result = subprocess.run(
            ["python3", str(file)],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(f"[PASS] {file.name}")
            passed += 1
        else:
            print(f"[FAIL] {file.name}")
            print(result.stdout)
            print(result.stderr)
            failed += 1

    print()
    print(f"Summary: {passed} passed, {failed} failed")

if __name__ == "__main__":
    main()
