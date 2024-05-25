import re
import os
import platform
from cwstorm.dsl.dag_node import DagNode
from datetime import datetime
from cwstorm import __schema_version__

class Job(DagNode):
    """Job node.
    
    There's exactly one job node for each workflow. The job node summarizes the workflow and its status once tasks start running.
    """

    ATTRS = {
        "comment": {
            "type": "str",
            "validator": re.compile(r'^[_a-z0-9 ,.!?\'"]+$', re.IGNORECASE),
        },
        "project": {
            "type": "str",
            "validator": re.compile(r"^[a-z0-9_\-\.\s]+$", re.IGNORECASE),
        },
        "email": {
            "type": "str",
            "validator": re.compile(
                r"\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b", re.IGNORECASE
            ),
        },
        "author": {
            "type": "str",
            "validator": re.compile(r"^[a-z\s]+$", re.IGNORECASE),
        },
        "location": {
            "type": "str",
            "validator": re.compile(r'^(?:[a-z][a-z0-9]*$|([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$|^$)', re.IGNORECASE),
        },
        "created_at": {
            "type": "str",
            "validator": re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$"),
        },
        "account_id": {"type": "str", "validator": re.compile(r"^\d{16}$")},
        "metadata": {"type": "dict"},
        "schema_version": {
            "type": "str",
            "validator": re.compile(r"^\d{1,2}\.\d{1,2}.\d{1,2}$"),
        },
        "status": {
            "type": "str",
            "validator": re.compile(r"^(WAITING|\d{1,3}|RUNNING|SUCCESS|FAILED)$"),
            "default": "WAITING",
        },
    }

    def is_original(self, parent=None):
        """Always true."""
        return True

    def is_reference(self, parent):
        """Always false."""
        return False

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.created_at(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"))
        self.schema_version(__schema_version__)
        self.author(self.get_username())

    @staticmethod
    def get_username():
        """Return the username of the current user."""
        result =  os.environ.get("USERNAME") if platform.system() == "Windows" else os.environ.get("USER")
        if not result:
            result =   os.environ.get("CIRCLE_USERNAME")
        if not result:
            result =  "unknown"
        return result
