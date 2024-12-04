text="AABBBCAcDDEF"

#charactor_frequency

charactor_frequency={ch:text.count(ch) for ch in text}

print(charactor_frequency)

#non_recursive_elements

non_recursive_elements={k:v for k,v in charactor_frequency.items() if v==1}

print(non_recursive_elements)