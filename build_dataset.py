import json, os, shutil, csv

src = 'C:/ZeroCapital/businesses/wp_automation/data/backtest_results/'
dst = 'C:/ZeroCapital/github_dataset/'
data_dst = dst + 'data/'

os.makedirs(data_dst, exist_ok=True)

# Copy and rename JSON files
renames = {
    'dual_momentum_sp500.json':        'dual_momentum.json',
    'dual_momentum_optimization.json': 'dual_momentum_optimization.json',
    'bollinger_sp500.json':            'bollinger_bands.json',
    'bollinger_optimization.json':     'bollinger_bands_optimization.json',
    'ma_crossover_sp500.json':         'sma_ema_crossover.json',
    'ma_crossover_optimization.json':  'sma_ema_crossover_optimization.json',
    'donchian_sp500.json':             'donchian_channel.json',
    'donchian_optimization.json':      'donchian_channel_optimization.json',
    'rsi_sp500.json':                  'rsi_strategy.json',
    'kama_sp500.json':                 'kama_adaptive_ma.json',
    'volatility_breakout_sp500.json':  'volatility_breakout.json',
    'atr_breakout_optimization.json':  'atr_breakout_optimization.json',
}

for orig, new in renames.items():
    shutil.copy2(src + orig, data_dst + new)
    print(f'  copied {orig} -> {new}')

def load(f):
    with open(data_dst + f) as fp:
        return json.load(fp)

rows = []

# Buy & Hold benchmark
bh = load('bollinger_bands.json')['buy_and_hold']
rows.append({
    'strategy': 'Buy & Hold (S&P 500)',
    'variant': 'Benchmark',
    'cagr_pct': bh['cagr_pct'],
    'max_drawdown_pct': bh['max_drawdown_pct'],
    'sharpe_ratio': bh['sharpe_ratio'],
    'win_rate_pct': bh.get('win_rate_pct', ''),
    'total_trades': bh.get('total_trades', ''),
    'total_return_pct': bh['total_return_pct'],
    'data_file': 'data/bollinger_bands.json',
})

# Dual Momentum
dm = load('dual_momentum.json')['dual_momentum_strategy']
rows.append({
    'strategy': 'Dual Momentum', 'variant': 'SPY/AGG 12-month',
    'cagr_pct': dm['cagr_pct'], 'max_drawdown_pct': dm['max_drawdown_pct'],
    'sharpe_ratio': dm['sharpe_ratio'], 'win_rate_pct': dm['win_rate_pct'],
    'total_trades': dm['total_trades'], 'total_return_pct': dm['total_return_pct'],
    'data_file': 'data/dual_momentum.json',
})

dm_opt = load('dual_momentum_optimization.json')['best_parameters']
rows.append({
    'strategy': 'Dual Momentum (Optimized)',
    'variant': 'lookback=' + str(dm_opt['lookback_months']) + 'mo bond=' + dm_opt['bond_etf'],
    'cagr_pct': dm_opt['cagr'], 'max_drawdown_pct': dm_opt['max_drawdown'],
    'sharpe_ratio': dm_opt['sharpe_ratio'], 'win_rate_pct': dm_opt['win_rate'],
    'total_trades': dm_opt['total_trades'], 'total_return_pct': dm_opt['total_return'],
    'data_file': 'data/dual_momentum_optimization.json',
})

# Bollinger Bands
bb = load('bollinger_bands.json')['bollinger_strategy']
rows.append({
    'strategy': 'Bollinger Bands', 'variant': '20-period 2-std',
    'cagr_pct': bb['cagr_pct'], 'max_drawdown_pct': bb['max_drawdown_pct'],
    'sharpe_ratio': bb['sharpe_ratio'], 'win_rate_pct': bb['win_rate_pct'],
    'total_trades': bb['total_trades'], 'total_return_pct': bb['total_return_pct'],
    'data_file': 'data/bollinger_bands.json',
})

bb_opt = load('bollinger_bands_optimization.json')['best_parameters']
rows.append({
    'strategy': 'Bollinger Bands (Optimized)',
    'variant': 'period=' + str(bb_opt['period']) + ' std=' + str(bb_opt['num_std']),
    'cagr_pct': bb_opt['cagr'], 'max_drawdown_pct': bb_opt['max_drawdown'],
    'sharpe_ratio': bb_opt['sharpe_ratio'], 'win_rate_pct': bb_opt['win_rate'],
    'total_trades': bb_opt['total_trades'], 'total_return_pct': bb_opt['total_return'],
    'data_file': 'data/bollinger_bands_optimization.json',
})

# MA Crossover
ma_data = load('sma_ema_crossover.json')
for key, strat in ma_data['strategies'].items():
    rows.append({
        'strategy': 'MA Crossover', 'variant': strat['label'],
        'cagr_pct': strat['cagr_pct'], 'max_drawdown_pct': strat['max_drawdown_pct'],
        'sharpe_ratio': strat['sharpe_ratio'], 'win_rate_pct': strat['win_rate_pct'],
        'total_trades': strat['total_trades'], 'total_return_pct': strat['total_return_pct'],
        'data_file': 'data/sma_ema_crossover.json',
    })

ma_opt = load('sma_ema_crossover_optimization.json')['best']
rows.append({
    'strategy': 'MA Crossover (Optimized)',
    'variant': ma_opt['ma_type'] + ' ' + str(ma_opt['fast']) + '/' + str(ma_opt['slow']),
    'cagr_pct': ma_opt['cagr_pct'], 'max_drawdown_pct': ma_opt['max_drawdown_pct'],
    'sharpe_ratio': ma_opt['sharpe_ratio'], 'win_rate_pct': ma_opt['win_rate_pct'],
    'total_trades': ma_opt['total_trades'], 'total_return_pct': ma_opt['total_return_pct'],
    'data_file': 'data/sma_ema_crossover_optimization.json',
})

# Donchian Channel
don_data = load('donchian_channel.json')
for key, strat in don_data['strategies'].items():
    label = key.replace('donchian_', 'Donchian ') + '-day'
    rows.append({
        'strategy': 'Donchian Channel', 'variant': label,
        'cagr_pct': strat['cagr_pct'], 'max_drawdown_pct': strat['max_drawdown_pct'],
        'sharpe_ratio': strat['sharpe_ratio'], 'win_rate_pct': strat['win_rate_pct'],
        'total_trades': strat['total_trades'], 'total_return_pct': strat['total_return_pct'],
        'data_file': 'data/donchian_channel.json',
    })

don_opt = load('donchian_channel_optimization.json')['best_parameters']
rows.append({
    'strategy': 'Donchian Channel (Optimized)',
    'variant': 'entry=' + str(don_opt['entry_period']) + ' exit=' + str(don_opt['exit_period']),
    'cagr_pct': don_opt['cagr'], 'max_drawdown_pct': don_opt['max_drawdown'],
    'sharpe_ratio': don_opt['sharpe_ratio'], 'win_rate_pct': don_opt['win_rate'],
    'total_trades': don_opt['total_trades'], 'total_return_pct': don_opt['total_return'],
    'data_file': 'data/donchian_channel_optimization.json',
})

# RSI
rsi_data = load('rsi_strategy.json')
for key, strat in rsi_data['strategies'].items():
    label = 'RSI-' + key.replace('rsi_', '') + ' period'
    rows.append({
        'strategy': 'RSI Mean Reversion', 'variant': label,
        'cagr_pct': strat['cagr_pct'], 'max_drawdown_pct': strat['max_drawdown_pct'],
        'sharpe_ratio': strat['sharpe_ratio'], 'win_rate_pct': strat['win_rate_pct'],
        'total_trades': strat['total_trades'], 'total_return_pct': strat['total_return_pct'],
        'data_file': 'data/rsi_strategy.json',
    })

# KAMA
kama = load('kama_adaptive_ma.json')['kama_strategy']
rows.append({
    'strategy': 'KAMA Adaptive MA', 'variant': 'Default params',
    'cagr_pct': kama['cagr_pct'], 'max_drawdown_pct': kama['max_drawdown_pct'],
    'sharpe_ratio': kama['sharpe_ratio'], 'win_rate_pct': kama['win_rate_pct'],
    'total_trades': kama['total_trades'], 'total_return_pct': kama['total_return_pct'],
    'data_file': 'data/kama_adaptive_ma.json',
})

# Volatility Breakout
vb = load('volatility_breakout.json')['volatility_breakout_strategy']
rows.append({
    'strategy': 'Volatility Breakout', 'variant': 'Default params',
    'cagr_pct': vb['cagr_pct'], 'max_drawdown_pct': vb['max_drawdown_pct'],
    'sharpe_ratio': vb['sharpe_ratio'], 'win_rate_pct': vb['win_rate_pct'],
    'total_trades': vb['total_trades'], 'total_return_pct': vb['total_return_pct'],
    'data_file': 'data/volatility_breakout.json',
})

# ATR Breakout (optimization only)
atr_opt = load('atr_breakout_optimization.json')['best_parameters']
rows.append({
    'strategy': 'ATR Breakout (Optimized)',
    'variant': 'atr=' + str(atr_opt['atr_period']) + ' mult=' + str(atr_opt['atr_multiplier']),
    'cagr_pct': atr_opt['cagr'], 'max_drawdown_pct': atr_opt['max_drawdown'],
    'sharpe_ratio': atr_opt['sharpe_ratio'], 'win_rate_pct': atr_opt['win_rate'],
    'total_trades': atr_opt['total_trades'], 'total_return_pct': atr_opt['total_return'],
    'data_file': 'data/atr_breakout_optimization.json',
})

# Write summary.csv
fields = ['strategy', 'variant', 'cagr_pct', 'max_drawdown_pct', 'sharpe_ratio',
          'win_rate_pct', 'total_trades', 'total_return_pct', 'data_file']
with open(dst + 'summary.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for r in rows:
        w.writerow(r)

print('summary.csv written:', len(rows), 'rows')

# Print for README table
rows_sorted = sorted(rows, key=lambda x: float(x['sharpe_ratio']) if x['sharpe_ratio'] != '' else -99, reverse=True)
print('\nAll rows sorted by Sharpe:')
for r in rows_sorted:
    wr = r['win_rate_pct'] if r['win_rate_pct'] != '' and r['win_rate_pct'] is not None else 'N/A'
    print(f"  {r['strategy']:<35} {r['variant']:<30} CAGR={str(r['cagr_pct']):>6}%  Sharpe={str(r['sharpe_ratio']):>7}  MaxDD={str(r['max_drawdown_pct']):>7}%  WinRate={str(wr):>6}%")
