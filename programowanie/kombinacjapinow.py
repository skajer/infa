import itertools
n = '1234567890'
a = [''.join(i) for i in itertools.permutations(n, 4)]
x = len(a)
print(f"{x} Kombinacji, {x / 60} Godzin, {(x / 60) / 24} Dnia - do zlamania wszystkich kombinacji")