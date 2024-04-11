import math

def solution(numer1, denom1, numer2, denom2):
    bunza = denom1 * numer2 + denom2 * numer1
    bunmo = denom1 * denom2
    gcd = math.gcd(bunza, bunmo)
    return [bunza//gcd, bunmo//gcd]
