"""
Demo of the pathlib module
"""

from pathlib import Path

# Home
print(Path.home())

# CWD
print(Path.cwd())

# Data folder
data_folder = Path.cwd().joinpath("data")   # Old syntax
data_folder = Path.cwd() / "data"           # New syntax

# Example file
path = Path("C:/Users/Administrator/data/sub/sub/sub/sub")
file = Path("data.csv")
print(file.exists())
print(file.name)
print(file.stem)
print(file.suffix)
print(file.parent.resolve())

# Glob
path = Path("src")


# Reading & writing
file = Path("zen.txt")
file.write_text("Simple is better than complex")
file.read_text()

with open(file, "w") as f:
    f.write("Hello there")