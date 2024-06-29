import fuzzy
import levenshtein

soundex = fuzzy.Soundex(4)
metaphone = fuzzy.DMetaphone()


def fuzzy_search(query, texts):
    results = []
    for text in texts:
        lev_dist = levenshtein.levenshtein_distance_with_keyboard(query, text)
        soundex_code_query = soundex(query)
        soundex_code_text = soundex(text)
        metaphone_code_query = metaphone(query)
        metaphone_code_text = metaphone(text)
        
        if lev_dist <= len(query)/3 or (soundex_code_query == soundex_code_text and metaphone_code_query == metaphone_code_text):
            results.append(text)
    
    return results

results = fuzzy_search(query, texts)
print(results) 
