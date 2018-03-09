from matplotlib.pyplot import xlabel, ylabel, title
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [2, 3, 4, 5, 6, 7, 8]
    y = [0.65, 0.69, 0.67, 0.69, 0.65, 0.67, 0.60]
    plt.plot(x,y)
    xlabel("parameter for the pre-pruning(min number of samples for splicing)")
    ylabel("precision on the validation set")
    title('parameters tuning(pre-pruning) for ID3')
    plt.show()




