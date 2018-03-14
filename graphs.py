from matplotlib.pyplot import xlabel, ylabel, title
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = range(1, 21)
    # y = [0.740384615385, 0.740705128205, 0.751121794872, 0.736538461538, 0.738301282051, 0.746794871795, 0.744391025641,
    #      0.725961538462, 0.721794871795]
    # y = [0.815705128205, 0.824038461538, 0.830288461538, 0.813621794872, 0.832371794872, 0.811538461538, 0.832371794872,
    #      0.821955128205, 0.815705128205]
    # y = [0.729967948718, 0.775961538462, 0.813621794872, 0.821955128205, 0.792788461538, 0.714262820513, 0.656891025641]
    y = [0.878205128205, 0.81891025641, 0.836538461538, 0.817307692308, 0.855769230769, 0.855769230769, 0.855769230769,
         0.855769230769, 0.834935897436, 0.834935897436, 0.814102564103, 0.834935897436, 0.794871794872, 0.794871794872,
         0.774038461538, 0.774038461538, 0.774038461538, 0.774038461538, 0.774038461538, 0.774038461538]
    plt.plot(x, y)
    plt.axis([1, 20, 0.73, 0.90])
    xlabel("parameter for the k value")
    ylabel("precision on the validation set")
    title('parameters tuning KNN for ALL data (number of neighbors voting)')
    plt.show()
