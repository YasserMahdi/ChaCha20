class analyzer:
    def __init__(self, poly_function):
        self.function = poly_function


    def convert_pol_to_bin(self):
        #split poly function base on addition sign
        self.function = self.function.split('+')
        if (self.function[-1] == '1'):
            self.function.reverse()

        #remove x var and power sing
        for i in range(len(self.function)):
            self.function[i] = self.function[i].replace("x", "1")
            self.function[i] = self.function[i].replace("1^", "")
#                elif(len(self.init_state) == 1 and int(x) == 1):
 #                   flag = 1
        #convert power value to init state for shift reg.
        flag = 0
        if(self.function[0]!= self.function[1]):
            self.init_state = []
            for i in range(0, int(self.function[-1])):
                for x in self.function:
                    if (len(self.init_state) == int(x) - 1):
                        flag = 1
                if (flag == 1):
                    self.init_state.append(1)
                else:
                    self.init_state.append(0)
                flag = 0
            return self.init_state, self.function[-1]
        else:
            self.init_state = [1,1]
            for i in range(2, int(self.function[-1])+1):
                for x in self.function:
                    if (len(self.init_state) == int(x)):
                        flag = 1
                if (flag == 1):
                    self.init_state.append(1)
                else:
                    self.init_state.append(0)
                flag = 0
            return self.init_state, self.function[-1]




