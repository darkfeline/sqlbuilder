sqlbuilder
==========

A SQL builder for SQLite and Python 3.

Not complete, but what is done is well-tested.

Example:

    from sqlbuilder import *

    query = Select('table')
    query.add_column('col')
    query.where(BinaryOp('=', Identifier('col'), literal('hi')))
    assert query.build() == 'SELECT "col" FROM "table" WHERE "col" = \'hi\''

    query = CreateTable('table')
    query.add_column('col', type_name='INTEGER', primary_key=True)
    query.add_column('col2', type_name='TEXT')
    assert query.build() == 'CREATE TABLE "table" ( "col" "INTEGER" , "col2" "TEXT" , PRIMARY KEY ( "col" ) )'
