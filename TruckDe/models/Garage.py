from TruckDe.state.constants import ON_ROAD
from TruckDe.utils import fileReadWrite
from TruckDe.models.TruckAvailability import TruckAvailability


class Garage:
    def __init__(self):
        self.__garageTrucks = []

    def populateGarageWithTrucks(self):
        trucksReadFromFile = fileReadWrite.readTrucksFromGarageFile()
        self.setGarageTrucks(trucksReadFromFile)

    def setGarageTrucks(self, newGarageTrucks):
        self.__garageTrucks = newGarageTrucks

    def getGarageTrucks(self):
        return self.__garageTrucks

    def sendTruckOnRoad(self, plateNumber: str):
        truck: TruckAvailability
        foundTruck = self.getTruckByPlateNumber(plateNumber)

        if foundTruck is not None:
            foundTruck.setAvailability(False)

    def sendTruckToGarage(self, plateNumber: str):
        truck: TruckAvailability
        foundTruck = self.getTruckByPlateNumber(plateNumber)

        if foundTruck is not None:
            foundTruck.setAvailability(True)

    def getTruckByPlateNumber(self, plateNumber: str):
        for truck in self.__garageTrucks:
            if truck.getPlateNumber() == plateNumber:
                return truck

        return None

    def isTruckOnRoad(self, plateNumber: str):
        truck: TruckAvailability
        for truck in self.__garageTrucks:
            if truck.getPlateNumber() == plateNumber and truck.getAvailability() == ON_ROAD:
                return True
        return False
