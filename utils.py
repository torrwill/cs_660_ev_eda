import pandas as pd

# TODO: Modify functions to use .merge() or .map() to avoid row iteration

"""Range Data Cleaning Function"""
def calculateRange(argData: pd.DataFrame):
    data = argData.copy(deep=True) # Copy argument DataFrame to avoid side effects.

    sparseData = data.drop(columns=[
        'VIN (1-10)', 'County', 'City', 'State', 'Postal Code',
        'Model Year','Electric Vehicle Type',
        'Clean Alternative Fuel Vehicle (CAFV) Eligibility',
        'Base MSRP', 'Legislative District', 'DOL Vehicle ID',
        'Vehicle Location', 'Electric Utility', '2020 Census Tract']) # drop unnessecary features

    rangeByMakeAndModel = sparseData[sparseData['Electric Range'].gt(0)].groupby(['Make', 'Model'])
    unrecordedRanges = []
    def getRange(record):
        if record['Electric Range'] == 0:
            recordedRange = 0 #TODO: this value may be better served as something else. 
            try:
                recordedRange = rangeByMakeAndModel.get_group((record['Make'], record['Model']))['Electric Range'].mean()
            except KeyError as e:
                unrecordedRanges.append((record['Make'], record['Model']))
            
            record['Electric Range'] = recordedRange
        return record

    result = data.apply(getRange, axis=1, result_type='broadcast')
    return result
    

"""
Populates Base MSRP where possible. 

Please note that MSRP data is very scarce in the source data, 
"""
def calculateMSRP(argData: pd.DataFrame):
    data = argData.copy(deep=True) # Copy argument DataFrame to avoid side effects.

    sparseData = data.drop(columns=[
        'VIN (1-10)', 'County', 'City', 'State', 'Postal Code',
        'Model Year','Electric Vehicle Type',
        'Clean Alternative Fuel Vehicle (CAFV) Eligibility',
        'Electric Range', 'Legislative District', 'DOL Vehicle ID',
        'Vehicle Location', 'Electric Utility', '2020 Census Tract']) # drop unnecessary features

    msrpByMakeAndModel = sparseData[sparseData['Base MSRP'].gt(0)].groupby(['Make', 'Model'])
    unrecordedMSRP = []

    def getMSRP(record):
        if record['Base MSRP'] == 0:
            recordedPrice = 0
            try:
                recordedPrice = msrpByMakeAndModel.get_group((record['Make'], record['Model']))['Base MSRP'].mean()
            except KeyError as e:
                unrecordedMSRP.append((record['Make'], record['Model']))
            
            record['Base MSRP'] = recordedPrice
        return record
    
    result = data.apply(getMSRP, axis=1, result_type='broadcast')
    return result


"""
Convert Clean Alternative Fuel Vehicle (CAFV) Eligibility feature to be binary.

Please note that we loose a little bit of resolution here due to assigning 0 to
records which have the values 'Eligibility unknown as battery range has not been researched'
and 'Not eligible due to low battery range', this should not present an issue for our analysis.

TODO: add call out in presentation of how many models have not been researched
"""
def convertEligibility(argData: pd.DataFrame):
    data = argData.copy(deep=True)

    key = 'Clean Alternative Fuel Vehicle (CAFV) Eligibility'
    eligibilityString = 'Clean Alternative Fuel Vehicle Eligible'

    def getEligibility(row):
        if(row[key] == eligibilityString):
            row[key] = 1
        else:
            row[key] = 0
        return row
    
    result = data.apply(getEligibility, axis=1, result_type='broadcast')

    return result

"""
Convert Postal Code dtype to int.

Please note that three records are excluded from the dataset by this function,
these records are outliers because they are registered in canada, removing
them ensures that the data-set represents only EVs registered in Washington State.
"""
def convertPostalCode(argData: pd.DataFrame):
    data = argData.copy(deep=True)

    result = data.dropna(subset=['Postal Code'])
    result = result['Postal Code'].astype(int)

    return result