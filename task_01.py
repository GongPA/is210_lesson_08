#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: Creating and Accessing Instances"""

import data

TOMATO = data.Produce()
EGGPLANT = data.Produce(1311210802)
TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
