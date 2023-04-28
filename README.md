# ABS-2016-Births-by-Postcode-approximation
Data on births by postcode may not be available from the Australian Bureau of Statistics, however some disease incidence data is only available for postcodes.  This code relates data on persons aged zero at the 2016 census for Australian postcodes to Queensland open data on births by mother's postcode of residence to see if it matches well.

Broadly, I think it provides an adequate approximation, noting there are some differences in these datasets: 
- The census data will include persons aged zero born in 2015, while the Queensland dataset is for persons born in 2016
  - so there is the assumption that these are similar, but in effect there will be differences due to time mis-match
- The census data is based on place of usual residence, while the births data is mother's postcode of residence
  - assumption that these are broadly similar, but some minor difference could be expected
  - we restricted to Queensland postcodes, as the Queensland dataset contains some births in Queensland from other states, which would be incomplete counts

