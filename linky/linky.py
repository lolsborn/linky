import re
import types

# Match most urls
URL_REGEX1 = r'(http|www\.)[^\s<>\(\)\[\],]+[\.]+[^\s<>\(\)\[\],.]+'

# Match short urls without www or http for [com|org|net]
# URL_REGEX2 = r'[^\s<>;&]+[\.]+(com|org|net)[^\s<>;&]+'

# Match email addresses
EMAIL_REGEX = r'[^\s<>\(\)\[\],<>]+@[^\s<>\(\)\[\],<>]+\.+[^\s<>\(\)\[\],.<>]+'

# Match US Phone Numbers
PHONE_REGEX = r'([1][\.\- ])?[0-9]{3}[\.\- ][0-9]{3}[\.\- ][0-9]{4}'


def email_handler(match):
    text = match.group(0)
    start = ""
    tail = ""
    if text.startswith("<"):
        text = text[1:]
        start = "<"
    if text.endswith(">"):
        text = text[:-1]
        tail = ">"
    if text.startswith("&lt;"):
        text = text[4:]
        start = "&lt;"
    if text.endswith("&gt;"):
        text = text[:-4]        
        tail = "&gt;"

    return '%(start)s<a href="mailto:%(email)s" target="_blank">%(email)s</a>%(tail)s' % \
    { 'email': text, 'tail': tail, 'start': start}

def url_handler(match):
    text = match.group(0)
    start = ""
    tail = ""
    if text.startswith("<"):
        text = text[1:]
        start = "<"
    if text.endswith(">"):
        text = text[:-1]
        tail = ">"
    if text.startswith("&lt;"):
        text = text[4:]
        start = "&lt;"
    if text.endswith("&gt;"):
        text = text[:-4]        
        tail = "&gt;"
    url = text
    if not url.startswith("http"):
        url = "http://" + url
    return '%(start)s<a href="%(url)s" target="_blank">%(text)s</a>%(tail)s' % \
        { 'url': url, 'text': text, 'start': start, 'tail': tail }

def phone_handler(match):
    text = match.group(0)
    onlynum = ''.join(c for c in text if c.isdigit())
    return '<a href="tel:%(num)s" target="_blank">%(num)s</a>' % { 'num': onlynum }

def linky(text, url_regex=URL_REGEX1, email_regex=EMAIL_REGEX, \
    phone_regex=PHONE_REGEX, url_callback=url_handler, email_callback=email_handler, \
    phone_callback=phone_handler):
    newtext = text

    if email_callback:
        newtext = re.sub(email_regex, email_callback, newtext, flags=re.I)

    if phone_callback:
        newtext = re.sub(phone_regex, phone_callback, newtext, flags=re.I)

    if url_callback:
        if isinstance(url_regex, types.StringTypes):
            newtext = re.sub(url_regex, url_callback, newtext, flags=re.I)
        else:
            for regex in url_regex:
                newtext = re.sub(regex, url_callback, newtext, flags=re.I)

    return newtext