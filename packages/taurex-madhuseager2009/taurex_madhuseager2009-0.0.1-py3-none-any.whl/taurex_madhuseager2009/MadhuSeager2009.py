from taurex.temperature import TemperatureProfile
import numpy as np
from taurex.data.fittable import fitparam
import scipy as sp
from taurex.exceptions import InvalidModelException

class InvalidTemperatureException(InvalidModelException): 
    """
    Exception, called when atmosphere mix is greater than unity
    """
    pass



class MadhuSeager2009(TemperatureProfile):
    """

    TP profile from Madhusudhan and Seager 2009, arXiv:0910.147v2

    Parameters
    -----------
        T_top: float
            temperature at the top of the atmosphere in Kelvin
        P_top: float
            pressure at the top of the atmosphere in Pascal (TauREx default)
        T_1,2,3: float
            temperature at Layer 1,2,3 (deepest layer) of the atmosphere in Kelvin
        P_1,2,3: float
            pressure at Layer 1,2,3 (deepest layer) of the atmosphere in Pascal (TauREx default)
        alpha_1,2: float
            multiplicative factor
            the lower the value the steeper the Layer 1 gradient
        beta_1,2: float
            multiplicative factor
            the lower the value the steeper the Layer 2 gradient
    """

    ### Initializing the new class
    def __init__(self, T_top = 1000, P_top = 1, T_1 = 1400, T_2 = 1100, T_3 = 1500, P_1 = 700, P_2 = 9000, P_3 = 1e5, alpha_1 = 50, alpha_2 =50, beta_1 = 0.5, beta_2 = 0.5):
        super().__init__('Madhuuuuuu')

        self.info('MadhuSeager2009 temperature profile initialised')
        self._T_top = T_top
        self._P_top = P_top
        self._T_1 = T_1
        self._T_2 = T_2 
        self._T_3 = T_3
        self._P_1 = P_1 
        self._P_2 = P_2 
        self._P_3 = P_3 
        self._alpha_1 = alpha_1
        self._alpha_2 = alpha_2 
        self._beta_1 = beta_1
        self._beta_2 = beta_2
    
    ### Defining the get and set function for the fitting parameter 'mean'
    @fitparam(param_name='T_top',
              param_latex='$T_{top}$',
              default_fit=False,
              default_bounds=[300.0,2000.0])
    def topTemperature(self):
        return self._T_top
    
    @topTemperature.setter
    def topTemperature(self, value):
        self._T_top = value
        
    @fitparam(param_name='P_top',
              param_latex='$P_{top}$',
              default_fit=False,
              default_bounds=[1,700])
    def topPressure(self):
        return self._P_top
    
    @topPressure.setter
    def topPressure(self, value):
        self._P_top = value
    
    @fitparam(param_name='alpha_1',
              param_latex= '$\\alpha_{1}$',
              default_fit=False,
              default_bounds=[0.15,0.35])
    def oneAlpha(self):
        return self._alpha_1
    
    @oneAlpha.setter
    def oneAlpha(self, value):
        self._alpha_1 = value
    
    # a note on the fitting boundaries
    # for alpha 2: madhu seager 2009
    # IRS data set constrains α2 to be greater than 0.2
    # broadband photometry data set constrains to be 0.18 - 0.35 
    # HST data set constrains to be 0.15 - 0.27
    
    @fitparam(param_name='alpha_2',
              param_latex= '$\\alpha_{2}$',
              default_fit=False,
              default_bounds=[0.15,0.35])
    def twoAlpha(self):
        return self._alpha_2
    
    @twoAlpha.setter
    def twoAlpha(self, value):
        self._alpha_2 = value
        
    @fitparam(param_name='T_1',
              param_latex='$T_{1}$',
              default_fit=False,
              default_bounds=[300.0,2000.0])
    def oneTemperature(self):
        return self._T_1
    
    @oneTemperature.setter
    def oneTemperature(self, value):
        self._T_1 = value
    
    @fitparam(param_name='T_2',
              param_latex='$T_{2}$',
              default_fit=False,
              default_bounds=[300.0,2000.0])
    def twoTemperature(self):
        return self._T_2
    
    @twoTemperature.setter
    def twoTemperature(self, value):
        self._T_2 = value
        
    @fitparam(param_name='T_3',
              param_latex='$T_{3}$',
              default_fit=False,
              default_bounds=[300.0,2000.0])
    def threeTemperature(self):
        return self._T_3
    
    @threeTemperature.setter
    def threeTemperature(self, value):
        self._T_3 = value
    
    @fitparam(param_name='P_1',
              param_latex='$P_{1}$',
              default_fit=False,
              default_bounds=[1e5,1])
    def onePressure(self):
        return self._P_1
    
    @onePressure.setter
    def onePressure(self, value):
        self._P_1 = value
    
    @fitparam(param_name='P_2',
              param_latex='$P_{2}$',
              default_fit=False,
              default_bounds=[1e5,1])
    def twoPressure(self):
        return self._P_2
    
    @twoPressure.setter
    def twoPressure(self, value):
        self._P_2 = value
        
    @fitparam(param_name='P_3',
              param_latex='$P_{3}$',
              default_fit=False,
              default_bounds=[1e5,1])
    def threePressure(self):
        return self._P_3
    
    @threePressure.setter
    def threePressure(self, value):
        self._P_3 = value
    
    ### The key of this class, this provides the temperature profile.
    ### This 'profile()' function is mandatory for all classes inheriting from the TemperatureProfile class.

    
    def check_profile(self,Ppt): 

        for i in range(len(Ppt)-1):
            if Ppt[i+1] - Ppt[i] < 0:
                self.warning('Temperature profile is not valid! PLEAAASE Michelle, give the man some right P points! :) ')
                raise InvalidTemperatureException

         # P1 < P2 < P3 as a condition 
        #if not (any(Ppt[i] <= Ppt[i+1] for i in range(len(Ppt)-1))): 
        #    self.warning('Temperature profile is not valid! A pressure point is inverted.')
        #    raise InvalidTemperatureException

    
    @property
    def profile(self):
        """Returns stratified pressure-temperature layer with two constraints of continuity at the two layer boundaries, i.e., Layers 1–2 and Layers 2–3
        """

        self._T_2 = self._T_top + np.power( (1/self._alpha_1)*np.log(self._P_1/self._P_top) , 1/self._beta_1) - np.power( (1/self._alpha_2)*np.log(self._P_1/self._P_2) , 1/self._beta_2)
        self._T_3 = self._T_2 + np.power( (1/self._alpha_2)*np.log(self._P_3/self._P_2) , 1/self._beta_2)
        # continuity conditions from MaduSeager 2009
        
        P = self.pressure_profile
        T = np.zeros((self.nlayers))

        less_P = [self._P_top,self._P_1,self._P_2,self._P_3]
#         print(less_P)
        self.check_profile(less_P)
        # check that P still viable--and that they follow the convention P_top < P_1 < P_2 < P_3 
    
        for i, p in enumerate(P):
            if (p > self._P_top ) and (p < self._P_1):
                T[i] = self._T_top + np.power( (1/self._alpha_1)*np.log(p/self._P_top) , 1/self._beta_1)
            elif (p > self._P_1) and (p < self._P_3):
                T[i] = self._T_2 + np.power( (1/self._alpha_2)*np.log(p/self._P_2) , 1/self._beta_2)
            elif (p > self._P_3):
                T[i] = self._T_3
            else:
                T[i] = self._T_top
                # isothermal in deepest layers of atm
            
        return T
    

    ### This is to tell TauREx what outputs to save
    def write(self, output):
        temperature = super().write(output)
        temperature.write_scalar('T_top', self._T_top)
        temperature.write_scalar('P_top', self._P_top)
        temperature.write_scalar('T_1', self._T_1)
        temperature.write_scalar('T_2', self._T_2)
        temperature.write_scalar('T_3', self._T_3)
        temperature.write_scalar('P_1', self._P_1)
        temperature.write_scalar('P_2', self._P_2)
        temperature.write_scalar('P_3', self._P_3)
        temperature.write_scalar('alpha_1', self._alpha_1)
        temperature.write_scalar('alpha_2', self._alpha_2)
        temperature.write_scalar('beta_1', self._beta_1)
        temperature.write_scalar('beta_2', self._beta_2)
        return temperature

    ### This is the keyword to use in the parfile
    @classmethod
    def input_keywords(cls):
        return ['MadhuSeager2009', 'madhuseager2009']