import pandas as pd
import numpy as np
import scipy
from utils.util import _den, _num
from check_accuracy import rga

def rgr(yhat, yhat_pert):
    """
        ### RANK GRADUATION Robustness (RGR) MEASURE ###
        Function for the RGR measure computation regarding perturbation of a single variable
    """ 
    rgr = rga(yhat, yhat_pert)
    return rgr


def rgr_statistic_test(yhat, yhat_mod2, yhat_pert, yhat_mode2_pert):
    """
    RGR based test for comparing the robustness of a model with that of a further model when a variable is perturbed.
    """
    yhat = np.array(yhat)
    yhat_mod2 = np.array(yhat_mod2)
    yhat_pert = np.array(yhat_pert)
    yhat_mode2_pert = np.array(yhat_mode2_pert)
    
    # Compute the number of samples
    n = len(yhat)
    
    # Compute jackknife results
    jk_results = []
    for i in range(n):
        # Use numpy indexing to exclude the i-th sample
        jk_yhat = np.delete(yhat, i)
        jk_yhat_mode2 = np.delete(yhat_mod2, i)
        jk_yhat_pert = np.delete(yhat_pert, i)
        jk_yhat_mode2_pert = np.delete(yhat_mode2_pert, i)
        result = rgr(yhat, yhat_pert) - rgr(yhat_mod2, yhat_mode2_pert)
        jk_results.append(result)

    se = np.sqrt(((n-1)/n)*(sum([(x-np.mean(jk_results))**2 for x in jk_results])))
    z = (rgr(yhat, yhat_pert) - rgr(yhat_mod2, yhat_mode2_pert))/se
    p_value = 2*scipy.stats.norm.cdf(-abs(z))
    return p_value