#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:38:20 2024
pokedextext
@author: antoine
"""
from importlib import resources as impr
from . import dexpoke
from . import somemons

dpath = somemons.dexpath

hh = dexpoke.pokedexer(dpath)
hh.shape()

