import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker


def set_up_plotting(width,height,title):

    plt.style.use('seaborn-white')
    plt.rcParams["xtick.labelsize"] = 14
    plt.rcParams["ytick.labelsize"] = 14
    plt.rcParams["font.size"] = 14
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'
    plt.rcParams['legend.facecolor'] = 'white'
    plt.rcParams['axes.linewidth'] = 0
    
    fig = plt.figure(figsize=(width,height), num = title)
    ax = fig.add_subplot(111)

    ax.xaxis.set_tick_params(which = 'major',length = 10, width = 2)
    ax.yaxis.set_tick_params(which = 'major',length = 10, width = 2)
        
    ax.xaxis.set_tick_params(which = 'minor',length = 6, width = 1.5)
    ax.yaxis.set_tick_params(which = 'minor',length = 6, width = 1.5)
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero') 
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')    

    return (fig,ax)
