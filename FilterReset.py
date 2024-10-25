

####################################################################
##
## Reset Filters
##
"""
used for reseting filter flags in a targeted listing

PARAMS:
tables : comma separated list of tables on which to reset the filters
"""

from Spotfire.Dxp.Application.Filters import FilteringSchemeCollection

#Get a list of tables from the active page
tg = Document.ActivePageReference.FilterPanel.TableGroups

table_list = [x.strip() for x in tables.split(',')] 

#Show available filters
print "Available filters:"
for t in tg:
    if (t.Name) in table_list: print t
print "------------\n"


#See if a filter is available on the filter panel
#print "Visibility of filters in a table group"
#for h in tg[0].FilterHandles:
#    print h.FilterReference.Name, h.Visible
#print "------------\n"

#Reset all available filters
for t in tg:
    if (t.Name) in table_list:
        for h in t.FilterHandles:
            h.FilterReference.Reset()


Document.Properties['AEvECLabel'] = "No Flag Set"
print "Done!"

