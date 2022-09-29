# main
import numpy as np
import pandas as pd
from yahooweekcalander import maincal
from getnews import mainsia
import yfinance
# tickerslist = maincal(1)


def stockanalysis(tickers, returnformat):
    print("got tickers")
    tickerdic = mainsia(tickers, returnformat)
    print(tickerdic)


def calendaryahoo(rtype):
    summary = (maincal(rtype))
    print(summary)
    return summary


if __name__ == "__main__":
    t = calendaryahoo(1)
    stockanalysis(t, 1)
