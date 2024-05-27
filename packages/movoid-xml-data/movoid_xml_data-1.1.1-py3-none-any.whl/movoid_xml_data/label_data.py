#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Version: 3.8.10
Creator:        sunyifan0649
Create Date:    2024/5/20
Description:    
"""
import pathlib
import re

from lxml import etree


class DataItem:
    __kw_type = ['dict']
    __v_type = ['list', 'tuple', 'set']
    create = 0

    def __init__(self, value, parent=None, description='', value_type=None):
        self._value = value
        self._type = type(value).__name__ if value_type is None else value_type
        self._parent = parent
        self._son = None
        self._description = description
        self._son_init()

    def __getitem__(self, item):
        key, value, keys = self._key_analyse(item)
        if value is None:
            raise KeyError(f'there is no key:{key}')
        else:
            if keys:
                return value[keys]
            else:
                return value

    def __setitem__(self, item, value):
        key, target, keys = self._key_analyse(item)
        if keys:
            target[keys] = DataItem.new(value)
        else:
            self._son[key] = DataItem.new(value)

    def __contains__(self, keys):
        key, value, keys = self._key_analyse(keys)
        if value is None:
            return False
        else:
            if keys:
                return keys in value
            else:
                return True

    def __iter__(self):
        self._iter_list = list(self.values())
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self._iter_list):
            raise StopIteration
        else:
            self._iter_index += 1
            return self._iter_list[self._iter_index - 1]

    def __len__(self):
        return len(self.values())

    def __add__(self, item):
        if self._type in self.__kw_type:
            if isinstance(item, (dict, DataItem)):
                for k, v in item.items():
                    self[k] = v
        elif self._type in self.__v_type:
            if isinstance(item, (list, tuple, set, DataItem)):
                for v in item:
                    self.insert(v)
        else:
            raise TypeError('不能对非dict,list,set,tuple使用+')
        return self

    @classmethod
    def read_from_xml(cls, xml: etree.Element, parent=None, tag_name='var'):
        if xml.tag == tag_name:
            xml.tag = 'root'
            ele_type = xml.get('type', 'str')
            ele_desc = xml.get('description', '')
            if ele_type in cls.__kw_type:
                re_item = DataItem(value=None, parent=parent, description=ele_desc, value_type=ele_type)
                ele_child = xml.cssselect('root > var')
                for i in ele_child:
                    re_item[i.get('key')] = DataItem.read_from_xml(i, re_item)
            elif ele_type in cls.__v_type:
                re_item = DataItem(value=None, parent=parent, description=ele_desc, value_type=ele_type)
                ele_child = xml.cssselect('root > var')
                for i in ele_child:
                    re_item.insert(DataItem.read_from_xml(i, re_item))
            else:
                ele_value = xml.text
                if ele_type == 'None':
                    ele_value = None
                elif ele_type == 'bool':
                    ele_value = True if ele_value.lower() in ('true', 'yes') else False
                elif ele_type == 'int':
                    try:
                        ele_value = int(ele_value)
                    except ValueError:
                        ele_value = 0
                elif ele_type == 'float':
                    try:
                        ele_value = float(ele_value)
                    except ValueError:
                        ele_value = 0.0
                elif ele_type == 'number':
                    try:
                        ele_value = int(ele_value)
                    except ValueError:
                        try:
                            ele_value = float(ele_value)
                        except ValueError:
                            ele_value = 0
                else:
                    ele_value = str(ele_value)
                re_item = DataItem(value=ele_value, parent=parent, description=ele_desc, value_type=ele_type)
        else:
            return ValueError(f'xml item can only be <{tag_name}> tag')
        return re_item

    @classmethod
    def new(cls, item, *args, type_check=None, **kwargs):
        if type_check:
            if isinstance(item, DataItem):
                if item._type != type_check:
                    raise TypeError(f'target data item is {item._type} not {type_check}')
            else:
                if type(item).__name__ != type_check:
                    raise TypeError(f'target value is {type(item).__name__} not {type_check}:{item}')
        return item if isinstance(item, DataItem) else DataItem(item, *args, **kwargs)

    def _key_analyse(self, keys):
        if isinstance(keys, (list, tuple, set)):
            key_list = keys
        else:
            key_str = str(keys)
            key_list = []
            while key_str.startswith('.'):
                key_list.append('.')
                key_str = key_str[1:]
            key_list += list([_ for _ in key_str.split(' ') if _])
        if len(key_list) == 0:
            return '', self, []
        elif len(key_list) >= 1:
            return key_list[0], self._get_son(key_list[0]), []
        else:
            return key_list[0], self._get_son(key_list[0]), key_list[1:]

    def _son_init(self):
        if self._type in self.__kw_type:
            if isinstance(self._value, dict):
                self._son = {k: DataItem(v, self) for k, v in self._value.items()}
            else:
                self._son = {}
        elif self._type in self.__v_type:
            if isinstance(self._value, (list, tuple, set)):
                self._son = [DataItem(v, self) for v in self._value]
            else:
                self._son = []

    def _get_son(self, son_key):
        if son_key == '.':
            return self._parent
        elif self._son is None:
            return None
        else:
            if isinstance(self._son, list):
                try:
                    index = int(son_key)
                except:
                    return None
                else:
                    return self._son[index]
            elif isinstance(self._son, dict):
                return self._son.get(son_key)
            else:
                return None

    def has_son(self):
        return self._type in self.__kw_type or self._type in self.__v_type

    @property
    def value(self):
        if self._type in self.__kw_type:
            return {k: v.value for k, v in self._son.items()}
        elif self._type in self.__v_type:
            return [_.value for _ in self._son]
        else:
            return self._value

    def items(self, value=False):
        if self._type in self.__kw_type:
            return [(k, (v.value if value else v)) for k, v in self._son.items()]
        elif self._type in self.__v_type:
            return [(k, (v.value if value else v)) for k, v in enumerate(self._son)]
        else:
            return [['', (self.value if value else self)]]

    def keys(self):
        if self._type in self.__kw_type:
            return self._son.keys()
        elif self._type in self.__v_type:
            return range(len(self._son))
        else:
            return ['']

    def values(self, value=False):
        if self._type in self.__kw_type:
            return [(v.value if value else v) for k, v in self._son.items()]
        elif self._type in self.__v_type:
            return [(v.value if value else v) for v in self._son]
        else:
            return [(self.value if value else self)]

    def pure_keys(self, header=''):
        re_list = []
        if self._type in self.__kw_type + self.__v_type:
            for k, v in self._son.items():
                re_list += v.pure_keys(f'{header} {k}' if header else k)
        else:
            re_list = [header] if header else []
        return re_list

    def pure_values(self, value=False, header=''):
        re_list = []
        if self._type in self.__kw_type + self.__v_type:
            for k, v in self._son.items():
                re_list += v.pure_keys(value, f'{header} {k}' if header else k)
        else:
            re_list = [(self.value if value else self)] if header else []
        return re_list

    def pure_items(self, value=False, header=''):
        re_list = []
        if self._type in self.__kw_type + self.__v_type:
            for k, v in self._son.items():
                re_list += v.pure_items(value, f'{header} {k}' if header else k)
        else:
            re_list = [[header, (self.value if value else self)]] if header else []
        return re_list

    def all_keys(self, header=''):
        re_list = [header] if header else []
        if self._type in self.__kw_type + self.__v_type:
            for k, v in self._son.items():
                re_list += v.all_keys(f'{header} {k}' if header else k)
        return re_list

    def all_values(self, value=False, header=''):
        re_list = [(self.value if value else self)] if header else []
        if self._type in self.__kw_type + self.__v_type:
            for k, v in self._son.items():
                re_list += v.all_keys(value, f'{header} {k}' if header else k)
        return re_list

    def all_items(self, value=False, header=''):
        re_list = [[header, (self.value if value else self)]] if header else []
        if self._type in self.__kw_type + self.__v_type:
            for k, v in self._son.items():
                re_list += v.all_keys(value, f'{header} {k}' if header else k)
        return re_list

    def to_xml(self, parent_root=None, tag_name='var', **kwargs):
        if parent_root is None:
            root = etree.Element(tag_name)
        else:
            root = etree.SubElement(parent_root, tag_name)
        root.set('description', self._description)
        root.set('type', self._type)
        for k, v in kwargs.items():
            root.set(str(k), str(v))
        if self._type in self.__kw_type:
            if len(self):
                for k, v in self._son.items():
                    v.to_xml(root, key=str(k))
            else:
                root.text = ' '
        elif self._type in self.__v_type:
            if len(self):
                for v in self._son:
                    v.to_xml(root)
            else:
                root.text = ' '
        else:
            root.text = str(self._value)
        return root

    def insert(self, son, index=None):
        if index is None:
            self._son.append(DataItem.new(son))
        else:
            self._son.insert(index, DataItem.new(son))

    def pop(self, index=None):
        self._son.pop(index)

    def clear(self):
        self._son.clear()

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value

    def get(self, key, __default=None, *args, __value=True, __analyse=True, **kwargs):
        try:
            temp_value = self[key].value if __value else self[key]
        except KeyError:
            temp_value = __default
        finally:
            if __analyse and isinstance(temp_value, str):
                temp_value = self.analyse(temp_value, *args, **kwargs)
        return temp_value

    def analyse(self, ori_text, *args, **kwargs):
        temp_str = ori_text
        while True:
            re_result = re.search(r'(.*?)<<([^<>]*?)>>(.*)', temp_str)
            if re_result:
                template_str = re_result.group(2)
                template_list = template_str.split('!', 1)
                template_key = template_list[0]
                template_default = template_list[1] if len(template_list) >= 2 else ''
                template_value = None
                if template_key in kwargs:
                    template_value = str(kwargs[template_key])
                elif template_key in self:
                    template_value = str(self[template_key])
                else:
                    for data_item in args:
                        if isinstance(data_item, DataItem) and template_key in data_item:
                            template_value = str(data_item[template_key])
                            break
                template_value = template_default if template_value is None else template_value
                temp_str = re_result.group(1) + template_value + re_result.group(3)
            else:
                break
        return temp_str


class LabelData:
    def __init__(self):
        self._label = DataItem({"__init__": []})
        self._body = DataItem({})
        self._now = DataItem({})
        self._label_list = ['__init__']
        self.use_labels(self._label_list)

    def __getitem__(self, item):
        return self._now.get(item)

    @property
    def label(self):
        return self._label

    @property
    def body(self):
        return self._body

    @property
    def now(self):
        return self._now

    def get(self, key, __analyse: bool = True, **kwargs):
        return self._now.get(key, __analyse=__analyse, **kwargs)

    def keys(self):
        return self._now.keys()

    def values(self):
        return self._now.values()

    def items(self):
        return self._now.items()

    def pure_keys(self):
        return self._now.pure_keys()

    def pure_values(self):
        return self._now.pure_values()

    def pure_items(self):
        return self._now.pure_items()

    def all_keys(self):
        return self._now.all_keys()

    def all_values(self):
        return self._now.all_values()

    def all_items(self):
        return self._now.all_items()

    def set_label(self, key: str, label: (list, DataItem)):
        self._label[key] = DataItem.new(label, type_check='list')

    def set_body(self, key: str, body: (list, DataItem)):
        self._body[key] = DataItem.new(body, type_check='dict')

    def remove_label(self, key: str):
        self._label.pop(key)

    def remove_body(self, key: str):
        self._body.pop(key)

    def clear_now(self, clear=True):
        if clear:
            self._label_list = ["__init__"]
            self._now.clear()
            self.use_labels(self._label_list)

    def use_labels(self, labels, clear_now=False):
        labels = [labels] if isinstance(labels, str) else list(labels)
        self.clear_now(clear_now)
        for label in labels:
            if label in self._label:
                label_list = self._label[label].value
                self._label_list.append(label)
                for body_label in label_list:
                    if body_label in self._body:
                        self._now += self._body[body_label]

    def read(self, file_name, replace=True, reuse_label=True, reuse_label_clear=True, error=False):
        file_path = pathlib.Path(file_name)
        if file_path.is_file():
            if replace:
                self._label.clear()
                self._body.clear()
            with file_path.open(mode='r', encoding='utf8') as f:
                file_xml = etree.fromstring(f.read().encode('utf8'))
            file_xml.tag = 'root'
            label_elements = file_xml.cssselect('root > label')[0]
            body_elements = file_xml.cssselect('root > body')[0]
            self._label += DataItem.read_from_xml(label_elements, tag_name='label')
            self._body += DataItem.read_from_xml(body_elements, tag_name='body')
            if reuse_label:
                self.use_labels(self._label_list, reuse_label_clear)
        else:
            if error:
                raise FileExistsError(f'{file_name} is not a file')

    def write(self, file_name):
        root = etree.Element('root')
        self._label.to_xml(root, tag_name='label')
        self._body.to_xml(root, tag_name='body')
        file_path = pathlib.Path(file_name)
        with file_path.open(mode='w', encoding='utf8') as f:
            f.write(etree.tostring(root, encoding='utf-8', pretty_print=True, xml_declaration=True).decode('utf-8'))
