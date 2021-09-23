tridy = [
    {"třída": "IT1A", "počet žáku": 17},
    {"třída": "IT1B", "počet žáku": 16},
    {"třída": "IT2A", "počet žáku": 15},
    {"třída": "IT2B", "počet žáku": 14},
    {"třída": "IT3A", "počet žáku": 13},
    {"třída": "IT3B", "počet žáku": 12}    
]

for x in range(len(tridy)):
    print(f'třída: {tridy[x]["třída"]} ; počet žáku: {tridy[x]["počet žáku"]}')

for c in range(len(tridy)):
    print(c)
#vypíšou se čísla od 0 do 5 protože jsou ve tridy 6 různých dat...

for trida in tridy:
    print(f'Třída: {trida["třída"]} ; Počet žáku: {trida["počet žáku"]}')