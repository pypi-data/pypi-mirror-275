
import numpy as np
import random
import numpy as np
import glob
# import matplotlib.pyplot as plt

# seed for reproducibility
np.random.seed(12038)
random.seed(12038)

from phylokrr.datasets import load_vcv,load_1d_data_example
from phylokrr.utils import sim_data, split_data, PGLS, P_mat_simple, myfunc, k_fold_cv_random, P_inv_simple
from phylokrr.kernels import KRR 


rbf_grid_params = {
    'lambda': np.logspace(-10, 5, 200, dtype=float, base=2),
    'gamma': np.logspace(-10, 5, 200, dtype=float, base=2),
}


path_trees = '/Users/ulises/Desktop/ABL/software/phylokrr/data/r_coal_sim_500spps_100trees'
vcvs = glob.glob(path_trees + '/*.csv')

vcv = np.loadtxt(vcvs[0], delimiter=',')
I_vcv = np.diag(np.diag(vcv))
testing_covs = [vcv, I_vcv]


n = vcv.shape[0]
b = 2
n_var = 3
noise_var = 1
sample = 200
num_test = round(0.5*n)


noise = np.random.normal(0, noise_var, n)
X_uw = np.random.normal(0, 1, n).reshape(-1,1)

y_wc = myfunc(X_uw, b=b, type='pol', 
                    add_noise=True,
                    noise=noise).ravel()

P_inv = P_inv_simple(vcv)
X_uw_uc = P_inv @ X_uw
y_uw_uc = P_inv @ y_wc


Y = np.zeros((num_test, len(testing_covs)))
F = np.zeros((num_test, len(testing_covs)))

krr_rbf_tmp = KRR(kernel='rbf', fit_intercept=False)

for i in range(len(testing_covs)):

    vcv_i = testing_covs[i]
    print("Testing cov matrix ", i)
    
    Pi = P_mat_simple(vcv_i)
    # np.sqrt(np.linalg.inv(vcv_i))

    X_wc_tmp = Pi @ X_uw_uc
    y_wc_tmp = Pi @ y_uw_uc
    
    X_wc_tmp = np.ones(X_wc_tmp.shape[0]).reshape(-1,1)

    (X_wc_train_tmp, X_wc_test_tmp,
     y_wc_train_tmp, y_wc_test_tmp,) = split_data(X_wc_tmp, y_wc_tmp, 
                                                  num_test=num_test,
                                                  seed=12038)

    # if i == 0:
    rbf_param_tmp = k_fold_cv_random(X_wc_train_tmp, y_wc_train_tmp,
                                      krr_rbf_tmp, rbf_grid_params, 
                                      verbose=False, folds=2,
                                      sample=sample)
    
    krr_rbf_tmp.set_params(**rbf_param_tmp)
    krr_rbf_tmp.fit(X_wc_train_tmp, y_wc_train_tmp)
    print(krr_rbf_tmp.score(X_wc_test_tmp, y_wc_test_tmp, metric='rmse'))
    out1 = krr_rbf_tmp.predict(X_wc_test_tmp)

    Y[:,i] = y_wc_test_tmp
    F[:,i] = out1

    # # if i == 0:
    # rbf_param_tmp2 = k_fold_cv_random(X_wc_test_tmp,
    #                                    y_wc_test_tmp, 
    #                                    krr_rbf_tmp, 
    #                                    rbf_grid_params, 
    #                                    verbose=False, 
    #                                    folds=2, sample=sample)

    # krr_rbf_tmp.set_params(**rbf_param_tmp2)
    # krr_rbf_tmp.fit(X_wc_test_tmp, y_wc_test_tmp)
    # print(krr_rbf_tmp.score(X_wc_train_tmp, y_wc_train_tmp, metric='rmse'))
    # out2 = krr_rbf_tmp.predict(X_wc_train_tmp)

    # Y[:,i] = np.hstack((y_wc_test_tmp, y_wc_train_tmp))
    # F[:,i] = np.hstack((out1, out2))

# Y -= np.mean(Y, axis=0)
# F -= np.mean(F, axis=0)

# Import packages.
import cvxpy as cp
import numpy as np
# Y = 
Q = (Y - F).T @ (Y - F)
m = Q.shape[0]
ones = np.ones(m)

# Define and solve the CVXPY problem.
w = cp.Variable(m)
prob = cp.Problem(cp.Minimize( cp.quad_form(w, Q) ),
                 [ones.T @ w == 1, w >= 0])
prob.solve()

# Print result.
print(np.round(w.value,3))


