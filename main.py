from src.parser import read_fasta
from src.analysis import gc_content, nucleotide_frequency, find_motif, sequence_length
from src.visualization import plot_gc_content, plot_nucleotide_distribution

def main():
    file_path = "data/sample.fasta"
    
    sequences = read_fasta(file_path)
    
    gc_values = []
    freq_list = []

    for seq_data in sequences:
        seq_id = seq_data["id"]
        sequence = seq_data["sequence"]

        print(f"\nProcessing: {seq_id}")

        gc = gc_content(sequence)
        freq = nucleotide_frequency(sequence)
        motifs = find_motif(sequence, "ATG")
        length = sequence_length(sequence)

        print(f"Length: {length}")
        print(f"GC Content: {gc}%")
        print(f"Nucleotide Frequency: {freq}")
        print(f"ATG Motif Positions: {motifs}")

        gc_values.append(gc)
        freq_list.append(freq)

    # Visualization
    plot_gc_content(gc_values)
    plot_nucleotide_distribution(freq_list)

if __name__ == "__main__":
    main()