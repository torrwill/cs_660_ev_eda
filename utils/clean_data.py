import pandas as pd

"""Range Data Cleaning Function"""
def dataCleaner(argData: pd.DataFrame):
    data = argData.copy()
    rangeByMakeAndModel = data[data['Electric Range'].gt(0)].groupby(['Make', 'Model'])
    unrecordedRanges = []
    data.merge(rangeByMakeAndModel)
    print(data)
    # def getRange(record):
    #     if record['Electric Range'] == 0:
    #         recordedRange = 0 #TODO: this value may be better served as something else. 
    #         try:
    #             recordedRange = rangeByMakeAndModel.get_group((record['Make'], record['Model']))['Electric Range'].mean()
    #         except KeyError as e:
    #             unrecordedRanges.append((record['Make'], record['Model']))
            
    #         record['Electric Range'] = recordedRange

    msrpByMakeAndModel = data[data['Base MSRP'].gt(0)].groupby(['Make', 'Model'])
    unrecordedMSRP = []
    # def getMSRP(record):
    #     if record['Base MSRP'] == 0:
    #         recordedPrice = 0
    #         try:
    #             recordedPrice = msrpByMakeAndModel.get_group((record['Make'], record['Model']))['Base MSRP'].mean()
    #             print('Found Price!')
    #         except KeyError as e:
    #             print('Key Error')
    #             unrecordedMSRP.append((record['Make'], record['Model']))
            
    #         record['Base MSRP'] = recordedPrice

    data.apply(getRange, axis=1)
    data.apply(getMSRP, axis=1)
    return data
    
    