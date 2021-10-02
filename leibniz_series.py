import numpy as np
import matplotlib.pyplot as plt

class Leibniz_Series_Approximation():
    """
    This approximation creates a finite, alternating series to calculate pi.
    
    """
    
    def __init__(self, n=100):
        
        self.n = n
        
        
    def approximate_pi(self):
        """
        Function to approximate pi by a finite, alternating sum.

        """
        
        # approximate pi with a Leibniz series
        pi_app = 4*sum((-1)**i/(2*i + 1) for i in range(self.n))
        
        error = round(100*abs(pi_app - np.pi)/np.pi,6)
        
        return 'Approximation of pi: {}, error: {}%'.format(pi_app, error)
    
    
    def series_plot(self):
        """
        Function to plot the series by the number of iterations.

        """
        
        fig, ax = plt.subplots(1)
        
        # for loop to create bar plots
        for x in range(self.n+1):
            ax.bar(x-1, 4*sum((-1)**i/(2*i + 1) for i in range(x)),
                   width=0.5,
                   alpha=0.2,
                   align='edge',
                   edgecolor='b',
                   color='g')
        
        # create red line to indicate pi
        ax.axhline(y=np.pi, color='r').set_linewidth(0.5)

        plt.xlim(-0.25,self.n + 1)
        plt.ylim(-0.25,4.25)
        
        plt.grid(linestyle='--')

        plt.title('Leibniz Series converting to pi', fontsize=8)
        
        plt.show()