from string import digits
def order(sentence):
    words = sentence.split()
    words2pos = {}
    numbers = []
    for word in words:
        for char in word:
            if char in digits:
                numbers.append(char)
        for num in numbers:
            words2pos[word] = num
    pairs = [pair for pair in words2pos.items()]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    sorted_list = [pair[0] for pair in sorted_pairs]
    return " ".join(sorted_list)