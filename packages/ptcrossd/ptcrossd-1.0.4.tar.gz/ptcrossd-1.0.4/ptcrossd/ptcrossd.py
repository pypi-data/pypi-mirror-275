#!/usr/bin/python3
"""
    Copyright (c) 2024 Penterep Security s.r.o.

    ptcrossd - Crossdomain.xml Testing Tool

    ptcrossd is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ptcrossd is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ptcrossd.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import re
import sys; sys.path.append(__file__.rsplit("/", 1)[0])
import urllib

import requests
import defusedxml.ElementTree as DEFUSED_ET
import xml.etree.ElementTree as ET

from _version import __version__
from ptlibs import ptjsonlib, ptprinthelper, ptmisclib, ptnethelper


class PtCrossd:
    def __init__(self, args):
        self.ptjsonlib   = ptjsonlib.PtJsonLib()
        self.headers     = ptnethelper.get_request_headers(args)
        self.use_json    = args.json
        self.timeout     = args.timeout
        self.cache       = args.cache
        self.proxies     = {"http": args.proxy, "https": args.proxy}
        self.file_test   = args.cross_domain_file
        self.header_test = args.cross_origin_header
        self._validate_url(args.url)
        if not any([args.cross_domain_file, args.cross_origin_header]):
            self.file_test = self.header_test = True

    def run(self, args) -> None:
        if self.use_json:
            if self.file_test:
                url_path, url = self._adjust_url(args.url)
                self._test_crossdomain(url, url_path)
            if self.header_test:
                self._test_headers(args.url)
            self.ptjsonlib.set_status("finished")
            ptprinthelper.ptprint(self.ptjsonlib.get_result_json())
        else:
            if self.file_test:
                url_list = self._get_paths_for_crossdomain(args.url)
                for url in url_list:
                    if url != url_list[-1]: ptprinthelper.ptprint(" ", "", not self.use_json)
                    if self._test_crossdomain(url):
                        args.url = url
                        break
            if self.header_test:
                self._test_headers(args.url)

    def _test_crlf(self, url, header_name) -> None:
        headers = self.headers.copy()
        headers.update({header_name: "test%0D%0Atestcrlf:crlf"})
        r, r_dump = self._get_response(url)

        if r.headers.get("testcrlf"):
            ptprinthelper.ptprint(f"Header {header_name} is vulnerable to CRLF injection", "VULN", not self.use_json)
            self.ptjsonlib.add_vulnerability(f"PTV-WEB-INJECT-CORS{header_name.capitalize()[0]}CSRF")

    def _test_headers(self, url) -> None:
        ptprinthelper.ptprint(f"Testing: Access-Control-Allow-Origin header", "TITLE", not self.use_json, colortext=True, newline_above=False)
        headers = self.headers.copy()
        headers.update({"Referer": "https://test-cors-referer.com", "Origin": "https://test-cors-origin.com"})
        response, response_dump = self._get_response(url, headers=headers)

        if response.headers.get("Access-Control-Allow-Origin"):
            if response.headers.get("Access-Control-Allow-Origin") == "*":
                ptprinthelper.ptprint("Open CORS vulnerability detected in Access-Control-Allow-Origin header", "VULN", not self.use_json)
                self.ptjsonlib.add_vulnerability("PTV-WEB-HTTP-CORSS", vuln_request=response_dump["request"], vuln_response=response_dump["response"])

            if response.headers.get("Access-Control-Allow-Origin") == "https://test-cors-referer.com":
                ptprinthelper.ptprint("Reflecting Referer header to Access-Control-Allow-Origin header", "VULN", not self.use_json)
                self.ptjsonlib.add_vulnerability("PTV-WEB-HTTP-CORSR", vuln_request=response_dump["request"], vuln_response=response_dump["response"])
                self._test_crlf(url, header_name="Referer")

            if response.headers.get("Access-Control-Allow-Origin") == "https://test-cors-origin.com":
                ptprinthelper.ptprint("Reflecting Origin header to Access-Control-Allow-Origin header", "VULN", not self.use_json)
                self.ptjsonlib.add_vulnerability("PTV-WEB-HTTP-CORSO", vuln_request=response_dump["request"], vuln_response=response_dump["response"])
                self._test_crlf(url, header_name="Origin")

        else:
            ptprinthelper.ptprint(f'Header Access-Control-Allow-Origin is not present', "INFO", not self.use_json)

    def _test_crossdomain(self, url, url_path=None) -> bool:
        ptprinthelper.ptprint(f"Testing: {url}", "TITLE", not self.use_json, colortext=True)
        response, response_dump = self._get_response(url)
        ptprinthelper.ptprint(f"Returned Status Code: {response.status_code}", "INFO", not self.use_json)

        if response.status_code == 200:
            self._process_crossdomain(response, response_dump)
            if self.use_json:
                self.ptjsonlib.add_node(self.ptjsonlib.create_node_object("webSource", properties={"url": url, "name": url_path, "webSourceType": "crossdomain.xml"}))
            return True
        else:
            ptprinthelper.ptprint(f"crossdomain.xml not found", "INFO", not self.use_json, end="\n\n")
            self.ptjsonlib.set_message("crossdomain.xml not found")
            return False


    def _process_crossdomain(self, response, response_dump) -> None:
        try:
            tree = DEFUSED_ET.fromstring(response.text)
        except DEFUSED_ET.ParseError:
            ptprinthelper.ptprint(f"Error parsing provided XML file", "ERROR", not self.use_json)
            self.ptjsonlib.set_message("Error parsing provided XML file")
            return
        except DEFUSED_ET.EntitiesForbidden:
            ptprinthelper.ptprint(f"Forbidden entities found", "ERROR", not self.use_json)
            self.ptjsonlib.set_message("Forbidden entities found")
            return

        if not self.use_json:
            element = ET.XML(response.text); ET.indent(element)
            xml_string = ET.tostring(element, encoding='unicode')
            ptprinthelper.ptprint("XML content:", "TITLE", not self.use_json)
            ptprinthelper.ptprint(ptprinthelper.get_colored_text(xml_string, "INFO"), condition=not self.use_json, newline_above=True)

        ptprinthelper.ptprint(" ", "", not self.use_json)
        self._run_allow_access_from_test(tree, response, response_dump)

    def _run_allow_access_from_test(self, tree, response, response_dump) -> None:
        is_open_cors = False
        http_allowed = False
        acf_elements = tree.findall("allow-access-from")
        if acf_elements:
            for acf_element in acf_elements:
                if "domain" in acf_element.keys() and acf_element.attrib["domain"] == "*":
                    is_open_cors = True
                if "secure" in acf_element.keys() and not acf_element.attrib["secure"]:
                    http_allowed = True
            if is_open_cors:
                ptprinthelper.ptprint("Open CORS vulnerability detected in crossdomain.xml file", "VULN", not self.use_json)
                self.ptjsonlib.add_vulnerability("PTV-WEB-HTTP-CROSSD", vuln_request=response_dump["request"], vuln_response=response_dump["response"])
            if http_allowed:
                ptprinthelper.ptprint("Non-secure communication detected in crossdomain.xml file", "VULN", not self.use_json)

        if not is_open_cors:
            self.ptjsonlib.set_message(response.text)

    def _adjust_url(self, url: str) -> tuple[str, str]:
        """Adjusts a given URL to ensure it points to a 'crossdomain.xml' file."""
        parsed_url = urllib.parse.urlparse(url)
        if not parsed_url.path.endswith("/crossdomain.xml"):
            if parsed_url.path in ["", "/"]:
                parsed_url = parsed_url._replace(path="/crossdomain.xml")
            else:
                directories = [d for d in parsed_url.path.split("/") if d]
                if "." in directories[-1]: directories.pop()
                parsed_url = parsed_url._replace(path='/'.join(directories) + "/crossdomain.xml")
        return (parsed_url.path if not parsed_url.path.startswith("/") else parsed_url.path[1:], urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, "", "", "")))

    def _get_paths_for_crossdomain(self, url) -> list:
        """Generates a list of URLs pointing to potential 'crossdomain.xml' locations based on the given URL."""
        parsed_url = urllib.parse.urlparse(url)
        result = []
        if parsed_url.path not in ["/", ""]:
            directories = [d for d in parsed_url.path.split("/") if d]
            if "." in directories[-1]:
                directories.pop()
            while directories:
                path = '/'.join(directories) + "/crossdomain.xml"
                result.append(urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, path, "", "", "")))
                directories.pop()
        result.append(urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, "/crossdomain.xml", "", "", "")))
        return result

    def _validate_url(self, url: str) -> None:
        parsed_url = urllib.parse.urlparse(url)
        if not re.match("https?$", parsed_url.scheme):
            self.ptjsonlib.end_error("Missing or wrong scheme, only HTTP(s) schemas are supported", self.use_json)
        if not parsed_url.netloc:
            self.ptjsonlib.end_error("Provided URL is not valid", self.use_json)

    def _get_response(self, url: str, headers: dict|None = None):
        if not headers:
            headers = self.headers
        try:
            response, response_dump = ptmisclib.load_url_from_web_or_temp(url, method="GET", headers=headers, proxies=self.proxies, timeout=self.timeout, redirects=True, verify=False, cache=self.cache, dump_response=True)
            return response, response_dump
        except requests.RequestException:
            self.ptjsonlib.end_error(f"Cannot connect to server", self.use_json)


def get_help():
    return [
        {"description": ["Crossdomain.xml Testing Tool"]},
        {"usage": ["ptcrossd <options>"]},
        {"usage_example": [
            "ptcrossd -u https://www.example.com/crossdomain.xml",
            "ptcrossd -u https://www.example.com/",

        ]},
        {"options": [
            ["-u",  "--url",                    "<url>",            "Connect to URL"],
            ["-cf",  "--cross-domain-file",     "",                 "Test crossdomain.xml file"],
            ["-ch", "--cross-origin-header",    "",                 "Test Access-Control-Allow-Origin header"],
            ["-p",  "--proxy",                  "<proxy>",          "Set proxy (e.g. http://127.0.0.1:8080)"],
            ["-T",  "--timeout",                "<timeout>",        "Set timeout (default to 10)"],
            ["-c",  "--cookie",                 "<cookie>",         "Set cookie"],
            ["-a", "--user-agent",              "<user-agent>",     "Set User-Agent header"],
            ["-H",  "--headers",                "<header:value>",   "Set custom header(s)"],
            ["-C",  "--cache",                  "",                 "Cache requests (load from tmp in future)"],
            ["-v",  "--version",                "",                 "Show script version and exit"],
            ["-h",  "--help",                   "",                 "Show this help message and exit"],
            ["-j",  "--json",                   "",                 "Output in JSON format"],
        ]
        }]


def parse_args():
    parser = argparse.ArgumentParser(add_help="False")
    parser.add_argument("-u",   "--url",                 type=str, required=True)
    parser.add_argument("-p",   "--proxy",               type=str)
    parser.add_argument("-c",   "--cookie",              type=str)
    parser.add_argument("-a",  "--user-agent",           type=str, default="Penterep Tools")
    parser.add_argument("-T",   "--timeout",             type=int, default=10)
    parser.add_argument("-H",   "--headers",             type=ptmisclib.pairs, nargs="+")
    parser.add_argument("-cf",  "--cross-domain-file",   action="store_true")
    parser.add_argument("-ch",  "--cross-origin-header", action="store_true")
    parser.add_argument("-j",   "--json",                action="store_true")
    parser.add_argument("-C",   "--cache",               action="store_true")
    parser.add_argument("-v",   "--version",             action="version", version=f"{SCRIPTNAME} {__version__}")

    parser.add_argument("--socket-address",          type=str, default=None)
    parser.add_argument("--socket-port",             type=str, default=None)
    parser.add_argument("--process-ident",           type=str, default=None)



    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        ptprinthelper.help_print(get_help(), SCRIPTNAME, __version__)
        sys.exit(0)

    args = parser.parse_args()
    ptprinthelper.print_banner(SCRIPTNAME, __version__, args.json)
    return args


def main():
    global SCRIPTNAME
    SCRIPTNAME = "ptcrossd"
    requests.packages.urllib3.disable_warnings()
    args = parse_args()
    script = PtCrossd(args)
    script.run(args)


if __name__ == "__main__":
    main()
