class Dac:
  def __init__(self, analog_voltage, max_Analog_Voltage, bits): #constructor
    while not ( analog_voltage >= 0 and analog_voltage <= max_Analog_Voltage ) :
      analog_voltage = float(input(" analog volage out of range. Please enter an analog voltage between 0-" + str(max_Analog_Voltage) + ": "))
    self.analog_voltage = analog_voltage
    self.max_Analog_Voltage = max_Analog_Voltage
    self.bits = bits


  def convert_dec_to_binary(dec, bits_number):
    result = ""
    while dec>0:
      if dec%2==0:
        result="0"+result
      else:
        result="1"+result
      dec=dec//2
    while(len(result) < bits_number):
      result = "0" + result
    return result


  def convert_binary_to_dec(binary, bits_number):
    while len(binary) > bits_number:
      binary = input("Too much bits. Please enter binary num of " + str(bits_number) + " bits: ")
    while len(binary) < bits_number:
      binary = "0" + binary
    dec = 0
    counter = bits_number - 1
    for i in range(bits_number):
      dec += (2**counter) * int(binary[i])
      counter -= 1
    return dec

  
  def ToDigital(self):
    bits_options = 2**self.bits
    re = self.max_Analog_Voltage/bits_options

    digital = bits_options - 1

    for i in range(0,bits_options - 1):
      if re*(i)<=self.analog_voltage and self.analog_voltage<re*(i+1):
        digital = i
    return Dac.convert_dec_to_binary(digital, self.bits)    

  def SetDigitalValue(self, value):
    bits_options = 2**self.bits
    re = self.max_Analog_Voltage/bits_options
    value = Dac.convert_binary_to_dec(value, self.bits)
    if value == bits_options - 1:
      self.analog_voltage = self.max_Analog_Voltage
    else:
      self.analog_voltage = re*value



def main():
  obj1 = Dac(10.5, 11, 12)
  print(obj1.ToDigital())
  obj1.SetDigitalValue("1101")
  print(obj1.ToDigital())


if __name__ == "__main__":
    main()