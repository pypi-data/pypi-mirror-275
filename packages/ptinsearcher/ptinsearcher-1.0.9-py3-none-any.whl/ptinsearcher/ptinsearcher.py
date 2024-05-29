#!/usr/bin/python3
"""
    Copyright (c) 2024 Penterep Security s.r.o.

    ptinsearcher - Web / File information extractor

    ptinsearcher is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ptinsearcher is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ptinsearcher. If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import os
import re
import sys; sys.path.append(__file__.rsplit("/", 1)[0])
import urllib

import requests

from ptlibs import ptmisclib, ptjsonlib, ptprinthelper
from modules import scrape_websites, scrape_files, metadata, results

from _version import __version__


class PtInsearcher:
    def __init__(self, args):
        self.ptjsonlib              = ptjsonlib.PtJsonLib()
        self.url_list               = list(dict.fromkeys(self._get_url_list(args)))
        self.extract_types          = self._get_extract_types(args.extract)
        self.domain                 = self._get_domain(args.domain)
        self.use_json               = args.json
        self.grouping               = args.grouping
        self.grouping_complete      = args.grouping_complete
        self.group_parameters       = args.group_parameters
        self.without_parameters     = args.without_parameters
        self.output_file            = args.output
        self.output_parts           = args.output_parts
        args.use_json               = args.json
        args.file_handle            = self.file_handler = open(self.output_file, "w") if args.output and not args.output_parts else None
        self._check_args_combination(args)
        self.result_list = []

    def run(self, args: argparse.Namespace):
        for index, target in enumerate(self.url_list):
            # Process URLs
            if self.is_url(target):
                try:
                    scrape_result = scrape_websites.WebsiteScraper(target, args, self.extract_types, self.ptjsonlib).process_website( target, args, self.extract_types, self.ptjsonlib )
                    if scrape_result:
                        self.result_list.append(scrape_result)
                    else:
                        self.handle_whitespace(index)
                        continue
                except requests.exceptions.RequestException:
                    self.handle_network_error()

            # Process Files
            elif self.is_file(target):
                scrape_result = scrape_files.FileScraper(path_to_local_file=os.path.abspath(target), args=args, things_to_extract=self.extract_types, ptjsonlib=self.ptjsonlib).process_file(path_to_local_file=os.path.abspath(target), args=args, things_to_extract=self.extract_types, ptjsonlib=self.ptjsonlib)
                if scrape_result:
                    self.result_list.append(scrape_result)
                else:
                    self.handle_whitespace(index)
                    continue

            else:
                err_msg = f"The provided source ('{target}') contains neither an existing file nor a valid URL."
                if len(self.url_list) > 1:
                    ptprinthelper.ptprint(err_msg, "ERROR")
                    return
                else:
                    self.ptjsonlib.end_error(err_msg, self.use_json)

            # Print current result
            if not self.grouping and not self.grouping_complete:
                if not self.use_json and self.result_list:
                    results.print_result([self.result_list[-1]], args)
                    self.handle_whitespace(index)


        # Print all results at once (when done scraping)
        if self.grouping_complete or self.grouping:
            if not self.use_json and self.result_list:
                results.print_result(self.result_list, args)

        self.ptjsonlib.set_status("finished")
        ptprinthelper.ptprint(self.ptjsonlib.get_result_json(), "", self.use_json)


    def _check_args_combination(self, args) -> None:
        """Checks whether provided args are in a valid combination"""
        if self.extract_types["metadata"]:
            try:
                metadata.is_exiftool_executable()
            except PermissionError as e:
                self.ptjsonlib.end_error(str(e), self.use_json)

        if len(self.url_list) > 1 and self.use_json:
            self.ptjsonlib.end_error("Cannot test more than 1 domain while --json parameter is present", "ERROR")
        if any([args.grouping, args.grouping_complete]) and self.use_json:
            self.ptjsonlib.end_error("Cannot use -g or -gc parameters while --json parameter is present", self.use_json)
        if args.grouping and args.grouping_complete:
            self.ptjsonlib.end_error("Cannot use both -g and -gc parameters together", self.use_json)
        if args.output_parts and not args.output:
            self.ptjsonlib.end_error("Missing --output parameter", self.use_json)
        if args.input and args.list:
            self.ptjsonlib.end_error("Cannot use --input and --list parameter together", self.use_json)
        if args.domain and not args.list:
            self.ptjsonlib.end_error("--list required to use with --domain", self.use_json)
        if not args.input and not args.list:
            self.ptjsonlib.end_error("--input or --list parameter required", self.use_json)
        if (args.extension_yes or args.extension_no) and not args.list:
            self.ptjsonlib.end_error("--list required for usage of --extension-yes / --extension-no parameters", self.use_json)
        if args.extension_yes and args.extension_no:
            self.ptjsonlib.end_error("Cannot combine --extension-yes together with --extension-no", self.use_json)

    def handle_whitespace(self, index):
        if index+1 != len(self.url_list):
            # Add whitespace
            ptprinthelper.ptprint(" ", "", not self.use_json)

    def handle_network_error(self):
        error_message = "Server not responding"
        if len(self.url_list) > 1:
            ptprinthelper.ptprint(error_message, "ERROR", not self.use_json)
            return
        else:
            self.ptjsonlib.end_error(error_message, self.use_json)

    def handle_invalid_source(self):
        if len(self.url_list) > 1:
            ptprinthelper.ptprint("The provided source is neither an existing file nor a valid URL.", "ERROR")
            return
        else:
            self.ptjsonlib.end_error("The provided source is neither an existing file nor a valid URL.", self.use_json)

    def is_file(self, source: str) -> bool:
        """Check whether the provided source is an existing file"""
        return os.path.isfile(source)

    def is_url(self, source: str) -> bool:
        """Check whether the provided source is a valid URL"""
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?' # optional ports
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return regex.match(source)

    def _get_domain(self, domain: str) -> str:
        if domain and not re.match("https?:\/\/", domain):
            self.ptjsonlib.end_error("Scheme required for --domain parameter", self.use_json)
        if domain and not domain.endswith("/"):
            domain += "/"
        return domain

    def _get_url_list(self, args) -> list:
        if args.list:
            try:
                url_list = self._read_file(args.list, args.domain)
                if args.extension_yes:
                   url_list = list(dict.fromkeys([url for url in url_list if url.endswith(tuple(args.extension_yes))]))
                if args.extension_no:
                    url_list = list(dict.fromkeys([url for url in url_list if not url.endswith(tuple(args.extension_no))]))
                return url_list

            except FileNotFoundError:
                self.ptjsonlib.end_error(f"File not found {os.path.join(os.getcwd(), args.list)}", self.use_json)
        else:
            return args.input

    def _read_file(self, filepath, domain) -> list:
        domain = self._adjust_domain(domain) if domain else None
        target_list = []
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip("\n")
                if domain:
                    path = urllib.parse.urlparse(line).path
                    while path.startswith("/"): path = path[1:]
                    while path.endswith("/"): path = path[:-1]
                    if not path: continue
                    target_list.append(domain + path)
                else:
                    if re.match('https?:\/\/', line):
                        while line.endswith("/"): line = line[:-1]
                        target_list.append(line)
        return target_list

    def _adjust_domain(self, domain: str) -> str:
        """Adjusts provided <domain>"""
        o = urllib.parse.urlparse(domain)
        if not re.match("http[s]?$", o.scheme):
            self.ptjsonlib.end_error(f"Missing or invalid scheme, supported schemes are: [HTTP, HTTPS]", self.use_json)
        return domain + "/" if not o.path.endswith("/") else domain


    def _get_extract_types(self, extract_str: str) -> dict:
        allowed_letters = {
            "E": "emails",
            "S": "subdomains",
            "C": "comments",
            "F": "forms",
            "U": "internal_urls",
            "X": "external_urls",
            "P": "phone_numbers",
            "M": "metadata",
            "N": "insecure_sources",
            "I": "ip_addresses",
            "Q": "internal_urls_with_parameters",
            "A": "all"
        }
        extract_types = {
            "emails": None,
            "comments": None,
            "forms": None,
            "internal_urls": None,
            "external_urls": None,
            "internal_urls_with_parameters": None,
            "insecure_sources": None,
            "phone_numbers": None,
            "ip_addresses": None,
            "metadata": None,
            "subdomains": None,
            "all": None,
        }

        for char in extract_str:
            char = char.upper()
            if char in allowed_letters.keys():
                extract_types.update({allowed_letters[char]: True})
                if char == "A":
                    for i in extract_types:
                        extract_types[i] = True
            else:
                self.ptjsonlib.end_error(f"Invalid parameter '{char}' in --extract argument, allowed characters ({''.join(allowed_letters.keys())})", self.use_json)
        return extract_types


def get_help():
    return [
        {"description": ["Source information extractor"]},
        {"usage": ["ptinsearcher <options>"]},
        {"usage_example": [
            "ptinsearcher -i https://www.example.com/",
            "ptinsearcher -i https://www.example.com/ --extract E        # Extract emails",
            "ptinsearcher -i https://www.example.com/ --extract UQX      # Extract internal URLs, internal URLs w/ parameters, external URLs",
            "ptinsearcher -l url_list.txt --grouping                     ",
            "ptinsearcher -l url_list.txt --grouping-complete            ",
            "ptinsearcher -l url_list.txt",
        ]},
        {"options": [
            ["-i",  "--input",                  "<input>",          "Test URL or File"],
            ["-l",  "--list",                   "<list>",           "Load list of URLs from file"],
            ["-d",  "--domain",                 "<domain>",         "Domain - merge domain with filepath. Use when wordlist contains filepaths (e.g. /index.php)"],
            ["-e",  "--extract",                "<extract>",        "Specify data to extract:"],
            ["",    "",                         "   A",             "  All (extracts everything - default option)"],
            ["",    "",                         "   E",             "  Emails"],
            ["",    "",                         "   S",             "  Subdomains"],
            ["",    "",                         "   C",             "  Comments"],
            ["",    "",                         "   F",             "  Forms"],
            ["",    "",                         "   I",             "  IP addresses"],
            ["",    "",                         "   P",             "  Phone numbers"],
            ["",    "",                         "   U",             "  Internal urls"],
            ["",    "",                         "   Q",             "  Internal urls with parameters"],
            ["",    "",                         "   X",             "  External urls"],
            ["",    "",                         "   N",             "  Insecure urls"],
            ["",    "",                         "   M",             "  Metadata"],
            ["",    "",                         "",                 ""],
            ["-ey", "--extension-yes",          "<extensions>",     "Process only URLs from <list> that end with <extension-yes>"],
            ["-en", "--extension-no",           "<extensions>",     "Process only URLs from <list> that do not end with <extension-no>"],
            ["-g",  "--grouping",               "",                 "Group findings from multiple sources into one table"],
            ["-gc", "--grouping-complete",      "",                 "Group and merge findings from multiple sources into one result"],
            ["-gp", "--group-parameters",       "",                 "Group URL parameters"],
            ["-wp", "--without-parameters",     "",                 "Without URL parameters"],
            ["-op", "--output-parts",           "",                 "Save each extract-type to separate file"],
            ["-o",  "--output",                 "<output>",         "Save output to file"],
            ["-p",  "--proxy",                  "<proxy>",          "Set proxy (e.g. http://127.0.0.1:8080)"],
            ["-T",  "--timeout",                "<timeout>",        "Set timeout"],
            ["-c",  "--cookie",                 "<cookie=value>",   "Set cookie"],
            ["-a",  "--user-agent",             "<user-agent>",     "Set User-Agent"],
            ["-H",  "--headers",                "<header:value>",   "Set custom header(s)"],
            ["-r",  "--redirects",              "",                 "Follow redirects (default False)"],
            ["-C",  "--cache",                  "",                 "Cache requests (load from tmp in future)"],
            ["-v",  "--version",                "",                 "Show script version and exit"],
            ["-h",  "--help",                   "",                 "Show this help message and exit"],
            ["-j",  "--json",                   "",                 "Output in JSON format"],
        ]
        }]


def parse_args():
    parser = argparse.ArgumentParser(add_help=False, usage=f"{SCRIPTNAME} <options>")
    parser.add_argument("-i",  "--input",              type=str, nargs="+")
    parser.add_argument("-d",  "--domain",             type=str)
    parser.add_argument("-l",  "--list",               type=str)
    parser.add_argument("-e",  "--extract",            type=str, default="A")
    parser.add_argument("-ey", "--extension-yes",      type=str, nargs="+")
    parser.add_argument("-en", "--extension-no",       type=str, nargs="+")
    parser.add_argument("-pd", "--post-data",          type=str)
    parser.add_argument("-o",  "--output",             type=str)
    parser.add_argument("-p",  "--proxy",              type=str)
    parser.add_argument("-T",  "--timeout",            type=int)
    parser.add_argument("-c",  "--cookie",             type=str, nargs="+")
    parser.add_argument("-a",  "--user-agent",         type=str, default="Penterep Tools")
    parser.add_argument("-H",  "--headers",            type=ptmisclib.pairs, nargs="+")
    parser.add_argument("-r",  "--redirects",          action="store_true")
    parser.add_argument("-op", "--output-parts",       action="store_true")
    parser.add_argument("-g",  "--grouping",           action="store_true")
    parser.add_argument("-gc", "--grouping-complete",  action="store_true")
    parser.add_argument("-gp", "--group-parameters",   action="store_true")
    parser.add_argument("-wp", "--without-parameters", action="store_true")
    parser.add_argument("-C",  "--cache-requests",     action="store_true")
    parser.add_argument("-j",  "--json",               action="store_true")
    parser.add_argument("-v",  "--version",            action="version", version=f"%(prog)s {__version__}", help="show version")

    parser.add_argument("--socket-address",          type=str, default=None)
    parser.add_argument("--socket-port",             type=str, default=None)
    parser.add_argument("--process-ident",           type=str, default=None)

    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        ptprinthelper.help_print(get_help(), SCRIPTNAME, __version__)
        sys.exit(0)

    args = parser.parse_args()
    ptprinthelper.print_banner(SCRIPTNAME, __version__, args.json, space=0)
    return args


def main():
    global SCRIPTNAME
    SCRIPTNAME = "ptinsearcher"
    requests.packages.urllib3.disable_warnings()
    args = parse_args()
    script = PtInsearcher(args)
    script.run(args)


if __name__ == "__main__":
    main()
