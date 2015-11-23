def to_rna(dna):
    rna = ""
    for c in dna.replace("A", "U").replace("T", "A"):
        rna += "C" if c == "G" else "G" if c == "C" else c
    return rna
