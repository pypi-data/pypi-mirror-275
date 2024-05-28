"""Module that provides utility functions"""

# Copyright © 2023-2024 Tiago Trotta

# This file is part of Python ReBase.

# Python ReBase is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Python ReBase is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Python ReBase.  If not, see <https://www.gnu.org/licenses/>

from typing import Callable

def is_valid_str(value) -> bool:
    """Checks wether a given string is valid"""

    return isinstance(value, str)

def is_valid_number(value) -> bool:
    """Checks wether a given number is valid"""

    return type(value) in (int, float)

def is_valid_id(value) -> bool:
    """Checks wether a given id is valid"""

    # pylint: disable=unidiomatic-typecheck
    return (is_valid_str(value) and value != '') or (type(value) == int and value > 0)

def is_valid_movement_field(field: str, value: any) -> bool:
    """Checks wether a given field-value pair is valid for a Movement object"""

    if field in ['id', '_id', 'sessionId', 'professionalId', 'patientId', 'appCode', 'app.code']:
        return is_valid_id(value)
    if field in ['label', 'description', 'device', 'insertionDate', 'updateDate']:
        return is_valid_str(value)
    if field in ['fps', 'duration', 'numberOfRegisters']:
        return is_valid_number(value)
    if field in ['articulations', 'registers']:
        return isinstance(value, list)
    return field in ['appData', 'app.data']

def is_valid_session_field(field: str, value: any) -> bool:
    """Checks wether a given field-value pair is valid for a Session object"""

    if field in ['id', '_id', 'professionalId', 'patientId', 'patient.id']:
        return is_valid_id(value)
    if field in ['title', 'description', 'insertionDate', 'updateDate', 'mainComplaint',
                 'historyOfCurrentDisease', 'historyOfPastDisease', 'diagnosis',
                 'relatedDiseases', 'medications', 'physicalEvaluation',
                 'medicalData.mainComplaint', 'medicalData.historyOfCurrentDisease',
                 'medicalData.historyOfPastDisease', 'medicalData.diagnosis',
                 'medicalData.relatedDiseases', 'medicalData.medications',
                 'medicalData.physicalEvaluation']:
        return is_valid_str(value)
    if field in ['patientSessionNumber', 'patientAge', 'patientHeight', 'patientWeight',
                 'numberOfMovements', 'patient.age', 'patient.height', 'patient.weight']:
        return is_valid_number(value)
    if field in ['movements', 'movementIds']:
        return isinstance(value, list)
    return False

def exclude_keys_from_dict(dictionary: dict, keys: list) -> None:
    """Excludes a given list of keys from a dictionary"""

    if keys is not None:
        for key in keys:
            if key in dictionary:
                del dictionary[key]

def validate_initialization_dict(validation_function: Callable[[str, any], bool],
                                 resource_name: str, field_rules: dict, dictionary: dict) -> None:
    """Validates a dictionary used to initialize a resource"""

    for key in dictionary.keys():
        if key not in field_rules:
            raise ValueError(f"Invalid attribute in {resource_name} object: '{key}'")

        if field_rules[key] is None:
            value = dictionary[key]
            if not validation_function(key, value):
                raise ValueError(f"Inappropriate value for attribute '{key}' in {resource_name} object: {type(value)} {value}")

        else:
            if not isinstance(dictionary[key], dict):
                raise ValueError(f"Inappropriate value for attribute '{key}' in {resource_name} object: {type(dictionary[key])} {dictionary[key]}")

            for sub_key in dictionary[key].keys():
                if sub_key not in field_rules[key]:
                    raise ValueError(f"Invalid attribute in {resource_name} object: '{key}.{sub_key}'")

                value = dictionary[key][sub_key]
                if not validation_function(f'{key}.{sub_key}', value):
                    raise ValueError(f"Inappropriate value for attribute '{key}.{sub_key}' in {resource_name} object: {type(value)} {value}")
