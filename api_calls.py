# API codes taken from
# http://www2.census.gov/programs-surveys/acs/summary_file/2014/documentation/user_tools/ACS_1yr_Seq_Table_Number_Lookup.txt

# Call for age grouping populations per state
age_api_call = ('http://api.census.gov/data/2014/acs1?'
'get=NAME,'
'B01001_002E,' # Male Population
'B01001_003E,' # men under 5
'B01001_004E,' # men 5 to 9 years
'B01001_005E,' # men 10 to 14 years
'B01001_006E,' # men 15 to 17 years
'B01001_007E,' # men 18 and 19 years
'B01001_008E,' # men 20 years
'B01001_009E,' # men 21 years
'B01001_010E,' # men 22 to 24 years
'B01001_011E,' # men 25 to 29 years
'B01001_012E,' # men 30 to 34 years
'B01001_013E,' # men 35 to 39 years 
'B01001_014E,' # men 40 to 44 years
'B01001_015E,' # men 45 to 49 years
'B01001_016E,' # men 50 to 54 years
'B01001_017E,' # men 55 to 59 years
'B01001_018E,' # men 60 and 61 years
'B01001_019E,' # men 62 to 64 years
'B01001_020E,' # men 65 and 66 years
'B01001_021E,' # men 67 to 69 years
'B01001_022E,' # men 70 to 74 years
'B01001_023E,' # men 75 to 79 years
'B01001_024E,' # men 80 to 84 years
'B01001_025E,' # men 85 years and over
'B01001_026E,' # Female Population
'B01001_027E,' # female under 5 years
'B01001_028E,' # female 5 to 9 years
'B01001_029E,' # female 10 to 14 years
'B01001_030E,' # female 15 to 17 years
'B01001_031E,' # female 18 and 19 years
'B01001_032E,' # female 20 years
'B01001_033E,' # female 21 years
'B01001_034E,' # female 22 to 24 years
'B01001_035E,' # female 25 to 29 years
'B01001_036E,' # female 30 to 34 years
'B01001_037E,' # female 35 to 39 years
'B01001_038E,' # female 40 to 44 years
'B01001_039E,' # female 45 to 49 years
'B01001_040E,' # female 50 to 54 years
'B01001_041E,' # female 55 to 59 years
'B01001_042E,' # female 60 and 61 years
'B01001_043E,' # female 62 to 64 years
'B01001_044E,' # female 65 to 66 years
'B01001_045E,' # female 67 to 69 years
'B01001_046E,' # female 70 to 74 years
'B01001_047E,' # female 75 to 79 years
'B01001_048E,' # female 80 to 84 years
'B01001_049E' # female 85 years and over
'&for=state:*'
'&key=a5078c224c10c1a5e6be6702543cfc8c9abdebac')

# Call for race populations per state
race_api_call = ('http://api.census.gov/data/2014/acs1?'
'get=NAME,'
'B01001A_001E,' # White
'B01001B_001E,' # Black or African American
'B01001C_001E,' # American Indian and Alaska
'B01001D_001E,' # Asian
'B01001E_001E,' # Native Hawiian and Other
'B01001F_001E,' # Some Other Race
'B01001G_001E,' # Two or more races
'B01001I_001E' # hispanic or latino
'&for=state:*'
'&key=a5078c224c10c1a5e6be6702543cfc8c9abdebac')

test_api_call = ('http://api.census.gov/data/2014/acs1?'
'C01001A_001E' # White alone total population
'&for=state:*'
'&key=a5078c224c10c1a5e6be6702543cfc8c9abdebac'
)

