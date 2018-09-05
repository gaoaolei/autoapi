class CommonUtil:
    ''' 该类用于比较期望结果和实际结果 '''
    def contain(self, expect, result):
        if expect in result:
            return True
        else:
            return False
