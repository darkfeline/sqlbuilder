# Copyright (C) 2016  Allen Li
#
# This file is part of sqlbuilder.
#
# sqlbuilder is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sqlbuilder is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with sqlbuilder.  If not, see <http://www.gnu.org/licenses/>.

from . import tokens
from . import expr
from . import statements


def load_tests(loader, tests, pattern):
    tests.addTest(loader.loadTestsFromModule(tokens))
    tests.addTest(loader.loadTestsFromModule(expr))
    tests.addTest(loader.loadTestsFromModule(statements))
    return tests
