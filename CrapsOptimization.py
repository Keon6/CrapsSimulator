import numpy as np
import math
from scipy.optimize import minimize
'''
Script running non-linear optimization to find best Craps strategy
'''


# Pass/DP
def f_pdp(x):
    """
    Pass/Don't Pass Bets
    :param x: decision variables - x[0]: pass & x[1] don't pass
    :param c: parameter c = penalty for variance
    :return:
    """
    # x[0]=1
    return -(-0.014*x[0] + 0.014*x[1] - c*(0.999804*(x[0]**2 + x[1]**2) + 0.038808*x[0]*x[1]))


def gradient_pdp(x):
    return np.array([-(-0.014 - c*(2*0.999804*x[0] + 0.038808*x[1])), -(0.014 - c*(2*0.999804*x[1] + 0.038808*x[0]))])


# def f_pdp(x):
#     """
#     Pass/Don't Pass Bets
#     :param x: decision variables - x[0]: pass & x[1] don't pass
#     :param c: parameter c = penalty for variance
#     :return:
#     """
#     return -(-0.014 + 0.014*x[0] - c*(0.999804*(1 + x[0]**2) + 0.038808*x[0]))
#
#
# def gradient_pdp(x):
#     return np.array([-(0.014 - c*(2*0.999804*x[0] + 0.038808))])


# Pass + Field
def f_pf(x):
    """
    Pass + Field
    :param x: decision variables - x[0]: pass & x[1] don't pass
    :param c: parameter c = penalty for variance
    :return:
    """
    return -(-0.014*x[0] - (1/6)*x[1] - c*(0.999804*x[0]**2 + (41/36)*x[1]**2))


def gradient_pf(x):
    return np.array([-(-0.014 - c*(2*0.999804*x[0])), -(-(1/6) - c*((82/36)*x[1]))])


# Don't Pass + Field
def f_dpf(x):
    """
    Don't Pass + Field
    :param x: decision variables - x[0]: pass & x[1] don't pass
    :param c: parameter c = penalty for variance
    :return:
    """
    return -(0.014*x[0] - (1/6)*x[1] - c*(0.999804*x[0]**2 + (41/36)*x[1]**2))


def gradient_dpf(x):
    return np.array([-(0.014 - c*(2*0.999804*x[0])), -(-(1/6) - c*((82/36)*x[1]))])


if __name__ == "__main__":
    # C=0 means just maximize expected value

    bnds = ((0, 1), (0, 1))
    cons = ({'type': "ineq", "fun": lambda x: x[0]+x[1]-1})  # have to bet (each number will be percentage)
    # cons = None
    for c in range(5):
        print(f"######## c={c} ########")
        # Pass / Don't Pass
        res = minimize(f_pdp, np.array([1, 1]), method="SLSQP", jac=gradient_pdp, bounds=bnds, constraints=cons) # Have to bet
        # res = minimize(f_pdp, np.array([1, 1]), method="SLSQP", jac=gradient_pdp, bounds=bnds) # don't have to bet
        print("------ Pass/Don't Pass ------")
        print("Solutions: ", res.x)
        print("Utility Value:", -res.fun)
        print(res.message)
        pdp = res.x

        # Pass + Field
        # bounds = (0,1)
        res = minimize(f_pf, np.array([1, 1]), method="SLSQP", jac=gradient_pf, bounds=[(pdp[0], 1), (0, 1)], constraints=cons)
        # res = minimize(f_pf, np.array([1, 1]), method="SLSQP", jac=gradient_pf, bounds=[(pdp[0], 1), (0, 1)]) # don't have to bet
        print("------ Pass + Field ------")
        print("Solutions: ", res.x)
        print("Utility Value:", -res.fun)
        print(res.message)
        # Don't Pass + Field
        # bounds = (0,1)

        res = minimize(f_dpf, np.array([1, 1]), method="SLSQP", jac=gradient_dpf, bounds=[(pdp[1], 1), (0, 1)],
                       constraints=cons)
        # res = minimize(f_dpf, np.array([1, 1]), method="SLSQP", jac=gradient_dpf, bounds=[(pdp[1], 1), (0, 1)]) 3 don't have to bet
        print("------ Don't Pass + Field ------")
        print("Solutions: ", res.x)
        print("Utility Value:", -res.fun)
        print(res.message)

