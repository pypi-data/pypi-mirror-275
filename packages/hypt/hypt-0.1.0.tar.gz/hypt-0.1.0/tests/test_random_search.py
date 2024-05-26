# %%
import hypt
import hypt.random as r

# %%
params = hypt.RandomSearch({
    'a': r.IntLogUniform(1, 1000),
    'b': r.LogUniform(0.01, 10),
    'c': r.OrZero(r.Uniform(0.1, 0.5)),
    'd': r.UniformCategorical([1, 5, 'a']),
    'e': 2.72,
    'f': r.UniformInt(10),
    'g': r.UniformPower(4, 15)
}, 10000, seed=123)

# %%
params_df = params.to_pandas(with_static=True)
# %%
params_df.max()
# %%
params_df.min()
# %%

params = hypt.GridSearch({
    'a': [1, 10, 100, 1000],
    'b': [0.01, 0, 0.1],
    'c': ['v1', 'v2', 'v3'],
    'd': [True, False],
})

# %%
