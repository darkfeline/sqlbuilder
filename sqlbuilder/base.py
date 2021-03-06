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

from abc import ABC, abstractmethod


class SQLBuilder(ABC):

    """Base SQLBuilder abstract class."""

    @abstractmethod
    def tokens(self):
        """Return a Tokens for the current query."""

    def build(self):
        """Return the query as a string."""
        return str(self.tokens())
