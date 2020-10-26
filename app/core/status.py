"""
This is partially used in the example. However, many use cases have kind of a `status`
entity/attribute and this dummy state machine has been really useful for me.
"""

from app.exceptions import InvalidStatusError

ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"

RULES = {
    ACTIVE: [INACTIVE],
    INACTIVE: [ACTIVE],
}

STATUS_LIST = [ACTIVE, INACTIVE]


class Status:
    def __init__(self, value):
        if value not in STATUS_LIST:
            raise InvalidStatusError({"current": None, "new_value": value})
        self.value = value

    def next(self, new_value):
        if new_value not in RULES.get(self.value, []):
            raise InvalidStatusError({"current": self.value, "new_value": new_value})
        self.value = new_value
        return self
