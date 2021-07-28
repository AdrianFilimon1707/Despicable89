from application import Garage, Reports, Truck, FixedValues, UpdatedValues, Report

fixedValues = FixedValues(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
initialUpdatedValues = UpdatedValues(0, "", 0, "", 0, "", 0, "")
secondUpdatedValues = UpdatedValues(1, "", 2, "tire break", 1, "", 1, "")

garage = Garage()
reports = Reports()

plateNumber = "CJ01RAR"
truck: Truck = Truck(plateNumber, True)

if not garage.isTruckDefined(plateNumber):
    garage.addElement(truck)
    if garage.__getitem__(plateNumber) is not None:
        print('Truck added in garage with success')
    else:
        print('[1] Should not be here in ELSE')
else:
    print('[2] Should not be here in ELSE')

if garage.isTruckDefined(plateNumber):
    print("Truck with " + plateNumber + " it is stored in garage")
else:
    print('[3] Should not be here in ELSE')

if garage.truckAvailability(plateNumber) and garage.__len__() == 1:
    print("Truck is available in garage")
else:
    print('[4] Should not be here in ELSE')

garage.sendTruckOnRoad(plateNumber)
firstReport = Report(fixedValues, initialUpdatedValues)
reports[plateNumber] = [firstReport]

if not garage.truckAvailability(plateNumber):
    print('Truck is on the road')
else:
    print('[5] Should not be here in ELSE')

if reports.__getitem__(plateNumber) is not None:
    print('Report added with success')
else:
    print('[6] Should not be here in ELSE')

if garage.isTruckDefined(plateNumber):
    print('Cannot add another truck with the same plate number')
else:
    print('[7] Should not be here in ELSE')

print('Sending a new report')
newReport = Report(fixedValues, secondUpdatedValues) + firstReport
reportsList = reports.__getitem__(plateNumber)
reportsList.append(newReport)

if len(reportsList) == 2:
    print('There are two reports for truck ' + plateNumber)
    print("The first one when the truck was sent on road")
    print("And the second one when the a week updated was given")

print("Printing now the 2 reports")
reportsSequence = reports.setReportsSequence(plateNumber)
try:
    currentReport: Report = next(reportsSequence)
    while currentReport is not None:
        currentReport.calculateForReport()
        currentReport: Report = next(reportsSequence)
except StopIteration:
    pass
