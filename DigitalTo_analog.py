class Dac:
  def __init__(self, analog_voltage): #constructor
    while not ( analog_voltage >= 0 and analog_voltage <= 5 ) :
      analog_voltage = float(input("Please enter an analog voltage between 0-5: "))
    self.analog_voltage = analog_voltage


  def convert_dec_to_binary(dec):
    result = ""
    while dec>0:
      if dec%2==0:
        result="0"+result
      else:
        result="1"+result
      dec=dec//2
    while(len(result) < 10):
      result = "0" + result
    return result


  def convert_binary_to_dec(binary):
    while len(binary) > 10:
      binary = input("Too much bits. Please enter binary num of 10 bits: ")
    while len(binary) < 10:
      binary = "0" + binary
    dec = 0
    counter = 9
    for i in range(10):
      dec += (2**counter) * int(binary[i])
      counter -= 1
    return dec

  
  def ToDigital(self):
    re = 5/1024

    if self.analog_voltage==5:
      digital = 1023

    for i in range(0,1024):
      if re*(i)<=self.analog_voltage and self.analog_voltage<re*(i+1):
        digital = i
    return Dac.convert_dec_to_binary(digital)    

  def SetDigitalValue(self, value):
    re = 5/1024
    value = Dac.convert_binary_to_dec(value)
    if value == 1023:
      self.analog_voltage = 5
    else:
      self.analog_voltage = re*value



def main():
  obj1 = Dac(5)
  print(obj1.ToDigital())
  obj1.SetDigitalValue("010")
  print(obj1.ToDigital())


if __name__ == "__main__":
    main()