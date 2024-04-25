def find_orfs(dna_sequence, min_length):
    """
    Find Open Reading Frames (ORFs) in a DNA sequence.

    Parameters:
        dna_sequence (Bio.Seq.Seq): The DNA sequence to search for ORFs.
        min_length (int): The minimum length of an ORF to be considered.

    Returns:
        list: List of ORFs found in the DNA sequence.
    """
    orfs = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    for start in range(len(dna_sequence)):
        if dna_sequence[start:start+3] == start_codon:
            end = start + 3
            while end < len(dna_sequence):
                codon = dna_sequence[end:end+3]
                if codon in stop_codons:
                    orf = dna_sequence[start:end+3]
                    if len(orf) >= min_length:
                        orfs.append(orf)
                    break
                end += 3

    return orfs


def validate_dna_sequence(sequence):
    """
    Validate whether a sequence contains only valid DNA characters ('A', 'T', 'C', or 'G').

    Parameters:
        sequence (str): The DNA sequence to validate.

    Returns:
        bool: True if the sequence contains only valid DNA characters, False otherwise.
    """
    valid_chars = set('ATCG')
    return all(char in valid_chars for char in sequence)