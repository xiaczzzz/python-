# 导入需要的包
from matplotlib import pyplot as plt
import numpy as np


def DFT(input_Signal, isPrintW=False):
    Signal_Length = len(input_Signal)  # 信号长度
    n = np.arange(0, Signal_Length)
    n = n.reshape(1, Signal_Length)
    m = n.reshape(Signal_Length, 1)
    base = np.exp((0-1j) * 2 * np.pi / Signal_Length)  # 基底
    w = np.dot(m, n)  # 指数矩阵
    W = base ** w  # W矩阵

    outputSig = np.dot(W, input_Signal)
    if isPrintW:
        return outputSig, W
    else:
        return outputSig


def test_fun(fn):
    # 对比验证函数正确，调用numpy的FFT进行对比
    # 第一行图形
    ax1 = plt.subplot(3, 1, 1)
    ax2 = plt.subplot(3, 1, 2)
    ax3 = plt.subplot(3, 1, 3)
    # 选择ax1
    plt.sca(ax1)
    plt.stem(n, fn)

    # 选择ax2
    plt.sca(ax2)
    ans = np.fft.fft(fn)  # 计算FFT，正确的结果
    plt.stem(n, ans)

    # 选择ax3
    plt.sca(ax3)
    test = DFT(fn)  # 测试结果
    plt.stem(n, test)
    plt.show()


# 开始
if __name__ == '__main__':
    # 随便找一个函数进行验证
    N = 12
    n = np.arange(N)
    fn = np.cos(2 * np.pi * 2 * (n / N) + np.pi / 4)
    test_fun(fn)

