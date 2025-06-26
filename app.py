import argparse
from form_utils import match_template

def parse_arguments():
    parser = argparse.ArgumentParser(description="Form template matcher")
    parser.add_argument("get_tpl", help="Get template name", nargs='?')
    parser.add_argument("--kv", nargs='*', help="Key=Value pairs", metavar="key=value")
    args = parser.parse_args()

    if args.kv is None:
        return {}

    parsed = {}
    for item in args.kv:
        if '=' not in item:
            continue
        key, value = item.split("=", 1)
        parsed[key] = value

    return parsed

def main():
    args = parse_arguments()
    result = match_template(args)
    if isinstance(result, str):
        print(result)
    else:
        import json
        print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
