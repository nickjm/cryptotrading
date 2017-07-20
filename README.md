# Cryptocurrency Trading Algorithms

Setup:

```
virtualenv --no-site-packages env
source env/bin/activate
```

## GDAX - Moving Average Crossover

Simple MA Crossover Strategy with adjustable parameters. Requires GDAX API keys
to run. Be sure to generate keys for the correct platform (real / sandbox)

To run (after activating your virtualenv):

```
pip install gdax
python gdax/moving-average-crossover.py
```
