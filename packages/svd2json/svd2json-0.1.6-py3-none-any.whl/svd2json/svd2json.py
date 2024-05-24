# SPDX-License-Identifier: Apache-2.0
#
# Copyright 2023 Ledger SAS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
from xml.etree import ElementTree
import json


class Svd2Json:
    class interrupt:
        pass

    TagValueType = {
        "cpu": dict,
        "device": dict,
        "name": str,
        "endian": str,
        "revision": str,
        "mpuPresent": bool,
        "fpuPresent": bool,
        "fpuDP": bool,
        "dspPresent": bool,
        "icachePresent": bool,
        "dcachePresent": bool,
        "itcmPresent": bool,
        "dtcmPresent": bool,
        "vtorPresent": bool,
        "nvicPrioBits": int,
        "deviceNumInterrupts": int,
        "sauNumRegions": int,
        "version": str,
        "description": str,
        "peripherals": list,
        "peripheral": dict,
        "fields": list,
        "field": dict,
        "baseAddress": int,
        "addressOffset": int,
        "size": int,
        "bitOffset": int,
        "bitWidth": int,
        "access": str,
        "registers": list,
        "register": dict,
        "interrupt": interrupt,
        "value": int,
        "groupName": str,
    }

    def __init__(self):
        self._out = dict()
        self._interrupts = list()

    def parse(self, root):
        self._out = self._parse(root)
        self._peripheral_name_fixup()
        self._interrupts.sort(key=lambda x: x["value"])
        self._out["interrupts"] = self._interrupts
        return self._out

    def _parse(self, node: ElementTree.Element) -> list | dict | str | int | None:
        try:
            value_type = self.TagValueType[node.tag]
            return getattr(self, f"_parse_{value_type.__name__}")(node)
        except KeyError:
            return None

    def _parse_dict(self, node: ElementTree.Element) -> dict:
        out = dict()
        for child in node:
            ret = self._parse(child)
            if ret is not None:
                out[child.tag] = ret

        return out

    def _parse_str(self, node: ElementTree.Element) -> str:
        return node.text if node.text is not None else str("")

    def _parse_bool(self, node: ElementTree.Element) -> bool:
        return True if node.text == "true" or node.text == "1" else False

    def _parse_int(self, node: ElementTree.Element) -> int | None:
        # If the field is empty, skip it
        if node.text is None:
            return None
        str_val = node.text
        if str_val.lower().startswith("0x"):
            return int(str_val, 16)
        else:
            return int(str_val)

    def _parse_list(self, node: ElementTree.Element) -> list:
        out = list()
        for child in node:
            ret = self._parse(child)
            if ret is not None:
                out.append(ret)

        return out

    def _parse_interrupt(self, node: ElementTree.Element) -> None:
        interrupt = dict()
        for elem in node:
            ret = self._parse(elem)
            if ret is not None:
                interrupt[elem.tag] = ret
        # Some irq are shared so, do not insert twice an interrupt with same name
        exist = next((irq for irq in self._interrupts if irq["name"] == interrupt["name"]), None)
        if not exist:
            self._interrupts.append(interrupt)
        return None

    def _peripheral_name_fixup(self) -> None:
        """
        Some SVD may have the peripheral's name as prefix for register's name
        As this is not consistent **AND** there is already such a concatenation
        in peripherals layout template, we can trim this
        """
        for p in self._out["peripherals"]:
            if "groupName" in p.keys() and "registers" in p.keys():
                for r in p["registers"]:
                    r["name"] = r["name"].removeprefix((p["groupName"] + "_").upper())


def svd2json(svd_path: str) -> dict:
    svd_tree = ElementTree.parse(svd_path)
    out = Svd2Json().parse(svd_tree.getroot())
    return out


def run():
    parser = argparse.ArgumentParser(prog="svd2json", description="convert svd file to json")

    parser.add_argument("output", default="out.json", help="output filename")
    parser.add_argument("-s", "--svd", required=True, action="store", help="SVD file to convert")
    args = parser.parse_args()

    try:
        svd_json = json.dumps(svd2json(args.svd), indent=2)
        with open(args.output, "w") as outfile:
            outfile.write(svd_json)
    except FileNotFoundError as e:
        print(e)
        exit(e.errno)
