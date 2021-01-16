#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init,Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.sonarqube")
use_plugin('python.integrationtest')
use_plugin('source_distribution')

default_task = ["clean", "install_dependencies", "analyze"]

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
    project.build_depends_on("coverage")
    project.build_depends_on_requirements("requirements.txt")
    
    project.set_property("dir_source_unittest_python", "src/unittest/python")
    project.set_property("dir_source_integrationtest_python", "src(integrationtest/python")
    project.set_property("integrationtest_parallel",True) 
    project.set_property("flake8_break_build",False)
    
    project.set_property("coverage_break_build", False)
    project.set_property("coverage_threshold_warn",75)
    
    project.set_property("flake8_include_test_sources",True)
    project.get_property("distutils_commands").append('bdist_wheels')
    project.set_property("distutils_classifiers", [
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Console",
        "Intended Audience :: Developers"])

@init
def set_sonarqube(project):
    project.set_property("sonarqube_project_key",'Expensetracker')
    project.set_property("sonarqube_project_name",'Expensetracker')

