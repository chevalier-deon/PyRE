import pandas as pd
from tables import crosstab

#odds and risk ratio TODO: update to let them accept correctly formatted pandas tables

def odds_ratio(a, b, c, d):
    return (a*d) / (b*c)

def relative_risk(i_e, c_e, i_n, c_n):
    return (i_e * (c_e + c_n)) / (c_e * (i_e + i_n))

def chi_square(a, b, c, d, n):
    return ((abs((a*d) - (b*c)) - (n/2)) * n) / ((a+b)*(c+d)*(a+c)*(b+d))