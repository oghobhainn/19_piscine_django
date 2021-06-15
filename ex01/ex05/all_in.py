#! /usr/bin/env python3

import sys

def		capital_city(states, capital_cities, item):
	
	if item in states:
		city_code = states[item]
		return(capital_cities[city_code])
	else:
		return("")

def		state(states, capital_cities, item):

	key_cc_list = list(capital_cities.keys())
	val_cc_list = list(capital_cities.values())
	key_states_list = list(states.keys())
	val_states_list = list(states.values())
	if item in val_cc_list:
		pos_state_code = val_cc_list.index(item)
		state_code = key_cc_list[pos_state_code]
		pos_states = val_states_list.index(state_code)
		state = key_states_list[pos_states]
		return(state)
	else:
		return("")

def		all_in():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
		}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
		}
	
	if len(sys.argv) == 2:
		lst = sys.argv[1].split(',')
		lst = [i.strip() for i in lst if i.strip()]
		for item in lst:
			my_capital = capital_city(states, capital_cities, item.title())
			my_state = state(states, capital_cities, item.title())
			if my_capital == "" and my_state == "":
				print("{0} is neither a capital city nor a state".format(item))
			else:
				if my_capital == "": my_capital = item
				else: my_state = item
				print("{0} is the capital of {1}".format(my_capital.title(), my_state.title()))


if __name__=='__main__':
	all_in()