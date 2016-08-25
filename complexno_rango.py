from __future__ import division
class ComplexNumber: 

	def __init__(self,a=0,b=0):
		if not (isinstance(a,int) or isinstance(a,float)):
			raise TypeError("Real part should be a real number")
		if not (isinstance(b,int) or isinstance(b,float)):
			raise TypeError("Imaginary part should be a real number")
		self.a = a
		self.b = b

	def __str__(self):
		if(self.b < 0):
			return "%.4f - i%.4f"%(self.a,-self.b)
		else:
			return "%.4f + i%.4f"%(self.a,self.b)

	def __add__(self,other):
		return ComplexNumber(self.a + other.a, self.b+other.b)

	def __sub__(self,other):
		return ComplexNumber(self.a - other.a, self.b-other.b)

	def __mul__(self,other):
		c = (self.a*other.a - self.b*other.b)
		d = (self.a*other.b + self.b*other.a)
		return ComplexNumber(c,d)

	def __truediv__(self,other):
		mod = (other.a)**2 + (other.b)**2
		if(mod==0):
			raise AssertionError("Cannot divide by zero.")
		otherT = ComplexNumber(other.a/mod,-other.b/mod)
		return self*otherT

	def __eq__(self,other):
		return (self.a == other.a and self.b == other.b)

	def __ne__(self,other):
		return not self==other