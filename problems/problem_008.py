# Problem 008. Largest Product in a Series

from pathlib import Path

cwd = Path.cwd()

TXT_PATH = cwd / "problems" / "problem_008.txt"

with open(TXT_PATH, "r") as file:
    digits = file.read()

products = []  # type: ignore

for i in range(len(digits) - 13):
    pass
