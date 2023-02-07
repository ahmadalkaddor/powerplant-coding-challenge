from payload import *
def generate_response(payload: PayLoad):
    response = []
    for energy_source in payload.powerplants:
        response.append({"name":energy_source.name, "p":0})
    return response



def marginal_cost(fuel_cost, efficiency, powerplant_type, pmin):
    """
    marginal_cost function calculates the the cost of operating a powerplant considering it's efficiency and minimum power produced 
    by the corresponding powerplant. The lower the cost is, the more efficient the powerplant is considerd.
    Windturbines are the most efficient with cost = 0
    """
    if powerplant_type in ["gasfired", "turbojet"]:
        return (fuel_cost / efficiency) + (pmin  * efficiency)
    elif powerplant_type == "windturbine":
        return 0
    else:
        raise ValueError(f"Unsupported power plant type: {powerplant_type}")

def process_payload(payload: PayLoad):
    """Please notice that this implementation is based on the basic understanding of the context. 
       It is desired to communicate with the experts to have a better understanding of their preferences.
    """
    required_energy = payload.load    
    response_temp = []
    # sort the powerplants by the margina cost(ascending). The wind turbines are the most efficient and are placed in the beginning of the array
    payload.powerplants = sorted(payload.powerplants, key=lambda pp: marginal_cost(payload.get_price(pp.type), pp.efficiency, pp.type, pp.pmin))
    
    # iterate over the available powerplants 
    for pp in payload.powerplants:
        # variable pmax_efficiency is the maximum power considering the efficiency
        pmax_efficiency = 0
        # the formula for pmax_efficiency is different for the wind turbines since they depend on wind percentage(%).
        if pp.type == "windturbine":
            pmax_efficiency = pp.pmax * pp.efficiency * (payload.fuels.wind_percent/100)
        else:
            pmax_efficiency = pp.pmax * pp.efficiency
        # if the required energy is more than the energy that can be provided by the powerplant, then swith the powerplant on full capacity 
        if pmax_efficiency <= required_energy:
            response_temp.append({"name":pp.name ,"p":round(pmax_efficiency, 1)})
            required_energy -= round(pmax_efficiency, 1)
        # if the required energy is less than the energy that can be provided by the powerplant:
        else:
            # if required_energy == 0, then add the corresponding powerplant to results with p = 0.
            # this helps to generate a full response (overview) containing all powerplants and the required energy
            # otherwise then overview will only contain the powerplants that should be switched on
            if required_energy == 0:
                response_temp.append({"name":pp.name ,"p":0})
            else:
                """
                if the required energy is greater than 0 and less than pmin: then switch the powerplant with pmin
                since the powerplant cannot generate power below this dremple.
                if required_energy < pp.pmin:
                    response_temp.append({"name":pp.name ,"p":pp.pmin})
                else:
                """
                response_temp.append({"name":pp.name ,"p":round(required_energy, 1)})
                current_energy_provision += round(required_energy, 1)
                required_energy = 0
    # if all power plants cannot provide the required power then generate a response that mentions that it is not possible to provide the demanded engery
    if required_energy > 0:
        response_error = "the load required cannot be provided by the powerplants"
        return response_error
    # at the end, all resting powerplants that are not used should be added in order to provide a response similar to the response required
    return response_temp




# def process_payload_v1(payload: PayLoad):
#     """Please notice that this implementation is based on the basic understanding of the context. 
#        It is desired to communicate with the experts to have a better understanding of their preferences.
#     """
#     required_energy = payload.load    
#     response_temp = []
#     current_energy_provision = 0
#     # sort the powerplants by the margina cost(ascending). The wind turbines are the most efficient and are placed in the beginning of the array
#     payload.powerplants = sorted(payload.powerplants, key=lambda pp: marginal_cost(payload.get_price(pp.type), pp.efficiency, pp.type, pp.pmin))
    
#     # iterate over the available powerplants 
#     for pp in payload.powerplants:
#         # variable pmax_efficiency is the maximum power considering the efficiency
#         pmax_efficiency = 0
#         # the formula for pmax_efficiency is different for the wind turbines since they depend on wind percentage(%).
#         if pp.type == "windturbine":
#             pmax_efficiency = pp.pmax * pp.efficiency * (payload.fuels.wind_percent/100)
#         else:
#             pmax_efficiency = pp.pmax * pp.efficiency
#         # if the required energy is more than the energy that can be provided by the powerplant, then swith the powerplant on full capacity 
#         if pmax_efficiency <= required_energy:
#             response_temp.append({"name":pp.name ,"p":round(pmax_efficiency + 0.05, 1)})# we can add 0.05 to the  and round off to the first decimal e.g. 2.14 -> 2.19 -> 2.2
#             required_energy -= pmax_efficiency
#         # if the required energy is less than the energy that can be provided by the powerplant:
#         else:
#             # if required_energy == 0, then add the corresponding powerplant to results with p = 0.
#             # this helps to generate a full response (overview) containing all powerplants and the required energy
#             # otherwise then overview will only contain the powerplants that should be switched on
#             if required_energy == 0:
#                 response_temp.append({"name":pp.name ,"p":0})
#             else:
#                 """
#                 if the required energy is greater than 0 and less than pmin: then switch the powerplant with pmin
#                 since the powerplant cannot generate power below this dremple.
#                 if required_energy < pp.pmin:
#                     response_temp.append({"name":pp.name ,"p":pp.pmin})
#                 else:
#                 """
#                 response_temp.append({"name":pp.name ,"p":round(required_energy + 0.05, 1)})  
#                 required_energy = 0
    
#     # if all power plants cannot provide the required power then generate a response that mentions that it is not possible to provide the demanded engery
#     if required_energy > 0:
#         response_error = "the load required cannot be provided by the powerplants"
#         return response_error
#     # at the end, all resting powerplants that are not used should be added in order to provide a response similar to the response required
#     return response_temp