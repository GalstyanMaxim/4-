def votes_count(filename):
    with open(filename, encoding='utf-8') as f:
        tokens = f.read().split()

    counts = []
    spoiled = 0

    for tok in tokens:
        try:
            v = int(tok)
        except ValueError:
            spoiled += 1
            continue

        if v < 0: #отрицательные бланки
            spoiled += abs(v)
            counts.append(0)
        else:
            counts.append(v)

    total = sum(counts) + spoiled
    if total == 0:
        print("Нет голосов.")
        return

    # Составление списка
    party_list = [(i+1, cnt) for i, cnt in enumerate(counts) if cnt > 0]
    party_list.sort(key=lambda x: (-x[1], x[0]))

    for i, (num, cnt) in enumerate(party_list, start=1):
        pct = cnt / total * 100
        print(f"{i}. Партия №{num} | {cnt} | {pct:.2f}%")

    print(f"\nИспорченные бланки: {spoiled} | {spoiled / total * 100:.2f}%")
votes_count("votes.txt")