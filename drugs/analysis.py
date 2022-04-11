"""Ad-hoc analysis of drugs data."""

from collections import Counter
from pathlib import Path

import ndjson


def analyse_drugs(extract: Path) -> str:
    """Return the journal with the most citations."""
    with extract.open("r") as f:
        drugs_data = ndjson.load(f)

    journal_citations = Counter()

    for drug in drugs_data:
        for trial in drug["clinical_trials"]:
            journal_citations[trial["journal"]] += 1
        for pubmed in drug["pubmed"]:
            journal_citations[pubmed["journal"]] += 1

    return journal_citations.most_common(1)[0][0]
