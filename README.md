# S&P 500 Trading Strategy Backtests: 211 Combinations, 15 Strategies, 25 Years of Data

Comprehensive backtest results for 15 trading strategies applied to the S&P 500 index, covering 25 years of market data (2000–2025). Includes 211 parameter combinations across 6 optimization runs.

All backtests use:
- **Initial capital**: $10,000
- **Period**: 2000-01-03 to 2025-12-30 (25 years)
- **Risk-free rate**: 2.0% annualized (Sharpe ratio denominator)
- **Benchmark**: Buy & Hold S&P 500

Full analysis and articles at **[rational-growth.com](https://rational-growth.com)**.

---

## Strategies Included

| # | Strategy | Data File |
|---|----------|-----------|
| 1 | Dual Momentum (SPY vs AGG) | [data/dual_momentum.json](data/dual_momentum.json) |
| 2 | Dual Momentum — 30 parameter combinations | [data/dual_momentum_optimization.json](data/dual_momentum_optimization.json) |
| 3 | Bollinger Band Mean Reversion | [data/bollinger_bands.json](data/bollinger_bands.json) |
| 4 | Bollinger Bands — 20 parameter combinations | [data/bollinger_bands_optimization.json](data/bollinger_bands_optimization.json) |
| 5 | SMA/EMA Crossover (50/200, 12/26) | [data/sma_ema_crossover.json](data/sma_ema_crossover.json) |
| 6 | MA Crossover — 32 parameter combinations | [data/sma_ema_crossover_optimization.json](data/sma_ema_crossover_optimization.json) |
| 7 | Donchian Channel (20/55/100-day) | [data/donchian_channel.json](data/donchian_channel.json) |
| 8 | Donchian Channel — 15 parameter combinations | [data/donchian_channel_optimization.json](data/donchian_channel_optimization.json) |
| 9 | RSI Mean Reversion (7/14/21-period) | [data/rsi_strategy.json](data/rsi_strategy.json) |
| 10 | KAMA Adaptive Moving Average | [data/kama_adaptive_ma.json](data/kama_adaptive_ma.json) |
| 11 | Volatility Breakout | [data/volatility_breakout.json](data/volatility_breakout.json) |
| 12 | ATR Breakout — 60 parameter combinations | [data/atr_breakout_optimization.json](data/atr_breakout_optimization.json) |

**Total combinations tested: 211**

---

## Results Summary (Ranked by Sharpe Ratio)

| Strategy | Variant | CAGR | Max DD | Sharpe | Win Rate | Trades |
|----------|---------|-----:|-------:|-------:|---------:|-------:|
| Dual Momentum (Optimized) | lookback=1mo bond=TLT | 10.66% | -32.90% | 0.625 | 75.0% | — |
| **Dual Momentum** | SPY/AGG 12-month | **9.29%** | **-22.24%** | **0.598** | **79.3%** | 29 |
| MA Crossover (Optimized) | SMA 50/250 | 7.19% | -33.92% | 0.447 | 83.3% | — |
| MA Crossover | SMA 50/200 | 6.72% | -33.92% | 0.418 | 75.0% | 12 |
| **Buy & Hold (Benchmark)** | S&P 500 | **6.17%** | **-56.78%** | **0.303** | — | — |
| Donchian Channel | 55-day | 5.04% | -26.06% | 0.320 | 57.6% | 33 |
| Donchian Channel | 100-day | 4.81% | -24.62% | 0.311 | 72.2% | 18 |
| RSI Mean Reversion | RSI-21 | 5.43% | -45.76% | 0.292 | 83.3% | 12 |
| Bollinger Bands (Optimized) | period=10 std=1.5 | 4.48% | -32.86% | 0.246 | 73.1% | — |
| MA Crossover | EMA 12/26 | 3.86% | -31.38% | 0.220 | 40.0% | 30 |
| RSI Mean Reversion | RSI-14 | 4.34% | -52.58% | 0.220 | 79.2% | 24 |
| RSI Mean Reversion | RSI-7 | 3.33% | -49.73% | 0.161 | 74.1% | 68 |
| Donchian Channel (Optimized) | entry=30 exit=20 | 2.95% | -30.86% | 0.143 | 43.8% | — |
| Donchian Channel | 20-day | 2.88% | -47.88% | 0.131 | 45.1% | 71 |
| ATR Breakout (Optimized) | atr=10 mult=1.5 | 2.88% | -42.52% | 0.130 | 45.7% | — |
| Bollinger Bands | 20-period 2-std | 2.76% | -33.84% | 0.121 | 74.1% | 112 |
| KAMA Adaptive MA | Default params | 0.31% | -47.62% | -0.096 | 31.4% | 48 |
| Volatility Breakout | Default params | -0.77% | -45.30% | -0.239 | 35.9% | 41 |

**Key finding**: Dual Momentum (12-month lookback, SPY vs AGG) achieves the best risk-adjusted return among all tested strategies, with a Sharpe of 0.598 vs 0.303 for buy-and-hold, while cutting maximum drawdown from -56.78% to -22.24%.

---

## JSON Schema

Each strategy file contains:

```json
{
  "metadata": {
    "strategy": "Strategy name",
    "ticker": "^GSPC or SPY",
    "start_date": "2000-01-03",
    "end_date": "2025-12-30",
    "initial_capital": 10000.0
  },
  "strategy_name": {
    "cagr_pct": 9.29,
    "max_drawdown_pct": -22.24,
    "sharpe_ratio": 0.5981,
    "win_rate_pct": 79.31,
    "total_trades": 29,
    "total_return_pct": 622.19,
    "final_capital": 72218.58,
    "equity_curve": [{"date": "2003-09-29", "value": 10000.0}, "..."],
    "trades": ["..."]
  },
  "buy_and_hold": {"cagr_pct": 6.17, "..."}
}
```

Optimization files additionally contain `all_results_ranked_by_sharpe` — a ranked list of every tested parameter combination.

---

## Usage

### Python

```python
import json

with open('data/dual_momentum.json') as f:
    data = json.load(f)

strategy = data['dual_momentum_strategy']
print(f"CAGR: {strategy['cagr_pct']}%")
print(f"Sharpe: {strategy['sharpe_ratio']}")
print(f"Max Drawdown: {strategy['max_drawdown_pct']}%")

# Plot equity curve
import pandas as pd
ec = pd.DataFrame(strategy['equity_curve'])
ec['date'] = pd.to_datetime(ec['date'])
ec.set_index('date')['value'].plot(title='Dual Momentum Equity Curve')
```

### Load summary CSV

```python
import pandas as pd

df = pd.read_csv('summary.csv')
print(df.sort_values('sharpe_ratio', ascending=False).to_string())
```

---

## Full Analysis

Detailed articles with charts and interpretation for each strategy:

- [Dual Momentum Strategy — Full Analysis](https://rational-growth.com)
- [MA Crossover Strategy — SMA vs EMA](https://rational-growth.com)
- [Bollinger Bands Mean Reversion](https://rational-growth.com)
- [Donchian Channel Breakout](https://rational-growth.com)
- [RSI Mean Reversion](https://rational-growth.com)

All strategy research published at **[rational-growth.com](https://rational-growth.com)** — evidence-based investing and personal finance.

---

## Citation

If you use this dataset in research, analysis, or publications, please credit the source:

```
S&P 500 Trading Strategy Backtests Dataset (2000–2025)
rational-growth.com
https://github.com/[your-username]/sp500-strategy-backtests
```

Or in academic style:

> rational-growth.com. (2025). *S&P 500 Trading Strategy Backtests: 211 Combinations, 15 Strategies, 25 Years of Data* [Dataset]. GitHub. https://rational-growth.com

Linking back to [rational-growth.com](https://rational-growth.com) helps keep this dataset maintained and updated.

---

## License

MIT — see [LICENSE](LICENSE). Data is provided for educational and research purposes. Past performance does not guarantee future results.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) to add your own backtest results.
