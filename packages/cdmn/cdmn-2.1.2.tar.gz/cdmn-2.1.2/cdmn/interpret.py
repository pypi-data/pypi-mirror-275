"""
    Copyright 2020 Simon Vandevelde, Bram Aerts, Joost Vennekens
    This code is licensed under GNU GPLv3 license (see LICENSE) for more
    information.
    This file is part of the cDMN solver.
"""

import re
from Levenshtein import distance
from cdmn.glossary import Glossary, Predicate
from cdmn.idpname import idp_name
from typing import Dict


class VariableInterpreter:
    """
    TODO
    """
    def __init__(self, glossary: Glossary):
        """
        Initialises the VariableInterpreter.

        :arg glossary: a glossary object.
        :returns Object:
        """
        self.glossary = glossary

    def interpret_value(self,
                        value: str,
                        variables: Dict = {},
                        expected_type=None):
        """
        Method to interpret a value of a cDMN notation.
        Here be dragons.

        :arg value: string which needs to be interpreted.
        :arg variables: list containing the variables.
        :arg expected_type:
        :returns str: the interpretation of the notation.
        """
        # TODO: instead of string variables, make Variable class with existing
        # type to which can be referred.
        lu = self.glossary.lookup(str(value))
        interpretations = []

        # Length of lookup is zero if it is a variable, and not a relation or
        # function. Alternatively, we look if the value has already been
        # declared as a varibale before-hand.
        if len(lu) == 0 or value in variables:
            if str(value) == '__PLACEHOLDER__':
                pass
            elif not expected_type:
                expected_type = variables[str(value)]
            return Value(value, expected_type, variables)
        for l in lu:
            if (expected_type is not None and expected_type !=
                    l[0].is_function()):
                pass  # TODO: fix this!
            try:
                interpretations.append(
                        PredicateInterpretation(l[0], l[1], self, variables))
            except ValueError:
                continue

        if len(interpretations) == 0:
            raise ValueError(f'The value of "{value}" could not be'
                             f' interpreted.')
        if len(interpretations) == 1:
            return interpretations[0]
        if len(interpretations) > 1:
            # Find most likely interpretation by applying a heuristic to find
            # the "most likely". First, we prioritize nested symbols: for
            # instance in the Programmer example, `lead knows Java` should be
            # interpreted as `Employee knows Language`, and not as `lead`.
            # Practically, we find the highest arity omong the interpretations,
            # and throw out all those that have a lower arity.
            # Second, we sort on Levenshtein Distance.
            # This ensures that, for instance, "SummerTime" is interpreted as
            # such and not as "Summer".

            # Throw out all interpretations with a lower arity.
            max_arity = max([x.pred.arity for x in interpretations])
            interpretations = [x for x in interpretations if x.pred.arity ==
                               max_arity]
            # Sort on LDistance
            interpretations.sort(key=lambda interp: distance(value,
                                                             interp.value))
            print(f"Warning: Multiple possible interpretations for {value}."
                  f" Selecting the most likely interpretation:"
                  f" {interpretations[0].value}")
            return interpretations[0]


class Value:
    """
    An object to represent a value.
    """
    def __init__(self, value: str, valuetype, variables):
        """
        Initialised a Value object.

        :arg value: a string containing the value.
        :arg valuetype:
        :arg variables:
        :returns Object:
        """
        self.value = value
        self.type = valuetype
        self.check(variables)

    def check(self, variables):
        """
        TODO
        """
        if re.match('.* (and|of) .*', str(self.value)):
            raise ValueError(f'The compiler does not know how to interpret'
                             f' the following: "{self.value}".')
        return
        # TODO: reinclude below code.
        if self.value not in variables.keys() and \
                self.value not in self.type.possible_values:
            raise ValueError(f'WARNING: {self.value} occurs in a position'
                             f' of type {self.type.name}'
                             f' but does not appear in possible values')

    def __str__(self) -> str:
        """
        Magic method to format a variable interpretation to string.

        :returns str:
        """
        return f'{idp_name(self.value)}'


class PredicateInterpretation:
    """
    TODO
    """
    def __init__(self, pred: Predicate,
                 arguments,
                 inter: VariableInterpreter,
                 variables):
        """
        Initialises the PredicateInterpretation object.

        :arg pred: the predicate to interpret.
        :arg arguments:
        :arg inter: the variable interpreter.
        :arg variables:
        :returns Object:
        """
        self.pred = pred
        self.args = [inter.interpret_value(arg, variables=variables,
                                           expected_type=t) for arg, t in
                     zip(arguments, pred.args)]
        # if

    @property
    def type(self):
        """
        Method to get the type of the predicate.

        :returns Type: supertrype of the predicate.
        """
        return self.pred.super_type

    @property
    def value(self):
        """
        TODO
        """
        return self.pred.name

    def __str__(self):
        """
        Magic method to return this object in string form.
        """
        return '{}({})'.format(idp_name(self.pred.name),
                               ', '.join([arg.__str__() for arg in self.args]))
