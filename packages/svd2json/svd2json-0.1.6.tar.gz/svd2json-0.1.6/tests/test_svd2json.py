# SPDX-FileCopyrightText: 2024 Ledger SAS
# SPDX-License-Identifier: Apache-2.0

# coding: utf-8

# import pytest
from svd2json import Svd2Json


def test_internals():
    converter = Svd2Json()
    assert isinstance(converter._interrupts, list)
