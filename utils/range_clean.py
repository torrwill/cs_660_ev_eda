import pandas as pd


"""Range Data Cleaning Function"""
def dataCleaner(argData: pd.DataFrame):
    data = argData.copy()
    knownRanges = data[data['Electric Range'].gt(0)].groupby(['Make', 'Model'])
    unrecordedRanges = []
    def getRange(record):
        if record['Electric Range'] == 0:
            recordedRange = 0 #TODO: this value may be better served as something else. 
            try:
                recordedRange = knownRanges.get_group((record['Make'], record['Model']))['Electric Range'].mean()
            except KeyError as e:
                unrecordedRanges.append((record['Make'], record['Model']))
            
            record['Electric Range'] = recordedRange

    data.apply(getRange, axis=1)
    return data
    
    