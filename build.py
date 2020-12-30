#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init,Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "ExpenseTracker"
version="1.0"

summary = "ExpenseTracker / Software Development Project"
url     = "https://github.com/FelixLehn/ExpenseTracker.git"

description="""This is the Build Station for the Expense Tracker. For more Details please lookup in the
Git repository of Felix """

authors=[Author("Felix Lehner","felix.lehner@t-online.de")]
license="None"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("coverage_break_build", False)
