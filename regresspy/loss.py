import numpy as np
from numpy import ndarray


def mae(pred: ndarray, label: ndarray) -> ndarray:
    """Returns the mean absolute error between the predicted values and the
    actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): mean absolute errors.
    """
    return np.mean(np.abs(label - pred))


def sse(pred: ndarray, label: ndarray) -> ndarray:
    """Returns the residual sum of squared errors between the predicted 
    values and the actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): residual sum of squared errors.
    """
    return np.sum(np.power((label - pred), 2))


def mse(pred: ndarray, label: ndarray) -> ndarray:
    """Returns the mean squared errors between the predicted 
    values and the actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): mean squared errors.
    """
   return np.mean(np.power((label - pred), 2))


def rmse(pred: ndarray, label: ndarray) -> ndarray:
    """Returns the root mean squared error between the predicted values
    and the actual values.

    Args:
        pred (ndarray): the array of predicted values.
        label (ndarray): the array of ground truths.
    Returns:
        (ndarray): root mean squared errors.
    """
  return np.sqrt(np.mean(np.power((label - pred), 2)))
