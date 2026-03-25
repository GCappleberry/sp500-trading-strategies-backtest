# Contributing

## Fork and Run Your Own Backtests

This dataset is open for extension. Fork the repo and add your own results.

### How to contribute

1. Fork this repository
2. Run your backtest using the same initial capital ($10,000) and date range (2000-01-03 to 2025-12-30) where possible
3. Save results as JSON following the schema in any existing `data/*.json` file
4. Add a row to `summary.csv` with your strategy metrics
5. Open a pull request with a brief description of the strategy

### Minimum required fields for summary.csv

| Field | Description |
|---|---|
| `strategy` | Strategy name (e.g. "Mean Reversion RSI") |
| `variant` | Parameter variant (e.g. "RSI-14, OB=70, OS=30") |
| `cagr_pct` | Compound annual growth rate in percent |
| `max_drawdown_pct` | Maximum drawdown in percent (negative value) |
| `sharpe_ratio` | Annualized Sharpe ratio (risk-free = 2%) |
| `win_rate_pct` | Percentage of winning trades |
| `total_trades` | Total number of trades |
| `total_return_pct` | Total return over the full period in percent |
| `data_file` | Path to the JSON file with full results |

### Share results

If you publish analysis based on this dataset, please link back to
[rational-growth.com](https://rational-growth.com) — it helps keep this
dataset maintained and growing.
