import sys
from TruckDe.models import Menu

from TruckDe.models.Garage import Garage
from TruckDe.models.Menu import Menu
from TruckDe.models.TruckKnownValues import TruckKnownValues
from TruckDe.models.TruckWeekUpdates import TruckWeekUpdates
from TruckDe.models.Truck import Truck
from TruckDe.state.constants import FIXED_VALUES, TARGET_VALUES
from TruckDe.utils import prettyTable, fileReadWrite
from TruckDe.utils.data_files import targetValues, fixedValues
from TruckDe.utils import search


def main():
    menu = Menu()
    garage = Garage()
    garage.populateGarageWithTrucks()
    while True:
        try:
            menu.printMenu()
            selectedOption = int(input("Option: "))
            if selectedOption == 0:
                sys.exit(0)

            if selectedOption == 1:
                plateNumber = str(input("\tPlate number: "))
                if garage.getTruckByPlateNumber(plateNumber) is None:
                    fileReadWrite.addNewTruck(plateNumber)
                    garage.populateGarageWithTrucks()
                    print("\tTruck - " + plateNumber + " - added with success")
                else:
                    print("\tA truck with this plate number already exists")

            if selectedOption == 2:
                plateNumber = str(input("\tPlate number: "))
                if garage.getTruckByPlateNumber(plateNumber) is not None:
                    if not garage.isTruckOnRoad(plateNumber):
                        fileReadWrite.removeTruck(plateNumber, garage.getGarageTrucks())
                        garage.populateGarageWithTrucks()
                        print("\tTruck - " + plateNumber + " - removed with success")
                    else:
                        print("\tThe truck is on road. You cannot remove a truck while it has this state")
                else:
                    print("\tThere is no such truck")

            if selectedOption == 3:
                table = prettyTable.computeGarageTrucksTable(garage.getGarageTrucks())
                print(table)

            if selectedOption == 4:
                plateNumber = str(input("\tPlate number: "))
                if garage.getTruckByPlateNumber(plateNumber) is None:
                    print('\tThere is no such track with the inserted plate number')
                elif garage.isTruckOnRoad(plateNumber):
                    print("\tThe truck with the plate number " + plateNumber + " is already on road.")
                elif not garage.isTruckOnRoad(plateNumber) and search.checkIfCarWasAlreadyOnRoadThisMonth(plateNumber):
                    print("\tThe truck has already finished the work for this month")
                else:
                    garage.sendTruckOnRoad(plateNumber)
                    truckKnownValues: TruckKnownValues = fixedValues.readFixedDataWhenSendingTruckOnRoad(plateNumber)
                    truckWeekUpdates: TruckWeekUpdates = targetValues.readTargetDataWhenSendingTruckOnRoad(plateNumber)
                    if truckKnownValues is not None and truckWeekUpdates is not None:
                        truck: Truck = Truck(plateNumber, truckKnownValues, truckWeekUpdates)
                        fileReadWrite.createFilesWhenSendingTruckOnRoad(truck)
                        fileReadWrite.writeTrucksInGarageFile(garage.getGarageTrucks())
                        print("\tThe truck was sent on road")
                    else:
                        print("An error occurred, please try again...")

            if selectedOption == 5:
                plateNumber = str(input("\tPlate number: "))
                if not garage.isTruckOnRoad(plateNumber):
                    print("\tThe truck with the plate number " + plateNumber + " is already in garage.")
                else:
                    if targetValues.endOfWeek(garage, plateNumber):
                        garage.sendTruckToGarage(plateNumber)
                        fileReadWrite.writeTrucksInGarageFile(garage.getGarageTrucks())
                        print("\tThe truck was sent to garage")

            if selectedOption == 6:
                plateNumber = str(input("\tPlate number: "))

                inLoop = True
                while inLoop:
                    menu.printSubMenuOptionSixAndSeven()
                    subMenuOption = int(input("\t\tOption: "))

                    if subMenuOption == 0:
                        inLoop = False

                    if subMenuOption == 1:
                        textFiles = fileReadWrite.getAllFilesByPlateNumber(plateNumber, FIXED_VALUES + "/")
                        fileName = search.getLastReportFile(textFiles)
                        if fileName is not None:
                            truckKnownValues: TruckKnownValues = \
                                fileReadWrite.readFixedValuesFromFile(plateNumber, FIXED_VALUES + "/" + fileName)
                            table = prettyTable.printTruckKnownValues(truckKnownValues)
                            print(table)
                            print()
                        else:
                            print("\t\tNo information for the truck with plate number " + plateNumber)

                    if subMenuOption == 2:
                        year = int(input("\t\t\tYear: "))
                        month = int(input("\t\t\tMonth: "))
                        week = int(input("\t\t\tWeek: "))
                        textFiles = fileReadWrite.getAllFilesByPlateNumber(plateNumber, FIXED_VALUES + "/")
                        fileName = search.findFileByMonthAndYear(textFiles, week, month, year)
                        if fileName is not None:
                            truckKnownValues: TruckKnownValues = \
                                fileReadWrite.readFixedValuesFromFile(plateNumber, FIXED_VALUES + "/" + fileName)
                            table = prettyTable.printTruckKnownValues(truckKnownValues)
                            print(table)
                            print()
                        else:
                            print("\t\tNo information for the truck with plate number " + plateNumber)

            if selectedOption == 7:
                plateNumber = str(input("\tPlate number: "))
                textFiles = fileReadWrite.getAllFilesByPlateNumber(plateNumber, FIXED_VALUES + "/")
                fileName = search.getLastReportFile(textFiles)
                if fileName is not None:
                    truckKnownValues: TruckKnownValues = \
                        fileReadWrite.readFixedValuesFromFile(plateNumber, FIXED_VALUES + "/" + fileName)
                    kmPrice = truckKnownValues.getKilometerPrice()
                    kmExtraPrice = truckKnownValues.getKilometerExtraPrice()
                    expectedAmount = truckKnownValues.getExpectedPayedAmount()

                    inLoop = True
                    while inLoop:
                        menu.printSubMenuOptionSixAndSeven()
                        subMenuOption = int(input("\t\tOption: "))
                        if subMenuOption == 0:
                            inLoop = False

                        if subMenuOption == 1:
                            textFiles = fileReadWrite.getAllFilesByPlateNumber(plateNumber, TARGET_VALUES + "/")
                            fileName = search.getLastReportFile(textFiles)
                            if fileName is not None:
                                truckWeekUpdates: TruckWeekUpdates = \
                                    fileReadWrite.readWeekValuesFromFile(plateNumber, TARGET_VALUES + "/" + fileName)
                                table = prettyTable.printTruckWeekValues(truckWeekUpdates, kmPrice, kmExtraPrice, expectedAmount)
                                print(table)
                                print()
                            else:
                                print("\t\tNo information for the truck with plate number + " + plateNumber)

                        if subMenuOption == 2:
                            year = int(input("\t\t\tYear: "))
                            month = int(input("\t\t\tMonth: "))
                            week = int(input("\t\t\tWeek: "))
                            textFiles = fileReadWrite.getAllFilesByPlateNumber(plateNumber, TARGET_VALUES + "/")
                            fileName = search.findFileByMonthAndYear(textFiles, week, month, year)
                            if fileName is not None:
                                truckWeekUpdates: TruckWeekUpdates = \
                                    fileReadWrite.readWeekValuesFromFile(plateNumber, TARGET_VALUES + "/" + fileName)
                                table = prettyTable.printTruckWeekValues(truckWeekUpdates, kmPrice, kmExtraPrice, expectedAmount)
                                print(table)
                                print()
                            else:
                                print("\t\tNo information for the truck with plate number + " + plateNumber)

            if selectedOption == 8:
                plateNumber = str(input("\tPlate number: "))
                if garage.getTruckByPlateNumber(plateNumber) is not None:
                    targetValues.endOfWeek(garage, plateNumber)
                else:
                    print("\tSuch track does not exist")

            if selectedOption == 9:
                plateNumber = str(input("\tPlate number: "))
                if garage.getTruckByPlateNumber(plateNumber) is not None:
                    textFiles = fileReadWrite.getAllFilesByPlateNumber(plateNumber, TARGET_VALUES + "/")
                    fileName = search.getLastReportFile(textFiles)
                    if fileName is not None:
                        truckWeekUpdates: TruckWeekUpdates = \
                            fileReadWrite.readWeekValuesFromFile(plateNumber, TARGET_VALUES + "/" + fileName)
                        print("\tService have to be done in: " + str(truckWeekUpdates.kmUntilService()) + " kilometers")
                    else:
                        print("\tThe car was not on road before in order to check it's real kilometers")
                else:
                    print("\tThere is not truck in garage having the plate number: " + plateNumber)

            if selectedOption == 10:
                plateNumber = str(input("\tPlate number: "))
                textFilesFixed = fileReadWrite.getAllFilesByPlateNumber(plateNumber, FIXED_VALUES + "/")
                fileNameFixed = search.getLastReportFile(textFilesFixed)

                textFilesTarget = fileReadWrite.getAllFilesByPlateNumber(plateNumber, TARGET_VALUES + "/")
                fileNameTarget = search.getLastReportFile(textFilesTarget)

                if fileNameFixed is not None and fileNameTarget is not None:
                    truckKnownValues: TruckKnownValues = \
                        fileReadWrite.readFixedValuesFromFile(plateNumber, FIXED_VALUES + "/" + fileNameFixed)
                    knownTable = prettyTable.printTruckKnownValues(truckKnownValues)
                    kmPrice = truckKnownValues.getKilometerPrice()
                    kmExtraPrice = truckKnownValues.getKilometerExtraPrice()
                    expectedAmount = truckKnownValues.getExpectedPayedAmount()

                    truckWeekUpdates: TruckWeekUpdates = \
                        fileReadWrite.readWeekValuesFromFile(plateNumber, TARGET_VALUES + "/" + fileNameTarget)
                    updateTable = prettyTable.printTruckWeekValues(truckWeekUpdates, kmPrice, kmExtraPrice, expectedAmount)

                    print(knownTable)
                    print(updateTable)
                    print()

                else:
                    print("\tNo files found for the selected truck: " + plateNumber)

            if selectedOption == 11:
                plateNumber = str(input("\tPlate number: "))
                textFilesTarget = fileReadWrite.getAllFilesByPlateNumber(plateNumber, TARGET_VALUES + "/")
                fileNameTarget = search.getLastReportFile(textFilesTarget)
                if fileNameTarget is not None:
                    truckWeekUpdates: TruckWeekUpdates = \
                        fileReadWrite.readWeekValuesFromFile(plateNumber, TARGET_VALUES + "/" + fileNameTarget)
                    serviceCost = float(input("\t\tService cost:"))
                    truckAfterService: TruckWeekUpdates = targetValues.sendTruckInService(truckWeekUpdates, serviceCost)
                    fileReadWrite.writeTruckWeekUpdateFile(truckAfterService, TARGET_VALUES + "/" + fileNameTarget)
                    print("\tTruck registered with success to service")
                else:
                    print("\tNo files found for the selected truck: " + plateNumber)
        except:
            print("\tInput type must be a number")
            continue


if __name__ == "__main__":
    main()
