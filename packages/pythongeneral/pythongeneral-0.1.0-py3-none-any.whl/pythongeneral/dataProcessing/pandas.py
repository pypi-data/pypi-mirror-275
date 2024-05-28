import pandas as pd
import pythonGeneral.dataProcessing.string as pds
import os
import orjson

class df_data:
    def __init__(self, path_settings=None, useColumns=None):
        if path_settings:
            self.set_pathSettings(path_settings=path_settings)
        else:
            self.path_settings["importFile"] = ""
        self.setImportDf(useColumns)

    def set_pathSettings(self, path_settings):
        self.path_settings = {
            "importDir": path_settings.get("importDir"),
            "importFile": path_settings.get("importFile"),
            "exportDir": path_settings.get("exportDir"),
            "exportFile": path_settings.get("exportFile")
        }
    
    def setExportFile(self,exportFile):
        self.path_settings["exportFile"] = exportFile

    def set_mergeSettings(self, mergeSettings):
        self. mergeSettings = {
            "mergeOnList": mergeSettings.get("mergeOnList"),
            "dropList": mergeSettings.get("dropList"),
            "renameDict": mergeSettings.get("renameDict")
        }

    def setImportDf(self, useColumns):
        if str(self.path_settings["importFile"]).split('.')[1] == 'xlsx':
            self.df = pd.DataFrame(pd.read_excel(
                self.path_settings["importDir"]+self.path_settings["importFile"], usecols=useColumns))
        elif str(self.path_settings["importFile"]).split('.')[1] == 'csv':
            self.df = pd.DataFrame(pd.read_csv(
                self.path_settings["importDir"]+self.path_settings["importFile"], usecols=useColumns, error_bad_lines=False))
        else:
            self.df = pd.DataFrame(columns=useColumns)

    def setData(self, df):
        self.df = df

    def dropStringNotInData(self, inString, column):
        self.df = self.df[self.df[column].str.contains(inString)]
        
    def dropStringInData(self,dropString,column):
        self.df = self.df[~self.df[column].str.contains(dropString,na=False)]
    
    def cutData(self, start=None, end=None):
        self.df = self.df.iloc[start:end, :]

    def sortData(self, sortColumns):
        self.df = self.df.sort_values(by=sortColumns)

    def deleteDuplicate(self, deleteDupColumn: str):
        self.df.drop_duplicates(subset=deleteDupColumn, inplace=True)

    def deleteNone(self, deleteNoneColumn: str):
        for i in range(len(self.df)):
            if self.df.at[i,deleteNoneColumn] == "":
                self.df.drop(i,axis=0,inplace=True)
        self.df.dropna(axis=0, subset=deleteNoneColumn, inplace=True)
    
    def getNone(self, getNoneColumn):
        self.df = self.df[self.df[getNoneColumn].isnull()]
    
    def processData(self, deleteNoneColumn, deleteDupColumn, sortColumns):
        self.df.dropna(axis=0, subset=deleteNoneColumn, inplace=True)
        self.df.drop_duplicates(subset=deleteDupColumn, inplace=True)
        self.df = self.df.sort_values(by=sortColumns)

    def substituteOneString(self, beSubString: str, subString: str, subColumn: str):
        for i in range(len(self.df)):
            d = pds.reString(str(self.df.at[i, subColumn]))
            d.substituteOneString(beSubString,subString)
            self.df.at[i, subColumn] = d.processStr
    
    def substituteManyString(self,subDict:dict,subColumn:str):
        for i in range(len(self.df)):
            d = pds.reString(str(self.df.at[i, subColumn]))
            d.substituteManyString(subDict)
            self.df.at[i, subColumn] = d.processStr
    
    def processPhoneNum(self,phoneNumColumn,addressColumn):
        for i in range(len(self.df)):
            d = pds.reString(str(self.df.at[i,phoneNumColumn]))
            d.processPhoneNum(str(self.df.at[i,addressColumn])[0:2])
            self.df.at[i,phoneNumColumn] = d.processStr
    
    def processRegexString(self,regex:str,processColumn:str):
        for i in range(len(self.df)):
            d = pds.reString(str(self.df.at[i, processColumn]))
            d.processRegexString(regex)
            self.df.at[i, processColumn] = d.processStr
    
    def deleteSpaceChar(self,deleteStrColumn):
        for i in range(len(self.df)):
            d = pds.reString(str(self.df.at[i,deleteStrColumn]))
            d.deleteSpace()
            self.df.at[i,deleteStrColumn] = d.processStr
            
    def deleteNullString(self,deleteColumn:str):
        for i in range(len(self.df)):
            if self.df.at[i,deleteColumn] == "":
                self.df.drop(i,axis=0,inplace=True)
    
    def dataToJson(self,index,transferColumns:list):
        self.dataDict = {}
        for j in transferColumns:
            self.dataDict[j] = self.df.at[index,j]
        self.dataJson = orjson.dumps(self.dataDict)
        
    def dataToGeoDict(self, transferColumns, index, xColumn, yColumn):
        self.dataDict = {}
        locationDict = {}
        locationDict["type"] = "Point"
        locationDict["coordinates"] = [
            float(self.df.at[index, xColumn]), float(self.df.at[index, yColumn])]
        for j in transferColumns:
            self.dataDict[transferColumns[j]] = str(self.df.at[index,j])
        self.dataDict["location"] = locationDict
        
    def jsonToData(self,index,jsonData):
        self.dataDict = orjson.loads(jsonData)
        for j in self.dataDict:
            self.df.at[index,j] = self.dataDict[j]
        
    def dataToTPSData(self,remarkColumns:list):
        for i in range(len(self.df)):
            capitalData = str(self.df.at[i, '資本額'])
            for col in remarkColumns:
                capitalData = "{0},{1}:{2}".format(capitalData,col,self.df.at[i,col])
                capitalDataRe = pds.reString(capitalData)
                capitalDataRe.deleteString("nan")
                capitalData = capitalDataRe.getProcessString()
            self.df.at[i,'資本額'] = capitalData
    
    def leftMergeData(self, dfRight, mergeSettings):
        self.set_mergeSettings(mergeSettings=mergeSettings)
        self.df = self.df.merge(
            right=dfRight.df,
            how="left",
            on=self.mergeSettings["mergeOnList"]
        )
        if self.mergeSettings["dropList"] != None:
            self.df.drop(self.mergeSettings["dropList"], axis=1, inplace=True)
        if self.mergeSettings["renameDict"] != None:
            self.df.rename(columns=self.mergeSettings["renameDict"], inplace=True)
            
    def innerMergeData(self, dfRight, mergeSettings):
        self.set_mergeSettings(mergeSettings=mergeSettings)
        self.df = self.df.merge(
            right=dfRight.df,
            how="inner",
            on=self.mergeSettings["mergeOnList"]
        )
        if self.mergeSettings["dropList"] != None:
            self.df.drop(self.mergeSettings["dropList"], axis=1, inplace=True)
        if self.mergeSettings["renameDict"] != None:
            self.df.rename(
                columns=self.mergeSettings["renameDict"], inplace=True)

    def toFile(self):
        if self.path_settings["exportFile"].split('.')[1] == 'csv':
            self.df.to_csv(
                self.path_settings["exportDir"]+self.path_settings["exportFile"], index=False, encoding='utf-8-sig')
        elif self.path_settings["exportFile"].split('.')[1] == 'xlsx':
            self.df.to_excel(
                self.path_settings["exportDir"]+self.path_settings["exportFile"], index=False)
        else:
            print("沒有設定exportFile或exportDir")

def concatDirData(path_settings):
    dfTotal = pd.DataFrame()
    for importFile in os.listdir(path_settings["importDir"]):
        data = df_data({"importDir": path_settings["importDir"],
                        "importFile": importFile,
                        "exportDir": path_settings["exportDir"],
                        "exportFile": path_settings["exportFile"]})
        dfTotal = pd.concat([dfTotal, data.df])
    dfTotal.to_excel(path_settings["exportDir"]+path_settings["exportFile"], index=False)

def concatFileData(exportPath, *concatDf):
    dfTotal = pd.DataFrame()
    for df in concatDf:
        dfTotal = pd.concat([dfTotal, df])
    dfTotal.to_excel(exportPath, index=False)