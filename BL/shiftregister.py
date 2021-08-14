from datetime import datetime
from functools import reduce

from tqdm import tqdm

class shift_register:
    def __init__(self, init_state, xor_input, max_clock):
        self.state = init_state
        self.xor_input = xor_input
        self.max_clock = max_clock
        #self.file_name_postfix=int(datetime.now().strftime("%Y%m%d%H%M%S"))



    #def shiffting(self):

        #self.lsfr_shift_reg = []

        # p = tqdm(total=self.max_clock, disable=False)
        # for i in range(self.max_clock):
        #     self.state = next_pulse(self.state, self.xor_input,self.file_name_postfix)
        #     p.update(1)

        # self.lsfr1_key_stream = ""
        # #shift_reg_len = (2 ** (int(self.state[-1])) - 1)
        # shift_reg_len = self.max_clock
        #
        # print(self.lsfr_shift_reg)
        # p = tqdm(total=shift_reg_len, disable=False)
        #
        # with open("keystream.txt", "a") as file_object:
        #     for counter in  range(shift_reg_len):
        #         file_object.write(str(self.lsfr_shift_reg[-1]))
        #         #self.lsfr1_key_stream += str(self.lsfr1_shift_reg[-1])
        #         self.lsfr_shift_reg.insert(xor(self.lsfr_shift_reg,self.xor_input))
        #         del self.lsfr_shift_reg[-1]
        #         p.update(1)
        #     file_object.close()
        #     return self.lsfr1_key_stream

    def xor(self):
            """Computes XOR digital logic
            Parameters:
                :param str state  : Current state of the register
                :param list inputs: Position to tap inputs from register
            Returns:
                :return output: Output of the XOR gate digital logic
                :rtype int :
            """

            """ fisrt i pick element we need to xor each other and put theme in list"""
            bits_to_xor = []
            for i in self.xor_input:
                bits_to_xor.append(self.state[i])

            """ next xor the list elemet usin reduce with lambda func."""
            res = reduce(lambda x, y: x ^ y, bits_to_xor)
            return res



    def next_pulse(self):
        #with open("keystream/keystream%d.txt" % self.file_name_postfix, "a") as file_object:
            output = (int(self.state[-1]))
            # self.lsfr1_key_stream += str(self.lsfr1_shift_reg[-1])
            self.state.insert(0, self.xor())
            del self.state[-1]
            return output

