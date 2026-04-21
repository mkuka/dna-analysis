def gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    return round((g + c) / len(sequence) * 100, 2)


def nucleotide_frequency(sequence):
    freq = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }
    return freq


def find_motif(sequence, motif="ATG"):
    positions = []
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            positions.append(i)
    return positions


def sequence_length(sequence):
    return len(sequence)