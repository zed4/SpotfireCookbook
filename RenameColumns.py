
#################################################################################################
##
## Dynamically change the column names, based on the selected category
##
##################################################################################################
'''
Parameters: 
   myViz : Visualization ## where does the table live

Other Requirements:
    * create calculated columns Q01 ... Qn with a case statement:
        case [Category]
            when 'cat1' then [cat1-col1]
            when 'cat2' then [cat2-col1]
            when 'cat3' then [cat3-col1]
            ...
            when 'catn' then [catn-col1]
        end

    * give each calculated column a property TrueName of 'Qn' (matching its initial name above)

    * change filter type of [Category] to Radio Button

'''
from Spotfire.Dxp.Application.Visuals import VisualContent
from Spotfire.Dxp.Application.Filters import FilteringSchemeCollection, RadioButtonFilter
from Spotfire.Dxp.Application import PanelTypeIdentifiers


QList = ['Q01','Q02','Q03','Q04','Q05','Q06','Q07','Q08','Q09','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']

d = {}
d ['cat1'] = {'Q01':'NewName'}
d ['cat2'] = {'Q01':'NewName'
    ,'Q02':'NewName'
    ,'Q03':'NewName'
    ,'Q04':'NewName'
    ,'Q05':'NewName'
    ,'Q06':'NewName'
    ,'Q07':'NewName'
    ,'Q08':'NewName'
    ,'Q09':'NewName'
    ,'Q10':'NewName'
    ,'Q11':'NewName'
    ,'Q12':'NewName'
    ,'Q13':'NewName'
    ,'Q14':'NewName'
    }
d ['cat3'] = {'Q01':'NewName'
    ,'Q02':'NewName'
    ,'Q03':'NewName'
    ,'Q04':'NewName'
    ,'Q05':'NewName'
    ,'Q06':'NewName'
    }
d ['cat4'] = {'Q01':'NewName'
    ,'Q02':'NewName'
    ,'Q03':'NewName'
    ,'Q04':'NewName'
    ,'Q05':'NewName'
    ,'Q06':'NewName'
    ,'Q07':'NewName'
    }
TableName = 'QOL'


TableName = 'table'
PropertyName = 'category'
QSCAT = 'Category'
DEBUG = 1

qol =  Document.Properties[PropertyName]
##qol = "PGI01"  ## DEBUG

#select random category
if DEBUG == 1:
    import random
    n = random.random()
    m = int (n*100 % len(d.keys()) )
    i=0
    for k, v in d.items():
        i += 1
        if (i == m) : qol = k

   Document.Properties[PropertyName] = qol
   print qol


dt = Document.Data.Tables[TableName]

#Get a list of tables from the active page
tg = Document.ActivePageReference.FilterPanel.TableGroups

# limit display to current QSCAT


#set the filter directly
Application.Document.ActivePageReference.FilterPanel.FilteringSchemeReference[dt][QSCAT].As[RadioButtonFilter]().Value = qol


# Get a handle on the visible columns
contentTable = myViz.As[VisualContent]()
showCol = []
hideCol = []
# rename columns based on category
for col in dt.Columns:
    if DEBUG == 1: print 'checking column', col, ":", col.Properties["TrueName"]
    if col.Properties["TrueName"] in QList:
        if DEBUG: print 'changing column', col
        # reset column names
        col.Name = col.Properties["TrueName"]

        
        #hide the column
        if contentTable.TableColumns.Contains(dt.Columns[col.Name]):
            contentTable.TableColumns.Remove(dt.Columns[col.Name])

        # if a new name exists...
        if col.Name in d.get(qol, []): 
            if DEBUG == 1: print 'renaming column', col, ' to ', d[qol][col.Name]
            # change the name
            col.Name = d[qol][col.Name]
            # show the column
            contentTable.TableColumns.Add(dt.Columns[col.Name])
            # show the filter
            showCol.Add(col.Name)
        #otherwise hide it
        else:
            hideCol.Add(col.Name)


# show and hide the correct filters, as needed
for group in tg:
    if group.Name == TableName:
        for filter in group.FilterHandles:
            if filter.FilterReference.Name in showCol:
                filter.Visible = True
            if filter.FilterReference.Name in hideCol:
                filter.Visible = False


