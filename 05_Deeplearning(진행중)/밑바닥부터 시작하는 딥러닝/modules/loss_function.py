import numpy as np


# 오차 제곱합
def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 교차 엔트로피 오차
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    delta = 1e-7  # np.log()에 0을 입력하면 음의 무한대가 되어 이를 방지
    return -np.sum(t * np.log(y + delta)) / batch_size