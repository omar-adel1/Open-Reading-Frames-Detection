import re

def find_orfs(dna_sequence, min_length):
    orfs = []
    if "ATG" in dna_sequence:
        for startmatch in re.finditer('ATG', dna_sequence):
            start_pos = startmatch.start()
            remaining = dna_sequence[start_pos:]
            for stopmatch in re.finditer('TAA|TGA|TAG', remaining):
                stop_pos = start_pos + stopmatch.end() - 1
                orf_sequence = remaining[:stopmatch.end()]
                if len(orf_sequence) >= min_length:
                    orfs.append((orf_sequence, start_pos, stop_pos))
                break
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