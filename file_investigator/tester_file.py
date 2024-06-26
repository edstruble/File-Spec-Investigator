from PIL import Image

img = Image.open("headshot.jpg")
# img_data = np.array(img)
mode = img.mode
info = img.info
width = img.width / 300
height = img.height / 300
file_res = info.get('dpi')
photoshop_info = info["photoshop"][1005]
# photoshop_res = photoshop_info[1]["Xresolutoin"]

print(f"Width: {width}")
print(f"Height: {height}")
print(f"File Res: {file_res}")
print(photoshop_info)
# print(info)

# st.write("File Res", file_res)
# st.write("Photoshop res", photoshop_info)
# st.write(info)
# st.write("File mode:", mode)

test = {
    1028: b'\x1c\x01Z\x00\x03\x1b%G\x1c\x02\x00\x00\x02\x00\x00\x1c\x027\x00\x0820240513\x1c\x02<\x00\x0b221544-0400',
    1061: b'\xb9\xf33\xa0\x05\xbe;-\xc1P=\x1e\xd1\xbcu\xc4',
    1082: b'\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x0bprintOutput\x00\x00\x00\x05\x00\x00\x00\x00PstSbool\x01\x00\x00\x00\x00Inteenum\x00\x00\x00\x00Inte\x00\x00\x00\x00Clrm\x00\x00\x00\x0fprintSixteenBitbool\x00\x00\x00\x00\x0bprinterNameTEXT\x00\x00\x00\x01\x00\x00\x00\x00\x00\x0fprintProofSetupObjc\x00\x00\x00\x0c\x00P\x00r\x00o\x00o\x00f\x00 \x00S\x00e\x00t\x00u\x00p\x00\x00\x00\x00\x00\nproofSetup\x00\x00\x00\x01\x00\x00\x00\x00Bltnenum\x00\x00\x00\x0cbuiltinProof\x00\x00\x00\tproofCMYK',
    1083: b'\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x12printOutputOptions\x00\x00\x00\x17\x00\x00\x00\x00Cptnbool\x00\x00\x00\x00\x00Clbrbool\x00\x00\x00\x00\x00RgsMbool\x00\x00\x00\x00\x00CrnCbool\x00\x00\x00\x00\x00CntCbool\x00\x00\x00\x00\x00Lblsbool\x00\x00\x00\x00\x00Ngtvbool\x00\x00\x00\x00\x00EmlDbool\x00\x00\x00\x00\x00Intrbool\x00\x00\x00\x00\x00BckgObjc\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00RGBC\x00\x00\x00\x03\x00\x00\x00\x00Rd  doub@o\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00Grn doub@o\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00Bl  doub@o\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00BrdTUntF#Rlt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Bld UntF#Rlt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00RsltUntF#Pxl@r\xc0\x00\x00\x00\x00\x00\x00\x00\x00\nvectorDatabool\x01\x00\x00\x00\x00PgPsenum\x00\x00\x00\x00PgPs\x00\x00\x00\x00PgPC\x00\x00\x00\x00LeftUntF#Rlt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Top UntF#Rlt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Scl UntF#Prc@Y\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10cropWhenPrintingbool\x00\x00\x00\x00\x0ecropRectBottomlong\x00\x00\x00\x00\x00\x00\x00\x0ccropRectLeftlong\x00\x00\x00\x00\x00\x00\x00\rcropRectRightlong\x00\x00\x00\x00\x00\x00\x00\x0bcropRectToplong\x00\x00\x00\x00',
    1005: {
        'XResolution': 300.0,
        'DisplayedUnitsX': 1,
        'YResolution': 300.0,
        'DisplayedUnitsY': 1},
    1062: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x80\x00\x00',
    1010: b'\x00\x00\xff\xff\xff\xff\xff\xff\x00\x00',
    1037: b'\x00\x00\x00\x1e',
    1049: b'\x00\x00\x00\x1e',
    1011: b'\x00\x00\x00\x00\x00\x00\x00\x00\x01', 10000: b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01', 1013: b'\x00/ff\x00\x01\x00lff\x00\x06\x00\x00\x00\x00\x00\x01\x00/ff\x00\x01\x00\xa1\x99\x9a\x00\x06\x00\x00\x00\x00\x00\x01\x002\x00\x00\x00\x01\x00Z\x00\x00\x00\x06\x00\x00\x00\x00\x00\x01\x005\x00\x00\x00\x01\x00-\x00\x00\x00\x06\x00\x00\x00\x00\x00\x01', 1016: b'\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00', 1032: b'\x00\x00\x00\x01\x00\x00\x02@\x00\x00\x02@\x00\x00\x00\x00', 1092: b'\x00\x00\x00\x02\x00\x00\x02@\x00\x00\x02@\x00\x00\x00\x00', 1054: b'\x00\x00\x00\x00', 1050: b'\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x084\x00\x00\x07\x08\x00\x00\x00\x08\x00h\x00e\x00a\x00d\x00s\x00h\x00o\x00t\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x08\x00\x00\x084\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00null\x00\x00\x00\x02\x00\x00\x00\x06boundsObjc\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00Rct1\x00\x00\x00\x04\x00\x00\x00\x00Top long\x00\x00\x00\x00\x00\x00\x00\x00Leftlong\x00\x00\x00\x00\x00\x00\x00\x00Btomlong\x00\x00\x084\x00\x00\x00\x00Rghtlong\x00\x00\x07\x08\x00\x00\x00\x06slicesVlLs\x00\x00\x00\x01Objc\x00\x00\x00\x01\x00\x00\x00\x00\x00\x05slice\x00\x00\x00\x12\x00\x00\x00\x07sliceIDlong\x00\x00\x00\x00\x00\x00\x00\x07groupIDlong\x00\x00\x00\x00\x00\x00\x00\x06originenum\x00\x00\x00\x0cESliceOrigin\x00\x00\x00\rautoGenerated\x00\x00\x00\x00Typeenum\x00\x00\x00\nESliceType\x00\x00\x00\x00Img \x00\x00\x00\x06boundsObjc\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00Rct1\x00\x00\x00\x04\x00\x00\x00\x00Top long\x00\x00\x00\x00\x00\x00\x00\x00Leftlong\x00\x00\x00\x00\x00\x00\x00\x00Btomlong\x00\x00\x084\x00\x00\x00\x00Rghtlong\x00\x00\x07\x08\x00\x00\x00\x03urlTEXT\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00nullTEXT\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00MsgeTEXT\x00\x00\x00\x01\x00\x00\x00\x00\x00\x06altTagTEXT\x00\x00\x00\x01\x00\x00\x00\x00\x00\x0ecellTextIsHTMLbool\x01\x00\x00\x00\x08cellTextTEXT\x00\x00\x00\x01\x00\x00\x00\x00\x00\thorzAlignenum\x00\x00\x00\x0fESliceHorzAlign\x00\x00\x00\x07default\x00\x00\x00\tvertAlignenum\x00\x00\x00\x0fESliceVertAlign\x00\x00\x00\x07default\x00\x00\x00\x0bbgColorTypeenum\x00\x00\x00\x11ESliceBGColorType\x00\x00\x00\x00None\x00\x00\x00\ttopOutsetlong\x00\x00\x00\x00\x00\x00\x00\nleftOutsetlong\x00\x00\x00\x00\x00\x00\x00\x0cbottomOutsetlong\x00\x00\x00\x00\x00\x00\x00\x0brightOutsetlong\x00\x00\x00\x00', 1064: b'\x00\x00\x00\x02?\xf0\x00\x00\x00\x00\x00\x00', 1044: b'\x00\x00\x00\x06', 1036: b'\x00\x00\x00\x01\x00\x00\x00\x89\x00\x00\x00\xa0\x00\x00\x01\x9c\x00\x01\x01\x80\x00\x00\x13\xc0\x00\x18\x00\x01\xff\xd8\xff\xed\x00\x0cAdobe_CM\x00\x01\xff\xee\x00\x0eAdobe\x00d\x80\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x0c\x08\x08\x08\t\x08\x0c\t\t\x0c\x11\x0b\n\x0b\x11\x15\x0f\x0c\x0c\x0f\x15\x18\x13\x13\x15\x13\x13\x18\x11\x0c\x0c\x0c\x0c\x0c\x0c\x11\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x01\r\x0b\x0b\r\x0e\r\x10\x0e\x0e\x10\x14\x0e\x0e\x0e\x14\x14\x0e\x0e\x0e\x0e\x14\x11\x0c\x0c\x0c\x0c\x0c\x11\x11\x0c\x0c\x0c\x0c\x0c\x0c\x11\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\xff\xc0\x00\x11\x08\x00\xa0\x00\x89\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xdd\x00\x04\x00\t\xff\xc4\x01?\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x02\x04\x05\x06\x07\x08\t\n\x0b\x01\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x10\x00\x01\x04\x01\x03\x02\x04\x02\x05\x07\x06\x08\x05\x03\x0c3\x01\x00\x02\x11\x03\x04!\x121\x05AQa\x13"q\x812\x06\x14\x91\xa1\xb1B#$\x15R\xc1b34r\x82\xd1C\x07%\x92S\xf0\xe1\xf1cs5\x16\xa2\xb2\x83&D\x93TdE\xc2\xa3t6\x17\xd2U\xe2e\xf2\xb3\x84\xc3\xd3u\xe3\xf3F\'\x94\xa4\x85\xb4\x95\xc4\xd4\xe4\xf4\xa5\xb5\xc5\xd5\xe5\xf5Vfv\x86\x96\xa6\xb6\xc6\xd6\xe6\xf67GWgw\x87\x97\xa7\xb7\xc7\xd7\xe7\xf7\x11\x00\x02\x02\x01\x02\x04\x04\x03\x04\x05\x06\x07\x07\x06\x055\x01\x00\x02\x11\x03!1\x12\x04AQaq"\x13\x052\x81\x91\x14\xa1\xb1B#\xc1R\xd1\xf03$b\xe1r\x82\x92CS\x15cs4\xf1%\x06\x16\xa2\xb2\x83\x07&5\xc2\xd2D\x93T\xa3\x17dEU6te\xe2\xf2\xb3\x84\xc3\xd3u\xe3\xf3F\x94\xa4\x85\xb4\x95\xc4\xd4\xe4\xf4\xa5\xb5\xc5\xd5\xe5\xf5Vfv\x86\x96\xa6\xb6\xc6\xd6\xe6\xf6\'7GWgw\x87\x97\xa7\xb7\xc7\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xf3\xc4\x92I\x04\xb3\xa5\x81\xee \xf6\x12\x8a(g\x87\xe2Tq\x04\xd8\xef\xea\xff\x00\x10\xad\xb5\x92S\xe3\xb2\xc3v\x8d\x98\xb5\x1e[?2\x88\xdc\x1aO\xe6~\'\xfb\xd5\x9a\xeb\'\x85\x7f\x07\x02\xdc\x9c\x8a\xf1\xe8a\xb2\xebN\xda\xd8;\x9f\xf5\xf7=\x1d;\x04j\xe7\xd3\xd2j\xb5\xec\xad\x94\x9b,\xb1\xc1\x95\xb1\xa5\xc5\xces\x8c5\xad\x13\xf9\xca\xeb>\xaa\xd9c\x9e\xca\xb1\x8d\xce\xa9\xdb,\xf4\x9f\xbc5\xde\x0f\xdbg\xb3\xfa\xef\xf6\x7f\x9e\xbaft\xfcN\x93X\xb2\xf6E\xdf\xce\x07\xbc9\xb7m\x00\xfan\xf4\xf7m\xc3\xab"\xdf\xa1\x8e\xef\xd7_O\xf4\xbbj\xf5~\xc7NC\xb2\x9bM\xb9Y-w\xe8\xc5lm\xb1\xc4\x97\xfac\xfe\xa90H\x13\xb2\xfe\x13Z\x96\x96\x0f\xd5\x1b:\x86\xb8\x95\xb1\xedi"\xc7:\xcd\x9e\x9cF\xef]\x96\xb9\x96\xd7\xf4\xbfs\xfe\xae\xb4\xb2\xfe\xaac\xe02\xb7f\xdf]o\xb4\x172\x9a\xc5\x96\xd9\xb6`=\xec\xdd_\xa6\xd7\x7fYi7\xa9UM99\x0f>\xe6?m\x91\xf9\xce,h\xd9\xfc\xafs\x9a\xa6\xcck,\x9b\xf3\x1cFC\xe0\x96\xfe\xe3F\xb5\xb5\xdf\xca\xfd\xca\x93\xbe\xc4W\x9b\x89\xff\x005\xcd\xb8\xf6da\x86\xe5\xb2\x9f\xe7\xabf\xf6\xdc\xc1\xfe\x93\xec\xb6{\xed\xab\xfe\x13\x1b\xd7T\x0e\x05\x11!\x9a\x1e5?\xde\xbb\x8e\x84\xc7\xfd\xb5\xf9T\xfe\x8a\xa6\x12K\x8e\xa5\xc4h?\xb5\xff\x00\x90Y\x9fXz}t\xe43+\x1e\xb1^6h.mm\x93\xb6\xc6\xff\x00<=\xdf\xe9w3!\x9f\xf1\xa9\x026\xa0\x83c\xab\xca\xbb\x12\xa1\xc3\x7f\x12\xa3\xf6j\xbfw\xf1+B\xca\xf5B,\t\xdav\x08\xd7\xb9s\xb2je{v\x88\x99\x9f\xc1\x05[\xea\x02=?\xed\x7f\xdfUD\xc9n\xba;)$\x92M\\\xff\x00\xff\xd0\xf3\xc4\x92I\x04\xb60\xbf\x9dw\xf5\x7f\x88W\xabl\xb9Q\xc1\xfeu\xdf\xd5\xfe!j\xe3\xd7&S\x86\xcbN\xed\xba*\x00I[\xfd$S\xd3\xb0m\xeb6\x12.;\xf1\xf1[\xd8L6\xfc\x86\x98\xfal\xf7P\xb1[\xedi\xf2Z\xbdJ\x8c\x8f\xf9\xba\xc8\xf5=G\x16\x8a+\xb9\xa2\xbb\x08\'kCjh\xfa\x1a\xff\x00\xc6\xa6H\xae\x80\xb2\xe2u.\xb3v@\xbe\xb2\xed--s<ZX6\xb5\xae\xfeC\x95\x1a\x0eK\xf0\x9d\x8c\xf9&\xfb\x03\x9d<\xedd9\x9f\xf4\xf7.\xb3\xa5\xfdV\xc7\xc7`9QvA\x1e\xf2ukO\xe72\xb9\xfd\xd5\xb6\xce\x97\x80\x03C\xabl\x8e\t\x1a\xa8\xcex\x8d\x00l\x8e\\\x91d\xbc&>>E~\x9b\xedi\xfd\x1b\x8d\xaclO\xe9\x1ew\xfa\xceo\xf8K[?\xa1\xfd\xcf\xe7U\xd6\xb36\xef\xcd#\x9d\xac\x1d\xa7\xe9=\xef\xfc\xeb\x9d\xff\x00Av6\xf4\xfcW\xbbt\x0f\x0f\xbdHa\xd6\xd6\xe9\x08}\xe3\xc1G\x97\xf1y\x9cL\x9b\xaa\xbd\x94X=0\xc06\xd4\x06\x81\xbe+K\xae\xe2\xd5\x7fM\x19\x8dv\xda\xe8n\x8c<\x97\xbd\xec\x0c\xdb\xfdf\xba\xdd\xea\xe6\x7fH\xa7\xa8S\xe9\x13\xb2\xdf\xf06\x8d\x0b]\xe7\xfb\xd5\xbb\xfc#\x15Ga\xdc\xef\xab\xd6\xef\ru\xcc\xdc\xcd\x8f;"\xd1\xfa=\x81\xd0\xf6\xb9\xef\xfa\x14\xfa\x9f\xf6\xea\x96\x13\x12\xd40e\xc6`\xf2W3M\x15R5WL9\x81\xc3V\x91 \xf9\x15]\xec\x82\xa5\x05\x85\xcc\xeab=/\xed\x7f\xdfU%{\xaa\xff\x00\x81\xfe\xd7\xfd\xf5QM\x96\xeb\xc6\xcaI$\x93R\xff\x00\xff\xd1\xf3\xc4\x92I\x04\xb6\xbap\x9b\xdd\xfdO\xe2\x16\xd5\r\x80\xb1\xfaP\x9c\x87\x7fS\xf8\xb5nV4G\xa2\xd2\x99\xa65\xf0\xf9\xae\x83\xa5b\xd2\xccL\x1cWV\xd6\xbe\xa3\xeb<\x1b\r\xcfi>\xf6\x8b,>\xd6\xbd\xdb\xbf\x9am\x7f\xa3X\rf\xf6\x96\xce\xd2\xe0@w\x81<;\xfb+_\xea\xd5M\xa3\x16\xba[\x02\xc2\xdd\xceh\x1c~n\xe5\x0eS\xe9f\xc2=N\xec\x92\xe2G\x8e\xa0#\xb2\x87\xbc\t\xd0\xf2\x10Zk\xabW<\x02{L)}\xb4VD\xfd\x1f\x10UM[\xc1?\xa2\xe09\xfb\x94\xbd/\xf5\x847\xe7\xd0\xe0\t#\xe2\x93r\xd8\xf1\xfa=~\t\xc0\x15\x16Ll<O\x88T\xba\x9b^\xdcl\xdaZ\xd0~\xd0\xf0\x00:\xb4\xef\xf6\xed\x7f\xf2\\\xe77z\xd0k\x9a\xe2\x15/\xac>\xa3q\xad8\xfa\xdc\xd6\xb6\xe2\xc3\xfe\x8d\x9e\xe7\xd9\x1f\xc9\xda\xaca\r>`\xec\xf0\xedc\xfd&o\x10\xed\xa3p\xf3\xfc\xef\xfaH\x16\xb5h[\'S\xa9:\x93\xe6U+\xda\xac\x06\xb3\x8f\xd5\x7f\xc0\xff\x00k\xfe\xfa\xa8+\xfd[\xfc\x0f\xf6\xbf\xef\xaa\x82\x07u\xc3e$\x92H%\xff\xd2\xf3\xc4\x92I\x04\xb7:Q\x8c\x87\x7fS\xf8\xb5n\xd6A\x01at\xbf\xe9\x0f\xfe\xa7\xf1j\xdc\xa8h\x12(\xea\xe8t\xfcC\x9b\x95^(\xb1\x94z\xa4\x83m\x9a1\xb0\x0b\xbd\xdf\xd6\xdb\xb1\xab\xa0\xc6\xc6\xfb&gR\xbc\xb45\x8cv\xd6\x01\xf4yq\xda\xc9\xfc\xc5\x85\xd2\x9c\xd6\xe6\xd3\xb8nc\xdd\xe9\xbd\xb12,\x0e\xa8\xe9\xfd\xb5\xd2aR\x06\x1d\xd8\x9e\xb0\xc8\xb6\xab\ro\xb8O\xb9\xcdhl{\xbf\xd1\xc6\xdd\xdf\x9e\xab\xe6:WF\xce\x08\n\xe2\xbdx\xb8k\xc3\x85\xe6\xba\x9ef;7?72\xda\xecx\x91]-\xde\xe1\xe7\xc2\xa5WU\xc9\xaa\xba\xee\xae\xe7]\x8ba"\xb2\xf6\x16\xee\xdb\xf4\xa3\xdc\xe6\xfew\xe6\xad\xec\x8f\xab\x1b^\xf7m\xf5E\xdf\xce\xb9\xd0K\xa7\xb7-\xdb\xb7\xf9.QoBi\xa5\x95m\r\xa2\x92K\x07\xf2\x9d\xf4\x88\x93\xf4\xdd\xfb\xe9\x91\x94)\x90\xc2|B\xaa\xbf\x16\xc7L\xae\xfc\xcc_[g\xb1\xe3p\x8e!a\xe6\xf5\xbc\xbc[_M6\x166\xa96=\xad\xdd\x02v\xf9.\xe7\xa6P\xca\xb0\x1b\x8e\xc0\x03Cv\x85\x85\xd4\xbe\xaf\xcd\x8e\xb00\x16<\x16>d\xe9\xcf\xbe?7\xf9I@\x8b\xd5~A-\x81htn\xa1\x8f\x96\xf6\xba\x9e\xa0\xebr\t\xdc\xd69\x9b&?sw\xd3\xff\x009uN\xc6~[\xdfi\xb1\xb5}\xa7\x01\xd8\xbb\x9f\xf4\x1a\xe7>\xc7\xd8\xe7q\xfe\r\xab\x07\x13\xea\xedl\xa9\x8dc\x00\xf4\\,\xa1\xcd\xe5\xaf\x90\xe3`t\xb9\xdb\x9d\xb7g\xbb\xf3\x16\xeeF\xcazf\xeb\xfe\x9bC\xddQ\xd4{\xdb\xb5\xcc\xff\x00\xc1\x14\xd0\x90\xb3\xc3\xf8\xb5\xa7\x13\xa7\x1e\x82\xf5\xe1\xfd\x8f\x19\x97_\xa5s\xea\x90v9\xcc\x91\xc1\xdav\xe9\xfc\x95J\xd0\xac\xdau#\x98U\xde\xa6\rg\x13\xac\x084\xff\x00k\xfe\xfa\xb3\x96\x9f\\\x11\xe8\x7fo\xfe\xf8\xb3\x12;\xae\x1b)$\x92A/\xff\xd3\xf3\xc4\x92I\x04\xb7:W\xf4\x87\xff\x00S\xfe\xfc\xd5\xbb^\x8b\x07\xa5\x9f\xd6\x1d\xfdO\xe2\xd5\xb9Y\xd0$P\xdf\xc3~\xcbX\xfe\xed \x8f\x92\xe9j\xf4\xe87\x9a\x1d,\xb2\xcfY\xb2 \x8fT\x0b}7\x7fQ\xce\xda\xb9J\x8e\xb1\xd9oaf\xd9\x93\x96\xf1q\x05\xe5\x8d"\x04H\x83\xcf\xf2\xb4Pf\x1a6yyU\x8b\xea\r;8\xd79\xcd\xfd#\x89\x1e||\x15N\xa3\xd4h\xaeM\xcf\xf4\xa8\xa8\x17\xdc\xf0$\xc7\xee\xb5/T\xb2GuG\xa8e`\xd9I\xc2l[k\xc6\xeb\x1cxh\x1a\xee?\xe8\xd5`5n\x19\xc6"\xcb\xa9\xd3\xba\xff\x00JuA\xc6\xe6\xb6\x96\xb7y\xc8%\xbb\x03\x7f\xd29\xee-n\xd5f\xbc\xfa\x1e\x18\xeamnF5\xed\xdf]\x8d\xee>\x8a\xe4\x1a+\xc3\xfd\rm\xae\xd3c\x0b\xacf\xc6\xba\x18\x0c\xfal\xa9\xcdeNs\x9b\xfaOKb\xdd\xc5\xc9\xe9\xa7\x11\xb8\xec\rad9\x8f\xaev\xc1\xe1\xfb]\xfe\r\xff\x00\xf8\x1a\x94\x80\x06\x8c^\xe0&\xcb\xac\xf65\xae\xdd^\x80\xea@\xee\xa9}a\xb0\xfe\xce\xab\xc7qh\x03\xcc\x02\xe7+8\xae\x05\x8d$\xeeoc\xc8?\xd5Y\xbfXm\r\xd9F\xbbZ\xd9\xf9\x9f\xfc\xc5K\x88P%\xaf\x9c\xf4y\x9b&L\xaa\xef:\xab\x16\x99*\xad\x87U0k\x17+\xae\x1f\xe8\xff\x00\xdb\xff\x00\xbe,\xb5\xa3\xd6I&\x9f\xed\xff\x00\xdfVr%#e$\x92H%\xff\xd4\xf3\xc4\x92I\x04\xb6\xbai\x8b\xdd\xfd_\xe2\x16\xddN\x04\x05\x83\x84b\xd2\x7f\x93\xfcB\xd7\xc7\xb3P\x12(o\xb1\xda\xab\xb4d}\x9c\xfd\xa2`\xb4D\xfc=\xd0\xb3\xda\xac\xd9eta5\xf6\x82\xef\xb4[\xe8\xd4\x01\x8f\xa0\xd3}\xf6\xf1\xee\xf4\x9b\xe9\xb7g\xef\xda\x98cv\xbe&\x8bg\xa8uW\xe44\n\xa5\x8d\x90^\xc1\xe67l.\xff\x00\xabY\x85\xf9nk\xbe\xce\xd2\xe0\xf3\x0e \xe93\xf4\xac\xdb\xef\xb3\xdc\xab\x07\xe4d\r\x95\xc3\x003\xea\x18.\r\xd3\xdc\xef\xcd\xdf\xff\x00\x90\x7f\xee-o\xab\xe5\x87 \xe3\x17\x10\xdeK\xcf\x1a\x02\\7{wY\xedP\x98\xf0\x8b\xa6a+:\xa7\xaf\xa3uL\xbcF\xc3\xb1\xb5$\xef\x87z\x80\xf3\x0ev\xcd\xdb\xb5T2*\xeb]9\xed~Ee\xd5\xd7?\xa4l\xc1i3\xc3\xa1\xcd\xda\xefz\xdc\xab#)\xb7z\x8e\xb5\xecc\x9e\xe050\x00\x01\xc0\xff\x00eX\xeb9F\xec\x17TN\xfb\xb6\xfb\xf7k\xa7\xe7w\xfa;R\x12\xe9K\xf2J$\n\x8dS\x0e\x87\xd7(w\xe8lp\x8d\x08\x9eb~\x9f\xfeIV\xea\xb9m\xca\xc9\xb2\xc6\xf6q\x04\xf1\xd9\xaeo\xf9\xab3\xa7\xb0T\xc2\xea\xe06\x1c\xdd\xa7R6\x8f\xdf\x8f\xd23v\xcd\x9f\xe1\x19\xf9\xfe\xcf\xe7-_Yc\x18\xe8 =\xa4\xb6N\xe9\x01\xce\x12\x1d\xf9\xde\xdd\x8ax\xc6\x81j\xcaVi\xa7aUl(\xf7;\x95M\xe7T\xf0\xb0\xb9\xbd_\xfc\x0f\xf6\xbf\xef\xab=_\xea\xdf\xe0\x7f\xb5\xff\x00}T\x12;\xa4l\xa4\x92I\x04\xbf\xff\xd5\xf3\xc4\x92I\x04\xa5\xc6\xfep\xfc\x16\x85N\x82\x16~1\r{\x8b\xb4\x1b\x7f\x8a\xd5\xe9\x98\x19\x9dA\xc4\xe2\xd7\xba\xb6j\xfb\x9d\xed\xad\xbd\xfd\xd6\xbb\xdb\xff\x00m\xefzp\x04\xec\x86\xee7\xa9k\xd9Um/\xb1\xe7k\x18\xdeI\xf0G\xeb5zY\xbd;\x108=\xb5\xe2\xde\xeb\x03{\xd8\xedl\xd8\xe2?\xab\xe9\xbdkt\xfc*z~(,\x8b\xf2n\x07}\x9bN\x8d\xfc\xd61\xbfI\x94\xfbw\xfe\xfd\xdf\xe1\x7fG\xfa5\x99\xd5KGQ\xa3"\xe3\x15\xb3\x19\xf1&@qv\xdd\xda\x7f\x85w\xe6\x7f\x84\xd9\xff\x00\x06\x89\x8dD\xf7(\x12\xb9\x0f\x079\x8f\x18\xd8\xe5\x8e\x03y~\xf2\x00\xe1\xa0\x11>\xef\xa5\xefW\xf0\xddUoh\xaa7\xd8\xd7o\xb0\x8f\xa2\x1a\xcf^\xef\xa3\xfc\x8d\x95\xb3\xfe\xb8\xb2:\xbeC$S\\\x07\xd8\xd0\xeb\\$\xed\x10"\xae\x1d\xf9\xceb~\x8bm\x9fk\xf4\x9c}\xcfi\xa8\x87{A\x01\x96\xd4\xc7s\xfc\xef\xbb\xf3\x94&\x16\x0b/\x13\xb4:\xab\xec\xb1\xa6\xb6\xed\xa8h\xe2y\x005\xcec?\xf2i\xcfQ\x15[.$\xd2\xdd\x1a\xfdH\x01\xc7\xdc\x07\xd2\xfc\xcd\xff\x00\xebb\xc6s\xfd7\xba\x935\x87\x00\xe6\x83\xcbKu\xbbO\xea\xfb?\xd6\xa4[\xdfs\rN\r.?H\x1e\xc1\xc02\xcd\xde\x99\xfc\xea\x99\xe9z~\xa7\xfcu\xa9G\x18T\xa6i\xd7\x18{2\xad\xd8&\xbbw\xb4\x01\xa0k\xc1#a\xd7\xe8Y\xf4\xebW1\xaa\xb7>\x97\xe1U\x1e\xadC\xd4\xa1\x8e\x86\x17<\x162\xfa\xb7?k\x7fIU\x8c\xb3\xf9v\xd3\xff\x00\x08\xabb\xb2\xc6P\xdd\xce/q\x15\xbe\x1ad\xb9\x96{\x1dM{\x88\xdc\xfd\xed\xab\xe9\xbe\xbb}\x9f\xf6\xe6\xae5u\xb3%\xcc\x11\xefc\xb7\x81\xc1s\x86\xd69\xba7v\xea\xfd\xcf\xf6\x7f\x82S\xc2=;\xb0N]^w)\x96\xd3k\xa9\xba\xb7Uk>\x95v4\xb5\xc3\xfb\x0f\xda\xe5E\xee]mV\xe3\xe6\xd3^7Q\xa7\xed5m\xdfX2,\xac\xfd\x1b=\x1b\x99\x16\xd5\xee\x1f\x9b\xfa?\xf8%\x97\xd4~\xa9\xe5\xb5\xa6\xee\x94\xf3\x9bP\xd5\xd8\xe6\x06C\x7f\xa9\x1bj\xcao\xfcW\xa7o\xfc\n\'\x1dm\xaa\x04\xc1\xdfG\x94\xeaf}/\xed\x7f\xdfU%s\xa9\x02\rm \xb5\xcd.\x0ei\x04\x10F\xd9k\x9a\xefs\\\xa9\xa8\xce\xec\x83e$\x92H%\xff\xd6\xf3\xc4\x92I\x04\xba\xbfV\xdd\x84\xcc\xdb\x9f\x99MW\x81I\xf4}a\xbd\x8c\xb3{?M\xe8\x9f\xd1\xde\xf6\xd7\xbf\xd3\xae\xdf\xd1\xae\x93/2\xe2\xda\xb1*%\x96\xdd\x069\xf4\xab\x9d\xde\xe9\xff\x00\rw\xf3\x96\x7f\x98\xb9\x9f\xab\xf6\xd3Ne\xb7Z7l\xa8\x966&]\xb9\x9by\xf6\xad\xec=\xfe\xa3\xae\xb6]}\xb2\xe7L\xc8\x1c{\x9d\xfc\xa5,6c\x96\xee\xd3\xeb\x8a\xdbX?\xa3k[\xb2d\x88h\x1f\xf7\xe5\xce\xfd`\xb0\x81\x8e\xf6\xc1xs\x9a\xc6\xc6\x83w\x1c~\xf3\x99\xfaO\xcf\xff\x00\x84]\x06E\xbe\xd2Z@cF\xae\'kF\x9d\xdc\xf3\xb5\xbf\xd7\\\x7fZ\xea]=\xee57 \\\x7f8\xd5\xee\x00N\xb3i>\x9f\xf9\x9e\xa2R\xd9Q\xdd\x0e;\x1dm\xa2\xd3\xb5\xc4\x1d\xees\x88\x80`\xfalh\x1fI\xdfO\xf3\xff\x00?\xf4\x8bq\x98/ch. ]c@w\'i\x7f\xb9\xfb\x1a\xed\xbfN\xa7o\xfeo\xf44\xaa\x9d0Q\x85O\xda\x08k\xf2\x1a\xd8\xa5\x80\xcbY\r;\x8b\x1b\xf9\xce\xdf\xec{\xff\x00\x91\xff\x00n[\x17\x1fS\xed\x17\x96\xbd\xcf\xf6\xb5\xa6^\xd2\xff\x00t\xb9\xee~\xd6\xfa5\xfa\x8d\xb7#\xfc\xcf\xf4U\xa8\xcb#\x9feM~x\ri$\xd6+\r\'q\xd9\xfc\xeb\xdfv\xc2\xef\xe6\xb1\xdb\xfc\xdf\xfe\xab[Xu\xb7 C\x08\xf5E\x83\xd0q=\xda\xd0==\xcd\xfa_\xe1j\xf5\x7f\xd3\x7f\xc1V\xb1\x19n\xdc\xebN\xc0\xe0\xf2\xc8\x1f\xc8x\xf5M\xd6\xff\x00\xa4\xb7g\xd0b\xd2\xe8V\xb9\xa6+w\xba\xd0]\'@\\\xd2]E\xccq\xf6\xb2\xcf\xcc\xbd\x88\x84I?L\xba\x96\xda\xea\xc7\xe8\xa9\xad\xc1\xd64j\xd6l&\xe7z\x1fK\xd1m\x7f\xcd\xfe\x8d\x9f\xa5\xb2\xff\x00M]\xc5\xc8.\xb0\xbc\xea,\xfd#|Ed\xbd\xdc\xb3\xf7\xad\xff\x00\xb7\x16O]\xab\x0f\x1b g9\xe7\x1e\x8c\xc7C\xc3\xdav\xb1\xe0\xff\x006=-\xcc\xfd\x1b\xab\xb3\xfe\xdb\xaf\xd4\xff\x00H\xb4pm\xc7\xcaq4dU~\xe1\xee\x15\xbd\xae#\x9f\xf0`\xee\xdd\xfd\x95$7b\x9e\xcbTv>\xcaH?\xa3y\xb2\xb2\x07\xe6\x93\xefo\xf6w+t\xe6\x9a\xde\x0bH\r?\xbc@\x13\xf8mY\x8e\xbc\xe3u\xc2$\x8a\xaep\xd3\x80\t\x1e\x9d\x91\xcf\xd3b\x8d\xb7\x1an\xb0\x11\xb1\xedv\xbcI\x03\xe6\x9e\xb1\x07\xd7\xfc\x86d\xb7\xa6\xdaZ=o\xd3\xb6\xc7\xf2\xe2\xd1\xe8\xfam}\x9fN\xcd\x9e\xed\xbb\xd7$\xb7\xfe\xb4\xbfu8\x1a\x10\x07\xab\x1cG\xf8.!`(g\xf3\x16h|\xa1I$\x92b\xf7\xff\xd7\xf3\xc4\x92I\x04\xb7\xba9\x03%\xe4\xf2+\xd3M\xda\xeeoe\xd1c9\xbe\xa3\'_\x1e\xff\x00\x7f\xe6.w\xa3\x89\xc9\x7f\x95d\xfe-[\xb4\xbc\xfa\xcc1.\x1f\x19\x1f\x86\xd6\x7f\x9e\xa5\x86\xcb%\xbb\x91\xd503s2\x1df^S\xad\xafq,a\xf6\xb5\xb3\xd9\x8c\xfa+6\xfc\x06\xe3\x96\xb9\x9a\xc7q\xe2\x16\xfeC\x87\xaa\xe0\x1d\xdf\xe9w\xf8*w\xb7\xd4\xdc\x08\x93\xe3#\xf2#AKcf7\xd5m@\x13\xe8\xd4\xe3Es\xed\x10\x18\xf7Wctu\x9fG\xd5o\xfa\xfas\xb3-\xa6\xa6\xd8\xf7z\xc2\xd2\x01\xf0s\xe0j\xf9\xdb\xeckk\xdf_\xfaO\xf0k3#x\x1a{m\xa8{H\x91-\xf9&\xab8z\xeei\xfek 5\xb7\x8bD\x82\xe1\xf9\xc7\xd3\xff\x00\xc0\xae\xaf\xd3\xb1FB\xe0[V^\xda\xb2\xfd\xee\x1e\x95\x95\xb4\xef<N\xe7[N\xef\xce\xf7\x7f%i\xd7p\xa5\xd8\xc0\x82\xdfM\xf62\xcf\x1d\xd0v\xeew\xbb\xf4Os\xab\xdc\xb0n\xba\x8c\x97}\xa5\xfb\xaa\xad\x87o\xa5\x1b\x88\xdb\x1e\x9bk\x7f\xb3\xf7U\xaf\xb7Y\xed\xba\xa6\xc6\xe6\x91\xfaOs\x81y\xfd5\x9b\xc45\xce{wl\xf6\xa4\x02\x89v\xb2\xb2NC\x1d\x87\x90\x01nC\x1be\x83C\xfaZ\xfd?\xd37o\xb7\x7f\xef\xbf\xf3\xff\x00K\xea*\xb8\xbd;\x02\xeb\xe2\xdaZ\xe0\xe1;\x84\x83?\xbc\x1e\xcd\xae@\xe9N\xb6\xfb,\xbb!\xc5\xeeq\xd5\xff\x00\xeb\xf9\xaa\xf3\xdb\xe9Z\xcb\x1b\xf4A\xd4\x95(\x1a1\x13\xabk\xacV\x18\xda\xec\xac:+\r\r$\xef0\xdd\x04\xb9\xees\xb7"g\x96\xe4b\xd7\x92\xd8\x9b\x19\x04\x08\x1e\xe1\xa3\xbf\xf2H\xf9MnN =\x88\x82V_M\xc8p\xae\xfc\x1b?\xc1\xfb\xd9\xa4\xc8\x1a=\x15\xbf\xb1\xce\xea\xd6z\x988G\xbb]sO\xc8T\xb3\x15\xcc\xf265\xa3\xf3m\xb3\xf1\x15\xaaj\x19\xfc\xc5\x9a\x1f(RI$\x9a\xb9\xff\xd0\xf3\xc4\x92I\x04\xb7:Q\x8c\x87\x9f\xe4\x7f\xdf\x9a\xb5\xea|\x13\xa4\x01\xf3+\x0f\n\xda\xea\xb5\xce\xb0\xc0-\x80`\x9dd~\xea\xbb\xf6\xfc`\xd8\x16O\x90\x0e\x1f\xc1I\x12+u\xa4j\xd8\xb1\xe1\xc4\x92wx\xe8`\xf9~\xea\x0b\x9cH;\x81\x03\xcb\xfd\xc8N\xcc\xa0\x88\xdf\xcf\x80?\xf9\x15\x03\x93\x8e\x7f<\x7f\x9aO\xe5\t\xd6;\xa2\x96\xbe\xa2\xff\x00s\x04\xb9\xbe\x07\x90\xa8\xddG\xbc\x06\x8f\xa7\xa7\xbbH\xd2w\x19\xfc\xd6+\x86\xfa?z~\x00\x8f\xc8\xa0\xcb\xab\x0e\xb1\xfb\x8b]\xf4k$n\xf6\xe8\xe7\xf3\xfe\x93\xe8\xfe\xfa\x16;\xabT\x0f\xa1\xae,\xa9\x80\xc0\xee\x7f\xe9=\xdf\xd6V\x8dP\xdd\xa0p#\xba\x8dv\xd4\xd7s\x1eq\xfe\xc4Gd\xd0t\xdd\xf8\x18J\xc7p\x8a=\x9b\xdd5\x81\x95\x9f?\x97\xf1V\xaf\r,\xd0}\xc4q\xf7\xac\xfc|\xecZ\xdb\xf4\xc3Oq\xb4\xff\x00\xe4Q]\xd4\xb0\x8bH\xf5N\xbd\x83H\xff\x00\xbe\xa7X\xee\x11G\xb3\xab\x81h~;\xea\x8f{D\x81\xfe\xbb\x96oRi\xc4\xc9\xab9\xa2Z\xd2=A\xe28{x\xfc\xe6\xa1\xe3\xf5<Z\xac\x0f\xdf\x11\xa1\xd1\xc6G\x7f\xcdD\xc8\xea]>\xfa,\xa5\xd7{\\4\x86:\'\xeeK\x88w\n\xa3\xd9\xcc\xcd\x01\xb2\xc0w\x06\xddf\xd7x\xb6+5\xbb\xfc\xd7*\xaao\xb3}U4\x99s\x01k\x8f\x8cCX\xef\xedV\xc6((\xa5\xba\xf8\xec\xa4\x92I5s\xff\xd9', 1057: b'\x00\x00\x00\x01\x01\x00\x00\x00\x0f\x00A\x00d\x00o\x00b\x00e\x00 \x00P\x00h\x00o\x00t\x00o\x00s\x00h\x00o\x00p\x00\x00\x00\x14\x00A\x00d\x00o\x00b\x00e\x00 \x00P\x00h\x00o\x00t\x00o\x00s\x00h\x00o\x00p\x00 \x002\x000\x002\x004\x00\x00\x00\x01', 1030: b'\x00\x05\x00\x00\x00\x01\x01'}

test_dict = {
    "total": 1498,
    "state": "0",
    "limit": 10,
    "offset": 0,
    "data": {
        "0": {
            "Pi": "18165592935938996736",
            "Ph": "keyword 1",
            "Kb": 20190326,
            "Tg": {},
            "Cp": "2.25",
            "Nq": "260",
            "Gs": "0",
            "Dt": {
                "20191225": {
                    "*.mysite.com\/*": 7
                }
            },
            "Be": {
                "*.mysite.com\/*": 7
            },
            "Fi": {
                "*.mysite.com\/*": 7
            },
            "Diff": {
                "*.mysite.com\/*": 0
            },
            "Diff1": {
                "*.mysite.com\/*": 93
            },
            "Diff7": {
                "*.mysite.com\/*": 93
            },
            "Diff30": {
                "*.mysite.com\/*": 93
            },
            "Vi": {
                "20191225": {
                    "*.mysite.com\/*": 0.0068999999999999999
                },
                "Diff": {
                    "*.mysite.com\/*": 0
                }
            },
            "Sf": {
                "20191225": [
                    "adt",
                    "rev",
                    "stl"
                ]
            },
            "Tr": {
                "20191225": {
                    "*.mysite.com\/*": 0.32000000000000001
                }
            },
            "Tc": {
                "20191225": {
                    "*.mysite.com\/*": 0.73999999999999999
                }
            },
            "Lu": {
                "20191225": {
                    "*.mysite.com\/*": "https:\/\/www.mysite.com\/product.cfm?p=155"
                }
            },
            "Lt": {
                "20191225": {
                    "*.mysite.com\/*": [
                        "org"
                    ]
                }
            }
        },
        "1": {
            "Pi": "1090615528833642752",
            "Ph": "keyword 2",
            "Kb": 20190326,
            "Tg": {},
            "Cp": "0.81",
            "Nq": "390",
            "Gs": "0",
            "Dt": {
                "20191225": {
                    "*.mysite.com\/*": 3
                }
            },
            "Be": {
                "*.mysite.com\/*": 3
            },
            "Fi": {
                "*.mysite.com\/*": 3
            },
            "Diff": {
                "*.mysite.com\/*": 0
            },
            "Diff1": {
                "*.mysite.com\/*": 97
            },
            "Diff7": {
                "*.mysite.com\/*": 97
            },
            "Diff30": {
                "*.mysite.com\/*": 97
            },
            "Vi": {
                "20191225": {
                    "*.mysite.com\/*": 0.017399999999999999
                },
                "Diff": {
                    "*.mysite.com\/*": 0
                }
            },
            "Sf": {
                "20191225": [
                    "adb"
                ]
            },
            "Tr": {
                "20191225": {
                    "*.mysite.com\/*": 1.23
                }
            },
            "Tc": {
                "20191225": {
                    "*.mysite.com\/*": 1
                }
            },
            "Lu": {
                "20191225": {
                    "*.mysite.com\/*": "https:\/\/www.mysite.com\/keyword2\/"
                }
            },
            "Lt": {
                "20191225": {
                    "*.mysite.com\/*": [
                        "org"
                    ]
                }
            }
        },
        "2": {
            "Pi": "13621862969727492608",
            "Ph": "keyword 3",
            "Kb": 20190326,
            "Tg": {},
            "Cp": "0.52",
            "Nq": "210",
            "Gs": "0",
            "Dt": {
                "20191225": {
                    "*.mysite.com\/*": 25
                }
            },
            "Be": {
                "*.mysite.com\/*": 25
            },
            "Fi": {
                "*.mysite.com\/*": 25
            },
            "Diff": {
                "*.mysite.com\/*": 0
            },
            "Diff1": {
                "*.mysite.com\/*": 75
            },
            "Diff7": {
                "*.mysite.com\/*": 75
            },
            "Diff30": {
                "*.mysite.com\/*": 75
            },
            "Vi": {
                "20191225": {
                    "*.mysite.com\/*": 0.0016000000000000001
                },
                "Diff": {
                    "*.mysite.com\/*": 0
                }
            },
            "Sf": {
                "20191225": [
                    "stl"
                ]
            },
            "Tr": {
                "20191225": {
                    "*.mysite.com\/*": 0.059999999999999998
                }
            },
            "Tc": {
                "20191225": {
                    "*.mysite.com\/*": 0.029999999999999999
                }
            },
            "Lu": {
                "20191225": {
                    "*.mysite.com\/*": "https:\/\/www.mysite.com\/keyword3\/"
                }
            },
            "Lt": {
                "20191225": {
                    "*.mysite.com\/*": [
                        "org"
                    ]
                }
            }
        }
},
"Sfc": {
    "org": {
        "Ex": 0,
        "Ne": 1498,
        "De": 0,
        "Dn": 0
    },
    "geo": {
        "Ex": 7,
        "Ne": 1491,
        "De": 0,
        "Dn": 7
    },
    "amp": {
        "Ex": 0,
        "Ne": 1498,
        "De": 0,
        "Dn": 0
    },
    "tea": {
        "Ex": 0,
        "Ne": 1498,
        "De": 0,
        "Dn": 0
    },
    "new": {
        "Ex": 4,
        "Ne": 1494,
        "De": 0,
        "Dn": 4
    },
    "rel": {
        "Ex": 56,
        "Ne": 1442,
        "De": 0,
        "Dn": 56
    },
    "img": {
        "Ex": 2,
        "Ne": 1496,
        "De": 0,
        "Dn": 2
    },
    "adt": {
        "Ex": 275,
        "Ne": 1223,
        "De": 82,
        "Dn": 193
    },
    "shp": {
        "Ex": 103,
        "Ne": 1395,
        "De": 0,
        "Dn": 103
    },
    "knw": {
        "Ex": 1,
        "Ne": 1497,
        "De": 0,
        "Dn": 1
    },
    "twt": {
        "Ex": 0,
        "Ne": 1498,
        "De": 0,
        "Dn": 0
    },
    "app": {
        "Ex": 0,
        "Ne": 1498,
        "De": 0,
        "Dn": 0
    },
    "vib": {
        "Ex": 0,
        "Ne": 1498,
        "De": 0,
        "Dn": 0
    },
    "rev": {
        "Ex": 1208,
        "Ne": 290,
        "De": 0,
        "Dn": 1208
    },
    "vid": {
        "Ex": 6,
        "Ne": 1492,
        "De": 0,
        "Dn": 6
    },
    "fsn": {
        "Ex": 67,
        "Ne": 1431,
        "De": 0,
        "Dn": 67
    },
    "stl": {
        "Ex": 911,
        "Ne": 587,
        "De": 69,
        "Dn": 842
    },
    "adb": {
        "Ex": 573,
        "Ne": 925,
        "De": 220,
        "Dn": 353
    },
    "kng": {
        "Ex": 32,
        "Ne": 1466,
        "De": 0,
        "Dn": 32
    }
},
"Vc": {
    "0-10": 199,
    "11 - 100": 36,
    "101 - 1000": 1006,
    "1001 - 10000": 204,
    "10001+": 53
},
"Topc": {
    "all": 1498,
    "all_improved": 0,
    "all_declined": 0,
    "all_difference": 0,
    "all_left": 0,
    "all_entered": 0,
    "all_unchanged": 1498,
    "top3": 177,
    "top3_improved": 0,
    "top3_declined": 0,
    "top3_difference": 0,
    "top3_left": 0,
    "top3_entered": 0,
    "top3_unchanged": 177,
    "top10": 512,
    "top10_improved": 0,
    "top10_declined": 0,
    "top10_difference": 0,
    "top10_left": 0,
    "top10_entered": 0,
    "top10_unchanged": 512,
    "top20": 741,
    "top20_improved": 0,
    "top20_declined": 0,
    "top20_difference": 0,
    "top20_left": 0,
    "top20_entered": 0,
    "top20_unchanged": 741,
    "4_10": 335,
    "4_10_improved": 0,
    "4_10_declined": 0,
    "4_10_difference": 0,
    "4_10_left": 0,
    "4_10_entered": 0,
    "4_10_unchanged": 335,
    "11_20": 229,
    "11_20_improved": 0,
    "11_20_declined": 0,
    "11_20_difference": 0,
    "11_20_left": 0,
    "11_20_entered": 0,
    "11_20_unchanged": 229,
    "21_100": 694,
    "21_100_improved": 0,
    "21_100_declined": 0,
    "21_100_difference": 0,
    "21_100_left": 0,
    "21_100_entered": 0,
    "21_100_unchanged": 694,
    "top100": 1435,
    "top100_improved": 0,
    "top100_declined": 0,
    "top100_difference": 0,
    "top100_left": 0,
    "top100_entered": 0,
    "top100_unchanged": 1435,
    "out": 63,
    "out_improved": 0,
    "out_declined": 0,
    "out_difference": 0,
    "out_left": 0,
    "out_entered": 0,
    "out_unchanged": 63
},
"server": "USA",
"exec_time": 2.705991
}