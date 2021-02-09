from math import log, sqrt

class Pricer():

  def __init__(self, choice, sigma, maturity, strike, stock_price, risk_free_rate):
    
    self.choice = choice
    self.sigma = sigma
    self.T = maturity
    self.K = strike
    self.S = stock_price
    self.rf = risk_free_rate

    self.d1 = (log(self.S/self.K)+(self.rf + 0.5 *(self.sigma**2)*self.T)) * 1/(self.sigma * sqrt(self.T))

    self.d2 = self.d1 - self.sigma * sqrt(self.T)

  def get_BS_price(self):

    if self.choice == "call":
      price = 