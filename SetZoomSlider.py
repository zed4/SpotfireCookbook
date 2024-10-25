
####################################################
##
##     set zoom slider to -30..max for patient profile
##


from Spotfire.Dxp.Application.Visuals import ScatterPlot,AxisRange

#iterate over visuals and pick the type we want to fiddle with
for vis in Application.Document.ActivePageReference.Visuals:
   if  vis.TypeId  == VisualTypeIdentifiers.ScatterPlot:
      mychart1 = vis;
      break;


## flip the visibility of the Zoom Slider
mychart1.As[ScatterPlot]().XAxis.ManualZoom = not(mychart1.As[ScatterPlot]().XAxis.ManualZoom)
mychart1.As[ScatterPlot]().YAxis.ManualZoom = not(mychart1.As[ScatterPlot]().YAxis.ManualZoom)

# set the zoom window to -20..max 
min=-20

if not(mychart1.As[ScatterPlot]().XAxis.ManualZoom ):
   mychart1.As[ScatterPlot]().XAxis.Range = AxisRange(min,'');
else:
   mychart1.As[ScatterPlot]().XAxis.Range = AxisRange('','');
   mychart1.As[ScatterPlot]().XAxis.ZoomRange = AxisRange(min,'');

