#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : tag_data
# Author        : Sun YiFan-Movoid
# Time          : 2024/5/19 17:11
# Description   : 
"""
from pathlib import Path
from typing import Any, Dict, List


class DataItem:
    def __init__(self, value: Any, source: str):
        self._value: Any = value
        self._root: str = source
        self._source: str = source

    @property
    def value(self) -> Any:
        return self._value

    @property
    def source(self) -> str:
        return self._source

    @property
    def root(self) -> str:
        return self._root

    def update(self, value=None, source=None):
        self._value = self._value if value is None else value
        self._source = self._source if source is None else source

    def inherit(self, source: str = None) -> 'DataItem':
        temp = DataItem(self._value, self._source)
        temp.update(source=source)
        return temp


class TreeItem(DataItem):
    def __init__(self, value: dict, source: str):
        super().__init__(value, source)

    def __getitem__(self, item: str):
        key_list = item.split(' ')
        key_list = [_ for _ in key_list if _]
        temp = self._value
        for key_index, key in enumerate(key_list):
            if key in temp:
                temp = temp[key]
            else:
                raise KeyError(f'{key} not in {temp}, which is index {key_index} of {item}')
        return temp


class TagData:
    __tag = '__tag__'

    def __init__(self, xml_file: str, print_func=None):
        self._path = Path(xml_file)
        self._ori: Dict[str, Dict[str, Any]] = {}
        self._now: Dict[str, DataItem] = {}
        self._label_list: List[str] = []
        self.init(xml_file, False)
        self.print = print if print_func is None else print_func

    def __contains__(self, item):
        return item in self._now

    def __getitem__(self, item):
        return self._now[item].value

    def get(self, item, default=None):
        return self._now[item].value if item in self._now else default

    def init(self, xml_file: str = None, new: bool = True):
        self._path = self._path if xml_file is None else Path(xml_file)
        if new or self._path.exists():
            self.read()
            self.use_suite_case_list('__init__')

    def write(self):
        temp_dict = {_k: _v for _k, _v in self._ori.items() if not _k.startswith('$')}
        with self._path.open(mode='w') as f:
            json.dump(temp_dict, f, default=lambda x: x.value, indent=2)
        temp_path = self._path.parent / f'${self._path.name}'
        temp_dict2 = {_k: _v for _k, _v in self._ori.items() if _k.startswith('$')}
        with temp_path.open(mode='w') as f:
            json.dump(temp_dict2, f, default=lambda x: x.value, indent=2)

    def read(self):
        if not self._path.is_file():
            self._path.touch()
            self._path.write_text('{}')
        with self._path.open(mode='r') as f:
            config_text = f.read()
            config_dict = json.loads(config_text)
        self.ori_init(config_dict)
        self._now = {}
        self._label_list = []

    def ori_init(self, config_dict: Dict[str, Dict[str, Any]]):
        self._ori = {}
        for i, v in config_dict.items():
            if i.startswith('$'):
                continue
            else:
                self.ori_update_label(i, v, file=False)
        self.write()

    def ori_update_label(self, label: str, kv_dict: Dict[str, Any], override=True, file=True):
        label_now = f'${label}'
        self._ori[label] = {}
        self._ori[label_now] = {}
        for i, v in kv_dict.items():
            self._ori[label][i] = ConfigItem(v, label)
            self._ori[label_now][i] = self._ori[label][i].inherit()
            if i == '__inherit__':
                v_now = f'${v}'
                if v in self._ori and v_now in self._ori:
                    for j, w in self._ori[v_now].items():
                        if override:
                            self._ori[label_now][j] = w.inherit(label)
                        else:
                            self._ori[label_now].setdefault(j, w.inherit(label))
                else:
                    raise KeyError(f'config "{label}" try to inherit "{v}" which does not exist.')
        if file:
            self.write()

    def now_update_key(self, key, value, label=None, override=True, ori=True, file=True):
        if key in self._now:
            if override:
                self._now[key].update(value, label)
        else:
            label = '__unknown__' if label is None else label
            self._now[key] = ConfigItem(value, label)
        if ori:
            label_ori = self._now[key].root
            label_now = f'${label_ori}'
            self._ori.setdefault(label_ori, {})
            self._ori.setdefault(label_now, {})
            self._ori[label_ori][key] = self._now[key]
            self._ori[label_now][key] = self._now[key]
        if file:
            self.write()

    def now_use_label(self, label, override=True, clear=False):
        if clear:
            self.now_clear()
        label_now = f'${label}'
        if label in self._ori and label_now in self._ori:
            self._label_list.append(label)
            for i, v in self._ori[label_now].items():
                if override:
                    self._now[i] = v
                else:
                    self._now.setdefault(i, v)

    def now_clear(self):
        self._now = {}
        self._label_list = []

    def show_now_value(self):
        self.print('***** now values start *****')
        for i, v in self._now.items():
            self.print(f'{i} : {v.value} ({type(v.value).__name__}) [from {v.source} & root {v.root}]')
        self.print('***** now values end *****')

    def show_now_list(self):
        self.print(f'now config contains :[{",".join(self._label_list)}]')

    def use_suite_case_list(self, suite_case_key, override=True, clear=False):
        suite_case_now = f'${self.__suite_case_label}'
        suite_case_platform_now = f'${self.__suite_case_platform_label}'
        if self.__suite_case_label not in self._ori:
            self.ori_update_label(self.__suite_case_label, {})
        if self.__suite_case_platform_label not in self._ori:
            self.ori_update_label(self.__suite_case_platform_label, {})
        should_write = False
        if suite_case_key not in self._ori[self.__suite_case_label]:
            self._ori[self.__suite_case_label][suite_case_key] = ConfigItem([], self.__suite_case_label)
            should_write = True
        if suite_case_key not in self._ori[suite_case_now]:
            self._ori[suite_case_now][suite_case_key] = self._ori[self.__suite_case_label][suite_case_key]
            should_write = True
        if suite_case_key not in self._ori[self.__suite_case_platform_label]:
            self._ori[self.__suite_case_platform_label][suite_case_key] = ConfigItem([], self.__suite_case_platform_label)
            should_write = True
        if suite_case_key not in self._ori[suite_case_platform_now]:
            self._ori[suite_case_platform_now][suite_case_key] = self._ori[self.__suite_case_platform_label][suite_case_key]
            should_write = True
        if should_write:
            self.write()
        if clear:
            self.now_clear()
        for label in self._ori[suite_case_now][suite_case_key].value:
            self.now_use_label(label, override=override, clear=False)
        for label in self._ori[suite_case_platform_now][suite_case_key].value:
            self.now_use_label(label, override=override, clear=False)
