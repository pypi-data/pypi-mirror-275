import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Any, Optional

import pyawsopstoolkit.models
from pyawsopstoolkit.__interfaces__ import IAccount, ISession
from pyawsopstoolkit.__validations__ import Validation
from pyawsopstoolkit.models import IAMUserLoginProfile, IAMUserAccessKey

MAX_WORKERS = 10

# This module supports various conditions for advanced searches, outlined below as global constants.
OR: str = 'OR'  # Represents the "or" condition
AND: str = 'AND'  # Represents the "and" condition

LESS_THAN: str = 'lt'  # Represents the less than ("<") value
LESS_THAN_OR_EQUAL_TO: str = 'lte'  # Represents the less than or equal to ("<=") value
GREATER_THAN: str = 'gt'  # Represents the greater than (">") value
GREATER_THAN_OR_EQUAL_TO: str = 'gte'  # Represents the greater than or equal to (">=") value
EQUAL_TO: str = 'eq'  # Represents the equal to ("=") value
NOT_EQUAL_TO: str = 'ne'  # Represents the not equal to ("!=") value
BETWEEN: str = 'between'  # Represents the between range ("< x <") value


def _match_condition(value: str, role_field: str | list, condition: str, matched: bool) -> bool:
    """
    Matches the condition based on the specified parameters.
    :param value: The value to be evaluated.
    :type value: str
    :param role_field: The value or list of values to compare against.
    :type role_field: str | list
    :param condition: The condition to be applied: 'OR' or 'AND'.
    :type condition: str
    :param matched: The current matching status.
    :type matched: bool
    :return: Returns a boolean value (True or False) based on the comparison.
    :rtype: bool
    """
    if not value or not role_field:
        return False

    if isinstance(role_field, str):
        role_field = [role_field]

    found_match = any(re.search(value, field, re.IGNORECASE) for field in role_field)

    if condition == OR:
        return matched or found_match
    elif condition == AND:
        return matched and found_match if matched else found_match

    return matched


def _match_compare_condition(value: dict, role_field: Any, condition: str, matched: bool) -> bool:
    """
    Matches the condition by comparing based on the specified parameters.
    :param value: The value to be evaluated.
    :type value: dict
    :param role_field: The value to compare against.
    :type role_field: Any
    :param condition: The condition to be applied: 'OR' or 'AND'.
    :type condition: str
    :param matched: The current matching status.
    :type matched: bool
    :return: Returns a boolean value (True or False) based on the comparison.
    :rtype: bool
    """
    match = True
    if isinstance(value, dict):
        for operator, compare_value in value.items():
            if isinstance(role_field, datetime) and isinstance(compare_value, str):
                compare_value = datetime.fromisoformat(compare_value).replace(tzinfo=None)

            if operator == LESS_THAN and not role_field < compare_value:
                match = False
            elif operator == LESS_THAN_OR_EQUAL_TO and not role_field <= compare_value:
                match = False
            elif operator == EQUAL_TO and not role_field == compare_value:
                match = False
            elif operator == NOT_EQUAL_TO and not role_field != compare_value:
                match = False
            elif operator == GREATER_THAN and not role_field > compare_value:
                match = False
            elif operator == GREATER_THAN_OR_EQUAL_TO and not role_field >= compare_value:
                match = False
            elif operator == BETWEEN:
                if not isinstance(compare_value, list) or len(compare_value) != 2:
                    raise ValueError('The "between" operator requires a list of two values.')
                if isinstance(role_field, datetime):
                    compare_value[0] = datetime.fromisoformat(compare_value[0]).replace(tzinfo=None)
                    compare_value[1] = datetime.fromisoformat(compare_value[1]).replace(tzinfo=None)
                if not (compare_value[0] <= role_field <= compare_value[1]):
                    match = False
    else:
        raise ValueError('Conditions should be specified as a dictionary with operators.')

    if condition == OR and match:
        return True
    elif condition == AND and not match:
        return False

    return matched


def _match_tag_condition(value, tags, condition: str, matched: bool, key_only: bool) -> bool:
    """
    Matches the condition based on the specified tags.
    :param value: The value to be evaluated.
    :type value: Any
    :param tags: The value to compare against.
    :type tags: Any
    :param condition: The condition to be applied: 'OR' or 'AND'.
    :type condition: str
    :param matched: The current matching status.
    :type matched: bool
    :param key_only: Flag to indicate to match just key or both key and value.
    :type key_only: bool
    :return: Returns a boolean value (True or False) based on the comparison.
    :rtype: bool
    """
    match = False
    if key_only:
        if value in tags:
            match = True
    else:
        match = True
        for key, val in value.items():
            if tags.get(key) != val:
                match = False
                break

    if not matched:
        return False

    if condition == "OR":
        return match
    elif condition == "AND":
        return match
    else:
        return matched


class IAM:
    """
    A class encapsulating advanced IAM-related search functionalities, facilitating the exploration of roles,
    users, and more.
    """

    def __init__(
            self,
            session: ISession
    ) -> None:
        """
        Initializes the constructor of the IAM class.
        :param session: An ISession object providing access to AWS services.
        :type session: ISession
        """
        Validation.validate_type(session, ISession, 'session should be of ISession type.')

        self._session = session

    @property
    def session(self) -> ISession:
        """
        Gets the ISession object which provides access to AWS services.
        :return: The ISession object which provide access to AWS services.
        :rtype: ISession
        """
        return self._session

    @session.setter
    def session(self, value: ISession) -> None:
        """
        Sets the ISession object which provides access to AWS services.
        :param value: The ISession object which provides access to AWS services.
        :type value: ISession
        """
        Validation.validate_type(value, ISession, 'session should be of ISession type.')

        self._session = value

    def _list_roles(self) -> list:
        """
        Utilizing boto3 IAM, this method retrieves a list of all roles leveraging the provided ISession object.
        Note: The returned dictionary excludes PermissionsBoundary, LastUsed, and Tags. For further details,
        please consult the official documentation:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_roles.html.
        :return: A list containing IAM roles.
        :rtype: list
        """
        roles_to_process = []

        from botocore.exceptions import ClientError
        try:
            iam_client = self.session.get_session().client('iam')
            iam_paginator = iam_client.get_paginator('list_roles')

            for page in iam_paginator.paginate():
                roles_to_process.extend(page.get('Roles', []))
        except ClientError as e:
            raise e

        return roles_to_process

    def _list_users(self) -> list:
        """
        Utilizing boto3 IAM, this method retrieves a list of all users leveraging the provided ISession object.
        Note: The returned dictionary excludes PermissionsBoundary and Tags. For further details,
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/list_users.html.
        :return: A list containing IAM users.
        :rtype: list
        """
        users_to_process = []

        from botocore.exceptions import ClientError
        try:
            iam_client = self.session.get_session().client('iam')
            iam_paginator = iam_client.get_paginator('list_users')

            for page in iam_paginator.paginate():
                users_to_process.extend(page.get('Users', []))
        except ClientError as e:
            raise e

        return users_to_process

    def _list_access_keys(self, user_name: str) -> list:
        """
        Utilizing boto3 IAM, this method retrieves a list of all access keys associated with IAM user leveraging the
        provided ISession object. For further details,
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/paginator/ListAccessKeys.html
        :return: A list containing IAM user access keys.
        :rtype: list
        """
        access_keys_to_process = []

        from botocore.exceptions import ClientError
        try:
            iam_client = self.session.get_session().client('iam')
            iam_paginator = iam_client.get_paginator('list_access_keys')

            for page in iam_paginator.paginate(UserName=user_name):
                access_keys_to_process.extend(page.get('AccessKeyMetadata', []))
        except ClientError as e:
            raise e

        return access_keys_to_process

    def _get_role(self, role_name: str) -> dict:
        """
        Utilizing boto3 IAM, this method retrieves comprehensive details of an IAM role identified by the
        specified role name.
        :return: Details of the IAM role.
        :rtype: dict
        """
        from botocore.exceptions import ClientError
        try:
            iam_client = self.session.get_session().client('iam')
            return iam_client.get_role(RoleName=role_name)
        except ClientError as e:
            raise e

    def _get_user(self, user_name: str) -> dict:
        """
        Utilizing boto3 IAM, this method retrieves comprehensive details of an IAM user identified by the
        specified username.
        :return: Details of the IAM user.
        :rtype: dict
        """
        from botocore.exceptions import ClientError
        try:
            iam_client = self.session.get_session().client('iam')
            return iam_client.get_user(UserName=user_name)
        except ClientError as e:
            raise e

    def _get_login_profile(self, user_name: str) -> dict:
        """
        Utilizing boto3 IAM, this method retrieves comprehensive details of an IAM user login profile identified
        by the specified username.
        :return: Details of the IAM user login profile.
        :rtype: dict
        """
        from botocore.exceptions import ClientError
        try:
            iam_client = self.session.get_session().client('iam')
            return iam_client.get_login_profile(UserName=user_name)
        except ClientError as e:
            raise e

    def _get_access_key_last_used(self, access_key_id: str) -> dict:
        """
        Utilizing boto3 IAM, this method retrieves comprehensive details of IAM user access key last used information
        identified by the specified username.
        :return: Details of the IAM user access key last used.
        :rtype: dict
        """
        from botocore.exceptions import ClientError
        try:
            iam_client = self.session.get_session().client('iam')
            return iam_client.get_access_key_last_used(AccessKeyId=access_key_id)
        except ClientError as e:
            raise e

    @staticmethod
    def _convert_to_iam_role(account: IAccount, role: dict) -> pyawsopstoolkit.models.IAMRole:
        """
        This function transforms the dictionary response from boto3 IAM into a format compatible with the
        AWS Ops Toolkit, adhering to the pyawsopstoolkit.models structure. Additionally, it incorporates
        account-related summary information into the IAM role details.
        :param account: An IAccount object containing AWS account information.
        :type account: IAccount
        :param role: The boto3 IAM service response for an IAM role.
        :type role: dict
        :return: An AWS Ops Toolkit compatible object containing all IAM role details.
        :rtype: IAMRole
        """
        iam_role = pyawsopstoolkit.models.IAMRole(
            account=account,
            name=role.get('RoleName', ''),
            id=role.get('RoleId', ''),
            arn=role.get('Arn', ''),
            max_session_duration=role.get('MaxSessionDuration', 0),
            path=role.get('Path', ''),
            created_date=role.get('CreateDate', None),
            assume_role_policy_document=role.get('AssumeRolePolicyDocument', None),
            description=role.get('Description', None)
        )

        _permissions_boundary = role.get('PermissionsBoundary', {})
        if _permissions_boundary:
            boundary = pyawsopstoolkit.models.IAMPermissionsBoundary(
                type=_permissions_boundary.get('PermissionsBoundaryType', ''),
                arn=_permissions_boundary.get('PermissionsBoundaryArn', '')
            )
            iam_role.permissions_boundary = boundary

        _last_used = role.get('RoleLastUsed', {})
        if _last_used:
            last_used = pyawsopstoolkit.models.IAMRoleLastUsed(
                used_date=_last_used.get('LastUsedDate', None),
                region=_last_used.get('Region', None)
            )
            iam_role.last_used = last_used

        _tags = role.get('Tags', [])
        if _tags:
            iam_role.tags = _tags

        return iam_role

    @staticmethod
    def _convert_to_iam_user(
            account: IAccount,
            user: dict,
            login_profile: Optional[dict] = None,
            access_keys: Optional[list] = None
    ) -> pyawsopstoolkit.models.IAMUser:
        """
        This function transforms the dictionary response from boto3 IAM into a format compatible with the
        AWS Ops Toolkit, adhering to the pyawsopstoolkit.models structure. Additionally, it incorporates
        account-related summary information into the IAM user details.
        :param account: An IAccount object containing AWS account information.
        :type account: IAccount
        :param user: The boto3 IAM service response for an IAM user.
        :type user: dict
        :param login_profile: The boto3 IAM login profile service response for an IAM user.
        :type login_profile: dict
        :param access_keys: The boto3 IAM access keys service response for an IAM user.
        :type access_keys: list
        :return: An AWS Ops Toolkit compatible object containing all IAM user details.
        :rtype: IAMUser
        """
        iam_user = pyawsopstoolkit.models.IAMUser(
            account=account,
            name=user.get('UserName', ''),
            id=user.get('UserId', ''),
            arn=user.get('Arn', ''),
            path=user.get('Path', ''),
            created_date=user.get('CreateDate', None),
            password_last_used_date=user.get('PasswordLastUsed', None)
        )

        _permissions_boundary = user.get('PermissionsBoundary', {})
        if _permissions_boundary:
            boundary = pyawsopstoolkit.models.IAMPermissionsBoundary(
                type=_permissions_boundary.get('PermissionsBoundaryType', ''),
                arn=_permissions_boundary.get('PermissionsBoundaryArn', '')
            )
            iam_user.permissions_boundary = boundary

        if login_profile is not None:
            _login_profile = IAMUserLoginProfile(
                created_date=login_profile.get('CreateDate', None),
                password_reset_required=login_profile.get('PasswordResetRequired', False)
            )
            iam_user.login_profile = _login_profile

        if access_keys is not None:
            for a_key in access_keys:
                _access_key = IAMUserAccessKey(
                    id=a_key.get('access_key', {}).get('AccessKeyId', ''),
                    status=a_key.get('access_key', {}).get('Status', ''),
                    created_date=a_key.get('access_key', {}).get('CreateDate', None),
                    last_used_date=a_key.get('last_used', {}).get('AccessKeyLastUsed', {}).get('LastUsedDate', None),
                    last_used_service=a_key.get('last_used', {}).get('AccessKeyLastUsed', {}).get('ServiceName', None),
                    last_used_region=a_key.get('last_used', {}).get('AccessKeyLastUsed', {}).get('Region', None)
                )
                if iam_user.access_keys is None:
                    iam_user.access_keys = [_access_key]
                else:
                    iam_user.access_keys.append(_access_key)

        _tags = user.get('Tags', [])
        if _tags:
            iam_user.tags = _tags

        return iam_user

    def search_roles(
            self,
            condition: str = OR,
            include_details: bool = False,
            **kwargs
    ) -> list[pyawsopstoolkit.models.IAMRole]:
        """
        Returns a list of IAM roles using advanced search features supported by the specified arguments.
        For details on supported kwargs, please refer to the readme document.
        :param condition: The condition to be applied: 'OR' or 'AND'.
        :type condition: str
        :param include_details: Flag to indicate to include additional details of the IAM role.
        This includes information about permissions boundary, last used, and tags. Default is False.
        :type include_details: bool
        :param kwargs: Key-based arguments defining search criteria.
        :return: A list of IAM roles.
        :rtype: list
        """
        Validation.validate_type(condition, str, 'condition should be a string and should be either "OR" or "AND".')
        Validation.validate_type(include_details, bool, 'include_details should be a boolean.')

        def _process_role(role_detail):
            if include_details:
                role_detail = self._get_role(role_detail.get('RoleName', '')).get('Role', {})

            return self._convert_to_iam_role(self.session.get_account(), role_detail)

        def _match_role(role_detail):
            if role_detail:
                matched = False if condition == OR else True
                for key, value in kwargs.items():
                    if value is not None:
                        role_field = ''
                        if key.lower() == 'path':
                            role_field = role_detail.get('Path', '')
                        elif key.lower() == 'name':
                            role_field = role_detail.get('RoleName', '')
                        elif key.lower() == 'id':
                            role_field = role_detail.get('RoleId', '')
                        elif key.lower() == 'arn':
                            role_field = role_detail.get('Arn', '')
                        elif key.lower() == 'description':
                            role_field = role_detail.get('Description', '')
                        elif key.lower() == 'permissions_boundary_type':
                            if include_details:
                                role_detail = self._get_role(role_detail.get('RoleName', '')).get('Role', {})
                                _permissions_boundary = role_detail.get('PermissionsBoundary', {})
                                role_field = _permissions_boundary.get('PermissionsBoundaryType', '')
                        elif key.lower() == 'permissions_boundary_arn':
                            if include_details:
                                role_detail = self._get_role(role_detail.get('RoleName', '')).get('Role', {})
                                _permissions_boundary = role_detail.get('PermissionsBoundary', {})
                                role_field = _permissions_boundary.get('PermissionsBoundaryArn', '')
                        elif key.lower() == 'max_session_duration':
                            role_field = role_detail.get('MaxSessionDuration', 0)
                            matched = _match_compare_condition(value, role_field, condition, matched)
                        elif key.lower() == 'created_date':
                            role_field = role_detail.get('CreateDate', None)
                            if isinstance(role_field, datetime):
                                role_field = role_field.replace(tzinfo=None)
                                matched = _match_compare_condition(value, role_field, condition, matched)
                        elif key.lower() == 'last_used_date':
                            if include_details:
                                role_detail = self._get_role(role_detail.get('RoleName', '')).get('Role', {})
                                _last_used = role_detail.get('RoleLastUsed', {})
                                role_field = _last_used.get('LastUsedDate', None)
                                if isinstance(role_field, datetime):
                                    role_field = role_field.replace(tzinfo=None)
                                    matched = _match_compare_condition(value, role_field, condition, matched)
                        elif key.lower() == 'last_used_region':
                            if include_details:
                                role_detail = self._get_role(role_detail.get('RoleName', '')).get('Role', {})
                                _last_used = role_detail.get('RoleLastUsed', {})
                                role_field = _last_used.get('Region', '')
                        elif key.lower() == 'tag_key':
                            if include_details:
                                role_detail = self._get_role(role_detail.get('RoleName', '')).get('Role', {})
                                tags = {tag['Key']: tag['Value'] for tag in role_detail.get('Tags', [])}
                                matched = _match_tag_condition(value, tags, condition, matched, key_only=True)
                        elif key.lower() == 'tag':
                            if include_details:
                                role_detail = self._get_role(role_detail.get('RoleName', '')).get('Role', {})
                                tags = {tag['Key']: tag['Value'] for tag in role_detail.get('Tags', [])}
                                matched = _match_tag_condition(value, tags, condition, matched, key_only=False)

                        if key.lower() not in [
                            'max_session_duration', 'created_date', 'last_used_date', 'tag_key', 'tag'
                        ]:
                            matched = _match_condition(value, role_field, condition, matched)

                        if (condition == OR and matched) or (condition == AND and not matched):
                            break

                if matched:
                    return _process_role(role_detail)

        roles_to_return = []

        from botocore.exceptions import ClientError
        try:
            include_details_keys = {
                'permissions_boundary_type',
                'permissions_boundary_arn',
                'last_used_date',
                'last_used_region',
                'tag',
                'tag_key'
            }

            if not include_details and any(k in include_details_keys for k in kwargs):
                from pyawsopstoolkit.exceptions import SearchAttributeError
                raise SearchAttributeError(
                    f'include_details is required for below keys: {", ".join(sorted(include_details_keys))}'
                )

            roles_to_process = self._list_roles()

            if len(kwargs) == 0:
                with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                    future_to_role = {executor.submit(_process_role, role): role for role in roles_to_process}
                    for future in as_completed(future_to_role):
                        role_result = future.result()
                        if role_result is not None:
                            roles_to_return.append(role_result)
            else:
                with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                    future_to_role = {executor.submit(_match_role, role): role for role in roles_to_process}
                    for future in as_completed(future_to_role):
                        role_result = future.result()
                        if role_result is not None:
                            roles_to_return.append(role_result)
        except ClientError as e:
            raise e

        return roles_to_return

    def search_users(
            self,
            condition: str = OR,
            include_details: bool = False,
            **kwargs
    ) -> list[pyawsopstoolkit.models.IAMUser]:
        """
        Returns a list of IAM users using advanced search feature supported by the specified arguments.
        For details on supported kwargs, please refer to the readme document.
        :param condition: The condition to be applied: 'OR' or 'AND'.
        :type condition: str
        :param include_details: Flag to indicate to include additional details of the IAM user.
        This includes information about permissions boundary and tags. Default is False.
        :type include_details: bool
        :param kwargs: Key-based arguments defining search criteria.
        :return: A list of IAM users.
        :rtype: list
        """
        Validation.validate_type(condition, str, 'condition should be a string and should be either "OR" or "AND".')
        Validation.validate_type(include_details, bool, 'include_details should be a boolean.')

        def _process_user(user_detail):
            login_profile_detail = None
            access_keys_detail = []

            if include_details:
                user_detail = self._get_user(user_detail.get('UserName', '')).get('User', {})
                login_profile_detail = self._get_login_profile(user_detail.get('UserName', '')).get('LoginProfile', {})
                for a_key in self._list_access_keys(user_detail.get('UserName', '')):
                    a_key_last_used = self._get_access_key_last_used(a_key.get('AccessKeyId', ''))
                    access_keys_detail.append({
                        'access_key': a_key,
                        'last_used': a_key_last_used
                    })

            return self._convert_to_iam_user(
                self.session.get_account(), user_detail, login_profile_detail, access_keys_detail
            )

        def _match_user(user_detail):
            if user_detail:
                matched = False if condition == OR else True
                for key, value in kwargs.items():
                    if value is not None:
                        user_field = ''
                        if key.lower() == 'path':
                            user_field = user_detail.get('Path', '')
                        elif key.lower() == 'name':
                            user_field = user_detail.get('UserName', '')
                        elif key.lower() == 'id':
                            user_field = user_detail.get('UserId', '')
                        elif key.lower() == 'arn':
                            user_field = user_detail.get('Arn', '')
                        elif key.lower() == 'created_date':
                            user_field = user_detail.get('CreateDate', None)
                            if isinstance(user_field, datetime):
                                user_field = user_field.replace(tzinfo=None)
                                matched = _match_compare_condition(value, user_field, condition, matched)
                        elif key.lower() == 'password_last_used_date':
                            user_field = user_detail.get('PasswordLastUsed', None)
                            if isinstance(user_field, datetime):
                                user_field = user_field.replace(tzinfo=None)
                                matched = _match_compare_condition(value, user_field, condition, matched)
                        elif key.lower() == 'permissions_boundary_type':
                            if include_details:
                                user_detail = self._get_role(user_detail.get('UserName', '')).get('User', {})
                                _permissions_boundary = user_detail.get('PermissionsBoundary', {})
                                user_field = _permissions_boundary.get('PermissionsBoundaryType', '')
                        elif key.lower() == 'permissions_boundary_arn':
                            if include_details:
                                user_detail = self._get_user(user_detail.get('UserName', '')).get('User', {})
                                _permissions_boundary = user_detail.get('PermissionsBoundary', {})
                                user_field = _permissions_boundary.get('PermissionsBoundaryArn', '')
                        elif key.lower() == 'tag_key':
                            if include_details:
                                user_detail = self._get_user(user_detail.get('UserName', '')).get('User', {})
                                tags = {tag['Key']: tag['Value'] for tag in user_detail.get('Tags', [])}
                                matched = _match_tag_condition(value, tags, condition, matched, key_only=True)
                        elif key.lower() == 'tag':
                            if include_details:
                                user_detail = self._get_user(user_detail.get('UserName', '')).get('User', {})
                                tags = {tag['Key']: tag['Value'] for tag in user_detail.get('Tags', [])}
                                matched = _match_tag_condition(value, tags, condition, matched, key_only=False)
                        elif key.lower() == 'login_profile_created_date':
                            if include_details:
                                login_profile_detail = (
                                    self._get_login_profile(user_detail.get('UserName', '')).get('LoginProfile', {})
                                )
                                user_field = login_profile_detail.get('CreateDate', None)
                                if isinstance(user_field, datetime):
                                    user_field = user_field.replace(tzinfo=None)
                                    matched = _match_compare_condition(value, user_field, condition, matched)
                        elif key.lower() == 'login_profile_password_reset_required':
                            if include_details:
                                login_profile_detail = (
                                    self._get_login_profile(user_detail.get('UserName', '')).get('LoginProfile', {})
                                )
                                user_field = login_profile_detail.get('PasswordResetRequired', False)
                        elif key.lower() == 'access_key_id':
                            if include_details:
                                user_field = []
                                for access_key in self._list_access_keys(user_detail.get('UserName', '')):
                                    user_field.append(access_key.get('AccessKeyId', ''))
                        elif key.lower() == 'access_key_status':
                            if include_details:
                                user_field = []
                                for access_key in self._list_access_keys(user_detail.get('UserName', '')):
                                    user_field.append(access_key.get('Status', ''))
                        elif key.lower() == 'access_key_service':
                            if include_details:
                                user_field = []
                                for access_key in self._list_access_keys(user_detail.get('UserName', '')):
                                    detail = self._get_access_key_last_used(access_key.get('AccessKeyId', ''))
                                    if detail is not None:
                                        user_field.append(detail.get('AccessKeyLastUsed', {}).get('ServiceName', ''))
                        elif key.lower() == 'access_key_region':
                            if include_details:
                                user_field = []
                                for access_key in self._list_access_keys(user_detail.get('UserName', '')):
                                    detail = self._get_access_key_last_used(access_key.get('AccessKeyId', ''))
                                    if detail is not None:
                                        user_field.append(detail.get('AccessKeyLastUsed', {}).get('Region', ''))

                        if key.lower() not in [
                            'created_date', 'password_last_used_date', 'tag_key', 'tag', 'login_profile_created_date'
                        ]:
                            matched = _match_condition(value, user_field, condition, matched)

                        if (condition == OR and matched) or (condition == AND and not matched):
                            break

                if matched:
                    return _process_user(user_detail)

        users_to_return = []

        from botocore.exceptions import ClientError
        try:
            include_details_keys = {
                'permissions_boundary_type',
                'permissions_boundary_arn',
                'tag',
                'tag_key',
                'login_profile_created_date',
                'login_profile_password_reset_required',
                'access_key_id',
                'access_key_status',
                'access_key_service',
                'access_key_region'
            }

            if not include_details and any(k in include_details_keys for k in kwargs):
                from pyawsopstoolkit.exceptions import SearchAttributeError
                raise SearchAttributeError(
                    f'include_details is required for below keys: {", ".join(sorted(include_details_keys))}'
                )

            users_to_process = self._list_users()

            if len(kwargs) == 0:
                with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                    future_to_user = {executor.submit(_process_user, user): user for user in users_to_process}
                    for future in as_completed(future_to_user):
                        user_result = future.result()
                        if user_result is not None:
                            users_to_return.append(user_result)
            else:
                with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                    future_to_user = {executor.submit(_match_user, user): user for user in users_to_process}
                    for future in as_completed(future_to_user):
                        user_result = future.result()
                        if user_result is not None:
                            users_to_return.append(user_result)
        except ClientError as e:
            raise e

        return users_to_return
