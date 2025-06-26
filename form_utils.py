import re
from tinydb import TinyDB, Query
from typing import Dict

def detect_type(value: str) -> str:
    if re.match(r"^(\d{2})\.(\d{2})\.(\d{4})$", value) or re.match(r"^(\d{4})-(\d{2})-(\d{2})$", value):
        return "date"
    if re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
        return "phone"
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", value):
        return "email"
    return "text"

DB_FILE = "form_template_app/db.json"
db = TinyDB(DB_FILE)

def match_template(args: Dict[str, str]) -> str:
    templates = db.all()
    parsed_input = {k: detect_type(v) for k, v in args.items()}

    for template in templates:
        template_fields = {k: v for k, v in template.items() if k != "name"}
        if all(k in parsed_input and parsed_input[k] == v for k, v in template_fields.items()):
            return template["name"]

    return parsed_input
