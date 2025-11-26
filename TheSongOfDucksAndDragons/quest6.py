from pathlib import Path

def load_data(filepath: str) -> str:
    return Path(filepath).read_text().strip()


def part1(filepath: str = "quest6.txt"):
    notes = load_data(filepath)
    count_A = 0
    total = 0

    for ch in notes:
        if ch == 'A':
            count_A += 1
        elif ch == 'a':
            total += count_A

    print("Part 1:", total)


def part2(filepath: str = "quest6.txt"):
    s = load_data(filepath)
    counts = {'A': 0, 'B': 0, 'C': 0}
    result = {'a': [], 'b': [], 'c': []}

    for ch in s:
        if ch in counts:  # Uppercase
            counts[ch] += 1
        elif ch in result:  # Lowercase
            result[ch].append(counts[ch.upper()])

    total = sum(sum(lst) for lst in result.values())
    print("Part 2:", total)


def part3(filepath: str = "quest6.txt", N: int = 1000, repeat: int = 1000):
    data = load_data(filepath)
    total = 0

    loop = data[-N:] + data + data[:N]
    start_pad = data + data[:N]
    end_pad = data[-N:] + data

    for idx in range(N, len(data) + N):
        if loop[idx].islower():
            start = max(idx - N, 0)
            end = idx + N + 1
            total += loop[start:end].count(loop[idx].upper())

    total *= (repeat - 2)

    for idx in range(len(data)):
        if start_pad[idx].islower():
            start = max(idx - N, 0)
            end = idx + N + 1
            total += start_pad[start:end].count(start_pad[idx].upper())

    for idx in range(N, len(data) + N):
        if end_pad[idx].islower():
            start = max(idx - N, 0)
            end = idx + N + 1
            total += end_pad[start:end].count(end_pad[idx].upper())

    print("Part 3:", total)


if __name__ == "__main__":
#    part1()
#    part2()
    part3()
