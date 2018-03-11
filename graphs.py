from matplotlib.pyplot import xlabel, ylabel, title
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [0.740384615385, 0.740705128205, 0.751121794872, 0.736538461538, 0.738301282051, 0.746794871795, 0.744391025641,
         0.725961538462, 0.721794871795]
    plt.plot(x, y)
    plt.axis([2,10,0.7,0.8])
    xlabel("parameter for the pre-pruning(min number of samples for splicing)")
    ylabel("precision on the validation set")
    title('parameters tuning(pre-pruning) for ID3 after filtering')
    plt.show()
