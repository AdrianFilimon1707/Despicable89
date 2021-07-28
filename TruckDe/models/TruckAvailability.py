from TruckDe.state.constants import ON_ROAD, IN_GARAGE


class TruckAvailability:
    def __init__(self, plateNumber: str, available: bool):
        self.__plateNumber = plateNumber
        self.__available = available

    def setAvailability(self, availability: bool):
        self.__available = availability

    def getPlateNumber(self):
        return self.__plateNumber

    def getAvailability(self):
        if self.__available:
            return IN_GARAGE
        else:
            return ON_ROAD
