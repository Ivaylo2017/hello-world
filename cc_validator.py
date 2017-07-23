class CreditCard():

	counter = 0

	def __init__(self, cc_num):
		self.cc_num = cc_num
		self.cc_type = self.checkType()
		self.cc_valid = self.isvalid()
		CreditCard.counter += 1

	def checkType(self):
		visa = ['4']
		mc = ['51','52','53','54','55']
		amex = ['34','37']
		disc = ['65','6011']

		if self.cc_num[0] in visa:
			self.cc_type = "Visa"
		elif self.cc_num[:2] in mc:
			self.cc_type = "MasterCard"
		elif self.cc_num[:2] in amex:
			self.cc_type = "AMEX"
		elif self.cc_num[:2] in disc or self.cc_num[:4] in disc:
			self.cc_type = "Discover"
		else:
			self.cc_type = "Invalid cc type"
		return self.cc_type 
			 

	def isvalid(self):
		if self.cc_type == "Visa" or self.cc_type == "MasterCard" or self.cc_type == "Discover" and len(self.cc_num) == 16:
			return self.checkLuhn()
		elif self.cc_type == "AMEX" and len(self.cc_num) == 15:
			return self.checkLuhn()
		else:
			return False

	def checkLuhn(self):
		sum = 0
		even = False
		reversed_cc_num = self.cc_num[::-1]
		for i in reversed_cc_num:
			n = int(i)
			if even:
				n *= 2
				if n > 9:
					n -= 9
				sum += n
				even = False
			else:
				sum += n
				even = True
		if sum%10 == 0:
			return True
		else:
			return False

	def __str__(self):
		if self.cc_valid == True:
			return "This is a valid {} credit card".format(self.cc_type)
		else: 
			return "The credit card number is invalid"


	def main(self):
		#cc = input("Please enter a credit card number for validation: ")
		#validation = CreditCard(cc)
		print(self)
		print("{} validations performed so far.".format(CreditCard.counter))

cc1 = CreditCard("9857495874045895")
cc1.main()
cc2 = CreditCard("5564593830084095")
cc2.main()
cc3 = CreditCard("5129925266193252")
cc3.main()

