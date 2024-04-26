import re

def find_orfs(dna_sequence, min_length):
    """
    Finds Open Reading Frames (ORFs) in a DNA sequence.

    Args:
        dna_sequence (str): The DNA sequence.
        min_length (int): The minimum length of ORFs to consider.

    Returns:
        list: A list of tuples containing ORFs along with their start and end positions.
              Each tuple format: (orf_sequence, start_position, end_position).
    """
    orfs = []
    if "ATG" in dna_sequence:
        # Iterate over each occurrence of 'ATG' in the sequence
        for startmatch in re.finditer('ATG', dna_sequence):
            start_pos = startmatch.start() # Get the start position of the ORF
            remaining = dna_sequence[start_pos:] # Get the remaining sequence starting from the 'ATG'
            # Iterate over each occurrence of stop codons ('TAA', 'TGA', 'TAG') in the remaining sequence
            for stopmatch in re.finditer('TAA|TGA|TAG', remaining):
                stop_pos = start_pos + stopmatch.end() - 1 # Calculate the end position of the ORF
                orf_sequence = remaining[:stopmatch.end()] # Extract the ORF sequence
                if len(orf_sequence) >= min_length:
                    orfs.append((orf_sequence, start_pos, stop_pos))  # Append ORF details to the list
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