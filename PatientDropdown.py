
####################################################
##
##     set specific filter based on a dropdown.
##     basically, it turns a listbox filter into a
##     dropdown in a specific filtering scheme, using
##     a document property
##     
##     
##

from Spotfire.Dxp.Application.Filters import *
from Spotfire.Dxp.Data import DataPropertyClass
from System import String


page = Application.Document.ActivePageReference
filterPanel = page.FilterPanel

# print lbFilter
print Document.Properties['PatientSelect']

#Get reference for FilteringScheme used for your filter
for fs in Document.FilteringSchemes:
    if fs.FilteringSelectionReference.Name == "PatientMatch": 
        filterPanel.FilteringSchemeReference = fs

#Let's find "Col_LBFilter" filter and read the selected Values
filterPanel.InteractiveSearchPattern = "*Match"
for myFilter in filterPanel.FiltersMatchingSearchPattern:
   lbFilter = myFilter.FilterReference.As[CheckBoxFilter]()

   if lbFilter != None:
      lbFilter.Check("Y")
      lbFilter.IncludeEmpty = False

## reset filter search
filterPanel.InteractiveSearchPattern = ""


for fs in Document.FilteringSchemes:
    if fs.FilteringSelectionReference.Name == "Filtering scheme": 
        filterPanel.FilteringSchemeReference = fs
