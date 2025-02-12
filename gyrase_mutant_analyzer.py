"""
NCBI Protein Sequence Analyzer

A tool to fetch and analyze protein sequences from NCBI with associated metadata.
"""

import os
import re
import argparse
from Bio import Entrez, SeqIO
import pandas as pd
from time import sleep

def setup_environment():
    os.makedirs("protein_sequences", exist_ok=True)
    os.makedirs("nucleotide_sequences", exist_ok=True)

def get_user_query():
    parser = argparse.ArgumentParser(description='NCBI Protein Sequence Analyzer')
    parser.add_argument('--query', type=str, required=True,
                       help='NCBI search query (enclose in quotes)')
    parser.add_argument('--email', type=str, required=True,
                       help='Your email address for NCBI access')
    return parser.parse_args()

def extract_protein_data(query):
    """Retrieve and process protein records from NCBI."""
    # [Keep the original function body unchanged]
    # ... (rest of the function as provided) ...

def main():
    """Main execution flow."""
    args = get_user_query()
    Entrez.email = args.email
    
    setup_environment()
    print(f"\nRunning query: {args.query}")
    
    data = extract_protein_data(args.query)
    
    # Save metadata
    df = pd.DataFrame(data)
    df.to_csv('protein_metadata.csv', index=False)
    
    print("\nProcessing complete!")
    print(f"Metadata saved to protein_metadata.csv")
    print(f"Protein sequences saved to protein_sequences/")
    print(f"Nucleotide sequences saved to nucleotide_sequences/")

if __name__ == "__main__":
    main()
