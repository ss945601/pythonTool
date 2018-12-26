#coding=utf-8
class Info:
    def __init__(self, id, height, width, x, y, rotate, color, family):
        self.id = id
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.rotate = rotate
        self.color = color
        self.family = family
    def getAllInfoText(self):
        strSpace = ""
        if self.width > self.height:
            strSpace = "<text x=\"{0}\" y=\"{1}\" fill=\"{2}\" style=\"stroke-width:0.1px\" alignment-baseline=\"middle\"  text-anchor=\"middle\" font-family=\"{3}\" letter-spacing=\"4\">{4}</text>".format(str(self.x+0.5*self.width),str(self.y+0.5*self.height),self.color,self.family,self.id)
        if self.height > self.width:
            strSpace = "<text x=\"{0}\" y=\"{1}\" transform=\"{2}\" style=\"text-align:center; stroke-width: 0.1px ;writing-mode:vertical-lr;text-orientation:upright;text-anchor:middle;\" fill=\"{3}\" letter-spacing=\"-14\" font-family=\"{4}\" >{5}</text> ".format(str(self.x+0.5*self.width+7),str(self.y+0.5*self.height+4),self.rotate,self.color,self.family,self.id)
        return strSpace
