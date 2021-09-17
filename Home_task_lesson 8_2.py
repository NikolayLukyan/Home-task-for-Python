class MyException(Exception):

   def div_with_exc(self, divider, denominator):

      try:
         if denominator == 0:
            raise MyException('Divide on zero is forbidden.\n')
      except MyException as err:
         print(err)
      else:
         res = round(divider / denominator, 2)
         print(f"{divider} / {denominator} = {res} \n")


MyException().div_with_exc(38, 12)
MyException().div_with_exc(28, 12)
MyException().div_with_exc(25, 0)
MyException().div_with_exc(12, 12)
