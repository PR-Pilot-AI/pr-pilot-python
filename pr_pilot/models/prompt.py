# coding: utf-8

"""
    PR Pilot API

    API for creating PR Pilot tasks

    The version of the OpenAPI document: 1.3.25
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Prompt(BaseModel):
    """
    Prompt
    """ # noqa: E501
    prompt: StrictStr = Field(description="The prompt for the task")
    github_repo: StrictStr = Field(description="The full name of the Github repository, e.g. 'owner/repo'")
    issue_number: Optional[StrictInt] = Field(default=None, description="Number of the issue if task is triggered in the context of an issue")
    pr_number: Optional[StrictInt] = Field(default=None, description="Number of the PR if task is triggered in the context of a PR")
    branch: Optional[StrictStr] = Field(default=None, description="A branch for PR Pilot to run this task on")
    gpt_model: Optional[StrictStr] = Field(default='gpt-4-turbo', description="The GPT model to use for the task")
    image: Optional[StrictStr] = Field(default=None, description="An image to be used in the task")
    __properties: ClassVar[List[str]] = ["prompt", "github_repo", "issue_number", "pr_number", "branch", "gpt_model", "image"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Prompt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Prompt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prompt": obj.get("prompt"),
            "github_repo": obj.get("github_repo"),
            "issue_number": obj.get("issue_number"),
            "pr_number": obj.get("pr_number"),
            "branch": obj.get("branch"),
            "gpt_model": obj.get("gpt_model") if obj.get("gpt_model") is not None else 'gpt-4-turbo',
            "image": obj.get("image")
        })
        return _obj


