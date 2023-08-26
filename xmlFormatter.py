
import xml.dom.minidom
  
OriginalXml = '<?xml version= "1.0" ?><gfg>\
<instructor><Name>Sandeep Jain Sir</Name></instructor></gfg>'
temp = xml.dom.minidom.parseString(OriginalXml)
new_xml = temp.toprettyxml()
print(new_xml)
