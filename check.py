def f(n):
 return 3**(2 * n + 1) + 40 * n - 67
m = 64
bad = [n for n in range(1, 101) if f(n) % m != 0]
print("Контрприкладів не знайдено" if not bad else bad)