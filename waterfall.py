import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

# aesthtics
font = {'family' : 'Helvetica',
        'weight' : 'bold',
        'size'   : 14}

matplotlib.rc('font', **font)

def waterfallPlot(x, y, xLabel = "", yLabel = "", title = "Waterfall Go Brrr"):
    """
    Generate waterfall plot

    Parameters
    ----------
    x : list
        the list of label on the horizontal axis.
    y : list
        the list of values associated with labels in x.
    xLabel : string, optional
        the x label. The default is "".
    yLabel : string, optional
        the y label. The default is "".
    title : string, optional
        the plot title. The default is "Waterfall Go Brrr".

    Returns
    -------
    None

    """
    # processing
    def changeBottom(val):
        bot = []
        for i in range(len(val) - 1):
            add = val[:i]
            bot.append(sum(add))
        bot.append(0)
        return tuple(bot)
    
    def attachColor(val):
        colorList = []
        for i in range(len(val) - 1):
            if val[i] >= 0:
                colorList.append("#ffb070")
            else:
                colorList.append("#abb9c4")
        if val[-1] > 0:
            colorList.append("#bf5700")
        else:
            colorList.append("#333f48")
        return colorList
    
    def autolabel(label, barPlot, yLoc, yLocOri):
        for idx,rect in enumerate(barPlot):
            height = yLoc[idx] + yLocOri[idx]
            ax.text(rect.get_x() + rect.get_width()/2., height,
                    label[idx],
                    ha='center', va='bottom', rotation=0)
    
    colors = attachColor(y)
    offset = changeBottom(y)
    y_pos = np.arange(len(x))
    
    # viz
    fig, ax = plt.subplots(figsize = (8,6))
    bar = ax.bar(y_pos, y, bottom=offset, align='center', color = colors)
    autolabel(y, bar, offset, y)
    ax.set_ylabel(yLabel)
    ax.set_xlabel(xLabel)
    ax.set_title(title, loc = "left")
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(top = 1.1 * ymax)
    plt.tight_layout()
    plt.xticks(y_pos,x)
    plt.show()

# test
x = ['Stonk', 'Bonds', 'NFTs', 'Loans', 'Bet', 'Mom', 'Net Total']
y = [1000, 2000, 3000, -1000, 2000, -500, 6500]
waterfallPlot(x, y , xLabel="", yLabel = "Value [$]", title = "Last Month Cashflow")