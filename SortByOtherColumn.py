# Copyright © 2017. TIBCO Software Inc.  Licensed under TIBCO BSD-style license.

####################################################################
##
## Sort table column A accorting to column b
##
"""
update the specified ListBox filter selection based on a parameter

Parameters to be created:
table       -- table
col_sort    -- column to sort
col_orderby -- column to sort *by*
"""
####################################################################

from System.Reflection import Assembly 
from Spotfire.Dxp.Data.Collections import *
from System.Runtime.Serialization import ISerializable
from System.Collections import IComparer
from System.Collections.Generic import IComparer



# tbl = '' # table
# col_target = '' # column to sort
# col_sort = '' # column to sort *by*


tbl = table
col_target = col_sort
col_sort = col_orderby


#get pairs of values (sorted_column, sortby_column)
myPairs = []
for eTableRows in range(0,Document.Data.Tables[tbl].RowCount):
    val_target = Document.Data.Tables[tbl].Columns[col_target].RowValues.GetFormattedValue(eTableRows)
    val_sort = Document.Data.Tables[tbl].Columns[col_sort].RowValues.GetFormattedValue(eTableRows)
    myPairs.Add( (val_target, val_sort) )

#print myPairs
# get unique values from column to sort
subs = []
for s in myPairs:
    #print s[0]
    if s[0] not in subs:
        subs.Add(s[0])
#print subs

# make a dict of (sorted_column, sortby_column) with max value for sortby
ord = {}
for x in subs:
    ord[x] = 0.0
    for y in myPairs:
        # initial value; take care of empty values
        if y[1] == '(Empty)':
            i = 0
        else:
            i = float(y[1])
        # if new value is larger, store that instead
        if (y[0] == x) & (i > ord[x]):
            ord[x] = i
#print ord
# we want to sort from big to small; sort() goes the other way
foo = dict(reversed(sorted(ord.items(), key=lambda item: item[1])))
newSort = sorted(ord, key=ord.get)
#print foo
# get the keys which are values in column to sort
#newSort = list(foo.keys())

# set the custom sort order
Document.Data.Tables[tbl].Columns[col_target].Properties.SetCustomSortOrder(newSort)
