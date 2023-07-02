# Problem name: ECOO '12 R1 P2 - Decoding DNA
# Code: ecoo12r1p2
# Link: https://dmoj.ca/problem/ecoo12r1p2

# SOLVED JUST NEED TO DOCUMENT THE CODE


def find_index_promoter(strand: str) -> int:
    """Find the index where the string 'TATAAT' starts

    Args:
        strand (str): strand of dna

    Returns:
        int: Number where the promoter starts
    """

    PROMOTER = 'TATAAT'
    for i in range(len(strand)):
        if strand[i: i + 6] == PROMOTER:
            return i

def complement_sequence(sequence: str) -> str:
    """Changes the A <--> T and C <--> G

    Args:
        sequence (str): dna strand

    Returns:
        str: returns the complementary of the strand
    """
    
    complement_sequence = ''
    for i in range(len(sequence)):
        if sequence[i] == 'A':
            complement_sequence += 'T'
        elif sequence[i] =='T':
            complement_sequence += 'A'
        elif sequence[i] =='C':
            complement_sequence += 'G'
        elif sequence[i] =='G':
            complement_sequence += 'C'
    return complement_sequence


def find_index_terminator(strand: str, index_of_promoter: int) -> int:
    """Find the index of the terminator.
    The terminator consists of two distinct, complementary, reversed
    sequences of at least length 6.

    Args:
        strand (str): dna strand
        index_of_promoter (int): index of the promoter 
        (use the function find_index_promoter())

    Returns:
        int: Index where the terminator starts
    """
    index_terminator = index_of_promoter + 10
    for i in range(len(strand[index_terminator:])):
        portion = strand[index_terminator: index_terminator + 6]
        portion_transformed = complement_sequence(portion)[::-1]
        if portion_transformed in strand[index_terminator + 6:]:
            return index_terminator
        
        index_terminator += 1




def extract_transcription_unit(strand: str) -> str:
    """Using the indexes of the promoter and terminator this function
    cuts the strand where the transcription unit is.

    Args:
        strand (str): strand that contains a transcription unit.

    Returns:
        str: transcription unit for a single strand of dna.
    """
    index_of_promoter = find_index_promoter(strand)
    index_of_terminator = find_index_terminator(strand, index_of_promoter)
    transcription_unit = strand[index_of_promoter + 10: index_of_terminator]
    return transcription_unit


# Main

# Inputs
NUMBER_OF_STRANDS = 5
strands_DNA = []

for _ in range(NUMBER_OF_STRANDS):
    strands_DNA.append(input())


# Extract Transcription Unit and Translate to RNA
transcription_units_rna = []
for strand in strands_DNA:
    transcription_unit = extract_transcription_unit(strand)
    transcription_unit_complement = complement_sequence(transcription_unit)
    transcription_unit_rna = transcription_unit_complement.replace('T', 'U')
    transcription_units_rna.append(transcription_unit_rna)

# Output

for i in range(NUMBER_OF_STRANDS):
    print(f'{i + 1}: {transcription_units_rna[i]}')