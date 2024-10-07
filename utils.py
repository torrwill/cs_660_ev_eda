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
"""
def convertPostalCode(argData: pd.DataFrame):
    data = argData.copy(deep=True)

    data['Postal Code'] = data['Postal Code'].astype(int)
    
    result = data

    return result



""""
Removes four international records from the dataset:

        VIN (1-10) County City State  Postal Code  Model Year       Make  
114     WBAJA9C50K    NaN  NaN    AE          NaN        2019        BMW   
148234  5YJXCAE24H    NaN  NaN    BC          NaN        2017      TESLA   
157590  5YJ3E1EA5K    NaN  NaN    BC          NaN        2019      TESLA   
175158  1G1RB6S53J    NaN  NaN    BC          NaN        2018  CHEVROLET 

These vehicles may be removed as outliers because they are registered outside of Washington State,
and are conceptually incongruent with the rest of the data set.
"""
def purgeInternationalOutliers(argData: pd.DataFrame):
    data = argData.copy(deep=True)

    result = result['Postal Code'].astype(int)
    return result




"""
Our data presents with 4 records that are missing Vehicle Location for an unknown reason.

The vehicle location data can be inferred by matching other location specific features on the records.
"""
def imputeLocationData(argData: pd.DataFrame):
    data = argData.copy(deep=True)

    # Because the missing data points are all for the same city and county, a non-generic implementation will suffice.
    location = data.groupby(['City', 'County']).get_group(('Long Beach','Pacific'))['Vehicle Location'].values[0]
    
    data['Vehicle Location'] = data['Vehicle Location'].fillna(location)
    
    result = data

    return result


"""
Normalize Utility
"""
