import key

def keyboard_distance(c1, c2):
    if c1 == c2:
        return 0
    if c2 in key.keyboard_proximity.get(c1, set()):
        return 0.6
    return 1

def levenshtein_distance_with_keyboard(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance_with_keyboard(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2) * keyboard_distance(c1, c2)
            current_row.append(min(insertions, deletions, substitutions))
        
        previous_row = current_row
    
    return previous_row[-1]