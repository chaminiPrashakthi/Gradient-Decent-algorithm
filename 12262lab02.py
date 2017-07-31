import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

class GCD():
	#function to plot the figure
	def plot_fig(): 
		plt.figure(figsize=(8,8))
		plt.title('Gradient Descent Alogorothem', fontsize=15)
		plt.xlabel('X Axis',fontsize=13)
		plt.ylabel('Y Axis',fontsize=13)

		x= [i for i in range(-100,100)]
		y=[4*i**2+2*i+2 for i in x]
		plt.plot(x,y,color='g',label='f(x)=4x^2-2x+2')
		plt.legend(loc=0)
		plt.show()


	#function to get the minima of the function
	def find_value(self,precision,learning_rate,current_x):

		step_size=abs(current_x)
		
		while(step_size>= precision):
			previous_x=current_x
			y = (8*current_x)-2
			current_x = current_x-(learning_rate*y)
			step_size= abs(current_x-previous_x)
			
		print current_x
		return current_x
		
	plot_fig() #call plot function to execute
		


#Test cases
import unittest
class Test(unittest.TestCase):
	
	def setUp(self):
		self.object=GCD()
		print("set up")
	
	def test_find_value1(self):
		self.object = GCD()
		test1=self.object.find_value(0.0000001,0.01,0.5)
		self.assertEquals(test1,0.2500010927943874)
	
	def tearDown(self):
		print("tear down")
		
	
if __name__== '__main__':
	unittest.main()