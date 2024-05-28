from rateslib import *

fxr = FXRates(fx_rates={"audusd": 0.62}, settlement=dt(2003, 4, 7))
fxr.rates_table()
aud = Curve({dt(2003, 4, 7): 1.0, dt(2005, 4, 7): 1.0}, id="aud")
usd = Curve({dt(2003, 4, 7): 1.0, dt(2005, 4, 7): 1.0}, id="usd")
fxf = FXForwards(
    fx_rates=fxr,
    fx_curves={"audaud": aud, "usdusd": usd, "audusd": aud}
)
solver = Solver(
    curves=[aud, usd],
    instruments=[
        Value(dt(2005, 4, 7), curves="aud", metric="cc_zero_rate", convention="30360"),
        Value(dt(2005, 4, 7), curves="usd", metric="cc_zero_rate", convention="30360"),
    ],
    s=[5.00, 7.00],
    fx=fxf,
)