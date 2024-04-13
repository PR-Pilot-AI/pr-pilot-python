# coding: utf-8

"""
    PR Pilot API

    API for creating PR Pilot tasks

    The version of the OpenAPI document: 1.2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pr_pilot.models.task import Task

class TestTask(unittest.TestCase):
    """Task unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Task:
        """Test Task
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Task`
        """
        model = Task()
        if include_optional:
            return Task(
                id = '',
                title = '',
                user_request = '',
                github_project = '',
                github_user = '',
                status = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                result = ''
            )
        else:
            return Task(
                id = '',
                title = '',
                github_project = '',
                github_user = '',
                status = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testTask(self):
        """Test Task"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
