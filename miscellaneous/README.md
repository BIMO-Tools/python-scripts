## Calculate Selected Lines Length mm

This Revit Python script calculates the total length of selected line elements and outputs the result in millimeters. It's designed to assist users in quickly obtaining the cumulative length of selected curves, particularly beneficial for tasks requiring precise measurements or documentation.

**Key Features:**
- **Selection-Based Calculation:** The script processes only the elements currently selected in the Revit active view, ensuring that users have control over which lines are measured.
- **Curve Detection:** It checks each selected element to determine if it is a curve element (such as a line). This ensures accuracy by only including relevant geometry in the calculation.
- **Unit Conversion:** The script automatically converts the measured length from Revit's native units (feet) to millimeters, catering to users accustomed to working in metric units.
- **Simple Output:** The total length is printed to the console in millimeters, providing a clear and concise metric for further use or analysis.

**Usage:**
1. Open a Revit project and select the lines you wish to measure.
2. Run this script to calculate the total length of the selected lines.
3. The script outputs the total length in millimeters to the console.

**Implementation Details:**
- Utilizes Autodesk Revit API classes such as `FilteredElementCollector` and `CurveElement` to access and process document elements.
- Employs a conversion factor of 304.8 to translate lengths from feet to millimeters.

This script enhances productivity by streamlining the process of obtaining length measurements in metric units within Revit projects.
