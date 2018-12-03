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
    Pass/Don't Pass Bets
    :param x: decision variables - x[0]: pass & x[1] don't pass
    :param c: parameter c = penalty for variance
    :return:
    """
    return -(-0.014*x[0] - (1/6)*x[1] - c*(0.999804*x[0]**2 + (4/3)*x[1]**2))


def gradient_pf(x):
    return np.array([-(-0.014 - c*(2*0.999804*x[0])), -(-(1/6) - c*((8/3)*x[1]))])


if __name__ == "__main__":
    # C=0 means just maximize expected value
    for c in range(5):
        res = minimize(f_pdp, np.array([1, 1]), method="L-BFGS-B", jac=gradient_pdp, bounds=[(0, 1), (0, 1)])
        print(f"######## c={c} ########")
        print("Solutions: ", res.x)
        print("Utility Value:", -res.fun)
        print(res.message)
    # for c in range(5):
    #     res = minimize(f_pdp, np.array([1]), method="L-BFGS-B", jac=gradient_pdp, bounds=[(0, 1)] )
    #     print(f"######## c={c} ########")
    #     print("Solutions: ", res.x)
    #     print("Utility Value:", -res.fun)
    #     print(res.message)

