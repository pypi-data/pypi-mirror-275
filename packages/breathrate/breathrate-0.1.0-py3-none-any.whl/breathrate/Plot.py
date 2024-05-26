import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import savgol_filter
from scipy.signal import find_peaks
from scipy.signal import peak_prominences
import time
from datetime import datetime


# Get the Figure
def run():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_facecolor((0,1,1)) # Set the background colour
    start_time = time.time()

    def animate(i):
        xs = []
        ys = []

        graph_data = open('file.csv', 'r').read()
        lines = graph_data.split('\n')
        for line in lines[1:]:
            if len(line) > 1:
                x, y = line.split(',')
                y = float(y)
                xs.append(x)
                ys.append(y)

        ax.clear()
        x = savgol_filter(ys, 10, 2)
        j = 0
        peak_count = 0
        peaks, _ = find_peaks(x)
        prominences = peak_prominences(x, peaks)[0]
        contour_heights = x[peaks] - prominences

        plt.plot(x)
        plt.plot(peaks, x[peaks], "x")
        plt.vlines(x=peaks, ymin=contour_heights, ymax=x[peaks])

        ymin = contour_heights
        ymax = x[peaks]

        now = datetime.now()
        current_time = time.time()

        for j in range(ymin.size):
            if ymin[j] - ymax[j] <= -10:
                peak_count = peak_count + 1
                print(peak_count)

        now = datetime.now()
        nowtime = now.strftime("%H:%M:%S")
        test_time = current_time - start_time


        ax.set_xlabel("Time")
        ax.set_ylabel("Breath")
        ax.set_title("Live Plot of Breathing Rate: " + str(peak_count) + "/" + str(round(test_time)) + "s")
        fig.tight_layout()
        ax.yaxis.grid(True)
        if test_time >= 60:
            plt.close()

    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()
