import os
import sys


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def __str__(self):
        return "FileManager(filename=" + self.filename + "mode=" + self.mode + ")"

    def __repr__(self):
        return {'filename': self.filename, 'mode': self.mode}


class PlateNumber:
    def __init__(self, pn):
        self.plateNumber = pn

    @property
    def plateNumber(self):
        return self.__plateNumber

    @plateNumber.setter
    def plateNumber(self, pn):
        self.__plateNumber = pn

    def __str__(self):
        return "PlateNumber(plateNumber=" + self.plateNumber + ")"

    def __repr__(self):
        return {"plateNumber": self.plateNumber}


class Truck(PlateNumber):
    def __init__(self, plateNumber: str, available: bool):
        PlateNumber.__init__(self, plateNumber)
        self.__available = available

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, a):
        self.__available = a

    def __str__(self):
        return "Truck(plateNumber=" + self.plateNumber + ", available=" + str(self.available) + ")"

    def __repr__(self):
        return {'plateNumber': str(self.plateNumber), 'available': str(self.available)}


class Garage:
    def __init__(self):
        self.trucks = []

    @property
    def trucks(self):
        return self.__trucks

    @trucks.setter
    def trucks(self, g):
        self.__trucks = g

    def addElement(self, truck):
        self.trucks = self.trucks + [truck]

    def sendTruckOnRoad(self, plateNumber):
        truck: Truck
        for truck in self.trucks:
            if truck.plateNumber == plateNumber:
                truck.available = False
                break

    def truckAvailability(self, plateNumber):
        truck: Truck = self.__getitem__(plateNumber)
        if truck is not None:
            return truck.available
        return False

    def isTruckDefined(self, plateNumber):
        truck: Truck = self.__getitem__(plateNumber)
        if truck is not None and truck.plateNumber == plateNumber:
            return True
        return False

    def __getitem__(self, plateNumber):
        truck: Truck
        for truck in self.trucks:
            if truck.plateNumber == plateNumber:
                return truck
        return None

    def __len__(self):
        return len(self.trucks)

    def __contains__(self, plateNumber):
        truck: Truck
        for truck in self.trucks:
            if truck.plateNumber == plateNumber:
                return True
        return False

    def __str__(self):
        trucks = "Garage cars: \n"
        for truck in self.trucks:
            status = "In garage"
            if not truck.available:
                status = 'On road'
            trucks += "\t" + truck.plateNumber + " - " + status + "\n"

        return trucks

    def __repr__(self):
        trucks = "\tGarage cars: \n"
        for truck in self.trucks:
            status = "In garage"
            if not truck.available:
                status = 'On road'
            trucks += "\t" + truck.plateNumber + " - " + status + "\n"

        return trucks

class FixedValues:
    def __init__(self, leasing: float, salary: float, insurance: float, officeSalary: float, eurovignete: float,
                 bonusDriver: float, kmPrice: float, kmExtraPrice: float, diesel: float, otherCosts: float,
                 daysOnRoad: int, km: float):
        self.leasing = leasing
        self.salary = salary
        self.insurance = insurance
        self.officeSalary = officeSalary
        self.eurovignete = eurovignete
        self.bonusDriver = bonusDriver
        self.kmPrice = kmPrice
        self.kmExtraPrice = kmExtraPrice
        self.diesel = diesel
        self.otherCosts = otherCosts
        self.daysOnRoad = daysOnRoad
        self.kilometers = km

    @property
    def leasing(self):
        return self.__leasing

    @leasing.setter
    def leasing(self, l):
        self.__leasing = l

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        self.__salary = s

    @property
    def insurance(self):
        return self.__insurance

    @insurance.setter
    def insurance(self, i):
        self.__insurance = i

    @property
    def officeSalary(self):
        return self.__officeSalary

    @officeSalary.setter
    def officeSalary(self, os):
        self.__officeSalary = os

    @property
    def eurovignete(self):
        return self.__eurovignete

    @eurovignete.setter
    def eurovignete(self, e):
        self.__eurovignete = e

    @property
    def bonusDriver(self):
        return self.__bonusDriver

    @bonusDriver.setter
    def bonusDriver(self, bd):
        self.__bonusDriver = bd

    @property
    def kmPrice(self):
        return self.__kmPrice

    @kmPrice.setter
    def kmPrice(self, kp):
        self.__kmPrice = kp

    @property
    def kmExtraPrice(self):
        return self.__kmExtraPrice

    @kmExtraPrice.setter
    def kmExtraPrice(self, kmEP):
        self.__kmExtraPrice = kmEP

    @property
    def diesel(self):
        return self.__diesel

    @diesel.setter
    def diesel(self, d):
        self.__diesel = d

    @property
    def otherCosts(self):
        return self.__otherCosts

    @otherCosts.setter
    def otherCosts(self, oc):
        self.__otherCosts = oc

    @property
    def daysOnRoad(self):
        return self.__daysOnRoad

    @daysOnRoad.setter
    def daysOnRoad(self, dor):
        self.__daysOnRoad = dor

    @property
    def kilometers(self):
        return self.__kilometers

    @kilometers.setter
    def kilometers(self, k):
        self.__kilometers = k

    def expectedPayedAmount(self):
        return self.leasing + self.salary + self.insurance + self.officeSalary + self.eurovignete + self.bonusDriver

    def __str__(self) -> str:
        return "FixedValues=(leasing=" + str(self.leasing) + "salary=" + str(self.salary) + "insurance=" + \
               str(self.insurance) + "officeSalary=" + str(self.officeSalary) + "eurovignete=" + str(self.eurovignete) + \
               "bonusDriver=" + str(self.bonusDriver) + "kmPrice=" + str(self.kmPrice) + "kmExtraPrice=" + \
               str(self.kmExtraPrice) + "diesel=" + str(self.diesel) + "otherCosts=" + str(self.__otherCosts) + \
               "daysOnRoad=" + str(self.daysOnRoad) + "kilometers=" + str(self.kilometers) + ")"

    def __repr__(self):
        return {
            'leasing': str(self.leasing),
            'salary': str(self.salary),
            'insurance': str(self.insurance),
            'officeSalary': str(self.officeSalary),
            'eurovignete': str(self.eurovignete),
            'bonusDriver': str(self.bonusDriver),
            'kmPrice': str(self.kmPrice),
            'kmExtraPrice': str(self.kmExtraPrice),
            'diesel': str(self.diesel),
            'otherCosts': str(self.otherCosts),
            'daysOnRoad': str(self.daysOnRoad),
            'kilometers': str(self.kilometers),
        }


class UpdatedValues:
    def __init__(self, diesel, dieselDetails, otherCosts, otherCostsDetails, daysOnRoad, daysOnRoadDetails, km, kmDetails):
        self.updatedDiesel = diesel
        self.updatedOtherCosts = otherCosts
        self.updatedDaysOnRoad = daysOnRoad
        self.updatedKilometers = km

        self.dieselDetails = dieselDetails
        self.otherCostsDetails = otherCostsDetails
        self.daysOnRoadDetails = daysOnRoadDetails
        self.kilometersDetails = kmDetails

    @property
    def updatedDiesel(self):
        return self.__updatedDiesel

    @updatedDiesel.setter
    def updatedDiesel(self, d):
        self.__updatedDiesel = d

    @property
    def updatedOtherCosts(self):
        return self.__updatedOtherCosts

    @updatedOtherCosts.setter
    def updatedOtherCosts(self, oc):
        self.__updatedOtherCosts = oc

    @property
    def updatedDaysOnRoad(self):
        return self.__updatedDaysOnRoad

    @updatedDaysOnRoad.setter
    def updatedDaysOnRoad(self, dor):
        self.__updatedDaysOnRoad = dor

    @property
    def updatedKilometers(self):
        return self.__updatedKilometers

    @updatedKilometers.setter
    def updatedKilometers(self, k):
        self.__updatedKilometers = k

    @property
    def dieselDetails(self):
        return self.__dieselDetails

    @dieselDetails.setter
    def dieselDetails(self, d):
        self.__dieselDetails = d

    @property
    def otherCostsDetails(self):
        return self.__otherCostsDetails

    @otherCostsDetails.setter
    def otherCostsDetails(self, oc):
        self.__otherCostsDetails = oc

    @property
    def daysOnRoadDetails(self):
        return self.__daysOnRoadDetails

    @daysOnRoadDetails.setter
    def daysOnRoadDetails(self, dor):
        self.__daysOnRoadDetails = dor

    @property
    def kilometersDetails(self):
        return self.__kilometersDetails

    @kilometersDetails.setter
    def kilometersDetails(self, k):
        self.__kilometersDetails = k

    def __str__(self):
        return "UpdatedValue=(diesel=" + str(self.updatedDiesel) + "dieselDetails=" + str(self.dieselDetails) + \
               "otherCosts=" + str(self.updatedOtherCosts) + "otherCostsDetails=" + str(self.otherCostsDetails) + \
               "daysOnRoad=" + str(self.updatedDaysOnRoad) + "daysOnRoadDetails=" + str(self.daysOnRoadDetails) + \
               "kilometers=" + str(self.__updatedKilometers) + "kilometersDetails=" + str(self.kilometersDetails) + ")"

    def __repr__(self):
        return {
            'diesel': str(self.updatedDiesel),
            'dieselDetails': str(self.dieselDetails),
            'otherCosts': str(self.updatedOtherCosts),
            'otherCostsDetails': str(self.otherCostsDetails),
            'daysOnRoad': str(self.updatedOtherCosts),
            'daysOnRoadDetails': str(self.daysOnRoadDetails),
            'kilometers': str(self.updatedKilometers),
            'kilometersDetails': str(self.kilometersDetails)
        }

class Mixin:

    def computeDifference(self,a ,b):
        return a-b

class Report:
    def __init__(self, fixedValues: FixedValues, updatedValues: UpdatedValues):
        self.fixedValues = fixedValues
        self.updatedValues = updatedValues

    @property
    def fixedValues(self):
        return self.__fixedValues

    @fixedValues.setter
    def fixedValues(self, fv):
        self.__fixedValues = fv

    @property
    def updatedValues(self):
        return self.__updatedValues

    @updatedValues.setter
    def updatedValues(self, uv):
        self.__updatedValues = uv

    def calculateForReport(self):
        fixedValues: FixedValues = self.fixedValues
        updatedValues: UpdatedValues = self.updatedValues
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\tExpected leasing: " + str(fixedValues.leasing))
        print("\tExpected salary: " + str(fixedValues.salary))
        print("\tExpected insurance: " + str(fixedValues.insurance))
        print("\tExpected office salary: " + str(fixedValues.officeSalary))
        print("\tExpected eurovignete: " + str(fixedValues.eurovignete))
        print("\tExpected bonus driver: " + str(fixedValues.bonusDriver))
        print("\tPrice/KM: " + str(fixedValues.kmPrice))
        print("\tExtra price/KM: " + str(fixedValues.kmExtraPrice))
        print('=========================================================')
        print("\t\t\tProfit/Loss: " + str(-fixedValues.expectedPayedAmount()))
        print("---------------------------------------------------------")
        print('\tExpected diesel: ' + str(fixedValues.diesel))
        print('\tActual diesel : ' + str(updatedValues.updatedDiesel))
        print('\tDiesel details: ' + str(updatedValues.dieselDetails))

        print('\tExpected other costs: ' + str(fixedValues.otherCosts))
        print('\tActual other costs : ' + str(updatedValues.updatedOtherCosts))
        print('\tOther costs details: ' + str(updatedValues.otherCostsDetails))

        print('\tExpected days: ' + str(fixedValues.daysOnRoad))
        print('\tActual days on road : ' + str(updatedValues.updatedDaysOnRoad))
        print('\tDays on road details: ' + str(updatedValues.daysOnRoadDetails))

        print('\tExpected KM: ' + str(fixedValues.kilometers))
        print('\tActual KM: ' + str(updatedValues.updatedKilometers))
        print('\tKM details: ' + str(updatedValues.kilometersDetails))

        dieselCosts = fixedValues.diesel - updatedValues.updatedDiesel
        amountForOtherCosts = fixedValues.otherCosts - updatedValues.updatedOtherCosts
        kilometersDone = fixedValues.kilometers - updatedValues.updatedKilometers

        totalProfitLoss = -fixedValues.expectedPayedAmount() + amountForOtherCosts + dieselCosts

        print("---------------------------------------------------------")
        if kilometersDone < 0:
            amountForExpectedKm = fixedValues.kmPrice * fixedValues.kilometers
            amountForExtraKm = (-kilometersDone) * fixedValues.kmExtraPrice
            totalProfitLoss += amountForExtraKm + amountForExpectedKm
            print("\tPrice for KM done: " + str(amountForExpectedKm))
            print("\tExtra KM done: " + str(-kilometersDone))
            print("\tPayed for extra KM done: " + str(amountForExtraKm))
        else:
            amountForRealKilometers = fixedValues.kmPrice * updatedValues.updatedKilometers
            totalProfitLoss += amountForRealKilometers
            print("\tPrice for KM done: " + str(amountForRealKilometers))
        print('=========================================================')
        print("\t\t\tTOTAL Profit/Loss: " + str(totalProfitLoss))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    def __add__(self, other: 'Report'):
        newDiesel = self.updatedValues.updatedDiesel + other.updatedValues.updatedDiesel
        otherCosts = self.updatedValues.updatedOtherCosts + other.updatedValues.updatedOtherCosts
        noOfDays = self.updatedValues.updatedDaysOnRoad + other.updatedValues.updatedDaysOnRoad
        target = self.updatedValues.updatedKilometers + other.updatedValues.updatedKilometers

        dieselDetailsOutput = self.updatedValues.dieselDetails
        if other.updatedValues.dieselDetails != "":
            dieselDetailsOutput += " - " + other.updatedValues.dieselDetails

        otherCostsDetailsOutput = self.updatedValues.otherCostsDetails
        if other.updatedValues.otherCostsDetails != "":
            otherCostsDetailsOutput += " - " + other.updatedValues.otherCostsDetails

        noOfDaysDetailsOutput = self.updatedValues.daysOnRoadDetails
        if other.updatedValues.daysOnRoadDetails != "":
            noOfDaysDetailsOutput += " - " + other.updatedValues.daysOnRoadDetails

        targetDetailsOutput = self.updatedValues.kilometersDetails
        if other.updatedValues.kilometersDetails != "":
            targetDetailsOutput += " - " + other.updatedValues.kilometersDetails

        self.updatedValues.updatedDiesel = newDiesel
        self.updatedValues.updatedOtherCosts = otherCosts
        self.updatedValues.updatedDaysOnRoad = noOfDays
        self.updatedValues.updatedKilometers = target

        self.updatedValues.dieselDetails = dieselDetailsOutput
        self.updatedValues.otherCostsDetails = otherCostsDetailsOutput
        self.updatedValues.daysOnRoadDetails = noOfDaysDetailsOutput
        self.updatedValues.kilometersDetails = targetDetailsOutput

        return self

    def __str__(self) -> str:
        return "Report(FixedValues(" + self.fixedValues + "), UpdatedValues(" + self.updatedValues + ")"

    def __repr__(self):
        return {'fixedValues': self.fixedValues, 'updatedValues': self.updatedValues}


class Reports:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)

    def setReportsSequence(self, plateNumber: str):
        for pn in self.__dict__:
            if pn == plateNumber:
                truckReports = self.__dict__[pn]
                for report in truckReports:
                    yield report
                break

    def __setitem__(self, key: str, value):
        self.__dict__[key] = value

    def __getitem__(self, key: str):
        try:
            return self.__dict__[key]
        except KeyError:
            return None

    def __delitem__(self, key: str):
        try:
            del self.__dict__[key]
        except KeyError:
            return None

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __str__(self):
        prettyPrint = ""
        for key, value in self.__dict__.items():
            prettyPrint += key + " - " + ", ".join(value)
        return prettyPrint

    def __repr__(self):
        return '{}, D({})'.format(super(Reports, self).__repr__(), self.__dict__)


def readFixedValues():
    try:
        print('\tPlease input the fixed data:')
        leasing = float(input("\t\tLeasing: "))
        salary = float(input("\t\tSalary: "))
        insurance = float(input("\t\tInsurance: "))
        officeSalary = float(input("\t\tOffice salary: "))
        eurovignete = float(input("\t\tEurovignete: "))
        bonusDriver = float(input("\t\tBonus driver: "))
        kmPrice = float(input("\t\tPrice/KM: "))
        kmExtraPrice = float(input("\t\tExtra price/KM: "))
        diesel = float(input("\t\tDiesel: "))
        otherCosts = float(input("\t\tOther costs: "))
        daysOnRoad = int(input("\t\tDays on road: "))
        kilometers = float(input("\t\tKilometers: "))

        return FixedValues(leasing, salary, insurance, officeSalary, eurovignete, bonusDriver, kmPrice, kmExtraPrice,
                           diesel, otherCosts, daysOnRoad, kilometers)
    except:
        print('Something went wrong when reading fixed values...')


def readWeekUpdatedValues():
    try:
        print('\tPlease input the target data:')
        dieselActual = float(input("\tDiesel: "))
        dieselDetails = str(input("\tDiesel details: "))
        otherCostsActual = float(input("\tOther costs: "))
        otherCostsDetails = str(input("\tOther costs details: "))
        noOfDaysActual = int(input("\tNo. of days: "))
        noOfDaysDetails = str(input("\tNo. of days details: "))
        targetActual = float(input("\tKilometers: "))
        targetDetails = str(input("\tKilometers details: "))

        return UpdatedValues(dieselActual, dieselDetails,
                             otherCostsActual, otherCostsDetails,
                             noOfDaysActual, noOfDaysDetails,
                             targetActual, targetDetails)
    except:
        print('Something went wrong when reading updated values...')


def printMenu():
    print('\n-------------------------')
    print("1. Add truck")
    print("2. Show trucks")
    print("3. Send truck on road")
    print("4. Truck status report")
    print("5. Reports")
    print("0. Exit\n")


def main():
    fileName = 'garage.txt'
    if os.path.exists(fileName):
        os.remove(fileName)
    garage = Garage()
    reports = Reports()

    while True:
        printMenu()
        try:
            option = int(input("Option: "))
            if option == 0:
                if os.path.exists(fileName):
                    os.remove(fileName)
                sys.exit(0)
            if option == 1:
                plateNumber = str(input("\tPlate number: "))
                truck: Truck = Truck(plateNumber, True)
                if not garage.isTruckDefined(plateNumber):
                    garage.addElement(truck)
                    fileManager = FileManager(fileName, 'w')
                    with fileManager as f:
                        f.write(garage.__repr__())
                else:
                    print('\tTruck already exists.')
            if option == 2:
                if garage.__len__() == 0:
                    print("\tThere are no trucks available")
                else:
                    print()
                    print(garage.__str__())

            if option == 3:
                plateNumber = str(input("\tPlate number: "))
                if garage.isTruckDefined(plateNumber) and garage.truckAvailability(plateNumber):
                    garage.sendTruckOnRoad(plateNumber)
                    fixedValues: FixedValues = readFixedValues()
                    updatedValues = UpdatedValues(0, "", 0, "", 0, "", 0, "")
                    report = Report(fixedValues, updatedValues)
                    reports[plateNumber] = [report]
                    print("\tTruck sent on road")
                else:
                    print('\tTruck does not exist or it is already on road')

            if option == 4:
                plateNumber = str(input("\tPlate number: "))
                if garage.isTruckDefined(plateNumber):
                    updatedValues: UpdatedValues = readWeekUpdatedValues()
                    reportsList = reports.__getitem__(plateNumber)
                    firstReport: Report = reportsList[0]
                    lastReport: Report = reportsList[len(reportsList) - 1]
                    newReport = Report(firstReport.fixedValues, updatedValues) + lastReport
                    reportsList.append(newReport)
                    reports[plateNumber] = reportsList
                else:
                    print('\tTruck does not exist')

            if option == 5:
                plateNumber = str(input("\tPlate number: "))
                if garage.isTruckDefined(plateNumber):
                    reportsSequence = reports.setReportsSequence(plateNumber)
                    try:
                        currentReport: Report = next(reportsSequence)
                        while currentReport is not None:
                            currentReport.calculateForReport()
                            currentReport: Report = next(reportsSequence)
                    except StopIteration:
                        continue
                else:
                    print('\tTruck does not exist or it is already on road')
        except ValueError:
            print('Something went wrong...')


if __name__ == '__main__':
    main()
