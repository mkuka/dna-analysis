import matplotlib.pyplot as plt


def plot_gc_content(gc_values):
    plt.figure()
    plt.hist(gc_values)
    plt.title("GC Content Distribution")
    plt.xlabel("GC %")
    plt.ylabel("Frequency")
    plt.savefig("results_gc_content.png")
    plt.close()


def plot_nucleotide_distribution(freq_list):
    total = {'A':0, 'T':0, 'G':0, 'C':0}

    for freq in freq_list:
        for key in total:
            total[key] += freq[key]

    plt.figure()
    plt.bar(total.keys(), total.values())
    plt.title("Nucleotide Distribution")
    plt.savefig("results_nucleotide_distribution.png")
    plt.close()