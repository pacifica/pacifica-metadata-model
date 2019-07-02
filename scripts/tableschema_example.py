#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Example tableschema sql from the website."""
from os import getenv
from tableschema import Table
from sqlalchemy import create_engine


def main():
    """Main method."""
    # Load and save table to SQL
    engine = create_engine(getenv('SQLALCHEMY_URL', 'sqlite://'))
    table = Table([], schema='users.json')
    table.save('users', storage='sql', engine=engine)


if __name__ == '__main__':
    main()
