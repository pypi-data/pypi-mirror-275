#!/usr/bin/python3
"""
    Copyright (c) 2024 Penterep Security s.r.o.

    ptcookiechecker - Cookie security testing tool

    ptcookiechecker is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ptcookiechecker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ptcookiechecker.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import re
import sys; sys.path.append(__file__.rsplit("/", 1)[0])
import urllib
from http.cookies import SimpleCookie

import requests

from _version import __version__
from ptlibs import ptjsonlib, ptprinthelper, ptmisclib, ptnethelper

class PtCookieChecker:
    def __init__(self, args):
        self.ptjsonlib   = ptjsonlib.PtJsonLib()
        self.headers     = ptnethelper.get_request_headers(args)
        self.use_json    = args.json
        self.timeout     = args.timeout
        self.cache       = args.cache
        self.proxies     = {"http": args.proxy, "https": args.proxy}

    def run(self, args) -> None:
        response, dump = self.send_request(args.url)
        ptprinthelper.ptprint(f"Testing cookies for site: {response.url} [{response.status_code}]", bullet_type="TITLE", condition=not self.use_json, colortext=True)

        cookie_list = response.cookies
        if not cookie_list:
            ptprinthelper.ptprint(f"Site returned no cookies", bullet_type="", condition=not self.use_json)


        for cookie in cookie_list:
            if args.cookie_name and (args.cookie_name != cookie.name):
                continue

            cookie_name = f"{cookie.name}={cookie.value}"
            cookie_path = cookie.path
            cookie_domain = cookie.domain
            cookie_expiration = cookie.expires
            cookie_secure_flag = cookie.secure
            cookie_http_flag = bool(cookie._rest.get('HttpOnly', False))
            cookie_samesite_flag = bool(cookie._rest.get('SameSite', False))

            ptprinthelper.ptprint(f"\n{cookie}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Name: {cookie.name}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Value: {cookie.value}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Domain: {cookie_domain}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Path: {cookie_path}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Secure: {cookie_secure_flag}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"HttpOnly: {cookie_http_flag}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Expires: {cookie_expiration}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Secure Flag: {cookie_secure_flag}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"HTTP Flag: {cookie_http_flag}", bullet_type="TEXT", condition=not self.use_json)
            ptprinthelper.ptprint(f"Same Site Flag: {cookie_samesite_flag}", bullet_type="TEXT", condition=not self.use_json)


            node = self.ptjsonlib.create_node_object("cookie", properties={
                "name": cookie_name,
                "path": cookie_path,
                "domain": cookie_domain,
                "cookieExpiration": cookie_expiration,
                "cookieSecureFlag": cookie_secure_flag,
                "cookieHttpFlag": cookie_http_flag,
                "cookieSameSiteFlag": cookie_samesite_flag
            }, vulnerabilities=[])

            if not args.list_cookies_only:
                ptprinthelper.ptprint(f" ", bullet_type="TEXT", condition=not self.use_json)
                if cookie.name in ["PHPSESSID", "JSESSIONID", "ASP.NET_SessionID"]:
                    vuln_code = "PTV-WEB-INFO-TEDEFSIDNAME"
                    self.ptjsonlib.add_vulnerability(vuln_code) if args.cookie_name else node["vulnerabilities"].append({"vulnCode": vuln_code})
                    ptprinthelper.ptprint(f"Cookie has default name", bullet_type="VULN", condition=not self.use_json, colortext=False)

                if ((len(cookie.value) == 24 or len(cookie.value) == 26) and re.match(r"^[a-z0-9]*$", cookie.value)) or len(cookie.value) == 32 and re.match(r"^[A-Z0-9]*$", cookie.value):
                    vuln_code = "PTV-WEB-INFO-TEDEFSIDFRM"
                    self.ptjsonlib.add_vulnerability(vuln_code) if args.cookie_name else node["vulnerabilities"].append({"vulnCode": vuln_code})
                    ptprinthelper.ptprint(f"Cookie is in default format", bullet_type="VULN", condition=not self.use_json, colortext=False)

                if not cookie_secure_flag:
                    vuln_code = "PTV-WEB-LSCOO-FLSECSENS"
                    self.ptjsonlib.add_vulnerability(vuln_code) if args.cookie_name else node["vulnerabilities"].append({"vulnCode": vuln_code})
                    ptprinthelper.ptprint(f"Cookie is missing Secure flag", bullet_type="VULN", condition=not self.use_json, colortext=False)


                if not cookie_http_flag:
                    vuln_code = "PTV-WEB-LSCOO-FLHTTPSENS"
                    self.ptjsonlib.add_vulnerability(vuln_code) if args.cookie_name else node["vulnerabilities"].append({"vulnCode": vuln_code})
                    ptprinthelper.ptprint(f"Cookie is missing HttpOnly flag", bullet_type="VULN", condition=not self.use_json, colortext=False)


                if not cookie_samesite_flag:
                    vuln_code = "PTV-WEB-LSCOO-FLSAMESENS"
                    self.ptjsonlib.add_vulnerability(vuln_code) if args.cookie_name else node["vulnerabilities"].append({"vulnCode": vuln_code})
                    ptprinthelper.ptprint(f"Cookie is missing SameSite flag", bullet_type="VULN", condition=not self.use_json, colortext=False)


                if not cookie_name.startswith("__Host-"):
                    vuln_code = "PTV-WEB-LSCOO-HSTPREFSENS"
                    self.ptjsonlib.add_vulnerability(vuln_code) if args.cookie_name else node["vulnerabilities"].append({"vulnCode": vuln_code})
                    ptprinthelper.ptprint(f"Cookie is missing '__Host-' prefix", bullet_type="VULN", condition=not self.use_json, colortext=False)

            if args.cookie_name:
                self.ptjsonlib.add_properties({**node["properties"]})
            else:
                self.ptjsonlib.add_node(node)

        self.ptjsonlib.set_status("finished")
        ptprinthelper.ptprint(self.ptjsonlib.get_result_json(), "", self.use_json)


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


    def _validate_url(self, url: str) -> None:
        parsed_url = urllib.parse.urlparse(url)
        if not re.match("https?$", parsed_url.scheme):
            self.ptjsonlib.end_error("Missing or wrong scheme, only HTTP(s) schemas are supported", self.use_json)
        if not parsed_url.netloc:
            self.ptjsonlib.end_error("Provided URL is not valid", self.use_json)

    def send_request(self, url: str) -> requests.models.Response:
        try:
            response, response_dump = ptmisclib.load_url_from_web_or_temp(url, method="GET", headers=self.headers, proxies=self.proxies, timeout=self.timeout, redirects=True, verify=False, cache=self.cache, dump_response=True)
            return response, response_dump
        except requests.RequestException:
            self.ptjsonlib.end_error(f"Cannot connect to server", self.use_json)


def get_help():
    return [
        {"description": ["Cookie security testing tool"]},
        {"usage": ["ptcookiechecker <options>"]},
        {"usage_example": [
            "ptcookiechecker -u https://www.example.com/",
            "ptcookiechecker -u https://www.example.com/ -c PHPSESSID -l",
        ]},
        {"options": [
            ["-u",  "--url",                    "<url>",               "Connect to URL"],
            ["-c", "--cookie-name",             "<cookie-name>",       "Parse only specific <cookie-name>"],
            ["-T",  "--timeout",                "<timeout>",           "Set timeout (defaults to 10)"],
            ["-a",  "--user-agent",             "<user-agent>",        "Set User-Agent header"],
            ["-H",  "--headers",                "<header:value>",      "Set custom header(s)"],
            ["-p",  "--proxy",                  "<proxy>",             "Set proxy (e.g. http://127.0.0.1:8080)"],
            ["-l",  "--list-cookies-only",      "<list-cookies-only>", "Return cookies without vulnerabilities"],
            ["-C",  "--cache",                  "",                    "Cache requests (load from tmp in future)"],
            ["-v",  "--version",                "",                    "Show script version and exit"],
            ["-h",  "--help",                   "",                    "Show this help message and exit"],
            ["-j",  "--json",                   "",                    "Output in JSON format"],
        ]
        }]


def parse_args():
    parser = argparse.ArgumentParser(add_help="False")
    parser.add_argument("-u",      "--url",               type=str, required=True)
    parser.add_argument("-c",      "--cookie-name",        type=str)
    parser.add_argument("-p",      "--proxy",             type=str)
    parser.add_argument("-l",      "--list-cookies-only", action="store_true")
    parser.add_argument("-a",      "--user-agent",        type=str, default="Penterep Tools")
    parser.add_argument("-T",      "--timeout",           type=int, default=10)
    parser.add_argument("-H",      "--headers",           type=ptmisclib.pairs, nargs="+")
    parser.add_argument("-j",      "--json",              action="store_true")
    parser.add_argument("-C",      "--cache",             action="store_true")
    parser.add_argument("-v",      "--version",           action="version", version=f"{SCRIPTNAME} {__version__}")

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
    SCRIPTNAME = "ptcookiechecker"
    requests.packages.urllib3.disable_warnings()
    args = parse_args()
    script = PtCookieChecker(args)
    script.run(args)


if __name__ == "__main__":
    main()
