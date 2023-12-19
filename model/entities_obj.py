class Module:
    # rpw will stand for (name, descrition)
    def __init__(self,row):
        self.name = row[0]
        self.description = row[1]

# Questions
class Questions:
    def __init__(self,name,order,text,type):
        self.name = name
        self.order = order
        self.text = text
        self.type = type







