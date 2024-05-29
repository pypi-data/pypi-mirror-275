from nipo_company_distance import find_best_match_levenshtein

companies = ["Ålesund AS", "Stavanger", "Bergen", "Trondheim", "Oslo1"]
sokere = ["ålesund A", "stavanges", "berrgen", "trrondheim", "oslo"]
threshold = 0.9
a = find_best_match_levenshtein(companies, sokere, threshold)
print(a)