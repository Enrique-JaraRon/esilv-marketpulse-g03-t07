"""Fonctions de comparaison de MarketPulse."""


def index_by_date(prices):
    raise NotImplementedError


def align_series(instrument_prices, benchmark_prices):
    instrument_index = index_by_date(instrument_prices) #on retrouve chaque observation par sa date
    benchmark_index = index_by_date(benchmark_prices)

    common_dates = sorted( #classe chronologiuqement les dates communes aux deux séries
        set(instrument_index) & set(benchmark_index)
    )

    aligned_instrument = []
    aligned_benchmark = []

    for date in common_dates:
        aligned_instrument.append(instrument_index[date]) #Construction de deux listes alignées sur les dates communes aux deux séries
        aligned_benchmark.append(benchmark_index[date])

    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):
    raise NotImplementedError


def calculate_base_100(prices):
    raise NotImplementedError


def calculate_relative_performance(instrument_return, benchmark_return):
    return instrument_return - benchmark_return