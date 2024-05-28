from datetime import datetime as dt
from rateslib.fx_volatility import FXDeltaVolSmile
from rateslib.fx import FXForwards, FXRates
from rateslib.curves import Curve
from rateslib.instruments import Value, VolValue, FXStraddle, FXRiskReversal, FXCall, IRS, FXStrangle
from rateslib.solver import Solver
from time import time

fxr = FXRates({"eurusd": 1.3088, "usdjpy": 90.68}, settlement=dt(2009, 1, 22))
eureur = Curve(id="eur", nodes={dt(2009, 1, 20): 1.0, dt(2009, 2, 25): 1.0})
usdusd = Curve(id="usd", nodes={dt(2009, 1, 20): 1.0, dt(2009, 2, 25): 1.0})
jpyjpy = Curve(id="jpy", nodes={dt(2009, 1, 20): 1.0, dt(2009, 2, 25): 1.0})
fxf = FXForwards(
    fx_rates=fxr,
    fx_curves={
        "eureur": eureur, "eurusd": eureur,
        "usdusd": usdusd,
        "jpyjpy": jpyjpy, "jpyusd": jpyjpy,
    }
)
solver = Solver(
    id="rates",
    curves=[eureur, usdusd, jpyjpy],
    instruments=[
        IRS(dt(2009, 1, 22), "1M", spec="eur_irs", curves=eureur),
        IRS(dt(2009, 1, 22), "1M", spec="usd_irs", curves=usdusd),
        IRS(dt(2009, 1, 22), "1M", spec="usd_irs", curves=jpyjpy),
    ],
    s=[2.0113, 0.3525, 0.42875],
    instrument_labels=["eur_1m", "usd_1m", "jpy_1m"],
    fx=fxf,
)
dvs = FXDeltaVolSmile(
    id="smile",
    nodes={0.25: 1.0, 0.50: 1.0, 0.75: 1.0},
    eval_date=dt(2009, 1, 20),
    expiry=dt(2009, 2, 20),
    delta_type="spot",
)

fxc = FXCall(
    pair="eurusd",
    expiry=dt(2009, 2, 20),
    payment_lag=2,
    delivery_lag=2,
    delta_type="spot",
    premium_ccy="usd",
    strike=1.34,
)

curves = [None, fxf.curve("eur", "usd"), None, fxf.curve("usd", "usd")]

irs = IRS(
    dt(2009, 2, 20), "10y", spec="usd_irs"
)
curves = fxf.curve("usd", "usd")

t0 = time()
for _ in range(3000):
    # irs.rate(curves=curves, vol=dvs, fx=fxf)
    irs.rate(curves=curves)
t1 = time()
print(f"executed in {t1-t0:.4f} seconds.")

