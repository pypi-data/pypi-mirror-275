#!/usr/bin/env python3

"""
Config Loader and Config Schema Validator
"""

import os

import yaml
from giturlparse import parse
from marshmallow import Schema, ValidationError, fields, validate, validates_schema


class RepoSchema(Schema):
    name = fields.Str(required=True)
    url = fields.Str(required=True)
    branch = fields.Str(required=True)
    auth = fields.Dict(keys=fields.Str(), values=fields.Str(), required=True)
    username = fields.Str()
    password = fields.Str()
    docker_compose_paths = fields.List(fields.Str(), required=True)

    @validates_schema
    def validate_auth(self, data, **kwargs):
        auth = data.get("auth", {})
        ssh_key_location = auth.get("ssh_key_location")
        username = auth.get("username")
        password = auth.get("password")

        if not (ssh_key_location or (username and password)):
            raise ValidationError(
                "Either 'ssh_key_location' or 'username' and 'password' must be provided for authentication."
            )

        if ssh_key_location:
            expanded_path = os.path.expanduser(ssh_key_location)
            if not os.path.exists(ssh_key_location):
                raise ValidationError(
                    f"SSH key({ssh_key_location}) location does not exist."
                )

    @validates_schema
    def validate_url(self, data, **kwargs):
        url = data.get("url")
        git_url = parse(url)
        if not git_url.valid:
            raise ValidationError("Invalid Git URL")


class ConfigSchema(Schema):
    repos = fields.List(fields.Nested(RepoSchema), required=True)
    sync_interval_seconds = fields.Int(required=True, validate=validate.Range(min=120))


class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file

    def get_config(self):
        config_data = self._load_from_yaml()
        return self._load_config(config_data)

    def _load_from_yaml(self):
        with open(self.config_file, "r", encoding="utf-8") as file:
            config_data = yaml.safe_load(file)
        return config_data

    def _load_config(self, config_data):
        schema = ConfigSchema()
        return schema.load(config_data)
