from payload import *
def generate_response(payload: PayLoad):
    response = []
    for energy_source in payload.powerplants:
        response.append({"name":energy_source.name, "p":0})
    return response


def fill_not_used_powerplants(payload: PayLoad, response):
    current_powerplants = {}
    for powerplant in payload.powerplants:
        current_powerplants[powerplant.name] = 0
    for powerplant in response:
        current_powerplants[powerplant["name"]]  = 1
    
    for key in current_powerplants:
        if current_powerplants[key] == 0:
            response.append({"name":key, "p": 0})

    return response

def process_payload(payload: PayLoad):
    required_energy = payload.load
    ## since the wind energy is the most cost effecient and provides clean energy, we get the maximum of the wind turbines
    response_temp = []
    
    
    
    
    
    # check if the minimum power provided by the gas powerplants meets the demand
    for powerplant in payload.powerplants:
        if powerplant.type == "gasfired":
            gas_fired_contribution = 0
            gas_fired_contribution = powerplant.pmin * powerplant.efficiency
            if required_energy - gas_fired_contribution > 0: # check if the the minimum enegry provided by gas powerplant  is not sufficient
                required_energy -= gas_fired_contribution

    # if the demand is lower than the minimum that can be provided by the gas powerplants
    # give a response that no powerplants should be switched on
    if required_energy <= 0.0:
        return generate_response(payload)
    
    
    
    ## since the wind energy is the most cost effecient and provides clean energy, we get the maximum of the wind turbines
    # we also keep checking if the wind turbines could provide enough power to meet the required load.
    # if not we make the gas powerplants produce more than the minimum in next steps.
    for powerplant in payload.powerplants:
        if powerplant.type == "windturbine":
            wind_contribution = 0
            wind_contribution = powerplant.pmax * powerplant.efficiency * (payload.fuels.wind_percent/100)
            if required_energy - wind_contribution > 0: 
                # the the enegry provided by one windturbine is not sufficient
                
                response_temp.append({"name" : powerplant.name, "p":round(wind_contribution, 1)})
                # the round function is not realistic here since it is not desired to provide slightly less than the demand
                # we can add 0.05 to the wind_contribution and round it off to the first decimal e.g. 2.14 -> 2.19 -> 2.2
                required_energy -= wind_contribution
            else:
                response_temp.append({"name" : powerplant.name, "p": round(required_energy, 1)})
                required_energy -= wind_contribution
                return response_temp
    
    # Now, if the wind energy is still not enough, strat using the gasfire powerplants        
    for powerplant in payload.powerplants:
        if powerplant.type == "gasfired":
            gas_fired_contribution = 0
            gas_fired_contribution = powerplant.pmax * powerplant.efficiency
            if required_energy - gas_fired_contribution > 0: 
                # the the enegry provided by one gasfire powerplant is not sufficient
                response_temp.append({"name" : powerplant.name, "p":round(gas_fired_contribution, 1)})
                # the round function is not realistic here since it is not desired to provide slightly less than the demand
                # possible solution: we can add 0.05 to the wind_contribution and round it off to the first decimal e.g. 2.14 -> 2.19 -> 2.2 or 3.88 -> 3.93 -> 3.90
                required_energy -= gas_fired_contribution
            else:
                # if we have enough power, then stop looking for more powerplants
                response_temp.append({"name" : powerplant.name, "p": round( required_energy, 1)})
                required_energy -= gas_fired_contribution
                return response_temp
    
    # if the wind and the gas powerplants are still not enough to meet the demand, start using the turbojet powerplants
    for powerplant in payload.powerplants:
        if powerplant.type == "turbojet":
            turbojet_contribution = 0
            turbojet_contribution = powerplant.pmax * powerplant.efficiency
            if required_energy - turbojet_contribution > 0: 
                # the the enegry provided by one gasfire powerplant is not sufficient
                response_temp.append({"name" : powerplant.name, "p":round(turbojet_contribution, 1)})
                # the round function is not realistic here since it is not desired to provide slightly less than the demand
                # possible solution: we can add 0.05 to the wind_contribution and round it off to the first decimal e.g. 2.14 -> 2.19 -> 2.2 or 3.88 -> 3.93 -> 3.90
                required_energy -= turbojet_contribution
            else:
                # if we have enough power, then stop looking for more powerplants
                response_temp.append({"name" : powerplant.name, "p": round( required_energy, 1)})
                required_energy -= turbojet_contribution
                return response_temp

    # if all power plants cannot provide the required power then generate a response that mentions that it is not possible to provide the demanded engery
    if required_energy > 0:
        response_error = {"the load required cannot be provided by the powerplants":0}
        return response_error
    # at the end, all resting powerplants that are not used should be added in order to provide a response similar to the response required
    response = fill_not_used_powerplants(payload, response_temp)
    return response
