import re
from typing import TYPE_CHECKING, Any, Dict, List, Callable

if TYPE_CHECKING:
    from .classes import Translation


__parentheses = re.compile(r'(\([^()]*\))')
__quotes = re.compile(r'(([\'"]).*?\2)')
__functions = re.compile(r'^([A-Za-z0-9_]*)\(([A-Za-z0-9_.,]*)\)$')
__slices = re.compile(r'^([A-Za-z0-9_]*)\[(\d*)(:?)(\d*):?(\d*)]$')


def _find(text, regex, holder):
    matches = []
    while new := re.findall(regex, text):
        for match in new:
            text = text.replace(match, f'{holder}{len(matches)}{holder}', 1)
            matches.append(match)

    return text, matches


def _replace(text, holder, matches):
    pattern = re.compile(f'{holder}(\\d+){holder}')
    while indexes := re.findall(pattern, text):
        for index in indexes:
            text = text.replace(f"{holder}{index}{holder}", matches[int(index)], 1)

    return text


def split_placeholder(text: str) -> List[str]:
    text, q_matches = _find(text, __quotes, '$')
    text, p_matches = _find(text, __parentheses, '%')
    split = text.split('.')
    for i in range(len(split)):
        split[i] = _replace(split[i], '%', p_matches)
    for i in range(len(split)):
        split[i] = _replace(split[i], '$', q_matches)

    return split


def split_args(text: str) -> List[str]:
    if text == '':
        return []

    text, q_matches = _find(text, __quotes, '$')
    text, p_matches = _find(text, __parentheses, '%')
    split = text.split(',')
    for i in range(len(split)):
        split[i] = _replace(split[i], '%', p_matches)
    for i in range(len(split)):
        split[i] = _replace(split[i], '$', q_matches)

    return split


def handle_placeholder(placeholder: str, translation: "Translation", objects: Dict[str, Any]) -> Any:
    # Possible None!
    if placeholder is None or placeholder == '' or placeholder.lower() == 'none' or placeholder.lower() == 'null':
        return None

    # If bool, return bool
    if placeholder.lower() == "true":
        return True
    if placeholder.lower() == "false":
        return False

    # If string, return string
    if match := re.match("^(['\"])(.*?)\1$", placeholder):
        return match.group(2)

    # If int, return int
    if match := re.match("^\\d+$", placeholder):
        return int(match.group(1))

    # If float, return float
    if match := re.match("^(-?(?:\\d+\\.\\d*|\\.\\d+|\\d+)(?:e-?\\d+)?)$", placeholder):
        return float(match.group(1))

    path = split_placeholder(placeholder)

    obj: None | object = {"translation": translation, **objects}
    while obj is not None and len(path) > 0:
        current = path.pop(0)

        # Handle callables
        if match := re.match(__functions, current):
            current = match.group(1)
            obj = get_from(current, obj)
            if isinstance(obj, Callable):
                args = split_args(match.group(2))
                for i in range(len(args)):
                    args[i] = handle_placeholder(args[i], translation, objects)

                # Todo KWARGS
                obj = obj(*args)
            else:
                obj = None

        # Handle slicing
        elif match := re.match(__slices, current):
            current = match.group(1)
            obj = get_from(current, obj)
            if isinstance(obj, list):
                si = match.group(2)
                si = int(si) if si else None
                if match.group(3) == ":":
                    ei = match.group(4)
                    ei = int(ei) if ei else None
                    ti = match.group(5)
                    ti = int(ti) if ti else None
                    obj = obj[slice(si, ei, ti)]
                else:
                    obj = obj[si]

        # Handle membership
        else:
            obj = get_from(current, obj)

    return str(obj)


def get_from(current, obj):
    if current is None or current == '':
        return obj
    if isinstance(obj, dict):
        return obj.get(current, None)
    else:
        return getattr(obj, current, None)