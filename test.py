def construct_sequence(p):
    n = len(p)
    varFiltersCg = [0] * n
    assigned = set()

    for i in range(n):
        count_needed = p[i]
        candidate = 1
        while True:
            if candidate not in assigned:
                count = sum(1 for j in range(i) if candidate + varFiltersCg[j] > 0)

                if count == count_needed:
                    break

            candidate += 1

        varFiltersCg[i] = candidate
        assigned.add(candidate)

    return varFiltersCg

p = [3, 2, 3]
result = construct_sequence(p)
print("Sequence a:", result)
