import json
from pprint import pprint


def get_json_for_object(class_object):
	attr_keys = [attr for attr in dir(class_object) if not callable(getattr(class_object, attr)) and not attr.startswith("__")]
	attr_values = [getattr(class_object, attr) for attr in attr_keys]
	
	return_dict = {}
	for item in range(len(attr_values)):
		return_dict.update({attr_keys[item] : attr_values[item]})

	# object_json = json.dumps(return_dict)
	# pprint(return_dict)
	return return_dict