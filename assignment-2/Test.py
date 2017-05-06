import itertools

class Test():
    fac_nodes = {'f_a': {'nbs': ['Influenza'], 'p_1': [0.05]}, 
                 'f_b': {'nbs': ['Smokes'], 'p_1': [0.2]},
                 'f_c': {'nbs': ['SoreThroat', 'Influenza'], 'p_1':[0.3, 0.001]},
                 'f_d': {'nbs': ['Fever', 'Influenza'], 'p_1': [0.9, 0.05]},
                 'f_e':{'nbs': ['Bronchitis', 'Influenza', 'Smokes'], 'p_1': [0.99, 0.9, 0.7, 0.0001]},
                 'f_f':{'nbs': ['Coughting', 'Bronchitis'], 'p_1': [0.8, 0.07]},
                 'f_g': {'nbs': ['Wheezing', 'Bronchitis'], 'p_1': [0.6, 0.001]}}

    influenza = [0.95, 0.05]
    smokes = [0.8, 0.2]
    soreThroat = [[0.999, 0.001], [0.7, 0.3]]
    fever = [[0.95, 0.05], [0.1, 0.9]]
    bronchitis = [[[0.9999, 0.0001], [0.3, 0.7]], [[0.1, 0.9], [0.01, 0.99]]]
    coughting = [[0.93, 0.07], [0.2, 0.8]]
    wheezing = [[0.999, 0.001], [0.4, 0.6]]

    def __init__(self):
        pass

    def calculate_joints(self):
        lst = list(itertools.product([0, 1], repeat=7))

        joints = []
        for states in lst:
            joint = self.calculate_joint(states)

            joints.append((states, joint))

        return joints

    def calculate_joint(self, states):
        _in, _sm, _so, _fe, _br, _co, _wh = states
        joint = self.p_inf(_in) * self.p_smok(_sm) * self.p_sor(_so, _in) * self.p_fev(_fe, _in) *\
                self.p_cou(_co, _br) * self.p_whe(_wh, _br) * self.p_bronch(_br, _in, _sm)
        print self.p_inf(_in), self.p_smok(_sm), self.p_sor(_so, _in), self.p_fev(_fe, _in),\
                self.p_cou(_co, _br), self.p_whe(_wh, _br), self.p_bronch(_br, _in, _sm)

        return joint  

    def p_inf(self, state=0):
        return self.influenza[state]

    def p_smok(self, state=0):
        return self.smokes[state]

    def p_sor(self, state=0, given_1=0):
        return self.soreThroat[given_1][state]

    def p_fev(self, state=0, given_1=0):
        return self.fever[given_1][state]
    
    def p_cou(self, state=0, given_1=0):
        return self.coughting[given_1][state]
    
    def p_whe(self, state=0, given_1=0):
        return self.wheezing[given_1][state]

    def p_bronch(self, state=0, given_1=0 ,given_2=0):
        return self.bronchitis[given_1][given_2][state]


if __name__ == '__main__':
    test = Test()
    print test.calculate_joints()
    # print test.calculate_joint([1,1,1,1,1,1,1])
    # print test.calculate_joint([0,0,0,0,0,0,0])
    # print 0.05 * 0.2 * 0.3 * 0.9 *0.99 * 0.8 * 0.6

