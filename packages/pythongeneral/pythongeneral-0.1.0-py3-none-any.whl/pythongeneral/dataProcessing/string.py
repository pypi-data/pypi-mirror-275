import re
numSubDict = {
    '零': '0', '一': '1', '二': '2', '兩': '2', '三': '3',
    '四': '4', '五': '5', '六': '6', '七': '7', '八': '8',
    '九': '9', '〇': '0', '○': '0', '○': '0', '０': '0', '１': '1',
    '２': '2', '３': '3', '４': '4', '５': '5', '６': '6', '７': '7',
    '８': '8', '９': '9', '壹': '1', '貳': '2', '參': '3', '肆': '4',
    '伍': '5', '陆': '6', '柒': '7', '捌': '8', '玖': '9'
}
charSubDict = {
    '臺' : '台'
}

cityCodeDict = {
    "台北" : "02",
    "臺北" : "02",
    "新北" : "02",
    "桃園" : "03",
    "新竹" : "03",
    "花蓮" : "03",
    "宜蘭" : "03",
    "苗栗" : "037",
    "台中" : "04",
    "臺中" : "04",
    "彰化" : "04",
    "南投" : "049",
    "嘉義" : "05",
    "雲林" : "05",
    "台南" : "06",
    "臺南" : "06",
    "澎湖" : "06",
    "高雄" : "07",
    "屏東" : "08",
    "台東" : "089",
    "臺東" : "089"
}
cityThreeLenList = ["苗栗","南投","台東","臺東"]
cityPhoneNumTenList = ["台北","新北","台中","南投","臺北","臺中"]
class reString:
    regex = ""

    def __init__(self, originStr):
        self.originStr = originStr
        self.processStr = originStr

    def getNumberString(self):
        processStr = ""
        self.regex = re.compile(r"\d")
        processObj = self.regex.finditer(self.processStr)
        for chr in processObj:
            processStr += chr.group()
        self.processStr = processStr

    def deleteSpace(self):
        self.processStr = re.sub(r" ", r"", self.processStr)

    def deleteString(self, deleteStr):
        self.processStr = re.sub(deleteStr, r"", self.processStr)

    def deleteOneChar(self, deleteChar: str):
        self.processStr = re.sub(deleteChar, r"", self.processStr)

    def deleteManyChar(self, deleteCharList: list):
        for deleteChar in deleteCharList:
            self.processStr = re.sub(deleteChar, r"", self.processStr)
    def splitChar(self,splitChar,getIndex):
        return str(self.processStr.split(splitChar)[getIndex])
    
    def insertChar(self, insertIndex: int, insertChar: str):
        insertStrList = list(self.processStr)
        insertStrList.insert(insertIndex, insertChar)
        insertStrList = "".join(insertStrList)
        self.processStr = insertStrList

    def substituteManyString(self, subDict: dict):
        for subChar in subDict:
            self.processStr = re.sub(
                subChar, subDict[subChar], self.processStr)

    def substituteOneString(self, beSubString: str, subString: str):
        self.processStr = re.sub(beSubString, subString, self.processStr)

    def processRegexString(self, regex: str):
        processStr = ""
        self.regex = re.compile(regex)
        processObj = self.regex.finditer(self.processStr)
        for chr in processObj:
            processStr += chr.group()
        self.processStr = processStr
    
    def processAddressString(self):
        if ("市" not in self.originStr) and ("縣" not in self.originStr):
            self.processStr = ""
            return
        else:
            self.processRegexString("..市..*|..縣..*")
    
    def turnChiNumberToNumber(self):
        self.substituteManyString(numSubDict)
    
    def deleteNotMatchCity(self,city,codeLen):
        for c in cityCodeDict:
            if c in city:
                if codeLen == 3:
                    if cityCodeDict[c] == self.processStr[0:3]:
                        return True
                else:
                    if cityCodeDict[c] == self.processStr[0:2]:
                        return True
        self.processStr = ""
        return False
    
    def processPhoneNum(self,city):
        isThreeCodeCity = False
        isPhoneNumTenCity = False
        self.getNumberString()
        if self.processStr == "":
            return
        if self.getProcessString()[0:3] == "886":
            self.substituteOneString("886","09")
        if self.getProcessString()[0:2] == "09":
            self.insertChar(4,"-")
            self.insertChar(-3,"-")
            return
        for ci in cityPhoneNumTenList:
            if ci in city:
                isPhoneNumTenCity = True
        for ci in cityThreeLenList:
            if ci in city:
                isThreeCodeCity = True
        if isPhoneNumTenCity:
            if len(self.getProcessString()) == 8:
                self.processStr = cityCodeDict[city]+self.processStr
            if len(self.getProcessString()) == 9:
                self.processStr = self.processStr.zfill(10)
            if len(self.getProcessString())<10:
                self.processStr = ""
                return
            self.insertChar(6, "-")
            if len(self.getProcessString()) > 11:
                self.insertChar(11, "#")
        else:
            if len(self.getProcessString()) == 7:
                self.processStr = cityCodeDict[city]+self.processStr
            if len(self.getProcessString()) == 8:
                self.processStr = self.processStr.zfill(9)
            if len(self.getProcessString())<9:
                self.processStr = ""
                return
            self.insertChar(5, "-")
            if len(self.getProcessString()) > 10:
                self.insertChar(10, "#")
        if isThreeCodeCity:
            isMatched = self.deleteNotMatchCity(city,3)
            if isMatched:
                self.insertChar(3,"-")
            else:
                return
        else:
            isMatched = self.deleteNotMatchCity(city,2)
            if isMatched:
                self.insertChar(2, "-")
            else:
                return
            
    def getOriginString(self):
        return self.originStr

    def getProcessString(self):
        return self.processStr


def InsertChar(insertStr, insertIndex, insertChar):
    insertStrList = list(insertStr)
    insertStrList.insert(insertIndex, insertChar)
    insertStrList = ''.join(insertStrList)
    return insertStrList


def deleteSpace(originStr):
    processStr = re.sub(r" ", r"", originStr)
    return processStr
