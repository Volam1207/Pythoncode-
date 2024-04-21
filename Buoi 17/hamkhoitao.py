class car:
        name = ''
        weight = 0
        model = ''
        color = ''
        def __init__(self,name,weight,color,model) -> None: #khoitaodoituong
            self.name = name
            self.weight = weight 
            self.color = color 
            self.model =  model
        def start(self):
            print("run!")
        def dive(self):
             pass
        def stop(self):
             pass
        def brake(self):
            pass
        def toString(self):
             pass
vinfast = car('v',1000,'black','vf8')
print('vinfast')
