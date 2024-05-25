import re
from datetime import datetime
from typing import Optional

import pyawsopstoolkit.models
from pyawsopstoolkit.__interfaces__ import ISession
from pyawsopstoolkit.__validations__ import Validation


class IAM:
    """
    A class that encapsulates insights related to the IAM service, including roles, users, and other entities.
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
        Validation.validate_type(session, ISession, 'session should be of Session type.')

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
        Validation.validate_type(value, ISession, 'session should be of Session type.')

        self._session = value

    def unused_roles(
            self,
            no_of_days: Optional[int] = 90,
            include_newly_created: Optional[bool] = False
    ) -> list[pyawsopstoolkit.models.IAMRole]:
        """
        Returns a list of unused IAM roles based on the specified parameters.
        :param no_of_days: The number of days (integer) to check if the IAM role has been used within the
        specified period. Defaults to 90 days.
        :type no_of_days: int
        :param include_newly_created: A flag indicating whether to include newly created IAM roles within the
        specified number of days. Defaults to False.
        :type include_newly_created: bool
        :return: A list of unused IAM roles.
        :rtype: list
        """
        Validation.validate_type(no_of_days, int, 'no_of_days should be an integer.')
        Validation.validate_type(include_newly_created, bool, 'include_newly_created should be a boolean.')

        from pyawsopstoolkit import advsearch

        current_date = datetime.today().replace(tzinfo=None)
        iam_object = advsearch.IAM(self.session)
        iam_roles = iam_object.search_roles(include_details=True)

        if iam_roles is None:
            return []

        def role_is_unused(_role):
            if _role.last_used is None:
                return True

            if (current_date - _role.last_used.used_date.replace(tzinfo=None)).days <= no_of_days:
                return False

            return True

        unused_roles_list = []

        for role in iam_roles:
            if not re.search(r'/aws-service-role/', role.path, re.IGNORECASE):
                if include_newly_created:
                    if role_is_unused(role):
                        unused_roles_list.append(role)
                else:
                    if (
                            (current_date - role.created_date.replace(tzinfo=None)).days > no_of_days
                            and role_is_unused(role)
                    ):
                        unused_roles_list.append(role)

        return unused_roles_list

    def unused_users(
            self,
            no_of_days: Optional[int] = 90,
            include_newly_created: Optional[bool] = False
    ) -> list[pyawsopstoolkit.models.IAMUser]:
        """
        Returns a list of unused IAM users based on the specified parameters.
        :param no_of_days: The number of days (integer) to check if the IAM user has been used within the
        specified period. Defaults to 90 days.
        :type no_of_days: int
        :param include_newly_created: A flag indicating whether to include newly created IAM users within the
        specified number of days. Defaults to False.
        :type include_newly_created: bool
        :return: A list of unused IAM users.
        :rtype: list
        """
        Validation.validate_type(no_of_days, int, 'no_of_days should be an integer.')
        Validation.validate_type(include_newly_created, bool, 'include_newly_created should be a boolean.')

        from pyawsopstoolkit import advsearch

        current_date = datetime.today().replace(tzinfo=None)
        iam_object = advsearch.IAM(self.session)
        iam_users = iam_object.search_users(include_details=True)

        if iam_users is None:
            return []

        def user_is_unused(_user):
            _last_login = None
            _access_key_last_used = None

            if _user.login_profile is not None:
                _last_login = _user.login_profile.created_date

            if _user.access_keys is not None:
                for _key in _user.access_keys:
                    _last_used_date = _key.last_used_date
                    if not _access_key_last_used or _last_used_date > _access_key_last_used:
                        _access_key_last_used = _last_used_date

            _password_last_used = _user.password_last_used_date

            _recent_activity_date: datetime = max(
                filter(None, [_last_login, _access_key_last_used, _password_last_used]), default=None
            )

            if _recent_activity_date is None:
                return True

            if (current_date - _recent_activity_date.replace(tzinfo=None)).days <= no_of_days:
                return False

            return True

        unused_users_list = []

        for user in iam_users:
            if include_newly_created:
                if user_is_unused(user):
                    unused_users_list.append(user)
            else:
                if (
                        (current_date - user.created_date.replace(tzinfo=None)).days > no_of_days
                        and user_is_unused(user)
                ):
                    unused_users_list.append(user)

        return unused_users_list
