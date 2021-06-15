#! /usr/bin/env python3

import sys

def		state():
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

		key_cc_list = list(capital_cities.keys())
		val_cc_list = list(capital_cities.values())

		key_states_list = list(states.keys())
		val_states_list = list(states.values())

		if sys.argv[1] in val_cc_list:
			pos_state_code = val_cc_list.index(sys.argv[1])
			state_code = key_cc_list[pos_state_code]
			pos_states = val_states_list.index(state_code)
			state = key_states_list[pos_states]
			print(state)
		else:
			print("Unknown capital city")

if __name__=='__main__':
	state()