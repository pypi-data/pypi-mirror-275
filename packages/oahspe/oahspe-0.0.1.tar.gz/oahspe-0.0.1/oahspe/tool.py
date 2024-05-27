# coding: utf-8

from pytz import timezone
from datetime import datetime


def setdefault(args, pair):
  def _setdefault(key, value):
    if key not in args:
      args[key] = value
      return args
    old = args[key]
    if old is None or (isinstance(old, int|float) and old == 0) or (isinstance(old, set|tuple|list|str) and len(old) == 0):
      args[key] = value

  if isinstance(pair, dict):
    for k,v in pair.items():
      _setdefault(k, v)
  else:
    _setdefault(pair[0], pair[1])
  return args
  

def now(zone:str='Asia/Ho_Chi_Minh'):
  return _local(lambda: datetime.now(), zone)


def _local(time, zone:str='Asia/Ho_Chi_Minh'):
  zone = timezone(zone)
  return zone.normalize(timezone('UTC').localize(time()).astimezone(zone))


def local(time, zone:str='Asia/Ho_Chi_Minh'):
  if isinstance(time, int):
    time = datetime.fromtimestamp(time)
  zone = timezone(zone)
  return zone.normalize(timezone('UTC').localize(time).astimezone(zone))



def jinja(template, data):
  from os import path
  from jinja2 import Template
  if path.exists(template):
    with open(template, 'r') as f:
      template = f.read()
  return Template(template).render(**data)


def json_load(content):
  from ujson import loads
  if isinstance(content, bool):
    return {}
  try:
    with open(content, 'r') as f:
      content = f.read()
  except: pass
  try: content = loads(content)
  except: content = {}
  if not isinstance(content, dict):
    content = {}
  return content


def json_dump(dict, file=None):
  from ujson import dumps
  if file is None:
    try: res = dumps(dict, indent=2)
    except: res = dumps({})
  else:
    try: res = dumps(dict, separators=(',', ':'))
    except: res = dumps({})
    with open(file, 'w') as f:
      f.write(res)
  return res


def json_write(file, key, value):
  res = json_load(file)
  res[key] = value
  json_dump(res, file)


def yml_load(content):
  from yaml import safe_load
  if isinstance(content, bool):
    return {}
  try:
    with open(content, 'r') as f:
      content = f.read()
  except: pass
  try:
    content = safe_load(content)
  except:
    content = {}
  if not isinstance(content, dict):
    content = {}
  return content


def yml_dump(dict, file=None):
  from yaml import safe_dump
  try: res = safe_dump(dict, indent=2)
  except: res = safe_dump({})
  if file is not None:
    with open(file, 'w') as f:
      f.write(res)
  return res


def yml_write(file, key, value):
  res = yml_load(file)
  res[key] = value
  yml_dump(res, file)


def csv_load(content):
  import pandas as pd
  from os.path import exists
  if exists(content):
    if content[-3:] == 'tsv':
      content = pd.read_csv(content, delimiter='\t')
    else:
      content = pd.read_csv(content)
  else:
    try:
      content = [row.split(',') for row in content.splitlines()]
      content = pd.DataFrame(content)
    except:
      content = pd.DataFrame({})
  return content
  

def parse_key(key):
  if '/' not in key:
    prefix = ''
  else:
    prefix = key.split('/')
    key = prefix[-1]
    prefix = '/'.join(prefix[:-1])
  return key, prefix


def gen_uuid(size:int=64, punc:str='') -> str:
  from random import choice
  from string import ascii_letters, digits

  def check(mess:str) -> bool:
    check_digits = False
    for ch in mess:
      if ch in digits:
        check_digits = True
        break
    if punc == '': check_punc = True
    else:
      check_punc = False
      for ch in mess:
        if ch in punc:
          check_punc = True
          break
    return check_digits and check_punc

  pool = ascii_letters + digits + punc
  size = size - 1
  def rand() -> str:
    return [choice(pool) for _ in range(size)]

  first = choice(ascii_letters)
  uuid = rand()
  while not check(uuid): uuid = rand()
  uuid = ''.join(uuid)
  uuid = first + uuid
  return uuid


def bash(code):
  import os
  sh = gen_uuid()
  sh = f'/tmp/{sh}.sh'
  with open(sh, 'w') as f:
    f.write('#!/usr/bin/bash\n')
    f.write(code)
  os.system(f'chmod +x {sh}')
  os.system(sh)
  os.remove(sh)


def output(code:str|bytes, path:str|None=None, title:str=''):
  if path is None:
    if isinstance(code, bytes):
      print(title)
      print(code.decode())
    else:
      print(title)
      print(code)
  else:
    if isinstance(code, bytes): f = open(path, 'wb')
    else: f = open(path, 'w')
    f.write(code)


def qrcode(text):
  '''max=1273'''
  from qrcode import QRCode, constants
  qr = QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
  )
  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill='black', back_color='white')
  return img
