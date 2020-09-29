import numpy as np
from modules.gradient_function import numerical_gradient_1d, gradient_descent


def function_2(x):
    return x[0]**2 + x[1]**2

print(numerical_gradient_1d(function_2, np.array([3.0, 4.0])))
print(numerical_gradient_1d(function_2, np.array([0.0, 2.0])))
print(numerical_gradient_1d(function_2, np.array([3.0, 0.0])))

# 적절한 lr(learning rate: 학습률)
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100))
# 과도한 lr
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=10.0, step_num=100))
# 너무 적은 lr
init_x = np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=1e-10, step_num=100))
