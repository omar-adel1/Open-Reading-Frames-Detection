import streamlit as st
from Bio.Seq import Seq
import Open_Reading_Frames_Detection_Functions as functions

# Set page configuration
st.set_page_config(page_title="Open Reading Frames Detection", page_icon='🧬', layout='wide')

# Create columns for layout
left_side, right_side = st.columns([2, 2.2])

# Left side column
with left_side:
    # Input for DNA sequence
    txt = st.text_input("Enter DNA Sequence:", "")

    # Validate input is non-empty
    if not txt:
        st.write("Please enter a DNA sequence.")
        st.stop()

    # Validate input contains only valid characters
    if not functions.validate_dna_sequence(txt.upper()):
        st.write("Invalid DNA sequence. Please enter only 'A', 'T', 'C', or 'G' characters.")
        st.stop()

    # Validate input is valid DNA sequence
    try:
        dna_sequence = Seq(txt.upper())
    except Exception as e:
        st.write("Invalid DNA sequence.")
        st.stop()

    # Validate input is numeric and less than or equal to the length of the DNA sequence
    max_length = len(txt)
    min_orf_length = st.number_input("Enter the minimum ORF length:", min_value=0, max_value=max_length, step=1, format="%d")

# Right side column
# Display the length of the input text
st.write(f'You wrote {len(txt)} characters.')

dna_sequence_str = str(dna_sequence)

# Call the find_orfs function with the converted sequence
orfs = functions.find_orfs(dna_sequence_str, min_length=min_orf_length)
with right_side:
    st.write("Open Reading Frames (ORFs):")
    if not orfs:
        st.write("No ORFs found.")
    else:
        for i, (orf_sequence, start_pos, stop_pos) in enumerate(orfs, 1):
            st.write(f"ORF {i}: {orf_sequence}   , Start: {start_pos}   , End: {stop_pos}")
