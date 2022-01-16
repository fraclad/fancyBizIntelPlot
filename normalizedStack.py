import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Helvetica"
plt.rcParams["font.size"] = 12

def normStacked(xValue, dataDict, toNormalize = True, col = None):
    """
    Create a simple normalized stacked plot

    Parameters
    ----------
    xValue : list
        a list of x values, typically a list of years.
    dataDict : dict
        a dictionary of elements to be plotted.
        the lenght of each values must be the same as the length of xValue
    toNormalize : bool, optional
        whether the dictionary still needs to be normalized or not. The default is True.
    col : list, optional
        a list of custom colors, length must match the length of the keys of the dataDict. The default is None.

    Raises
    ------
    ValueError
        some lenghts dont match bro.

    Returns
    -------
    None.

    """
    # check if data is to be normalized or not
    if toNormalize == True:
        df = pd.DataFrame(dataDict)
        dataUse = df.div(df.sum(axis = 1), axis = 0)
        dataUse = dataUse.to_dict(orient = "list")
    else:
        dataUse = dataDict
        
    if col is None:
        colPal = ["#001219", "#005F73", "#0A9396", "#94D2BD", "#E9D8A6", "#EE9B00", "#CA6702", "#BB3E03", "#AE2012", "9B2226"]
    else:
        colPal = col
    
    # check if there is a custom color palette input
    if len(colPal) == len(dataUse.keys()):
        pass
    else:
        try:
            colPal = colPal[:len(dataUse.keys())]
        except:
            raise ValueError("length of color list and data elements must match! Must provide ur own!")
            
    # viz
    fig, ax = plt.subplots(figsize = (8,8))
    ax.stackplot(xValue, dataUse.values(), labels = dataUse.keys(), colors = colPal)
    ax.set_ylim([0,1])
    ax.set_xlim(min(xValue), max(xValue))
    ax.spines['right'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title("Oil Production Proportion by Regions", loc = "left", y=1 + (0.04 * int(len(dataUse.keys())/2)))
    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left", borderaxespad=0, 
               ncol = int(len(dataUse.keys())/2), frameon = False)
    plt.tight_layout()
    plt.show()

# test
data = pd.read_csv("data/oilProd.csv")
xValue = data["year"].values
columnsToUse = data.columns[data.columns.str.contains("total")].values
data = data[columnsToUse]
normStacked(xValue, data.to_dict(orient = "list"))

