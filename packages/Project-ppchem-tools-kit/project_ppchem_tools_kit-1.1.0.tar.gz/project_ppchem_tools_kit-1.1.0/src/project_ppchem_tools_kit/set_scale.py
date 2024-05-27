from tkinter import simpledialog
import matplotlib.pyplot as plt

def set_scale(ax, plot_canvas):
    """Sets the scale of the x and y axes.

    Args:
        ax (matplotlib.axes.Axes): The Axes object containing the plot.
        plot_canvas (FigureCanvasTkAgg): The canvas on which the plot is drawn.
    """
    x_spacing = simpledialog.askfloat("X Spacing", "Enter spacing between x ticks:")
    y_spacing = simpledialog.askfloat("Y Spacing", "Enter spacing between y ticks:")
    if x_spacing and y_spacing:
        ax.xaxis.set_major_locator(plt.MultipleLocator(x_spacing))
        ax.yaxis.set_major_locator(plt.MultipleLocator(y_spacing))
        plt.tight_layout()
        plot_canvas.draw_idle()