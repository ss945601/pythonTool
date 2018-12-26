import spaceInfo
from xml.dom import minidom
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


#config of text attribute
#############################
tree = ET.ElementTree(file='B2_main.svg')   # map path
color = "#2E3F6C" # text color
family = "PingFangTC-Semibold, PingFang TC" # text font-faimily
fontSize = "30" # font-size


#get attribute from svg tag for "rect id == p_ or v_"
#############################
allID = []
allX = []
allY = []
allW = []
allH = []
allR = []
spaceList = []
for all_g_tag in tree.iter(tag='{http://www.w3.org/2000/svg}g'):
    if (all_g_tag.attrib.get('id') == 'p' or all_g_tag.attrib.get('id') == 'v'):
        for rectTag in all_g_tag.iter(tag='{http://www.w3.org/2000/svg}rect'):
            if  "p_" in rectTag.attrib.get("id") or "v_" in rectTag.attrib.get("id") or True:
                allID.append(rectTag.attrib.get("id"))
                allX.append(rectTag.attrib.get("x"))
                allY.append(rectTag.attrib.get("y"))
                allW.append(rectTag.attrib.get("width"))
                allH.append(rectTag.attrib.get("height"))
                allR.append(rectTag.attrib.get("transform"))


#set attribute to spaceInfo Object and Output the text svg content
#############################
allText = ""
for i in range(len(allX)):
    id = str(i).zfill(3);
    height = float(allH[i])
    width = float(allW[i])
    x = float(allX[i])
    y = float(allY[i])
    rotate = allR[i]
    space = spaceInfo.Info(id, height, width, x, y, rotate, color, family)
    spaceList.append(space)
    allText = allText + space.getAllInfoText() + "\n"



#set group of all text font Size and insert output content into original svg file
#############################
file = open("B2_main.svg", "r")
svgTxt = file.read()
key = "<gggg/>"
svgTxt =svgTxt.replace("id=\"p\"","id=\"p\"" + " font-size=\"{0}\"" ).format(fontSize)
svgTxt =svgTxt.replace("id=\"v\"","id=\"v\"" + " font-size=\"{0}\"" ).format(fontSize)
svgTxt =svgTxt.replace(key,"\n" + allText)


#write file
#############################
output = open("output.svg","w")
output.write(svgTxt)

