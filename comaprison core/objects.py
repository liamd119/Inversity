import json


class Battery:
    def __init__(self, filepath):
        with open(filepath) as file:
            _json_data = json.load(file)
        self.number_of_cycles: float = _json_data["number_of_cycles"]
        self.usage_per_day: float = _json_data["usage_per_day"]
        self.capacity: float = _json_data["capacity"]
        self.purchase_cost: float = _json_data["purchase_cost"]
        self.charge_time: float = _json_data["charge_time"]

    def cost_per_day(self) -> float:
        """Returns the approximate cost per day of the battery.
        Uses the formula `cost per day = total purchase cost / fraction of battery lifetime used per day`.
        The fraction of battery lifetime per day is calculated from
        `total lifetime cycles / (daily usage / total capacity)`."""
        return (self.purchase_cost / (self.number_of_cycles / (self.usage_per_day / self.capacity)) + self.charge_time)
