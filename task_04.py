#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Task 04: Subclassing
"""

import task_02
# import a module form task_02.py


class Tigerpaw(task_02.Tire):
    """
    Create a new class called Tigerpaw() subclassed to task_02.Tire()
    base class methods (__init__(), add_miles()) inherited.
    """

    __maximum_miles = 750
