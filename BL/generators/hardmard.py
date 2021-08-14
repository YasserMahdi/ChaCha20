from datetime import datetime
import threading

from tqdm import tqdm

from BL.shiftregister import shift_register


class hardmard:
      def __init__(self,function1,function2,xor_input1,xor_input2,max_clock):
          self.lsfr1=function1
          self.lsfr2=function2
          self.xor_input1 = xor_input1
          self.xor_input2 = xor_input2
          self.max_clock=max_clock
          self.file_name_postfix = int(datetime.now().strftime("%Y%m%d%H%M%S"))

      def start_key_streamming(self):
          p = tqdm(total=self.max_clock, disable=False)
          for counter in range(self.max_clock):
            shift1=shift_register(self.lsfr1,self.xor_input1,self.max_clock)
            x=shift1.next_pulse()
            shift2 = shift_register(self.lsfr2,self.xor_input2,self.max_clock)
            y=shift2.next_pulse()

            with open(r"C:\Users\yasse\PycharmProjects\dsc\keystream\hardmard\keystream%d.txt" % self.file_name_postfix, "a") as file_object:
                combine = str(int(bool(x) and bool(y)))
                file_object.write(combine)
                p.update(1)





