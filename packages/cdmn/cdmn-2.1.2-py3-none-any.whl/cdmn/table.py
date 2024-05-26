"""
    Copyright 2020 Simon Vandevelde, Bram Aerts, Joost Vennekens
    This code is licensed under GNU GPLv3 license (see LICENSE) for more
    information.
    This file is part of the cDMN solver.
"""


import numpy as np
import re
from cdmn.idply import Parser
from cdmn.idpname import idp_name
from typing import List
from collections import OrderedDict
from copy import copy


def variname(string: str) -> str:
    """
    Function to return the variable of a header in the form of "Type called
    var"

    :arg string: the headerstring of which the variable name needs to be found.
    :returns str: the variable name.
    """
    return re.split(r'\s+[cC]alled\s+', string)[-1]


def typeiname(string: str) -> str:
    """
    Function to return the type of a header in the form of "Type called var"

    :arg string: the headerstring of which the variable name needs to be found.
    :returns str: the variable name.
    """
    return re.split(r'\s+[cC]alled\s+', string)[0]


def is_variable_introducing(string: str, variables: OrderedDict) -> bool:
    """
    Checks whether a column name is variable introducing.
    There's two types of variable introducing columns:
        1. Using "Type called T" syntax
        2. Just using "Type"

    :arg string: the headerstring of a column.
    :returns bool:
    """
    return (len(re.findall(r'\s+[cC]alled\s+', string)) != 0
            or string in variables)


def is_singular_value(string: str) -> bool:
    """
    Check whether a cell contains a singular value, such as "foo".
    Specifically look for signs that there might be multiple values, such as
    "-", ",", ...

    :arg string: the content of a cell in string form
    :returns bool:
    """
    return len(re.findall(r'[,−()\s-]', string)) == 0


class Table:
    """
    The table object represents decision and constraint tables.

    :attr name: str
    :attr hit_policy: str
    :attr inputs: List[np.array]
    :attr outputs: List[np.array]
    :attr rules: List[np.array]
    """
    def __init__(self, array: np.array, parser: Parser):
        """
        Initialises a table object for decision or constraint tables.
        Table interprets and splits up every table into inputs, outputs, rules,
        name and hit policy, after which it doesn't save the table array.

        :arg array: the np.array containing the table.
        :arg Parser: the parser
        :returns Table:
        """
        self.inputs: List[np.array] = []
        self.outputs: List[np.array] = []
        self.rules: List[np.array] = []
        self.name = self._read_name(array)
        self.hit_policy = self._read_hitpolicy(array)
        self.annotations_present: bool = False

        self._read_inputs(array)
        self._read_outputs(array)  # Also detects presence of annotations.
        self._read_rules(array)
        self.parser = parser

    def _read_name(self, array: np.array) -> str:
        """
        Method to read the name of a table, which is located in the top-left
        cell.

        :arg array: the np.array containing the table.
        :returns str: the name of the table.
        """
        return array[0, 0]

    def _read_hitpolicy(self, array: np.array) -> str:
        """
        Method to read the hit policy of a table, which is located at [1,0].

        :arg array: the np.array containing the table.
        :returns str: the hit policy of the table.
        """
        # Single cells containing value shouldn't be interpreted as tables.
        if len(array) == 1:
            return "None"  # None in string, because it's used in regex checks.
        return array[1, 0]

    def _read_inputs(self, array: np.array) -> None:
        """
        Method to read all the input columns of a table.
        A column is an input column if the first cell contains the table name.
        E.g. the columns under the merged cells representing the name.

        :arg array: the np.array containing the table.
        :returns None:
        """
        for x in range(1, array.shape[1]):
            if array[0, x] != self.name:
                return
            self.inputs.append(array[1, x])

    def _read_outputs(self, array: np.array) -> None:
        """
        Method to read all the output columns + check for annotations.
        A column is an output column if the first cell (right above it)
        doesn't contain the table name.
        E.g. all columns not under the merged cells representing the name.

        :arg array: the np.array containing the table.
        :returns None:
        """
        for x in range(1, array.shape[1]):
            if array[0, x] == self.name:
                continue
            if re.match(r'[Aa]nnotation', array[1, x]):
                self.annotations_present = True
                continue
            self.outputs.append(array[1, x])

    def _read_rules(self, array: np.array) -> None:
        """
        Method to read all the rules of a table.
        Each row of the table is a rule.

        :arg array: the np.array containing the table.
        :returns None:
        """
        # Single cells containing value shouldn't be interpreted as tables.
        if len(array) == 1:
            return
        for x in range(1, array.shape[0]):
            if array[x, 0] != self.hit_policy:
                break
        self.rules = array[x:, 1:]

    def _read_types(self, array: np.array, filter_args=None):
        """
        Method to interpret the headers in a table.
        Interprets "Foo called Bar", and returns Bar.

        :args array: the np.array containing the table.
        :returns str: the variablename.
        """
        odict = OrderedDict()
        # Interpret the headers in a table.
        for header in array:
            tvals = re.split(r'\s+[cC]alled\s+', header)
            try:
                t = self.parser.interpreter.glossary.find_type(tvals[0]
                                                               .strip())
            except StopIteration:
                if len(tvals) == 2:
                    raise ValueError(f'{tvals[0]} is not a type, but is used'
                                     f' with \"called\" keyword')
                else:
                    continue
            if filter_args is not None and not filter_args(tvals[-1]):
                continue
            if tvals[-1] in odict.keys() and odict[tvals[-1]] != t:
                raise ValueError(f'{tvals[0]} is defined multiple times with a'
                                 f' different type')
            else:
                odict[tvals[-1]] = t
        return odict

    def _create_quantors(self, variables: dict, repres=None) -> str:
        """
        Creates the quantors using a specific format.

        :arg variables: the variables that need to be quantified.
        :arg repres: a string containing a Pythonic string format.
        :returns str: quantorstr
        """
        repr = repres or '!{0}[{1}]: '
        return ''.join(
            repr.format(idp_name(var), idp_name(typ.to_theory()))
            for var, typ in variables.items())

    def _create_quantors_list(self,
                              array: np.array,
                              filter_args=None) -> List[str]:
        """
        Creates a list of all possible quantors for a row.

        :returns List[str]: a list containing all the quantors.
        """
        repres = '{0}{1}]'
        return [repres.format(var, typ.to_theory()) for var, typ in
                self._read_types(array, filter_args).items()]

    @property
    def fstring(self) -> str:
        """
        Method to decide the string format for a certain hit policy.

        :returns str: the format string.
        """
        if self.hit_policy == 'E*':
            return '\t{0}{1} => {2}{3}.\n'
        elif re.match('[UA]', self.hit_policy):
            return '\t\t{0}{2}{3} <- {1}.\n'
        return ""

    def variables_iq_oq(self, repres=None):
        """
        Method to generate the needed variables and quantifiers
        :returns variables, iquantors, oquantors: TODO
        """

        variables = self._read_types(self.inputs + self.outputs)
        ivariables = self._read_types(self.inputs)
        iquantors = self._create_quantors(ivariables, repres)
        oquantors = self._create_quantors(OrderedDict(
            [x for x in variables.items() if x not in ivariables.items()]),
            repres)
        return variables, iquantors, oquantors

    def _parse_row_over_colums(self,
                               row: list[str],  # TODO type hint
                               variables: OrderedDict,
                               simplified_variables: dict[str, str],
                               quantors: str,
                               parse_inputs: bool = True
                               ) -> tuple[list[str],
                                          dict[str, str],
                                          str]:
        """
        Parse a row for every input/output column of a table.
        This function also takes care of simplification in the context of
        quantifiers with singular values. E.g.,

        Monkey called m1 | food of m1
        -----------------------------
        Frank            | Berry

        does not need a quantifier -- instead, we can replace m1 by "Frank" in
        the rest of the formula and drop the quantifier.

        :arg row: list[str], the row of values
        :arg variables: OrderedDict, mapping variables on Types
        :arg simplified_variables: dict[str, str], mapping variable names on
            singular type values.
        :arg quantors: str representing the quantors
        :arg parse_inputs: bool. True to parse inputs, Fales to parse outputs.


        :returns (list[str], dict[str, str], str):
        """
        quantors = copy(quantors)  # orig iquantors are shared over rows.

        if parse_inputs:
            columns = self.inputs
            offset = 0
        else:
            columns = self.outputs
            offset = len(self.inputs)

        parse_out = []
        for i, col in enumerate(columns):
            # If a variable introducing column has a single value in the
            # input cell, remove the quantification and replace the
            # variable by the value in every formula.
            if (is_variable_introducing(col, variables)
               and is_singular_value(str(row[i+offset]))):
                var_name = variname(col)
                type_name = typeiname(col)
                simplified_variables[var_name] = str(row[i+offset])
                quantors = quantors.replace(f"!{var_name.replace(' ', '_')} in"
                                            f" {type_name.replace(' ', '_')}_t:",
                                            '')  # Also remove quant
                continue
            atom = self.parser.parse_val(variname(col),
                                         row[i+offset],
                                         variables,
                                         simplified_variables)
            if atom:
                atom = atom.replace("<=", "=<")  # "=<" is inverted in IDP
                parse_out.append(atom)

        return parse_out, simplified_variables, quantors

    def _export_definitions(self) -> str:
        """
        Method to export the table as definitions.
        When the hitpolicy is 'U', 'A' or 'F', we can translate the entire
        table into definitions in idp form.

        If the output is idpz3, then we add a constraint which says that any
        one of the outputs needs to be true. Otherwise, they don't show up as
        relevant.

        :returns str: the table as definitions.
        """
        quantor_repr = '!{0} in {1}: '

        # Set the headername in special brackets.
        string = f'\t[#{self.name}#]\n'
        # Iterate over every outputcolumn.
        for i, col in enumerate(self.outputs):
            if i > 0:
                # When creating a definition for the second, third, ... output,
                # we need to add the name again.
                string += f'\t[#{self.name}#]\n'
            string += '\t{\n'
            variables, orig_iquantors, oquantors = self.variables_iq_oq(
                                                   repres=quantor_repr)
            # Iterate over every row and interpret it for the specific
            # outputcolumn (and disregard the other outputcolumns).
            previous_conditions = []

            falsecount = 0
            for r, row in enumerate(self.rules):
                conditions = []
                simplified_variables = {}
                conditions, simplified_variables, iquantors = \
                    self._parse_row_over_colums(row, variables,
                                                simplified_variables,
                                                orig_iquantors,
                                                True)
                conditions = ' & '.join(conditions)
                conclusion = self.parser.parse_val(col,
                                                   row[i + len(self.inputs)],
                                                   variables,
                                                   simplified_variables)
                # A definition can't contain a not in the conclusion.
                # A negation of a predicate is implied by the other rules.
                if '~' in conclusion:
                    # If all the row are 'not', we need to specify that none of
                    # the predicates are true because there's no implicit
                    # rule which defines this.
                    if falsecount == len(self.rules) - 1:
                        conditions = "false"
                        conclusion = conclusion.replace("~", " ")
                        conclusion = conclusion[2:-1]  # Strip the brackets.
                    else:
                        falsecount = falsecount + 1
                        continue

                if not conclusion:
                    continue
                if not conditions:
                    conditions = 'true'

                # If an annotation is present, use it. Otherwise, set None.
                if self.annotations_present:
                    annotation = f'\t\t[{row[-1]}]\n'
                else:
                    annotation = ''

                if self.hit_policy != 'F' or not previous_conditions:
                    if conditions:
                        string += (f'{annotation}\t\t{iquantors}{oquantors}'
                                   f'{conclusion} <- {conditions}.\n')
                    else:
                        string += (f'{annotation}\t\t{iquantors}{oquantors}'
                                   f'{conclusion}.\n')
                else:
                    # For first hit, we always add a negation of the previous
                    # conditions.
                    if conditions:
                        string += (f'{annotation}\t\t{iquantors}{oquantors}'
                                   f'{conclusion} <- {oquantors}{conditions} &'
                                   f' ~(({")|(".join(previous_conditions)})).\n')
                    else:
                        string += (f'{annotation}\t\t{iquantors}{oquantors}'
                                   f'{conclusion} <- {oquantors}'
                                   f' ~(({")|(".join(previous_conditions)})).\n')

                previous_conditions.append(conditions)
            string += '\t}\n\n'
        return string

    def _export_implication(self) -> str:
        """
        Method to export the table as implications.
        When the hitpolicy is 'E*', we can translate the entire table into
        implications in idp form.

        :returns str:
        """
        # Format quantor representation
        quantor_repr = '!{0} in {1}: '

        # Set the headername in comments.
        string = f'\t//{self.name}\n'
        # Depending on the inputs and outputs, we need different input and
        # output quantors.
        variables, orig_iquantors, orig_oquantors = self.variables_iq_oq(repres=quantor_repr)

        # For each row, form the conditions and the conclusions.
        # When no conditions are present, the condition defaults to 'true'.
        for row in self.rules:
            conditions = []
            simplified_variables = {}
            conditions, simplified_variables, iquantors = \
                self._parse_row_over_colums(row, variables,
                                            simplified_variables,
                                            orig_iquantors,
                                            parse_inputs=True)
            conditions = ' & '.join(conditions)

            conclusions, _, oquantors = \
                self._parse_row_over_colums(row, variables,
                                            simplified_variables,
                                            orig_oquantors,
                                            parse_inputs=False)

            conclusions = ' & '.join(conclusions)
            if not conclusions:
                raise ValueError(f'This line has no conclusion: {row}')

            if self.annotations_present:
                annotation = f'[{row[-1]}]'
            else:
                annotation = f'[{self.name}]'

            if conditions:
                string += (f'\t{annotation}\n\t{iquantors}{conditions} => '
                           f'{oquantors}{conclusions}.\n\n')
            else:
                string += (f'\t{annotation}\n\t{iquantors}'
                           f'{oquantors}{conclusions}.\n\n')
        return string

    def _export_aggregate(self) -> str:
        """
        Method to export the table as aggregates.
        When the hitpolicy is 'C+/>/</#', we can translate the table into
        aggregates in idp form.

        An aggregate is of the form: "aggr{ variables : condition : weights}"
        or in the case of count:     "#{variables : condition}".

        :returns str:
        """
        # Format quantifier representations
        i_repr = '!{0} in {1}: '
        a_repr = '{0} in {1}, '

        # Conversion table from specific hitpolicy to aggregate.
        conversion = {
            'C+': 'sum',
            'C>': 'max',
            'C<': 'min',
            'C#': '#'
        }
        # Set the headername in comments.
        string = f'\t//{self.name}\n'

        for i, col in enumerate(self.outputs):

            try:
                args = [x for x in
                        self.parser.interpreter.interpret_value(col).args]
            except AttributeError:
                raise ValueError(f"Column in table {self.name} in"
                                 f" list of predicates."
                                 f" Maybe you forgot the merge all"
                                 f" the inputs?")
            additional_inputs = [x.pred.super_type.name
                                 for x in args if hasattr(x, 'pred')]

            # Create the iquantors, for instance `!type[Type]`, and the
            # aggregate quantors, for instance `c[Component]`.
            # The aggregate quantors may not contain already quantified
            # variables.
            # variables = self._read_types(self.inputs + additional_inputs)
            variables = self._read_types(self.inputs)
            ivariables = dict((idp_name(arg.value), arg.type) for arg in args)
            iquantors = self._create_quantors(ivariables, repres=i_repr)
            aquantors = self._create_quantors(OrderedDict(
                [x for x in variables.items() if x not in ivariables.items()]),
                repres=a_repr)
            # Remove the final ', '. Dirty hack. :-(
            aquantors = aquantors[:-2]

            # Create the assigned variable, for instance `Function(Type)`.
            assigned_variable = self.parser.interpreter.interpret_value(col)
            assigned_variable = '{}({})'.format(
                idp_name(assigned_variable.pred.name),
                ', '.join([idp_name(arg.value) for arg in
                           assigned_variable.args]))

            if list(self._read_types(self.outputs)):
                raise NotImplementedError('quantors in output columns'
                                          ' are not yet supported')

            # Create a formatstring "fstring", by setting the correct
            # aggregate.
            # Generates a string like "sum{{{{ ({2}) | {0}: {1} }}}}",
            # which is later
            # formatted.
            if self.hit_policy == 'C#':
                fstring = ('{0}{{{{ {{0}}: {{1}} & {{2}} }}}}'
                           .format(conversion[self.hit_policy]))
            else:
                fstring = ('{0}{{{{{{{{ ({{2}}) | {{0}}: {{1}}}}}}}}}}'
                           .format(conversion[self.hit_policy]))

            aggs = []
            # Every row now gets formatted according to the formatstring.
            for row in self.rules:

                # Iterate over each column of the row and interpret the values.
                # Cells which can't be parsed return None values, we need to
                # filter these.
                parsed_cells = [self.parser.parse_val(variname(col),
                                                      row[i],
                                                      variables) for
                                i, col in enumerate(self.inputs)]
                conditions = list(filter(lambda x: x, parsed_cells))
                extra_conditions = [f'{arg} = {idp_name(arg.value)}'
                                    for arg in args]

                # Add the conditions into one string, seperated by '&'.
                conditions = ' & '.join(conditions + extra_conditions)

                # If no conditions are specified, default to 'true'.
                if not conditions:
                    conditions = 'true'

                # Get the weights of the aggregate.
                weights = self.parser.parse_val('__PLACEHOLDER__',
                                                row[i + len(self.inputs)],
                                                variables)
                if not weights or not re.search(r'__PLACEHOLDER__\s*=',
                                                weights):
                    raise ValueError(
                        f'There is no valid value appointed to {col}\'s'
                        f' weights in the following rule: {row}.'
                        f' Maybe you forgot to merge the correct cells?')
                if self.hit_policy == 'C#':
                    try:
                        x = self.parser.interpreter.interpret_value(
                                row[i + len(self.inputs)], variables)
                        if x.value not in variables:
                            additional_agg_vars = self._create_quantors(
                                {idp_name(x.value): x.pred.super_type},
                                repres=a_repr)

                            # Remove ", " at the end.
                            additional_agg_vars = additional_agg_vars[:-2]
                        else:
                            additional_agg_vars = ""
                        if iquantors != "" and additional_agg_vars != "":
                            additional_agg_vars = ", " + additional_agg_vars

                        weights = re.sub('__PLACEHOLDER__', idp_name(x.value),
                                         weights)
                    except AttributeError:
                        additional_agg_vars = ''
                        weights = 'true'
                    except TypeError:
                        raise TypeError("Failed looking up {} at row {} of"
                                        " table '{}'"
                                        .format(row[i + len(self.inputs)],
                                                i + len(self.inputs),
                                                self.name))
                else:
                    weights = re.sub(r'__PLACEHOLDER__\s*=\s*', '',
                                     weights)
                    additional_agg_vars = ''

                aggs.append(fstring.format(aquantors + additional_agg_vars,
                                           conditions, weights))

            # The combine operator is used to combine different aggregates.
            # idpz3 has no support for ',', this is only temporary!
            combine_operator = '+'
            if self.hit_policy == 'C#':
                string += ('\t{}{}{} = {}({}).\n'
                           .format(iquantors,
                                   " " if iquantors else "",
                                   assigned_variable,
                                   '',
                                   combine_operator.join(aggs)))
            else:
                # Define the operator which surrounds the aggregates.
                math_operator = conversion[self.hit_policy] + '(' if False else ''
                string += ('\t{}{}{} = {}{}{}.\n'
                           .format(iquantors,
                                   assigned_variable,
                                   " " if iquantors else "",
                                   math_operator,
                                   combine_operator.join(aggs),
                                   ''))
        return string

    def _export_FO(self) -> str:
        """ Export table directly to FO(.). For expert users only.

        :returns str:
        """
        string = ''
        for row in self.rules:
            if self.annotations_present:
                annotation = f'[{row[-1]}]'
            else:
                annotation = f'[{self.name}]'
            string += f'\n\t{annotation}\n\t'
            string += row[0] if str(row[0]).endswith('.') else f'{row[0]}.'
        return string

    def export(self):
        """
        Export tries to find the hit policy for a table, and then returns the
        method needed to transfer the table to idp form.
        These hit policies are currently:

          * A, U, F           -> translate to definitions;
          * E*                -> translate to implications;
          * C+, C<, C>, C#    -> translate to aggregates;
          * FO                -> translate directly to FO.

        Every hit policy has its own method.

        :returns method: the output of export method for the table.
        """

        # List all possible hit policies.
        actions = {
            r'^[AUF]$': self._export_definitions,
            r'^E\*$': self._export_implication,
            r'^C[\<\>\#\+]$': self._export_aggregate,
            r'^FO$': self._export_FO
        }
        # Try, except is necessary to avoid StopIteration error.
        try:
            # Find hit policy.
            hp = next(map(lambda x: x.re.pattern,
                          filter(lambda x: x,
                                 (re.match(x, self.hit_policy)
                                     for x in actions))))
        except StopIteration:
            return None
        return actions[hp]

    def find_auxiliary(self) -> List[str]:
        """
        Every output in a C# table needs to use an auxiliary variable to work
        correctly.
        This method makes a list of those output variables, so that the
        auxiliary versions can be created.

        :returns List[str]:
        """
        if "C#" != self.hit_policy:
            return None

        aux_var = []
        for i, col in enumerate(self.outputs):
            assigned_variable = self.parser.interpreter.interpret_value(col)
            assigned_variable = f'{idp_name(assigned_variable.pred.name)}'
            assigned_variable = assigned_variable.replace('_', ' ')
            aux_var.append(assigned_variable)
        return aux_var
