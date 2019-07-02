#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Validate the json schema documents against json schema."""
from os import path, listdir
from unittest import TestCase
from json import loads
from jsonschema import validate, ValidationError
from requests import get


class SchemaValidate(TestCase):
    """Validate any jsonschema document against tabular jsonschema."""

    schema_url = 'https://frictionlessdata.io/schemas/table-schema.json'
    schema = ''

    @classmethod
    def setUpClass(cls):
        """Setup the jsonschema from the url."""
        resp = get(cls.schema_url)
        assert resp.status_code == 200
        cls.schema = resp.json()

    def test_jsonschema(self):
        """Test the jsonschema at root of repo."""
        schema_dir = path.realpath(path.join(path.dirname(__file__), '..'))
        for file_name in listdir(schema_dir):
            full_path = path.join(schema_dir, file_name)
            if file_name[-5:] == '.json':
                hit_exception = False
                try:
                    validate(loads(open(full_path, 'r').read()), self.schema)
                except ValidationError:
                    hit_exception = True
                self.assertFalse(
                    hit_exception,
                    'failed to validate {}'.format(file_name[:-5])
                )
