"""
    Copyright 2019 Simon Vandevelde, Bram Aerts, Joost Vennekens
    This code is licensed under GNU GPLv3 license (see LICENSE) for more
    information.
    This file is part of the cDMN solver.
"""
import re
from typing import Dict
from collections import defaultdict


def merge_definitions(idp: str) -> str:
    """
    In cDMN, it is possible to create different tables that each define
    the same concept.
    In cases where relations are defined, this can be problematic.
    E.g., in the `Vacation_Days_Advanced_old` example, we define the `Employee
    eligible for Rule` relation in 5 different tables, each for a different
    value of `Rule`.
    In IDP, a definition is expected to be complete: all possible values for
    the defined concept should be defined. All other values are implicitly
    impossible. Because the cDMN implementation creates 5 different
    definitions, each defining a different value, this results in an unsat in
    IDP.

    The solution to this problem is to merge all tables defining the same
    concept.
    """
    # Grab all rules and their annotations.
    rules = re.findall(r"(\t\t\[.*?\])?\n(.+?)(?=<-)(.+?)(?=\.\n)", idp)

    # Remove all rules.
    new_idp = re.sub(r"(\[.*?\])?\n(.+?)(?=<-)(.+?)(?=\.\n)", "", idp)

    defined_concepts: Dict[str, str] = {}
    defined_concepts = defaultdict(list)
    # Go over every rule and identify the defined variable.
    for annotation, head, body in rules:
        rule = annotation + '\n' + head + body + '.'
        defined_concept = head.split(":")[-1].split("(")[0].strip()
        defined_concepts[defined_concept].append(rule)

    # Grab the common definition annotations, try to find out what concept they
    # annotate. If multiple annotations exist for the same concept, we need to
    # merge them as well.
    definition_annotations = re.findall(r"\[\#(.*?)\#\]\n\t{(.*?)<-", idp,
                                        re.DOTALL)
    # def_annotations: Dict[str, str] = []
    def_annotations = defaultdict(list)
    for annotation, rule in definition_annotations:
        defined_concept = head.split('\t')[-1].split(":")[-1].split("(")[0].strip()
        def_annotations[defined_concept].append(annotation)

    # Remove all { .. }
    new_idp = re.sub(r"\t{[\t\n\.]*?}", "", new_idp)
    new_idp = re.sub(r"\t\[(.*?)\]\n\n", "", new_idp)
    for key, val in defined_concepts.items():
        new_idp += f"\t[{' OR '.join(def_annotations[key])}]\n"
        new_idp += "\t{\n"
        new_idp += ''.join(val)
        new_idp += "\n\t}\n"
    return new_idp
