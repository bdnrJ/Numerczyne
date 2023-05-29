import sympy as sp

def pochodna_w_punkcie(f_str, x0):
    x = sp.Symbol('x')
    expr = sp.parse_expr(f_str)
    df = expr.diff(x)
    df_value = df.subs(x, x0)
    return df_value


funkcja = '2*x**2 + 3*x + 1'
df = pochodna_w_punkcie(funkcja, 3)
print(df)