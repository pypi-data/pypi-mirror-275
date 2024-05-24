"""
This module is highly inspired by Mail Scout: https://github.com/batuhanaky/mailscout
Do a regular check on their repository and implement the good ideas here.
"""
import re
import random
import string
import smtplib
import itertools
import time
import unicodedata
import dns.resolver
from functools import partial
from unidecode import unidecode
from concurrent.futures import ThreadPoolExecutor, as_completed



def find_generic_emails_bulk(domains: list[str], custom_prefixes: list[str] | None = None) -> dict[str, list[str]] | None:
    """
    Find valid generic email addresses in bulk for multiple domains.

    :param domains: List of domains to search for generic emails.
    :param custom_prefixes: List of custom prefixes to search for. If not provided, common prefixes will be used.
    :return: A dictionary containing: {domain: [generic_emails]}
    """
    results = {}
    with ThreadPoolExecutor() as executor:
        # We make futures a dict to keep track of the domain associated with each future (list of emails).
        futures = {}
        for domain in domains:
            future = executor.submit(partial(find_generic_emails, domain, custom_prefixes))
            futures[future] = domain
        for future in as_completed(futures):
            domain = futures[future]
            generic_emails = future.result()
            results[domain] = generic_emails
    return results or None

def find_personal_emails_bulk(domain: str, names: list[str], check_catchall: bool = True, normalize: bool = True) -> dict[str, list[str]] | None:
    """
    Find valid personal email addresses in bulk for multiple domains.

    :param domain: Domain to search for personal emails.
    :param names: List of names to search for.
    :param check_catchall: Check if the domain is a catch-all domain.
    :param normalize: Normalize the names to email-friendly format.
    :return: A dictionary containing: {name: [personal_emails]}
    """
    if _check_email_is_catchall(domain):
        print(f"{domain} is a catch-all domain.")
        return None

    results = {}
    with ThreadPoolExecutor() as executor:
        # We make futures a dict to keep track of the name associated with each future (list of emails).
        futures = {}
        for name in names:
            future = executor.submit(partial(find_personal_emails, domain, name, check_catchall, normalize))
            futures[future] = name

        for future in as_completed(futures):
            name = futures[future]
            personal_emails = future.result()
            results[name] = personal_emails
    return results or None

def find_generic_emails(domain: str, custom_prefixes: list[str] | None = None) -> list[str] | None:
    """
    Generate a list of generic email addresses for a given domain.

    :param domain: Domain to search for generic emails.
    :param custom_prefixes: List of custom prefixes to search for. If not provided, common prefixes will be used.
    :return: A list of generic email addresses. If the domain is a catch-all domain, returns None.
    """
    if _check_email_is_catchall(domain):
        print(f"{domain} is a catch-all domain.")
        return None

    generic_emails = _generate_generic_emails(domain, custom_prefixes)
    return [email for email in generic_emails if check_email_is_deliverable(email)]

def find_personal_emails(domain: str, name: str, check_catchall: bool = True, normalize: bool = True) -> list[str] | None:
    """
    Generate a list of personal email addresses for a given domain.

    :param domain: Domain to search for personal emails.
    :param name: Name to search for.
    :param check_catchall: Check if the domain is a catch-all domain.
    :param normalize: Normalize the name to email-friendly format.
    :return: A list of personal email addresses. If the domain is a catch-all domain, returns None.
    """
    if check_catchall and _check_email_is_catchall(domain):
        return None

    email_variants = _generate_email_variants(name.split(" "), domain, normalize=normalize)
    print("v", email_variants)
    return [email for email in email_variants if check_email_is_deliverable(email)]

def check_email_is_deliverable(email: str, smtp_port: int = 25, smtp_timeout: int = 2) -> bool:
    """Check if an email is deliverable using SMTP."""
    domain = email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)  # type: ignore
        with smtplib.SMTP(mx_record, smtp_port, timeout=smtp_timeout) as server:
            server.set_debuglevel(0)
            server.ehlo("example.com")
            server.mail('test@example.com')
            code, _ = server.rcpt(email)

        return code == 250
    except Exception as e:
        print(f"Error checking {email}: {e}")
        return False

def _check_email_is_catchall(email_domain: str) -> bool:
    """Check if a domain is a catch-all for email addresses."""
    random_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "falan"
    random_email = f"{random_prefix}@{email_domain}"
    return check_email_is_deliverable(random_email, smtp_timeout=2)

def _normalize_name(name: str) -> str:
    """Convert a non-email compliant name to a normalized email-friendly format."""
    name = unidecode(name.lower())
    normalized = unicodedata.normalize('NFKD', name)
    ascii_encoded = normalized.encode('ascii', 'ignore').decode('ascii')
    email_compliant = re.sub(r'[^a-z0-9]', '', ascii_encoded)
    return email_compliant

def _generate_generic_emails(domain: str, custom_prefixes: list[str] | None = None) -> list[str]:
    """Generate a list of email addresses with common or custom prefixes for a given domain."""
    common_prefixes = [
        "info", "contact", "support", "hello", "hi", "service", "team", "press", "help", "staff", "careers",
        "jobs", "customer", "office", "sales", "marketing", "hr", "accounts", "billing", "finance", "legal",
        "operations", "it", "admin", "research", "design", "engineering", "feedback", "dev", "developer",
        "tech", "management", "webmaster",
    ]
    prefixes = custom_prefixes if custom_prefixes else common_prefixes
    return [f"{prefix}@{domain}" for prefix in prefixes]

def _generate_email_variants(splitted_name: list[str], domain: str, normalize: bool = True) -> list[str]:
    """Generate a set of email address variants based on a list of names for a given domain."""
    variants: set[str] = set()

    if normalize:
        names = [_normalize_name(name) for name in splitted_name]

    for i in range(1, len(names)+1):
        for name_combination in itertools.permutations(names, i):
            variants.add(''.join(name_combination).lower())
            variants.add('.'.join(name_combination).lower())

    for name_part in splitted_name:
        variants.add(name_part.lower())
        variants.add(name_part[0].lower())

    return [f"{variant}@{domain}" for variant in variants]


# Your router's port 25 should be open to use this module. If it's not, you will think that the email is not deliverable.
# This makes the module crashes at import time if the port is not open.
assert check_email_is_deliverable("contact@inoopa.com", smtp_timeout=2), "contact@inoopa.com not deliverable, open your router's port 25"


if __name__ == "__main__":
    start = time.time()
    # Example usage
    inoopa_generic_emails = find_generic_emails("inoopa.com")
    print("Inoopa Generic emails:", inoopa_generic_emails)
    maxim_personal_emails = find_personal_emails("inoopa.com", "Maxim Berge")
    print("Maxim personal emails:", maxim_personal_emails)

    domains = ["inoopa.com", "becode.org"]
    generic_emails = find_generic_emails_bulk(domains)
    print("Generic emails:", generic_emails)

    personal_emails = find_personal_emails_bulk("inoopa.com", ["Maxim Berge", "Isidora Cupara"])
    print("personnal emails: ", personal_emails)
    end = time.time()
    print("Execution time:", end - start)
