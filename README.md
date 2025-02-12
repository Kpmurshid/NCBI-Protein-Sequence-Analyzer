# NCBI-Protein-Sequence-Analyzer
# NCBI Protein Sequence Analyzer

A Python tool to fetch and analyze protein sequences from NCBI with associated metadata.

## Features
- Fetches protein sequences and metadata from NCBI
- Retrieves linked nucleotide sequences
- Exports data in CSV and FASTA formats
- Extracts structural and functional annotations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kpmurshid/GyraseMutantAnalyzer.git
cd GyraseMutantAnalyzer
```
## Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Basic command:
```bash
python gyrase_mutant_analyzer.py --email your.email@example.com --query "your NCBI search query"
```

## Example query:
```bash
python gyrase_mutant_analyzer.py --email researcher@university.edu --query \
"(mutant[All Fields] AND (Gyrase A[Protein Name]) AND bacteria[Organism]"
```
## Output Structure

    protein_metadata.csv: Contains all annotation data

    protein_sequences/: FASTA files of protein sequences

    nucleotide_sequences/: FASTA files of linked DNA sequences

## Configuration

Mandatory arguments:

    --email: Your registered email with NCBI

    --query: NCBI search query in quotes

## Dependencies

    Python 3.7+

    Biopython

    Pandas

## ⚠️ Disclaimer

This tool is provided for **research purposes only**. Users should:
- Comply with NCBI's [Data Usage Policies](https://www.ncbi.nlm.nih.gov/home/about/policies/)
- Respect NCBI's rate limits (max 3 requests/second)
- Verify results through official NCBI channels
- Not use this for protected health information or sensitive data

The authors make no warranties about data accuracy or completeness. Use at your own risk.
