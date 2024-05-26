# %%
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from tqdm import tqdm
import hypt
import hypt.random as r

num_samples = 50

# define random search
hparams = hypt.RandomSearch({
    'loss': 'squared_error',
    'learning_rate': r.LogUniform(0.001, 0.5),
    'max_iter': 200,
    'max_leaf_nodes': r.IntLogUniform(16, 256),
    'min_samples_leaf': r.IntLogUniform(1, 100),
    'l2_regularization': r.OrZero(r.LogUniform(0.001, 10)),  # half of samples will be 0
    'validation_fraction': 0.2,
    'n_iter_no_change': 10,
    'random_state': 1984,
}, num_samples, seed=123)

# get data
X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# hpt loop
val_results = []
test_results = []
for hparam in tqdm(hparams):
    gbm = HistGradientBoostingRegressor(**hparam)
    gbm.fit(X_train, y_train)

    val_results.append(gbm.validation_score_.max())
    test_results.append(gbm.score(X_test, y_test))

# print best hparam and test score
best = np.argmax(val_results)
print('Best params:')
for k, v in hparams[best].items():
    print(f'\t{k} : {v}')
print('Test r2 score:', test_results[best])
# %%
