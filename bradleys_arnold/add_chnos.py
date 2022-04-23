"""
This script adds chapter numbers to example sentences, determined by the
rule associated.
"""

import csv
from pathlib import Path

DATAF = Path("bradleys_arnold_examples.tsv")
LABELF = Path("BA_labels.csv")

with DATAF.open() as f:
    reader = csv.DictReader(f, delimiter="\t")
    data = list(reader)

with LABELF.open() as f:
    reader = csv.DictReader(f, fieldnames=("chno", "chapter", "start rule", "end rule"))
    labels = {int(x["start rule"]): x for x in reader}


def find_rule(n: int):
    k = max(x for x in labels.keys() if x <= n)
    return labels[k]


for card in data:
    card["chapter"] = find_rule(int(card["rule"]))["chno"]

with DATAF.with_stem(DATAF.stem + "_chapters").open("w") as f:
    writer = csv.DictWriter(f, data[0].keys(), delimiter="\t")
    writer.writeheader()
    writer.writerows(data)
