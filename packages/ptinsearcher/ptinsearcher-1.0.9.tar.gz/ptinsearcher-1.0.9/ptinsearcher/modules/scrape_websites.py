import re
import requests
import urllib
import html

from bs4 import BeautifulSoup

from ptlibs import ptprinthelper, ptmisclib, ptnethelper
from modules import metadata, emails, comments, forms, phone_numbers, ip_addresses, urls


class WebsiteScraper:
    def __init__(self, url: str, args, things_to_extract: dict, ptjsonlib: object):
        self.target_url: str = url
        self.things_to_extract: dict = things_to_extract
        self.ptjsonlib: object = ptjsonlib
        self.args = args
        self.use_json: bool = args.json

    def process_website(self, url: str, args, extract_types: dict, ptjsonlib: object) -> dict:
        """Scrape <things_to_extract> from <url>'s response"""
        try:
            response = self.get_response(url, args)
        except requests.exceptions.RequestException:
            return {}

        ptprinthelper.ptprint(f"Provided source.............: {url}", "TITLE", not self.use_json, colortext=True)           #, newline_above=True if len(self.url_list) > 1 and index != 0 else False)
        #ptprinthelper.ptprint(f"Source-Type.................: URL", "TITLE", not self.use_json)
        ptprinthelper.ptprint(f"Content-Type................: {response.headers.get('content-type', '').split(';')[0]}", "TITLE", not self.use_json)
        ptprinthelper.ptprint(f"Status Code.................: {response.status_code}", "TITLE", not self.use_json, end=" ")

        if self.stop_on_redirect(response, args):
            return {}

        if response.content:
            return self._scrape_website(response, ptjsonlib, args, extract_types)
        else:
            ptprinthelper.ptprint(f"Response returned no content", "ERROR", not self.use_json, newline_above=True)
            return {}

    def get_response(self, url: str, args):
        """Retrieve response from <target>"""
        try:
            response = ptmisclib.load_url_from_web_or_temp(url=url, method="GET" if not args.post_data else "POST", headers=ptnethelper.get_request_headers(args), proxies={"http": args.proxy, "https": args.proxy}, data=args.post_data, timeout=args.timeout, redirects=args.redirects, verify=False, cache=args.cache_requests)
            response.encoding = response.apparent_encoding
            return response
        except requests.exceptions.RequestException:
            raise

    def stop_on_redirect(self, response, args: dict):
        """Stop on redirect if not --redirects"""
        if response.is_redirect and not args.redirects:
            if response.headers.get("location"):
                ptprinthelper.ptprint(f"[redirect] -> {ptprinthelper.get_colored_text(response.headers['location'], 'INFO')}", "", not self.use_json)
            if not response.headers.get("location"):
                ptprinthelper.ptprint(" ", "", not self.use_json)
            ptprinthelper.ptprint("Redirects disabled, use -r/--redirect to follow", "ERROR", not self.use_json, newline_above=True)
            return True
        if args.redirects and response.history:
            ptprinthelper.ptprint(f"[redirected] -> {ptprinthelper.get_colored_text(response.history[-1].headers['location'], 'INFO')}", "", not self.use_json)
        else:
            ptprinthelper.ptprint(" ", "", not self.use_json)

    def _get_soup(self, response, args):
        if "<!ENTITY".lower() in response.text.lower():
            ptprinthelper.ptprint(f"Forbidden entities found", "ERROR", not self.use_json, colortext=True)
            return False
        else:
            soup = BeautifulSoup(response.text, features="lxml")
            bdos = soup.find_all("bdo", {"dir": "rtl"})
            for item in bdos:
                item.string.replace_with(item.text[::-1])
            return soup

    def _scrape_website(self, response, ptjsonlib, args, extract_types: dict) -> dict:
            """Extracts <extract_types> from <response>"""
            result_data = {"url": response.url, "metadata": None, "emails": None, "phone_numbers": None, "ip_addresses": None, "abs_urls": None, "internal_urls": None, "internal_urls_with_parameters": None, "external_urls": None, "insecure_sources": list(), "subdomains": None, "forms": None, "comments": None}
            insecure_sources = set()

            # Find Metadata
            if extract_types["metadata"]:
                result_data["metadata"] = metadata.get_metadata(response)
                ptjsonlib.add_node(ptjsonlib.create_node_object("metadata", None, None, properties={"metadata": result_data["metadata"]}))

            PAGE_CONTENT = urllib.parse.unquote(urllib.parse.unquote(html.unescape(response.text)))

            # Find Emails
            if extract_types["emails"]:
                result_data["emails"] = emails.find_emails(PAGE_CONTENT)
                ptjsonlib.add_node(ptjsonlib.create_node_object("emails", None, None, properties={"emails": result_data["emails"]}))

            # Find Page Comments
            if extract_types["comments"]:
                result_data["comments"] = comments.find_comments(PAGE_CONTENT)
                ptjsonlib.add_node(ptjsonlib.create_node_object("comments", None, None, properties={"comments": result_data["comments"]}))

            # Find Phone numbers
            if extract_types["phone_numbers"]:
                result_data["phone_numbers"] = phone_numbers.find_phone_numbers(PAGE_CONTENT)
                ptjsonlib.add_node(ptjsonlib.create_node_object("phone_numbers", None, None, properties={"phone_numbers": result_data["phone_numbers"]}))

            # Find IP Addresses
            if extract_types["ip_addresses"]:
                result_data["ip_addresses"] = ip_addresses.find_ip_addresses(PAGE_CONTENT)
                ptjsonlib.add_node(ptjsonlib.create_node_object("ip_addresses", None, None, properties={"ip_addresses": result_data["ip_addresses"]}))

            # Find Forms
            if extract_types["forms"]:
                soup = self._get_soup(response, args)
                if soup:
                    result_data["forms"] = forms.get_forms(soup)
                    ptjsonlib.add_node(ptjsonlib.create_node_object("form", None, None, properties={"forms": result_data["forms"]}))

            # Find Absolute URLs
            if any([extract_types["external_urls"], extract_types["subdomains"], extract_types["internal_urls"], extract_types["internal_urls_with_parameters"], extract_types["insecure_sources"]]):
                result_data["abs_urls"] = urls.find_abs_urls(PAGE_CONTENT)
                #ptjsonlib.add_node(ptjsonlib.create_node_object("abs_urls", None, None, properties={"abs_urls": result_data["abs_urls"]}))

                # Find External URLs | Filters through absolute_urls
                if extract_types["external_urls"] or extract_types["insecure_sources"]:
                    result_data['external_urls'] = urls.find_urls_in_response(PAGE_CONTENT, r'(href=|src=)[\'"](.+?)[\'"]', response.url, "external", without_parameters=args.without_parameters, abs_urls=result_data["abs_urls"])
                    if extract_types["external_urls"]:
                        ptjsonlib.add_node(ptjsonlib.create_node_object("external_urls", None, None, properties={"external_urls": result_data["external_urls"]}))

                # Find Subdomains | Filters through absolute_urls
                if extract_types["subdomains"]:
                    result_data['subdomains'] = urls.find_urls_in_response(PAGE_CONTENT, r'(href=|src=)[\'"](.+?)[\'"]', response.url, "subdomain", without_parameters=args.without_parameters, abs_urls=result_data["abs_urls"])
                    ptjsonlib.add_node(ptjsonlib.create_node_object("subdomains", None, None, properties={"subdomains": result_data["subdomains"]}))

                # Find Internal URLs | Filters through absolute_urls
                if extract_types["internal_urls"] or extract_types["internal_urls_with_parameters"] or extract_types["insecure_sources"]:
                    result_data["internal_urls"] = urls.find_urls_in_response(PAGE_CONTENT, r'(href=|src=)[\'"](.+?)[\'"]', response.url, "internal", without_parameters=args.without_parameters, abs_urls = result_data["abs_urls"])

                    # Add to ptjsonlib
                    if extract_types["internal_urls"]:
                        ptjsonlib.add_node(ptjsonlib.create_node_object("internal_urls", None, None, properties={"internal_urls": result_data["internal_urls"]}))

                    # Find Internal URLs containing parameters | Filters through internal_urls
                    if extract_types["internal_urls_with_parameters"]:
                        result_data["internal_urls_with_parameters"] = sorted(urls._find_internal_parameters(result_data["internal_urls"], group_parameters=args.group_parameters), key=lambda k: k['url'])
                        ptjsonlib.add_node(ptjsonlib.create_node_object("internal_urls_with_parameters", None, None, properties={"internal_urls_with_parameters": result_data["internal_urls_with_parameters"]}))
                        if not extract_types["internal_urls"]:
                            result_data["internal_urls"] = None

                if extract_types["insecure_sources"]:
                    result_data["insecure_sources"].extend(self._find_insecure_sources(all_urls=result_data["abs_urls"] + result_data["external_urls"] + result_data["internal_urls"]))
                    ptjsonlib.add_node(ptjsonlib.create_node_object("insecure_sources", None, None, properties={"insecure_sources": result_data["insecure_sources"]}))
                    if not extract_types["internal_urls"]:
                            result_data["internal_urls"] = None
                    if not extract_types["external_urls"]:
                            result_data["external_urls"] = None

            return result_data


    def _find_insecure_sources(self, all_urls) -> list:
        """Find in <all_urls> urls that are loaded via unsecure HTTP protocol."""
        insecure_sources = list(set([u for u in all_urls if re.match(r"http://", u)]))
        return insecure_sources

    def parse_robots_txt(self, response):
        allow = list({pattern.lstrip() for pattern in re.findall(r"^Allow: ([\S ]*)", response.text, re.MULTILINE)})
        disallow = list({pattern.lstrip() for pattern in re.findall(r"^Disallow: ([\S ]*)", response.text, re.MULTILINE)})
        sitemaps = re.findall(r"[Ss]itemap: ([\S ]*)", response.text, re.MULTILINE)
        test_data = {"allow": allow, "disallow": disallow, "sitemaps": sitemaps}

        parsed_url = urllib.parse.urlparse(response.url)
        internal_urls = []
        for section_header in test_data.values():
            for finding in section_header:
                parsed_finding = urllib.parse.urlparse(finding)
                if not parsed_finding.netloc:
                    full_path = urllib.parse.urlunparse((parsed_url[0], parsed_url[1], parsed_finding[2], "", "", ""))
                else:
                    full_path = finding
                internal_urls.append(full_path)
        return internal_urls