from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, CurveElement

# Conversion factor from feet to millimeters
feet_to_mm = 304.8

# Retrieve the current document
uidoc = __revit__.ActiveUIDocument

selection = uidoc.Selection.GetElementIds()

total_length = 0.0

# Process each selected element
for elem_id in selection:
    element = __doc__.GetElement(elem_id)
    
    # Check if the element is a curve element (e.g., a line)
    if isinstance(element, CurveElement):
        curve = element.GeometryCurve
        total_length += curve.Length

# Convert to millimeters
length_in_mm = total_length * feet_to_mm

# Output the result in millimeters
print(length_in_mm)
