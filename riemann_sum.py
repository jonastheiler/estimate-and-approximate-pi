import math
import numpy as np
import matplotlib.pyplot as plt

class Riemann_Sum_Approximation():
    """
    This object approximates the area of a quarter circle by a finite (=n) sum. 
    Furthermore, it provides a method to plot what is going on.
    
    """
    
    def __init__(self, n=100):
        
        self.n = n
    
    
    def approximate_pi(self):
        """
        Function to approximate the integral of a quarter of the unit circle.
        
        """
        # divide in n sectors
        d = 1/self.n
        
        # function to approximate pi by summing the areas of the bars
        pi_app = 4*d*sum(math.sqrt(1 - x**2) for x in np.linspace(0,1,self.n + 1))
        
        # calcute the error
        error = round(100*abs(pi_app - np.pi)/np.pi,6)
        
        return 'Approximation of pi: {}, error: {}%'.format(pi_app, error)
            
        
    def bar_plot(self):
        """
        Function to plot a quarter of the unit circle and the approximation
        with n intervals.

        """
        
        d = 1/self.n
        
        seq = np.linspace(0, 0.5*np.pi, 25)

        u = np.cos(seq)
        v = np.sin(seq)
        
        fig, ax = plt.subplots(1)
        
        # for loop to create the bar plots
        for x in np.linspace(0,1,self.n + 1):
            ax.bar(x, math.sqrt(1 - x**2),
                   width=d,
                   alpha=0.2,
                   align='edge',
                   edgecolor='b',
                   color='g')

        ax.plot(u, v)

        ax.set_aspect(1)

        plt.xlim(-0.25,1.25)
        plt.ylim(-0.25,1.25)

        plt.grid(linestyle='--')

        plt.title('plot unit circle for pi approximation', fontsize=8)
        
        plt.show()