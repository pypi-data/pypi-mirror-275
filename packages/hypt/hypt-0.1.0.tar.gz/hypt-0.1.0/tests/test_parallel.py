import numpy as np
import hypt
from joblib import Parallel, delayed

# Himmelblau's function


def loss(x1, x2):
    return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2


# define grid search
hparams = hypt.GridSearch({
    'x1': np.linspace(-5, 5, 101),
    'x2': np.linspace(-5, 5, 101),
})

fvals = Parallel(n_jobs=2)(delayed(loss)(**hparam) for hparam in hparams)
best = np.argmin(fvals)

print(f'Best value found was {fvals[best]} at point {hparams[best]}')
