def make_probs(counts_list):
    return [ c / sum(counts_list) for c in counts_list ]
