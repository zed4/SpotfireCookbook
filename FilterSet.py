
####################################################################
##
## Set Filter to criteria
##
"""
update the specified ListBox filter selection based on a parameter

Parameters to be created:
table  -- the string name of the data table that will be filtered
column -- the string name of the column to filter
          IMPORTANT: set this filter type to ListBox using the Filters panel
values -- a CSV string of the values to be selected
"""
####################################################################


from Spotfire.Dxp.Application.Filters import *
from Spotfire.Dxp.Data import DataPropertyClass
from System import String


#Get a list of tables from the active page
#tg = Document.ActivePageReference.FilterPanel.TableGroups


#get the page ref
page = Application.Document.ActivePageReference
#get the filter panel
filterPanel = page.FilterPanel

#test values
# table = "table"
# column = "column"
# vals = ["value1", "value2"]

# get the data table reference
dt = Document.Data.Tables[table]
# format our values into a list

# for debugging; safe to remove
print("values:", vals)

# using the default Filtering Scheme and the supplied Data Table name, get the filter by its Column name
filter = Document.FilteringSchemes.DefaultFilteringSchemeReference[dt][column]
filter = filterPanel.FilteringSchemeReference[dt][column]

print ">", filter


####
## Setting a ListBox Filter
####

# cast it as a ListBox filter
lb = filter.As[ListBoxFilter]()

# reset the filter to its default state
lb.Reset()
print ">>", lb

lb.IncludeAllValues = False
lb.IncludeEmpty = False

#create a new list of valid choices
lists = [val for val in vals if lb.HasPropertyValue(val)]


print "usable values:", lists

if lists != []:
    # set the values according to the script parameter
    lb.SetSelection(lists)

# for debugging: safe to remove
print("filter selection:")
print(filter)

####
## Setting a CheckBox Filter
####

# table = "table"
# column = "column"
filter = filterPanel.FilteringSchemeReference[dt][column]
print ">", filter

# cast it as a ListBox filter
lb = filter.As[c]()

# reset the filter to its default state
if lb != None:
    lb.IncludeEmpty = False
    for CheckBoxVal in lb.Values: 
        if CheckBoxVal not in vals:        
            lb.Uncheck(CheckBoxVal)
            print ("uncheck ", CheckBoxVal)
        else:
            lb.Check(CheckBoxVal)
            print ("check ", CheckBoxVal)

print "done!"

