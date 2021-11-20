import pandas as pd
from tables import crosstab

def chi_square(a, b, c, d, n):
    return ((abs((a*d) - (b*c)) - (n/2)) * n) / ((a+b)*(c+d)*(a+c)*(b+d))