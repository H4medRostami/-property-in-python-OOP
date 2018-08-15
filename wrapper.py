class list_wrapper:
    def __init__(self,list_value=[],slice_num=2):
        self.__list_value=list_value # _ before variable means private class variable.
        self.slice_num=slice_num
        
    def wrapper(self):
        for i in range(len(self.__list_value)):
            if i == self.slice_num-1 :
                print(self.__list_value[:self.slice_num])
                del self.__list_value[:self.slice_num]
                return self.wrapper()
    @property
    def list_value(self):
        print("Getting value")
        return self.__list_value

    @list_value.setter
    def list_value(self, value):
        if type(value) != list:
            raise ValueError("only list type")
        print("Setting value")
        self.__list_value = value
        
        
      
