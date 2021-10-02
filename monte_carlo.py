import numpy as np
import matplotlib.pyplot as plt

class Monte_Carlo_Estimator():
    """
    This estimator creates a monte-carlo-simulation. The simulation builds n 
    points on a area of 2x2 (uniformly distributed) and returns the ratio of 
    the number of points that landed in the unit circle compared with the one 
    who do not.
    
    """
    
    def __init__(self, n=1000):
        
        self.n = n
        self.x = np.random.uniform(-1,1,self.n)
        self.y = np.random.uniform(-1,1,self.n)
        
        
    def estimate_pi(self):
        """
        Function to estimate pi given n uniformly distributed points on a area 2X2.
        
        """
        
        # count all points that are in the unit circle
        count_unit = sum(1 if (self.x[i]**2 + self.y[i]**2 <= 1) else 0 
                         for i in range(self.n))
            
        # calculate pi estimation
        pi_est = 4*count_unit/self.n
        
        # determine the error
        error = np.round(100*abs(pi_est - np.pi)/np.pi, 4)
        
        return 'Estimation of pi: {}, error: {}%'.format(pi_est, error)
    
    def circle_plot(self):
        """
        Function to plot the unit circle and the simulated points.
        
        """
        
        seq = np.linspace(0, 2*np.pi, 100)

        u = np.cos(seq)
        v = np.sin(seq)
        
        fig, ax = plt.subplots(1)
        
        # for loop to plot the points and color them
        for i in range(self.n):
            if self.x[i]**2 + self.y[i]**2 <= 1:
                ax.plot(self.x[i],self.y[i],'r.')
            else:
                ax.plot(self.x[i],self.y[i],'b.')

        ax.plot(u, v)

        ax.set_aspect(1)

        plt.xlim(-1.25,1.25)
        plt.ylim(-1.25,1.25)

        plt.grid(linestyle='--')

        plt.title('plot unit circle for pi estimation', fontsize=8)
        
        plt.show()