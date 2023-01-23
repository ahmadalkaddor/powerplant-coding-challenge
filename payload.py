
def get_payload():
    payload = {
  "load": 910,
  "fuels":
  {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredsomewhatsmaller",
      "type": "gasfired",
      "efficiency": 0.37,
      "pmin": 40,
      "pmax": 210
    },
    {
      "name": "tj1",
      "type": "turbojet",
      "efficiency": 0.3,
      "pmin": 0,
      "pmax": 16
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 150
    },
    {
      "name": "windpark2",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 36
    }
  ]
    }
    return payload




##save the prices in price class, expects the fuel feld of the playload object fuels : Fuel(payload["fuels"])
class Fuels():
    def __init__(self, fuels) -> None:
        self.gas_price_euro_megawatt = fuels["gas(euro/MWh)"]
        self.kerosine_price_euro_megawatt = fuels["kerosine(euro/MWh)"]
        self.co2_euro_ton = fuels["co2(euro/ton)"]
        self.wind_percent = fuels["wind(%)"]

    def __str__(self):
        print(self.gas_price_euro_megawatt)
        print(self.kerosine_price_euro_megawatt)
        print(self.co2_euro_ton)
        print(self.wind_percent)
        return "done!"


## build a powerplant object based on a dictionary, expects the a powerplant of the playload object fuels see main for examples
class PowerPlant():
    def __init__(self, powerPlant) -> None:
        self.name = powerPlant["name"]
        self.type = powerPlant["type"]
        self.effeciency = powerPlant["efficiency"]
        self.pmin = powerPlant["pmin"]
        self.pmax = powerPlant["pmax"]
    def __str__(self):
        print(self.name)
        print(self.type)
        print(self.effeciency)
        print(self.pmin)
        print(self.pmax)
        return "done!"
## build a Payload object based on a content of the of the post request
class PayLoad():
    def __init__(self, payload) -> None:
        self.load = payload["load"]
        self.fuels = Fuels(payload["fuels"])
        self.powerplants = []
        for powerplant in payload["powerplants"]:
            self.powerplants.append(PowerPlant(powerPlant=powerplant))
        
    def __str__(self):
        print("load : ", str(self.load))
        print("fuels: ")
        print(self.fuels)
        print("powerplants: ")
        for p in self.powerplants:
            print(p)
        
        
    
        
# def main():
    
#     payload = get_payload()
#     load = PayLoad(payload=payload)
#     load.print_payload()
    
# main()