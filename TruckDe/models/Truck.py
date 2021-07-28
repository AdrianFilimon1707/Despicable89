from TruckDe.state import constants
from TruckDe.models.TruckWeekUpdates import TruckWeekUpdates
from TruckDe.models.TruckKnownValues import TruckKnownValues


# TODO: create a new object for fixed and target values and pass them as classes in truck component
class Truck:
    def __init__(self, plateNumber: str, truckKnownValues: TruckKnownValues, truckWeekUpdates: TruckWeekUpdates):
        self.__plateNumber = plateNumber
        self.__truckWeekUpdates = truckWeekUpdates
        self.__truckKnownValues = truckKnownValues

    def getPlateNumber(self):
        return self.__plateNumber

    def getTruckWeekUpdates(self):
        return self.__truckWeekUpdates

    def getTruckKnownValues(self):
        return self.__truckKnownValues

