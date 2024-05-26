import re

from telethon.extensions.markdown import DEFAULT_DELIMITERS, DEFAULT_URL_RE
from telethon.helpers import add_surrogate, del_surrogate, strip_text
from telethon.tl.types import (MessageEntityCode, MessageEntityPre,
                               MessageEntityTextUrl)


def get_lang(message: str, i: int):
    """
    Get the language of the code block.
    :param message:
    :param i:
    :return:
    """
    # Find the position of the first newline character after
    # the end of the first delimiter
    newline_pos = message.find('\n', i)

    # If no newline is found, assume that no language is
    # specified
    if newline_pos == -1:
        return ''

    # Extract the language, which is between the end of the
    # delimiter and the newline
    else:
        lang = message[i:newline_pos].strip()
        print(lang)

    # If the language does not match the regular expression,
    # assume that no language is specified
    if not re.compile(r'[a-zA-Z0-9_-]{1,32}').fullmatch(lang):
        return '', message
    return lang


def patched_parse(message, delimiters=None, url_re=None):
    """
    Parses the given markdown message and returns its stripped representation
    plus a list of the MessageEntity's that were found.

    :param message: the message with markdown-like syntax to be parsed.
    :param delimiters: the delimiters to be used, {delimiter: type}.
    :param url_re: the URL bytes regex to be used. Must have two groups.
    :return: a tuple consisting of (clean message, [message entities]).
    """
    if not message:
        return message, []

    if url_re is None:
        url_re = DEFAULT_URL_RE
    elif isinstance(url_re, str):
        url_re = re.compile(url_re)

    if not delimiters:
        if delimiters is not None:
            return message, []
        delimiters = DEFAULT_DELIMITERS

    # Build a regex to efficiently test all delimiters at once.
    # Note that the largest delimiter should go first, we don't
    # want ``` to be interpreted as a single back-tick in a code block.
    delim_re = re.compile('|'.join('({})'.format(re.escape(k))
                                   for k in
                                   sorted(delimiters, key=len, reverse=True)))

    # Cannot use a for loop because we need to skip some indices
    i = 0
    result = []

    # Work on byte level with the utf-16le encoding to get the offsets right.
    # The offset will just be half the index we're at.
    message = add_surrogate(message)
    while i < len(message):
        m = delim_re.match(message, pos=i)

        # Did we find some delimiter here at `i`?
        if m:
            delim = next(filter(None, m.groups()))

            # +1 to avoid matching right after (e.g. "****")
            end = message.find(delim, i + len(delim) + 1)

            # Did we find the earliest closing tag?
            if end != -1:

                # Remove the delimiter from the string
                message = ''.join((
                    message[:i],
                    message[i + len(delim):end],
                    message[end + len(delim):]
                ))

                # Check other affected entities
                for ent in result:
                    # If the end is after our start, it is affected
                    if ent.offset + ent.length > i:
                        # If the old start is also before ours, it is fully enclosed
                        if ent.offset <= i:
                            ent.length -= len(delim) * 2
                        else:
                            ent.length -= len(delim)

                # Append the found entity
                ent = delimiters[delim]
                if ent == MessageEntityPre:
                    print(f'{delim=}, {len(delim)=}, {i=}, {end=}')
                    lang = get_lang(message, i)
                    start = i + len(lang) + 1
                    print(f'{lang=}, {i=}, {start=}')
                    result.append(ent(start + len(lang), end - start - len(delim), lang))
                else:
                    result.append(ent(i, end - i - len(delim)))

                # No nested entities inside code blocks
                if ent in (MessageEntityCode, MessageEntityPre):
                    i = end - len(delim)

                continue

        elif url_re:
            m = url_re.match(message, pos=i)
            if m:
                # Replace the whole match with only the inline URL text.
                message = ''.join((
                    message[:m.start()],
                    m.group(1),
                    message[m.end():]
                ))

                delim_size = m.end() - m.start() - len(m.group())
                for ent in result:
                    # If the end is after our start, it is affected
                    if ent.offset + ent.length > m.start():
                        ent.length -= delim_size

                result.append(MessageEntityTextUrl(
                    offset=m.start(), length=len(m.group(1)),
                    url=del_surrogate(m.group(2))
                ))
                i += len(m.group(1))
                continue

        i += 1

    message = strip_text(message, result)
    return del_surrogate(message), result
