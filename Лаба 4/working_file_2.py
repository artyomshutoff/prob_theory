from scipy.stats import norm
from math import factorial as fac


def binomial(k: int, n: int, p: float) -> float:
    k = int(k)
    n = int(n)
    return round(
        (fac(n) * (p**k) * (1 - p) ** (n - k)) / (fac(k) * fac(n - k)),
        4,
    )


PHI = lambda x: norm.cdf(x) - 0.5
phi = lambda x: norm.pdf(x)


# 26 вариант - 9 110 5 50 7 90 0.1
print("n1, n2, m1, m2, m3, m4, p:", end=" ")
n1, n2, m1, m2, m3, m4, p = map(float, input().split())
np = n2 * p
sqrt_npq = (n2 * p * (1 - p)) ** -0.5

print("1)", binomial(m1, n1, p))
print("2)", (sqrt_npq * phi((m2 - np) * sqrt_npq)))
print(
    "3)",
    round(
        sum([binomial(m, int(n1), p) for m in range(int(m1), int(m3) + 1)]), 4
    ),
)
print("4)", round(PHI((m4 - np) * sqrt_npq) - PHI((m2 - np) * sqrt_npq), 4))
