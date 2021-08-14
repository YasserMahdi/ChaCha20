from datetime import datetime

from tqdm import tqdm

from BL.shiftregister import shift_register


class threshold:
      def __init__(self,function1,function2,function3,oxr_input,max_clock):
          self.lsfr1=function1
          self.lsfr2=function2
          self.lsfr3=function3
          self.oxr_input = oxr_input
          self.max_clock = max_clock
          self.file_name_postfix = int(datetime.now().strftime("%Y%m%d%H%M%S"))


      def start_key_streamming(self):
          p = tqdm(total=self.max_clock, disable=False)
          for counter in range(self.max_clock):
              shift1 = shift_register(self.lsfr1, self.oxr_input, self.max_clock)
              s1 = shift1.next_pulse()
              shift2 = shift_register(self.lsfr2, self.oxr_input, self.max_clock)
              s2 = shift2.next_pulse()
              shift3= shift_register(self.lsfr3, self.oxr_input, self.max_clock)
              s3 = shift3.next_pulse()

              with open(r"C:\Users\yasse\PycharmProjects\dsc\keystream\threshold\keystream%d.txt" % self.file_name_postfix, "a") as file_object:
                  combine = str(int((bool(s1) & bool(s2)) ^ (int(bool(s1) & bool(s3)) ^ (int(bool(s1) & bool(s2))))))
                  file_object.write(combine)
                  p.update(1)



