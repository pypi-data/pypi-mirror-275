#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf2344702

# Compiled with Coconut version 3.1.0-post_dev13

# Coconut Header: -------------------------------------------------------------

import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.0-post_dev13', '3', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == '__coconut__':  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

import urllib  #1 (line in Coconut source)
import csv  #2 (line in Coconut source)
from warnings import warn  #3 (line in Coconut source)
from collections import defaultdict  #4 (line in Coconut source)

import requests  #6 (line in Coconut source)
import pypokedex  #7 (line in Coconut source)
from bs4 import BeautifulSoup  #8 (line in Coconut source)
from tqdm import tqdm  #9 (line in Coconut source)
from clize import run  #10 (line in Coconut source)


get_entries = (_coconut_base_compose(requests.get, (_coconut.operator.attrgetter("text"), 0, False), (_coconut_complex_partial(BeautifulSoup, {1: "html.parser"}, 2, ()), 0, False), (_coconut.operator.attrgetter("body"), 0, False), (_coconut.operator.methodcaller("find_all", class_="pokedex_entry"), 0, False)))  #13 (line in Coconut source)


name_formatters = (ident, "{}-incarnate".format, "{}-single-strike".format, _coconut.operator.methodcaller("replace", "-f", "-female"), _coconut.operator.methodcaller("replace", "-m", "-male"), _coconut_base_compose(_coconut.operator.methodcaller("split", "-", 1), (_coconut.operator.itemgetter((0)), 0, False)))  #22 (line in Coconut source)

def get_mons(url):  #31 (line in Coconut source)
    for entry in tqdm(get_entries(url)):  #32 (line in Coconut source)
        name = ((((urllib.parse.unquote)((entry).get("data-name"))).replace(" ", "-")).lower())  #33 (line in Coconut source)
        for formatter in name_formatters:  #40 (line in Coconut source)
            formatted_name = formatter(name)  #41 (line in Coconut source)
            try:  #42 (line in Coconut source)
                yield pypokedex.get(name=formatted_name)  #43 (line in Coconut source)
            except pypokedex.exceptions.PyPokedexHTTPError:  #44 (line in Coconut source)
                pass  #45 (line in Coconut source)
            else:  #46 (line in Coconut source)
                break  #47 (line in Coconut source)
        else:  #48 (line in Coconut source)
            warn("failed to find pokemon {_coconut_format_0}".format(_coconut_format_0=(name)))  #49 (line in Coconut source)



class Nature(_coconut.collections.namedtuple("Nature", ('multiplier', 'identifier', 'min_ev', 'min_iv'))):  #52 (line in Coconut source)
    __slots__ = ()  #52 (line in Coconut source)
    _coconut_is_data = True  #52 (line in Coconut source)
    __match_args__ = ('multiplier', 'identifier', 'min_ev', 'min_iv')  #52 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #52 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #52 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #52 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #52 (line in Coconut source)
    def __eq__(self, other):  #52 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #52 (line in Coconut source)
    def __hash__(self):  #52 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #52 (line in Coconut source)
    def __new__(_coconut_cls, multiplier, identifier, min_ev=False, min_iv=False):  #52 (line in Coconut source)
        return _coconut.tuple.__new__(_coconut_cls, (multiplier, identifier, min_ev, min_iv))  #52 (line in Coconut source)
    _coconut_data_defaults = {2: __new__.__defaults__[0], 3: __new__.__defaults__[1]}  # type: ignore  #52 (line in Coconut source)
    @_coconut_tco  #52 (line in Coconut source)
    def apply(self, stat):  #52 (line in Coconut source)
        return _coconut_tail_call(int, stat * self.multiplier)  #53 (line in Coconut source)

    def __str__(self):  #54 (line in Coconut source)
        return self.identifier  #54 (line in Coconut source)

    @property  #55 (line in Coconut source)
    def ev(self):  #56 (line in Coconut source)
        return 0 if self.min_ev else 252  #56 (line in Coconut source)

    @property  #57 (line in Coconut source)
    def iv(self):  #58 (line in Coconut source)
        return 0 if self.min_iv else 31  #58 (line in Coconut source)


_coconut_call_set_names(Nature)  #60 (line in Coconut source)
Helpful = Nature(1.1, "+")  #60 (line in Coconut source)
Neutral = Nature(1, "=")  #61 (line in Coconut source)
Uninvested = Nature(1, "0", min_ev=True)  #62 (line in Coconut source)
Harmful = Nature(0.9, "-", min_ev=True, min_iv=True)  #63 (line in Coconut source)


class Stage(_coconut.collections.namedtuple("Stage", ('stat_stage', 'stat_modifier'))):  #66 (line in Coconut source)
    __slots__ = ()  #66 (line in Coconut source)
    _coconut_is_data = True  #66 (line in Coconut source)
    __match_args__ = ('stat_stage', 'stat_modifier')  #66 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #66 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #66 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #66 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #66 (line in Coconut source)
    def __eq__(self, other):  #66 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #66 (line in Coconut source)
    def __hash__(self):  #66 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #66 (line in Coconut source)
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #66 (line in Coconut source)
        _coconut_match_check_6 = False  #66 (line in Coconut source)
        _coconut_match_set_name_stat_modifier = _coconut_sentinel  #66 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #66 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #66 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #66 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "stat_stage" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat_modifier" in _coconut_match_kwargs)) <= 1):  #66 (line in Coconut source)
            _coconut_match_temp_10 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("stat_stage")  #66 (line in Coconut source)
            _coconut_match_temp_15 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat_modifier") if "stat_modifier" in _coconut_match_kwargs else _coconut_sentinel  #66 (line in Coconut source)
            _coconut_match_temp_11 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #66 (line in Coconut source)
            if _coconut_match_temp_15 is _coconut_sentinel:  #66 (line in Coconut source)
                _coconut_match_temp_15 = 1  #66 (line in Coconut source)
            _coconut_match_set_name_stat_modifier = _coconut_match_temp_15  #66 (line in Coconut source)
            if not _coconut_match_kwargs:  #66 (line in Coconut source)
                _coconut_match_check_6 = True  #66 (line in Coconut source)
        if _coconut_match_check_6:  #66 (line in Coconut source)
            _coconut_match_check_6 = False  #66 (line in Coconut source)
            if not _coconut_match_check_6:  #66 (line in Coconut source)
                _coconut_match_set_name_stat_stage = _coconut_sentinel  #66 (line in Coconut source)
                if (_coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, int)) and (_coconut.len(_coconut_match_temp_10) >= 1):  #66 (line in Coconut source)
                    _coconut_match_set_name_stat_stage = _coconut_match_temp_10[0]  #66 (line in Coconut source)
                    _coconut_match_temp_12 = _coconut.len(_coconut_match_temp_10) <= _coconut.max(1, _coconut.len(_coconut_match_temp_10.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {}) and _coconut_match_temp_10[i] == _coconut.getattr(_coconut_match_temp_10, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_10.__match_args__))) if _coconut.hasattr(_coconut_match_temp_10, "__match_args__") else _coconut.len(_coconut_match_temp_10) == 1  # type: ignore  #66 (line in Coconut source)
                    if _coconut_match_temp_12:  #66 (line in Coconut source)
                        _coconut_match_check_6 = True  #66 (line in Coconut source)
                if _coconut_match_check_6:  #66 (line in Coconut source)
                    if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #66 (line in Coconut source)
                        stat_stage = _coconut_match_set_name_stat_stage  #66 (line in Coconut source)

            if not _coconut_match_check_6:  #66 (line in Coconut source)
                if (not _coconut_match_temp_11) and (_coconut.isinstance(_coconut_match_temp_10, int)):  #66 (line in Coconut source)
                    _coconut_match_check_6 = True  #66 (line in Coconut source)
                if _coconut_match_check_6:  #66 (line in Coconut source)
                    _coconut_match_check_6 = False  #66 (line in Coconut source)
                    if not _coconut_match_check_6:  #66 (line in Coconut source)
                        _coconut_match_set_name_stat_stage = _coconut_sentinel  #66 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #66 (line in Coconut source)
                            _coconut_match_set_name_stat_stage = _coconut_match_temp_10  #66 (line in Coconut source)
                            _coconut_match_check_6 = True  #66 (line in Coconut source)
                        if _coconut_match_check_6:  #66 (line in Coconut source)
                            if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #66 (line in Coconut source)
                                stat_stage = _coconut_match_set_name_stat_stage  #66 (line in Coconut source)

                    if not _coconut_match_check_6:  #66 (line in Coconut source)
                        _coconut_match_set_name_stat_stage = _coconut_sentinel  #66 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_10) in _coconut_self_match_types:  #66 (line in Coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #66 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #66 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #66 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #66 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #66 (line in Coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_temp_10, _coconut_match_temp_13[0], _coconut_sentinel)  #66 (line in Coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #66 (line in Coconut source)
                                _coconut_match_set_name_stat_stage = _coconut_match_temp_14  #66 (line in Coconut source)
                                _coconut_match_check_6 = True  #66 (line in Coconut source)
                        if _coconut_match_check_6:  #66 (line in Coconut source)
                            if _coconut_match_set_name_stat_stage is not _coconut_sentinel:  #66 (line in Coconut source)
                                stat_stage = _coconut_match_set_name_stat_stage  #66 (line in Coconut source)




        if _coconut_match_check_6:  #66 (line in Coconut source)
            if _coconut_match_set_name_stat_modifier is not _coconut_sentinel:  #66 (line in Coconut source)
                stat_modifier = _coconut_match_set_name_stat_modifier  #66 (line in Coconut source)

        if not _coconut_match_check_6:  #66 (line in Coconut source)
            raise _coconut_FunctionMatchError('data Stage(int(stat_stage), stat_modifier=1):', _coconut_match_args)  #66 (line in Coconut source)

        return _coconut.tuple.__new__(_coconut_cls, (stat_stage, stat_modifier))  #66 (line in Coconut source)
    @_coconut_tco  #66 (line in Coconut source)
    @_coconut_mark_as_match  #66 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #66 (line in Coconut source)
        _coconut_match_check_0 = False  #66 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #66 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #66 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #66 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #66 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #66 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #66 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #66 (line in Coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #66 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_0  #66 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_1  #66 (line in Coconut source)
            if not _coconut_match_kwargs:  #66 (line in Coconut source)
                _coconut_match_check_0 = True  #66 (line in Coconut source)
        if _coconut_match_check_0:  #66 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #66 (line in Coconut source)
                self = _coconut_match_set_name_self  #66 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #66 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #66 (line in Coconut source)
        if _coconut_match_check_0 and not (self.stat_modifier != 1):  #66 (line in Coconut source)
            _coconut_match_check_0 = False  #66 (line in Coconut source)
        if not _coconut_match_check_0:  #66 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def apply(self, stat if self.stat_modifier != 1) =', _coconut_match_args)  #66 (line in Coconut source)

        return _coconut_tail_call((int), self._replace(stat_modifier=1).apply(stat) * self.stat_modifier)  #68 (line in Coconut source)

    try:  #69 (line in Coconut source)
        _coconut_addpattern_0 = _coconut_addpattern(apply)  # type: ignore  #69 (line in Coconut source)
    except _coconut.NameError:  #69 (line in Coconut source)
        _coconut.warnings.warn("Deprecated use of 'addpattern def apply' with no pre-existing 'apply' function (use 'match def apply' for the first definition or switch to 'case def' syntax)", _coconut_CoconutWarning)  #69 (line in Coconut source)
        _coconut_addpattern_0 = lambda f: f  #69 (line in Coconut source)
    @_coconut_addpattern_0  #69 (line in Coconut source)
    @_coconut_mark_as_match  #69 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #69 (line in Coconut source)
        _coconut_match_check_1 = False  #69 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #69 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #69 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #69 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #69 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #69 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #69 (line in Coconut source)
            _coconut_match_temp_2 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #69 (line in Coconut source)
            _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #69 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_2  #69 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_3  #69 (line in Coconut source)
            if not _coconut_match_kwargs:  #69 (line in Coconut source)
                _coconut_match_check_1 = True  #69 (line in Coconut source)
        if _coconut_match_check_1:  #69 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #69 (line in Coconut source)
                self = _coconut_match_set_name_self  #69 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #69 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #69 (line in Coconut source)
        if _coconut_match_check_1 and not (self.stat_stage > 0):  #69 (line in Coconut source)
            _coconut_match_check_1 = False  #69 (line in Coconut source)
        if not _coconut_match_check_1:  #69 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage > 0) =', _coconut_match_args)  #69 (line in Coconut source)

        return stat * (2 + self.stat_stage) // 2  #70 (line in Coconut source)

    try:  #71 (line in Coconut source)
        _coconut_addpattern_1 = _coconut_addpattern(apply)  # type: ignore  #71 (line in Coconut source)
    except _coconut.NameError:  #71 (line in Coconut source)
        _coconut.warnings.warn("Deprecated use of 'addpattern def apply' with no pre-existing 'apply' function (use 'match def apply' for the first definition or switch to 'case def' syntax)", _coconut_CoconutWarning)  #71 (line in Coconut source)
        _coconut_addpattern_1 = lambda f: f  #71 (line in Coconut source)
    @_coconut_addpattern_1  #71 (line in Coconut source)
    @_coconut_mark_as_match  #71 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #71 (line in Coconut source)
        _coconut_match_check_2 = False  #71 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #71 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #71 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #71 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #71 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #71 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #71 (line in Coconut source)
            _coconut_match_temp_4 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #71 (line in Coconut source)
            _coconut_match_temp_5 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #71 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_4  #71 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_5  #71 (line in Coconut source)
            if not _coconut_match_kwargs:  #71 (line in Coconut source)
                _coconut_match_check_2 = True  #71 (line in Coconut source)
        if _coconut_match_check_2:  #71 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #71 (line in Coconut source)
                self = _coconut_match_set_name_self  #71 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #71 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #71 (line in Coconut source)
        if _coconut_match_check_2 and not (self.stat_stage < 0):  #71 (line in Coconut source)
            _coconut_match_check_2 = False  #71 (line in Coconut source)
        if not _coconut_match_check_2:  #71 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage < 0) =', _coconut_match_args)  #71 (line in Coconut source)

        return stat * 2 // (2 - self.stat_stage)  #72 (line in Coconut source)

    try:  #73 (line in Coconut source)
        _coconut_addpattern_2 = _coconut_addpattern(apply)  # type: ignore  #73 (line in Coconut source)
    except _coconut.NameError:  #73 (line in Coconut source)
        _coconut.warnings.warn("Deprecated use of 'addpattern def apply' with no pre-existing 'apply' function (use 'match def apply' for the first definition or switch to 'case def' syntax)", _coconut_CoconutWarning)  #73 (line in Coconut source)
        _coconut_addpattern_2 = lambda f: f  #73 (line in Coconut source)
    @_coconut_addpattern_2  #73 (line in Coconut source)
    @_coconut_mark_as_match  #73 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #73 (line in Coconut source)
        _coconut_match_check_3 = False  #73 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #73 (line in Coconut source)
        _coconut_match_set_name_stat = _coconut_sentinel  #73 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #73 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #73 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #73 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "stat" in _coconut_match_kwargs)) == 1):  #73 (line in Coconut source)
            _coconut_match_temp_6 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #73 (line in Coconut source)
            _coconut_match_temp_7 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("stat")  #73 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_6  #73 (line in Coconut source)
            _coconut_match_set_name_stat = _coconut_match_temp_7  #73 (line in Coconut source)
            if not _coconut_match_kwargs:  #73 (line in Coconut source)
                _coconut_match_check_3 = True  #73 (line in Coconut source)
        if _coconut_match_check_3:  #73 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #73 (line in Coconut source)
                self = _coconut_match_set_name_self  #73 (line in Coconut source)
            if _coconut_match_set_name_stat is not _coconut_sentinel:  #73 (line in Coconut source)
                stat = _coconut_match_set_name_stat  #73 (line in Coconut source)
        if _coconut_match_check_3 and not (self.stat_stage == 0):  #73 (line in Coconut source)
            _coconut_match_check_3 = False  #73 (line in Coconut source)
        if not _coconut_match_check_3:  #73 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def apply(self, stat if self.stat_stage == 0) = stat', _coconut_match_args)  #73 (line in Coconut source)

        return stat  #73 (line in Coconut source)


    def __str__(self):  #75 (line in Coconut source)
        return "{_coconut_format_0:+}".format(_coconut_format_0=(self.stat_stage)) + (" x{_coconut_format_0}".format(_coconut_format_0=(self.stat_modifier)) if self.stat_modifier != 1 else "")  #76 (line in Coconut source)


    @_coconut_mark_as_match  #78 (line in Coconut source)
    def modifier_str(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #78 (line in Coconut source)
        _coconut_match_check_4 = False  #78 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #78 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #78 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #78 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #78 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1):  #78 (line in Coconut source)
            _coconut_match_temp_8 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #78 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_8  #78 (line in Coconut source)
            if not _coconut_match_kwargs:  #78 (line in Coconut source)
                _coconut_match_check_4 = True  #78 (line in Coconut source)
        if _coconut_match_check_4:  #78 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #78 (line in Coconut source)
                self = _coconut_match_set_name_self  #78 (line in Coconut source)
        if _coconut_match_check_4 and not (self.stat_stage == 0):  #78 (line in Coconut source)
            _coconut_match_check_4 = False  #78 (line in Coconut source)
        if not _coconut_match_check_4:  #78 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def modifier_str(self if self.stat_stage == 0) = ""', _coconut_match_args)  #78 (line in Coconut source)

        return ""  #78 (line in Coconut source)

    try:  #79 (line in Coconut source)
        _coconut_addpattern_3 = _coconut_addpattern(modifier_str)  # type: ignore  #79 (line in Coconut source)
    except _coconut.NameError:  #79 (line in Coconut source)
        _coconut.warnings.warn("Deprecated use of 'addpattern def modifier_str' with no pre-existing 'modifier_str' function (use 'match def modifier_str' for the first definition or switch to 'case def' syntax)", _coconut_CoconutWarning)  #79 (line in Coconut source)
        _coconut_addpattern_3 = lambda f: f  #79 (line in Coconut source)
    @_coconut_addpattern_3  #79 (line in Coconut source)
    @_coconut_mark_as_match  #79 (line in Coconut source)
    def modifier_str(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #79 (line in Coconut source)
        _coconut_match_check_5 = False  #79 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #79 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #79 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #79 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #79 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1):  #79 (line in Coconut source)
            _coconut_match_temp_9 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #79 (line in Coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_9  #79 (line in Coconut source)
            if not _coconut_match_kwargs:  #79 (line in Coconut source)
                _coconut_match_check_5 = True  #79 (line in Coconut source)
        if _coconut_match_check_5:  #79 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #79 (line in Coconut source)
                self = _coconut_match_set_name_self  #79 (line in Coconut source)
        if not _coconut_match_check_5:  #79 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def modifier_str(self) = str(self) + " "', _coconut_match_args)  #79 (line in Coconut source)

        return str(self) + " "  #79 (line in Coconut source)



_coconut_call_set_names(Stage)  #82 (line in Coconut source)
@_coconut_tco  #82 (line in Coconut source)
def calc_stat(base, stage, nature, level,):  #82 (line in Coconut source)
    return _coconut_tail_call((stage.apply), (nature.apply)(((2 * base) + nature.iv + nature.ev // 4) * level // 100 + 5))  #82 (line in Coconut source)



class PokemonSpeed(_coconut.collections.namedtuple("PokemonSpeed", ('name', 'base_speed', 'speed_stage', 'speed_nature', 'level'))):  #94 (line in Coconut source)
    __slots__ = ()  #94 (line in Coconut source)
    _coconut_is_data = True  #94 (line in Coconut source)
    __match_args__ = ('name', 'base_speed', 'speed_stage', 'speed_nature', 'level')  #94 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #94 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #94 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #94 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #94 (line in Coconut source)
    def __eq__(self, other):  #94 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #94 (line in Coconut source)
    def __hash__(self):  #94 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #94 (line in Coconut source)
    def __new__(_coconut_cls, _coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #94 (line in Coconut source)
        _coconut_match_check_7 = False  #94 (line in Coconut source)
        _coconut_match_set_name_speed_stage = _coconut_sentinel  #94 (line in Coconut source)
        _coconut_match_set_name_speed_nature = _coconut_sentinel  #94 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #94 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #94 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #94 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 5) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "name" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "base_speed" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "speed_stage" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "speed_nature" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 4, "level" in _coconut_match_kwargs)) == 1):  #94 (line in Coconut source)
            _coconut_match_temp_16 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("name")  #94 (line in Coconut source)
            _coconut_match_temp_21 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("base_speed")  #94 (line in Coconut source)
            _coconut_match_temp_26 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("speed_stage")  #94 (line in Coconut source)
            _coconut_match_temp_27 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("speed_nature")  #94 (line in Coconut source)
            _coconut_match_temp_28 = _coconut_match_args[4] if _coconut.len(_coconut_match_args) > 4 else _coconut_match_kwargs.pop("level")  #94 (line in Coconut source)
            if ((isinstance)(_coconut_match_temp_26, Stage)) and ((isinstance)(_coconut_match_temp_27, Nature)):  #94 (line in Coconut source)
                _coconut_match_temp_17 = _coconut.getattr(str, "_coconut_is_data", False) or _coconut.isinstance(str, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in str)  # type: ignore  #94 (line in Coconut source)
                _coconut_match_temp_22 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #94 (line in Coconut source)
                _coconut_match_set_name_speed_stage = _coconut_match_temp_26  #94 (line in Coconut source)
                _coconut_match_set_name_speed_nature = _coconut_match_temp_27  #94 (line in Coconut source)
                _coconut_match_temp_29 = _coconut.getattr(int, "_coconut_is_data", False) or _coconut.isinstance(int, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in int)  # type: ignore  #94 (line in Coconut source)
                if not _coconut_match_kwargs:  #94 (line in Coconut source)
                    _coconut_match_check_7 = True  #94 (line in Coconut source)
        if _coconut_match_check_7:  #94 (line in Coconut source)
            _coconut_match_check_7 = False  #94 (line in Coconut source)
            if not _coconut_match_check_7:  #94 (line in Coconut source)
                _coconut_match_set_name_name = _coconut_sentinel  #94 (line in Coconut source)
                if (_coconut_match_temp_17) and (_coconut.isinstance(_coconut_match_temp_16, str)) and (_coconut.len(_coconut_match_temp_16) >= 1):  #94 (line in Coconut source)
                    _coconut_match_set_name_name = _coconut_match_temp_16[0]  #94 (line in Coconut source)
                    _coconut_match_temp_18 = _coconut.len(_coconut_match_temp_16) <= _coconut.max(1, _coconut.len(_coconut_match_temp_16.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_16, "_coconut_data_defaults", {}) and _coconut_match_temp_16[i] == _coconut.getattr(_coconut_match_temp_16, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_16.__match_args__))) if _coconut.hasattr(_coconut_match_temp_16, "__match_args__") else _coconut.len(_coconut_match_temp_16) == 1  # type: ignore  #94 (line in Coconut source)
                    if _coconut_match_temp_18:  #94 (line in Coconut source)
                        _coconut_match_check_7 = True  #94 (line in Coconut source)
                if _coconut_match_check_7:  #94 (line in Coconut source)
                    if _coconut_match_set_name_name is not _coconut_sentinel:  #94 (line in Coconut source)
                        name = _coconut_match_set_name_name  #94 (line in Coconut source)

            if not _coconut_match_check_7:  #94 (line in Coconut source)
                if (not _coconut_match_temp_17) and (_coconut.isinstance(_coconut_match_temp_16, str)):  #94 (line in Coconut source)
                    _coconut_match_check_7 = True  #94 (line in Coconut source)
                if _coconut_match_check_7:  #94 (line in Coconut source)
                    _coconut_match_check_7 = False  #94 (line in Coconut source)
                    if not _coconut_match_check_7:  #94 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_sentinel  #94 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_16) in _coconut_self_match_types:  #94 (line in Coconut source)
                            _coconut_match_set_name_name = _coconut_match_temp_16  #94 (line in Coconut source)
                            _coconut_match_check_7 = True  #94 (line in Coconut source)
                        if _coconut_match_check_7:  #94 (line in Coconut source)
                            if _coconut_match_set_name_name is not _coconut_sentinel:  #94 (line in Coconut source)
                                name = _coconut_match_set_name_name  #94 (line in Coconut source)

                    if not _coconut_match_check_7:  #94 (line in Coconut source)
                        _coconut_match_set_name_name = _coconut_sentinel  #94 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_16) in _coconut_self_match_types:  #94 (line in Coconut source)
                            _coconut_match_temp_19 = _coconut.getattr(str, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #94 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_19, _coconut.tuple):  #94 (line in Coconut source)
                                raise _coconut.TypeError("str.__match_args__ must be a tuple")  #94 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_19) < 1:  #94 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'str' only supports %s)" % (_coconut.len(_coconut_match_temp_19),))  #94 (line in Coconut source)
                            _coconut_match_temp_20 = _coconut.getattr(_coconut_match_temp_16, _coconut_match_temp_19[0], _coconut_sentinel)  #94 (line in Coconut source)
                            if _coconut_match_temp_20 is not _coconut_sentinel:  #94 (line in Coconut source)
                                _coconut_match_set_name_name = _coconut_match_temp_20  #94 (line in Coconut source)
                                _coconut_match_check_7 = True  #94 (line in Coconut source)
                        if _coconut_match_check_7:  #94 (line in Coconut source)
                            if _coconut_match_set_name_name is not _coconut_sentinel:  #94 (line in Coconut source)
                                name = _coconut_match_set_name_name  #94 (line in Coconut source)




        if _coconut_match_check_7:  #94 (line in Coconut source)
            _coconut_match_check_7 = False  #94 (line in Coconut source)
            if not _coconut_match_check_7:  #94 (line in Coconut source)
                _coconut_match_set_name_base_speed = _coconut_sentinel  #94 (line in Coconut source)
                if (_coconut_match_temp_22) and (_coconut.isinstance(_coconut_match_temp_21, int)) and (_coconut.len(_coconut_match_temp_21) >= 1):  #94 (line in Coconut source)
                    _coconut_match_set_name_base_speed = _coconut_match_temp_21[0]  #94 (line in Coconut source)
                    _coconut_match_temp_23 = _coconut.len(_coconut_match_temp_21) <= _coconut.max(1, _coconut.len(_coconut_match_temp_21.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_21, "_coconut_data_defaults", {}) and _coconut_match_temp_21[i] == _coconut.getattr(_coconut_match_temp_21, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_21.__match_args__))) if _coconut.hasattr(_coconut_match_temp_21, "__match_args__") else _coconut.len(_coconut_match_temp_21) == 1  # type: ignore  #94 (line in Coconut source)
                    if _coconut_match_temp_23:  #94 (line in Coconut source)
                        _coconut_match_check_7 = True  #94 (line in Coconut source)
                if _coconut_match_check_7:  #94 (line in Coconut source)
                    if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #94 (line in Coconut source)
                        base_speed = _coconut_match_set_name_base_speed  #94 (line in Coconut source)

            if not _coconut_match_check_7:  #94 (line in Coconut source)
                if (not _coconut_match_temp_22) and (_coconut.isinstance(_coconut_match_temp_21, int)):  #94 (line in Coconut source)
                    _coconut_match_check_7 = True  #94 (line in Coconut source)
                if _coconut_match_check_7:  #94 (line in Coconut source)
                    _coconut_match_check_7 = False  #94 (line in Coconut source)
                    if not _coconut_match_check_7:  #94 (line in Coconut source)
                        _coconut_match_set_name_base_speed = _coconut_sentinel  #94 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_21) in _coconut_self_match_types:  #94 (line in Coconut source)
                            _coconut_match_set_name_base_speed = _coconut_match_temp_21  #94 (line in Coconut source)
                            _coconut_match_check_7 = True  #94 (line in Coconut source)
                        if _coconut_match_check_7:  #94 (line in Coconut source)
                            if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #94 (line in Coconut source)
                                base_speed = _coconut_match_set_name_base_speed  #94 (line in Coconut source)

                    if not _coconut_match_check_7:  #94 (line in Coconut source)
                        _coconut_match_set_name_base_speed = _coconut_sentinel  #94 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_21) in _coconut_self_match_types:  #94 (line in Coconut source)
                            _coconut_match_temp_24 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #94 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_24, _coconut.tuple):  #94 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #94 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_24) < 1:  #94 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_24),))  #94 (line in Coconut source)
                            _coconut_match_temp_25 = _coconut.getattr(_coconut_match_temp_21, _coconut_match_temp_24[0], _coconut_sentinel)  #94 (line in Coconut source)
                            if _coconut_match_temp_25 is not _coconut_sentinel:  #94 (line in Coconut source)
                                _coconut_match_set_name_base_speed = _coconut_match_temp_25  #94 (line in Coconut source)
                                _coconut_match_check_7 = True  #94 (line in Coconut source)
                        if _coconut_match_check_7:  #94 (line in Coconut source)
                            if _coconut_match_set_name_base_speed is not _coconut_sentinel:  #94 (line in Coconut source)
                                base_speed = _coconut_match_set_name_base_speed  #94 (line in Coconut source)




        if _coconut_match_check_7:  #94 (line in Coconut source)
            _coconut_match_check_7 = False  #94 (line in Coconut source)
            if not _coconut_match_check_7:  #94 (line in Coconut source)
                _coconut_match_set_name_level = _coconut_sentinel  #94 (line in Coconut source)
                if (_coconut_match_temp_29) and (_coconut.isinstance(_coconut_match_temp_28, int)) and (_coconut.len(_coconut_match_temp_28) >= 1):  #94 (line in Coconut source)
                    _coconut_match_set_name_level = _coconut_match_temp_28[0]  #94 (line in Coconut source)
                    _coconut_match_temp_30 = _coconut.len(_coconut_match_temp_28) <= _coconut.max(1, _coconut.len(_coconut_match_temp_28.__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_temp_28, "_coconut_data_defaults", {}) and _coconut_match_temp_28[i] == _coconut.getattr(_coconut_match_temp_28, "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_temp_28.__match_args__))) if _coconut.hasattr(_coconut_match_temp_28, "__match_args__") else _coconut.len(_coconut_match_temp_28) == 1  # type: ignore  #94 (line in Coconut source)
                    if _coconut_match_temp_30:  #94 (line in Coconut source)
                        _coconut_match_check_7 = True  #94 (line in Coconut source)
                if _coconut_match_check_7:  #94 (line in Coconut source)
                    if _coconut_match_set_name_level is not _coconut_sentinel:  #94 (line in Coconut source)
                        level = _coconut_match_set_name_level  #94 (line in Coconut source)

            if not _coconut_match_check_7:  #94 (line in Coconut source)
                if (not _coconut_match_temp_29) and (_coconut.isinstance(_coconut_match_temp_28, int)):  #94 (line in Coconut source)
                    _coconut_match_check_7 = True  #94 (line in Coconut source)
                if _coconut_match_check_7:  #94 (line in Coconut source)
                    _coconut_match_check_7 = False  #94 (line in Coconut source)
                    if not _coconut_match_check_7:  #94 (line in Coconut source)
                        _coconut_match_set_name_level = _coconut_sentinel  #94 (line in Coconut source)
                        if _coconut.type(_coconut_match_temp_28) in _coconut_self_match_types:  #94 (line in Coconut source)
                            _coconut_match_set_name_level = _coconut_match_temp_28  #94 (line in Coconut source)
                            _coconut_match_check_7 = True  #94 (line in Coconut source)
                        if _coconut_match_check_7:  #94 (line in Coconut source)
                            if _coconut_match_set_name_level is not _coconut_sentinel:  #94 (line in Coconut source)
                                level = _coconut_match_set_name_level  #94 (line in Coconut source)

                    if not _coconut_match_check_7:  #94 (line in Coconut source)
                        _coconut_match_set_name_level = _coconut_sentinel  #94 (line in Coconut source)
                        if not _coconut.type(_coconut_match_temp_28) in _coconut_self_match_types:  #94 (line in Coconut source)
                            _coconut_match_temp_31 = _coconut.getattr(int, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #94 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_31, _coconut.tuple):  #94 (line in Coconut source)
                                raise _coconut.TypeError("int.__match_args__ must be a tuple")  #94 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_31) < 1:  #94 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'int' only supports %s)" % (_coconut.len(_coconut_match_temp_31),))  #94 (line in Coconut source)
                            _coconut_match_temp_32 = _coconut.getattr(_coconut_match_temp_28, _coconut_match_temp_31[0], _coconut_sentinel)  #94 (line in Coconut source)
                            if _coconut_match_temp_32 is not _coconut_sentinel:  #94 (line in Coconut source)
                                _coconut_match_set_name_level = _coconut_match_temp_32  #94 (line in Coconut source)
                                _coconut_match_check_7 = True  #94 (line in Coconut source)
                        if _coconut_match_check_7:  #94 (line in Coconut source)
                            if _coconut_match_set_name_level is not _coconut_sentinel:  #94 (line in Coconut source)
                                level = _coconut_match_set_name_level  #94 (line in Coconut source)




        if _coconut_match_check_7:  #94 (line in Coconut source)
            if _coconut_match_set_name_speed_stage is not _coconut_sentinel:  #94 (line in Coconut source)
                speed_stage = _coconut_match_set_name_speed_stage  #94 (line in Coconut source)
            if _coconut_match_set_name_speed_nature is not _coconut_sentinel:  #94 (line in Coconut source)
                speed_nature = _coconut_match_set_name_speed_nature  #94 (line in Coconut source)

        if not _coconut_match_check_7:  #94 (line in Coconut source)
            raise _coconut_FunctionMatchError('data PokemonSpeed(', _coconut_match_args)  #94 (line in Coconut source)

        return _coconut.tuple.__new__(_coconut_cls, (name, base_speed, speed_stage, speed_nature, level))  #94 (line in Coconut source)
    def __str__(self):  #94 (line in Coconut source)
        return self.speed_stage.modifier_str() + self.name + str(self.speed_nature)  #101 (line in Coconut source)

    @property  #102 (line in Coconut source)
    @_coconut_tco  #103 (line in Coconut source)
    def stat(self):  #103 (line in Coconut source)
        return _coconut_tail_call(calc_stat, self.base_speed, self.speed_stage, self.speed_nature, self.level)  #103 (line in Coconut source)


_coconut_call_set_names(PokemonSpeed)  #105 (line in Coconut source)
def get_all_speeds(url, level, stages, natures):  #105 (line in Coconut source)
    for mon, stage, nature in cartesian_product(get_mons(url), stages, natures):  #106 (line in Coconut source)
        yield PokemonSpeed(mon.name, mon.base_stats.speed, stage, nature, level)  #111 (line in Coconut source)



important_stages = _coconut.dict((("outspeed", (Stage(-1), Stage(0), Stage(-1, stat_modifier=2), Stage(+1), Stage(+2), Stage(+1, stat_modifier=2))), ("underspeed", (Stage(-1), Stage(0), Stage(+1), Stage(+2)))))  #114 (line in Coconut source)

important_natures = _coconut.dict((("outspeed", (Helpful, Neutral)), ("underspeed", (Helpful, Neutral, Uninvested, Harmful))))  #133 (line in Coconut source)

max_speed = 1000  #146 (line in Coconut source)

def get_benchmarks(url, level, underspeed=False):  #148 (line in Coconut source)
    natures = important_natures["underspeed" if underspeed else "outspeed"]  #149 (line in Coconut source)
    stages = important_stages["underspeed" if underspeed else "outspeed"]  #150 (line in Coconut source)
    speeds = set(get_all_speeds(url, level, stages, natures))  #151 (line in Coconut source)

    benchmarks = defaultdict(_coconut_partial(defaultdict, list))  # type: dict[int, dict[Stage, list[PokemonSpeed]]]  #153 (line in Coconut source)
    if "__annotations__" not in _coconut.locals():  #153 (line in Coconut source)
        __annotations__ = {}  # type: ignore  #153 (line in Coconut source)
    __annotations__["benchmarks"] = dict[int, dict[Stage, list[PokemonSpeed]]]  #153 (line in Coconut source)
    for stage in stages:  #154 (line in Coconut source)
        base_speed = max_speed if underspeed else 1  #155 (line in Coconut source)
        unused_speeds = speeds.copy()  #156 (line in Coconut source)
        while unused_speeds:  #157 (line in Coconut source)
            check_speed = (stage.apply)(base_speed)  #158 (line in Coconut source)
            for pokemon_speed in tuple(unused_speeds):  #159 (line in Coconut source)
                if (((_coconut.operator.lt) if underspeed else (_coconut.operator.gt)))(check_speed, pokemon_speed.stat):  #160 (line in Coconut source)
                    benchmarks[base_speed][stage].append(pokemon_speed)  #161 (line in Coconut source)
                    unused_speeds.remove(pokemon_speed)  #162 (line in Coconut source)
            base_speed += -1 if underspeed else 1  #163 (line in Coconut source)
    return benchmarks  #164 (line in Coconut source)



def write_csv(filename, url, level, underspeed=False):  #167 (line in Coconut source)
    stages = important_stages["underspeed" if underspeed else "outspeed"]  #168 (line in Coconut source)
    benchmarks = get_benchmarks(url, level, underspeed=underspeed)  #169 (line in Coconut source)
    with open(filename, "w", newline="") as csvfile:  #170 (line in Coconut source)
        writer = csv.writer(csvfile)  #171 (line in Coconut source)
        writer.writerow(["Speed: \\ Stage:",] + [str(stage) for stage in stages])  #172 (line in Coconut source)
        for base_speed in (sorted)(benchmarks, reverse=True):  #173 (line in Coconut source)
            row = [base_speed,]  #174 (line in Coconut source)
            for stage in stages:  #175 (line in Coconut source)
                pokemon_speeds = benchmarks[base_speed][stage]  #176 (line in Coconut source)
                row.append((", ".join)((map)(str, pokemon_speeds)))  #177 (line in Coconut source)
            writer.writerow(row)  #182 (line in Coconut source)



def main(*, out: str="", underspeed: bool=False, url: str="https://www.pikalytics.com", level: int=50,):  #185 (line in Coconut source)
    """Write Pokemon speed tier data in csv format.

    :param out: The csv file to write the speed tier data to.
    :param underspeed: Whether to calculate underspeed benchmarks instead of outspeed benchmarks.
    :param url: The Pikalytics url to get Pokemon from.
    :param level: The level of the Pokemon to compute speeds at.
    """  #198 (line in Coconut source)
    if not out:  #199 (line in Coconut source)
        out = "./underspeed_benchmarks.csv" if underspeed else "./outspeed_benchmarks.csv"  #200 (line in Coconut source)
    write_csv(out, url, level, underspeed=underspeed)  #201 (line in Coconut source)



run_main = _coconut_partial(run, main)  #204 (line in Coconut source)
