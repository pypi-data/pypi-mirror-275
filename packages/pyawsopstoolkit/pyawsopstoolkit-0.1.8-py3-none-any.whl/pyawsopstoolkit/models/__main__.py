from datetime import datetime
from typing import Optional, Union

from pyawsopstoolkit.__interfaces__ import IAccount
from pyawsopstoolkit.__validations__ import Validation
from pyawsopstoolkit.validators import ArnValidator, Validator


class IAMPermissionsBoundary:
    """
    A class representing an IAM role permissions boundary.
    """

    def __init__(
            self,
            type: str,
            arn: str
    ) -> None:
        """
        Initialize the IAMPermissionsBoundary object.
        :param type: The type of the permissions boundary.
        :type type: str
        :param arn: The Amazon Resource Name (ARN) of the permissions boundary.
        :type arn: str
        """
        Validation.validate_type(type, str, 'type should be a string.')
        ArnValidator.arn(arn, True)

        self._type = type
        self._arn = arn

    @property
    def arn(self) -> str:
        """
        Gets the ARN of the permissions boundary.
        :return: The ARN of the permissions boundary.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, value: str) -> None:
        """
        Sets the ARN of the permissions boundary.
        :param value: The new ARN of the permissions boundary.
        :type value: str
        """
        ArnValidator.arn(value, True)
        self._arn = value

    @property
    def type(self) -> str:
        """
        Gets the type of the permissions boundary.
        :return: The type of the permissions boundary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        """
        Sets the type of the permissions boundary.
        :param value: The new type of the permissions boundary.
        :type value: str
        """
        Validation.validate_type(type, str, 'type should be a string.')
        self._type = value

    def __str__(self) -> str:
        """
        Return a string representation of the IAMPermissionsBoundary object.
        :return: String representation of the IAMPermissionsBoundary object.
        :rtype: str
        """
        return (
            f'PermissionsBoundary('
            f'type="{self.type}",'
            f'arn="{self.arn}"'
            f')'
        )

    def __dict__(self) -> dict:
        """
        Return a dictionary representation of the IAMPermissionsBoundary object.
        :return: Dictionary representation of the IAMPermissionsBoundary object.
        :rtype: dict
        """
        return {
            "type": self.type,
            "arn": self.arn
        }


class IAMRoleLastUsed:
    """
    A class representing the last used information of an IAM role.
    """

    def __init__(
            self,
            used_date: Optional[datetime] = None,
            region: Optional[str] = None
    ) -> None:
        """
        Initializes the IAMRoleLastUsed instance with optional used_date and region.
        :param used_date: The last date and time the IAM role was used.
        :type used_date: datetime
        :param region: The AWS region where the IAM role was last used.
        :type region: str
        """
        Validation.validate_type(used_date, Union[datetime, None], 'used_date should be a datetime.')

        if region is not None:
            Validator.region(region, True)

        self._used_date = used_date
        self._region = region

    @property
    def region(self) -> Optional[str]:
        """
        Gets the AWS region where the IAM role was last used.
        :return: The AWS region where the IAM role was last used.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, value: Optional[str]) -> None:
        """
        Sets the AWS region where the IAM role was last used.
        :param value: The AWS region to set.
        :type value: str
        """
        Validator.region(value, True)
        self._region = value

    @property
    def used_date(self) -> Optional[datetime]:
        """
        Gets the last date and time the IAM role was used.
        :return: The last date and time the IAM role was used.
        :rtype: datetime
        """
        return self._used_date

    @used_date.setter
    def used_date(self, value: Optional[datetime]) -> None:
        """
        Sets the last date and time the IAM role was used.
        :param value: The last date and time to set.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'used_date should be a datetime.')
        self._used_date = value

    def __str__(self) -> str:
        """
        Returns a string representation of the IAMRoleLastUsed instance.
        :return: String representation of the IAMRoleLastUsed instance.
        :rtype: str
        """
        used_date = self.used_date.isoformat() if self.used_date else None
        region = self.region if self.region else None

        return (
            f'LastUsed('
            f'used_date={used_date},'
            f'region="{region}"'
            f')'
        )

    def __dict__(self) -> dict:
        """
        Returns a dictionary representation of the IAMRoleLastUsed instance.
        :return: Dictionary representation of the IAMRoleLastUsed instance.
        :rtype: dict
        """
        used_date = self.used_date.isoformat() if self.used_date else None
        region = self.region if self.region else None

        return {
            "used_date": used_date,
            "region": region
        }


class IAMUserLoginProfile:
    """
    A class representing the login profile information of an IAM user.
    """

    def __init__(
            self,
            created_date: Optional[datetime] = None,
            password_reset_required: Optional[bool] = False
    ) -> None:
        """
        Initialize the IAMUserLoginProfile object.
        :param created_date: The created date of the IAM user login profile.
        :type created_date: datetime
        :param password_reset_required: Flag to indicate if password reset required for the IAM user. Defaults to False.
        :type password_reset_required: bool
        """
        Validation.validate_type(created_date, Union[datetime, None], 'created_date should be a datetime.')
        Validation.validate_type(password_reset_required, bool, 'password_reset_required should be a boolean.')

        self._created_date = created_date
        self._password_reset_required = password_reset_required

    @property
    def created_date(self) -> Optional[datetime]:
        """
        Gets the created date of the IAM user login profile.
        :return: The created date of the IAM user login profile.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, value: Optional[datetime]) -> None:
        """
        Sets the created date of the IAM user login profile.
        :param value: The created date of the IAM user login profile.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'created_date should be a datetime.')

        self._created_date = value

    @property
    def password_reset_required(self) -> Optional[bool]:
        """
        Gets the flag to indicate if password reset required for the IAM user.
        :return: Flag to indicate if password reset required for the IAM user.
        :rtype: bool
        """
        return self._password_reset_required

    @password_reset_required.setter
    def password_reset_required(self, value: Optional[bool] = False) -> None:
        """
        Sets the flag to indicate if password reset required for the IAM user.
        :param value: The flag to indicate if password reset required for the IAM user. Defaults to False.
        :type value: bool
        """
        Validation.validate_type(value, bool, 'password_reset_required should be a boolean.')

        self._password_reset_required = value

    def __str__(self) -> str:
        """
        Return a string representation of the IAMUserLoginProfile object.
        :return: String representation of the IAMUserLoginProfile object.
        :rtype: str
        """
        created_date = self.created_date.isoformat() if self.created_date else None

        return (
            f'IAMUserLoginProfile('
            f'created_date={created_date},'
            f'password_reset_required={self.password_reset_required}'
            f')'
        )

    def __dict__(self) -> dict:
        """
        Return a dictionary representation of the IAMUserLoginProfile object.
        :return: Dictionary representation of the IAMUserLoginProfile object.
        :rtype: dict
        """
        created_date = self.created_date.isoformat() if self.created_date else None

        return {
            "created_date": created_date,
            "password_reset_required": self.password_reset_required
        }


class IAMUserAccessKey:
    """
    A class representing the access key information of an IAM user.
    """

    def __init__(
            self,
            id: str,
            status: str,
            created_date: Optional[datetime] = None,
            last_used_date: Optional[datetime] = None,
            last_used_service: Optional[str] = None,
            last_used_region: Optional[str] = None
    ) -> None:
        """
        Initializes the IAMUserAccessKey instance.
        :param id: The ID of the IAM user access key.
        :type id: str
        :param status: The status of the IAM user access key.
        :type status: str
        :param created_date: The created date of the IAM user access key. Defaults to None.
        :type created_date: datetime
        :param last_used_date: The last used date of the IAM user access key. Defaults to None.
        :type last_used_date: datetime
        :param last_used_service: The last used service of the IAM user access key. Defaults to None.
        :type last_used_service: str
        :param last_used_region: The last used region of the IAM user access key. Defaults to None.
        :type last_used_region: str
        """
        Validation.validate_type(id, str, 'id should be a string.')
        Validation.validate_type(status, str, 'status should be a string.')
        Validation.validate_type(created_date, Union[datetime, None], 'created_date should be a datetime.')
        Validation.validate_type(last_used_date, Union[datetime, None], 'last_used_date should be a datetime.')
        Validation.validate_type(last_used_service, Union[str, None], 'last_used_service should be a string.')
        if last_used_region is not None:
            Validator.region(last_used_region)

        self._id = id
        self._status = status
        self._created_date = created_date
        self._last_used_date = last_used_date
        self._last_used_service = last_used_service
        self._last_used_region = last_used_region

    @property
    def created_date(self) -> Optional[datetime]:
        """
        Gets the created date of the IAM user access key.
        :return: The created date of the IAM user access key.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, value: Optional[datetime]) -> None:
        """
        Sets the created date of the IAM user access key.
        :param value: The created date of the IAM user access key.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'created_date should be a datetime.')

        self._created_date = value

    @property
    def id(self) -> str:
        """
        Gets the ID of the IAM user access key.
        :return: The ID of the IAM user access key.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the ID of the IAM user access key.
        :param value: The ID of the IAM user access key.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')

        self._id = value

    @property
    def last_used_date(self) -> Optional[datetime]:
        """
        Gets the last used date of the IAM user access key.
        :return: The last used date of the IAM user access key.
        :rtype: datetime
        """
        return self._last_used_date

    @last_used_date.setter
    def last_used_date(self, value: Optional[datetime]) -> None:
        """
        Sets the last used date of the IAM user access key.
        :param value: The last used date of the IAM user access key.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'last_used_date should be a datetime.')

        self._last_used_date = value

    @property
    def last_used_region(self) -> Optional[str]:
        """
        Gets the last used region of the IAM user access key.
        :return: The last used region of the IAM user access key.
        :rtype: str
        """
        return self._last_used_region

    @last_used_region.setter
    def last_used_region(self, value: Optional[str]) -> None:
        """
        Sets the last used region of the IAM user access key.
        :param value: The last used region of the IAM user access key.
        :type value: str
        """
        if value is not None:
            Validator.region(value)

        self._last_used_region = value

    @property
    def last_used_service(self) -> Optional[str]:
        """
        Gets the last used service of the IAM user access key.
        :return: The last used service of the IAM user access key.
        :rtype: str
        """
        return self._last_used_service

    @last_used_service.setter
    def last_used_service(self, value: Optional[str]) -> None:
        """
        Sets the last used service of the IAM user access key.
        :param value: The last used service of the IAM user access key.
        :type value: str
        """
        Validation.validate_type(value, Union[str, None], 'last_used_service should be a string.')

        self._last_used_service = value

    @property
    def status(self) -> str:
        """
        Gets the status of the IAM user access key.
        :return: The status of the IAM user access key.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        """
        Sets the status of the IAM user access key.
        :param value: The status of the IAM user access key.
        :type value: str
        """
        Validation.validate_type(value, str, 'status should be a string.')

        self._status = value

    def __str__(self) -> str:
        """
        Return a string representation of the IAMUserAccessKey object.
        :return: String representation of the IAMUserAccessKey object.
        :rtype: str
        """
        created_date = self.created_date.isoformat() if self.created_date else None
        last_used_date = self.last_used_date.isoformat() if self._last_used_date else None

        return (
            f'IAMUserAccessKey('
            f'id={self.id},'
            f'status={self.status},'
            f'created_date={created_date},'
            f'last_used_date={last_used_date},'
            f'last_used_service={self.last_used_service},'
            f'last_used_region={self.last_used_region}'
            f')'
        )

    def __dict__(self) -> dict:
        """
        Return a dictionary representation of the IAMUserAccessKey object.
        :return: Dictionary representation of the IAMUserAccessKey object.
        :rtype: dict
        """
        created_date = self.created_date.isoformat() if self.created_date else None
        last_used_date = self.last_used_date.isoformat() if self._last_used_date else None

        return {
            "id": self.id,
            "status": self.status,
            "created_date": created_date,
            "last_used_date": last_used_date,
            "last_used_service": self.last_used_service,
            "last_used_region": self.last_used_region
        }


class IAMRole:
    """
    A class representing an IAM role.
    """

    def __init__(
            self,
            account: IAccount,
            name: str,
            id: str,
            arn: str,
            max_session_duration: int,
            path: str = '/',
            created_date: Optional[datetime] = None,
            assume_role_policy_document: Optional[dict] = None,
            description: Optional[str] = None,
            permissions_boundary: Optional[IAMPermissionsBoundary] = None,
            last_used: Optional[IAMRoleLastUsed] = None,
            tags: Optional[list] = None
    ) -> None:
        """
        Initialize a new IAMRole instance.
        :param account: The account associated with the IAM role.
        :type account: IAccount
        :param name: The name of the IAM role.
        :type name: str
        :param id: The unique identifier of the IAM role.
        :type id: str
        :param arn: The Amazon Resource Name (ARN) of the IAM role.
        :type arn: str
        :param max_session_duration: The maximum session duration for the IAM role.
        :type max_session_duration: int
        :param path: The path for the IAM role. Defaults to '/'.
        :type path: str
        :param created_date: The creation date of the IAM role. Defaults to None.
        :type created_date: datetime
        :param assume_role_policy_document: The policy document for assuming the IAM role. Defaults to None.
        :type assume_role_policy_document: dict
        :param description: A description of the IAM role. Defaults to None.
        :type description: str
        :param permissions_boundary: The permissions boundary for the IAM role. Defaults to None.
        :type permissions_boundary: IAMPermissionsBoundary
        :param last_used: Information about the last time the IAM role was used. Defaults to None.
        :type last_used: IAMRoleLastUsed
        :param tags: A list of tags associated with the IAM role. Defaults to None.
        :type tags: list
        """
        Validation.validate_type(account, IAccount, 'account should be of Account type.')
        Validation.validate_type(name, str, 'name should be a string.')
        Validation.validate_type(id, str, 'id should be a string.')
        ArnValidator.arn(arn, True)
        Validation.validate_type(max_session_duration, int, 'max_session_duration should be an integer.')
        Validation.validate_type(path, str, 'path should be a string.')
        Validation.validate_type(created_date, Union[datetime, None], 'created_date should be a datetime.')
        Validation.validate_type(
            assume_role_policy_document, Union[dict, None], 'assume_role_policy_document should be a dictionary.'
        )
        Validation.validate_type(description, Union[str, None], 'description should be a string.')
        Validation.validate_type(
            permissions_boundary,
            Union[IAMPermissionsBoundary, None],
            'permissions_boundary should be of IAMPermissionsBoundary type.'
        )
        Validation.validate_type(
            last_used, Union[IAMRoleLastUsed, None], 'last_used should be of IAMRoleLastUsed type.'
        )
        Validation.validate_type(tags, Union[list, None], 'tags should be a list.')

        self._account = account
        self._name = name
        self._id = id
        self._arn = arn
        self._max_session_duration = max_session_duration
        self._path = path
        self._created_date = created_date
        self._assume_role_policy_document = assume_role_policy_document
        self._description = description
        self._permissions_boundary = permissions_boundary
        self._last_used = last_used
        self._tags = tags

    @property
    def account(self) -> IAccount:
        """
        Gets the account associated with the IAM role.
        :return: The account associated with the IAM role.
        :rtype: IAccount
        """
        return self._account

    @account.setter
    def account(self, value: IAccount) -> None:
        """
        Sets the account associated with the IAM role.
        :param value: The account to be associated with the IAM role.
        :type value: IAccount
        """
        Validation.validate_type(value, IAccount, 'account should be of Account type.')
        self._account = value

    @property
    def arn(self) -> str:
        """
        Gets the ARN of the IAM role.
        :return: The ARN of the IAM role.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, value: str) -> None:
        """
        Sets the ARN of the IAM role.
        :param value: The ARN of the IAM role.
        :type value: str
        """
        ArnValidator.arn(value, True)
        self._arn = value

    @property
    def assume_role_policy_document(self) -> Optional[dict]:
        """
        Gets the trust relationship (or) assume role policy document associated with the IAM role.
        :return: The trust relationship (or) assume role policy document associated with the IAM role.
        :rtype: dict
        """
        return self._assume_role_policy_document

    @assume_role_policy_document.setter
    def assume_role_policy_document(self, value: Optional[dict] = None) -> None:
        """
        Sets the trust relationship (or) assume role policy document associated with the IAM role.
        :param value: The trust relationship (or) assume role policy document associated with the IAM role.
        :type value: dict
        """
        Validation.validate_type(value, Union[dict, None], 'assume_role_policy_document should be a dictionary.')
        self._assume_role_policy_document = value

    @property
    def created_date(self) -> Optional[datetime]:
        """
        Gets the created date of the IAM role.
        :return: The created date of the IAM role.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, value: Optional[datetime] = None) -> None:
        """
        Sets the created date of the IAM role.
        :param value: The created date of the IAM role.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'created_date should be a datetime.')
        self._created_date = value

    @property
    def description(self) -> Optional[str]:
        """
        Gets the description of the IAM role.
        :return: The description of the IAM role.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, value: Optional[str] = None) -> None:
        """
        Sets the description of the IAM role.
        :param value: The description of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, Union[str, None], 'description should be a string.')
        self._description = value

    @property
    def id(self) -> str:
        """
        Gets the ID of the IAM role.
        :return: The ID of the IAM role.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the ID of the IAM role.
        :param value: The ID of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')
        self._id = value

    @property
    def last_used(self) -> Optional[IAMRoleLastUsed]:
        """
        Gets the last used date of the IAM role.
        :return: The last used date of the IAM role.
        :rtype: IAMRoleLastUsed
        """
        return self._last_used

    @last_used.setter
    def last_used(self, value: Optional[IAMRoleLastUsed] = None) -> None:
        """
        Sets the last used date of the IAM role.
        :param value: The last used date of the IAM role.
        :type value: IAMRoleLastUsed
        """
        Validation.validate_type(value, Union[IAMRoleLastUsed, None], 'last_used should be of IAMRoleLastUsed type.')
        self._last_used = value

    @property
    def max_session_duration(self) -> int:
        """
        Gets the maximum session duration of the IAM role.
        :return: The maximum session duration of the IAM role.
        :rtype: int
        """
        return self._max_session_duration

    @max_session_duration.setter
    def max_session_duration(self, value: int) -> None:
        """
        Sets the maximum session duration of the IAM role.
        :param value: The maximum session duration of the IAM role.
        :type value: int
        """
        Validation.validate_type(value, int, 'max_session_duration should be an integer.')
        self._max_session_duration = value

    @property
    def name(self) -> str:
        """
        Gets the name of the IAM role.
        :return: The name of the IAM role.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the IAM role.
        :param value: The name of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, str, 'name should be a string.')
        self._name = value

    @property
    def path(self) -> str:
        """
        Gets the path of the IAM role.
        :return: The path of the IAM role.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, value: str = '/') -> None:
        """
        Sets the path of the IAM role.
        :param value: The path of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, str, 'path should be a string.')
        self._path = value

    @property
    def permissions_boundary(self) -> Optional[IAMPermissionsBoundary]:
        """
        Gets the permissions boundary associated with the IAM role.
        :return: The permissions boundary associated with the IAM role.
        :rtype: IAMPermissionsBoundary
        """
        return self._permissions_boundary

    @permissions_boundary.setter
    def permissions_boundary(self, value: Optional[IAMPermissionsBoundary] = None) -> None:
        """
        Sets the permissions boundary associated with the IAM role.
        :param value: The permissions boundary asociated with the IAM role.
        :type value: IAMPermissionsBoundary
        """
        Validation.validate_type(
            value, Union[IAMPermissionsBoundary, None], 'permissions_boundary should be of IAMPermissionsBoundary type.'
        )
        self._permissions_boundary = value

    @property
    def tags(self) -> Optional[list]:
        """
        Gets the tags associated with the IAM role.
        :return: The tags associated with the IAM role.
        :rtype: list
        """
        return self._tags

    @tags.setter
    def tags(self, value: Optional[list] = None) -> None:
        """
        Sets the tags associated with the IAM role.
        :param value: The tags associated with the IAM role.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'tags should be a list.')
        self._tags = value

    def __str__(self) -> str:
        """
        Return a string representation of the IAMRole object.
        :return: String representation of the IAMRole object.
        :rtype: str
        """
        account = self.account if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        assume_role_policy_document = self.assume_role_policy_document if self.assume_role_policy_document else None
        description = self.description if self.description else None
        last_used = self.last_used if self.last_used else None
        permissions_boundary = self.permissions_boundary if self.permissions_boundary else None
        tags = self.tags if self.tags else None

        return (
            f'IAMRole('
            f'account={account},'
            f'path="{self.path}",'
            f'name="{self.name}",'
            f'id="{self.id}",'
            f'arn="{self.arn}",'
            f'created_date={created_date},'
            f'assume_role_policy_document={assume_role_policy_document},'
            f'description="{description}",'
            f'max_session_duration={self.max_session_duration},'
            f'permissions_boundary={permissions_boundary},'
            f'last_used={last_used},'
            f'tags={tags}'
            f')'
        )

    def __dict__(self) -> dict:
        """
        Return a dictionary representation of the IAMRole object.
        :return: Dictionary representation of the IAMRole object.
        :rtype: dict
        """
        account = self.account.__dict__() if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        assume_role_policy_document = self.assume_role_policy_document if self.assume_role_policy_document else None
        description = self.description if self.description else None
        last_used = self.last_used.__dict__() if self.last_used else None
        permissions_boundary = self.permissions_boundary.__dict__() if self.permissions_boundary else None
        tags = self.tags if self.tags else None

        return {
            "account": account,
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "arn": self.arn,
            "created_date": created_date,
            "assume_role_policy_document": assume_role_policy_document,
            "description": description,
            "max_session_duration": self.max_session_duration,
            "permissions_boundary": permissions_boundary,
            "last_used": last_used,
            "tags": tags
        }


class IAMUser:
    """
    A class representing an IAM user.
    """

    def __init__(
            self,
            account: IAccount,
            name: str,
            id: str,
            arn: str,
            path: str = '/',
            created_date: Optional[datetime] = None,
            password_last_used_date: Optional[datetime] = None,
            permissions_boundary: Optional[IAMPermissionsBoundary] = None,
            login_profile: Optional[IAMUserLoginProfile] = None,
            access_keys: Optional[list[IAMUserAccessKey]] = None,
            tags: Optional[list] = None
    ) -> None:
        """
        Initialize a new IAMUser instance.
        :param account: The account associated with the IAM user.
        :type account: IAccount
        :param name: The name of the IAM user.
        :type name: str
        :param id: The unique identifier of the IAM user.
        :type id: str
        :param arn: The Amazon Resource Name (ARN) of the IAM user.
        :type arn: str
        :param path: The path for the IAM user. Defaults to '/'
        :type path: str
        :param created_date: The creation date of the IAM user. Defaults to None.
        :type created_date: datetime
        :param password_last_used_date: Information about the last time the IAM user password was used.
        Defaults to None.
        :type password_last_used_date: datetime
        :param permissions_boundary: The permissions boundary for the IAM user. Defaults to None.
        :type permissions_boundary: IAMPermissionsBoundary
        :param login_profile: The login profile of the IAM user. Defaults to None.
        :type login_profile: IAMUserLoginProfile
        :param access_keys: A list of access keys associated with the IAM user. Defaults to None.
        :type access_keys: list
        :param tags: A list of tags associated with the IAM user. Defaults to None.
        :type tags: list
        """
        Validation.validate_type(account, IAccount, 'account should be of Account type.')
        Validation.validate_type(name, str, 'name should be a string.')
        Validation.validate_type(id, str, 'id should be a string.')
        ArnValidator.arn(arn, True)
        Validation.validate_type(path, str, 'path should be a string.')
        Validation.validate_type(created_date, Union[datetime, None], 'created_date should be a datetime.')
        Validation.validate_type(
            password_last_used_date, Union[datetime, None], 'password_last_used_date should be a datetime.'
        )
        Validation.validate_type(
            permissions_boundary,
            Union[IAMPermissionsBoundary, None],
            'permissions_boundary should be of IAMPermissionsBoundary type.'
        )
        Validation.validate_type(
            login_profile, Union[IAMUserLoginProfile, None], 'login_profile should be of IAMUserLoginProfile type.'
        )
        Validation.validate_type(access_keys, Union[list, None], 'access_keys should be a list of IAMUserAccessKey.')
        if access_keys is not None and len(access_keys) > 0:
            all(
                Validation.validate_type(
                    access_key, IAMUserAccessKey, 'access_keys should be a list of IAMUserAccessKey.'
                ) for access_key in access_keys
            )
        Validation.validate_type(tags, Union[list, None], 'tags should be a list.')

        self._account = account
        self._name = name
        self._id = id
        self._arn = arn
        self._path = path
        self._created_date = created_date
        self._password_last_used_date = password_last_used_date
        self._permissions_boundary = permissions_boundary
        self._login_profile = login_profile
        self._access_keys = access_keys
        self._tags = tags

    @property
    def access_keys(self) -> Optional[list[IAMUserAccessKey]]:
        """
        Gets the list of access keys associated with the IAM user.
        :return: The list of access keys associated with the IAM user.
        :rtype: list
        """
        return self._access_keys

    @access_keys.setter
    def access_keys(self, value: Optional[list[IAMUserAccessKey]]) -> None:
        """
        Sets the list of access keys associated with the IAM user.
        :param value: The list of access keys associated with the IAM user.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'access_keys should be a list of IAMUserAccessKey.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(
                    access_key, IAMUserAccessKey, 'access_keys should be a list of IAMUserAccessKey.'
                ) for access_key in value
            )

        self._access_keys = value

    @property
    def account(self) -> IAccount:
        """
        Gets the account associated with the IAM user.
        :return: The account associated with the IAM user.
        :rtype: IAccount
        """
        return self._account

    @account.setter
    def account(self, value: IAccount) -> None:
        """
        Sets the account associated with the IAM user.
        :param value: The account to be associated with the IAM user.
        :type value: IAccount
        """
        Validation.validate_type(value, IAccount, 'account should be of Account type.')
        self._account = value

    @property
    def arn(self) -> str:
        """
        Gets the ARN of the IAM user.
        :return: The ARN of the IAM user.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, value: str) -> None:
        """
        Sets the ARN of the IAM user.
        :param value: The ARN of the IAM user.
        :type value: str
        """
        ArnValidator.arn(value, True)
        self._arn = value

    @property
    def created_date(self) -> Optional[datetime]:
        """
        Gets the created date of the IAM user.
        :return: The created date of the IAM user.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, value: Optional[datetime]) -> None:
        """
        Sets the created date of the IAM user.
        :param value: The created date of the IAM user.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'created_date should be a datetime.')
        self._created_date = value

    @property
    def id(self) -> str:
        """
        Gets the ID of the IAM user.
        :return: The ID of the IAM user.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the ID of the IAM user.
        :param value: The ID of the IAM user.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')
        self._id = value

    @property
    def login_profile(self) -> Optional[IAMUserLoginProfile]:
        """
        Gets the login profile of the IAM user.
        :return: The login profile of the IAM user.
        :rtype: IAMUserLoginProfile
        """
        return self._login_profile

    @login_profile.setter
    def login_profile(self, value: Optional[IAMUserLoginProfile]) -> None:
        """
        Sets the login profile of the IAM user.
        :param value: The login profile of the IAM user.
        :type value: IAMUserLoginProfile
        """
        Validation.validate_type(
            value, Union[IAMUserLoginProfile, None], 'login_profile should be of IAMUserLoginProfile type.'
        )

        self._login_profile = value

    @property
    def name(self) -> str:
        """
        Gets the name of the IAM user.
        :return: The name of the IAM user.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the IAM user.
        :param value: The name of the IAM user.
        :type value: str
        """
        Validation.validate_type(value, str, 'name should be a string.')
        self._name = value

    @property
    def password_last_used_date(self) -> Optional[datetime]:
        """
        Gets the password last used date of the IAM user.
        :return: The password last used date of the IAM user.
        :rtype: datetime
        """
        return self._password_last_used_date

    @password_last_used_date.setter
    def password_last_used_date(self, value: Optional[datetime]) -> None:
        """
        Sets the password last used date of the IAM user.
        :param value: The password last used date of the IAM user.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'password_last_used_date should be a datetime.')
        self._password_last_used_date = value

    @property
    def path(self) -> str:
        """
        Gets the path of the IAM user.
        :return: The path of the IAM user.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        """
        Sets the path of the IAM user.
        :param value: The path of the IAM user.
        :type value: str
        """
        Validation.validate_type(value, str, 'path should be a string.')
        self._path = value

    @property
    def permissions_boundary(self) -> Optional[IAMPermissionsBoundary]:
        """
        Gets the permissions boundary associated with the IAM user.
        :return: The permissions boundary associated with the IAM user.
        :rtype: IAMPermissionsBoundary
        """
        return self._permissions_boundary

    @permissions_boundary.setter
    def permissions_boundary(self, value: Optional[IAMPermissionsBoundary]) -> None:
        """
        Sets the permissions boundary associated with the IAM user.
        :param value: The permissions boundary associated with the IAM user.
        :type value: IAMPermissionsBoundary
        """
        Validation.validate_type(value, Union[IAMPermissionsBoundary, None],
                                 'permissions_boundary should be of IAMPermissionsBoundary type.')
        self._permissions_boundary = value

    @property
    def tags(self) -> Optional[list]:
        """
        Gets the tags associated with the IAM user.
        :return: The tags associated with the IAM user.
        :rtype: list
        """
        return self._tags

    @tags.setter
    def tags(self, value: Optional[list]) -> None:
        """
        Sets the tags associated with the IAM user.
        :param value: The tags associated with the IAM user.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'tags should be a list.')
        self._tags = value

    def __str__(self) -> str:
        """
        Return a string representation of the IAMUser object.
        :return: String representation of the IAMUser object.
        :rtype: str
        """
        account = self.account if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        password_last_used_date = self.password_last_used_date.isoformat() if self.password_last_used_date else None
        permissions_boundary = self.permissions_boundary if self.permissions_boundary else None
        tags = self.tags if self.tags else None
        login_profile = self.login_profile if self.login_profile else None
        access_keys = self.access_keys if self.access_keys and len(self.access_keys) > 0 else None

        return (
            f'IAMUser('
            f'account={account},'
            f'path={self.path},'
            f'name={self.name},'
            f'id={self.id},'
            f'arn={self.arn},'
            f'created_date={created_date},'
            f'password_last_used_date={password_last_used_date},'
            f'permissions_boundary={permissions_boundary},'
            f'login_profile={login_profile},'
            f'access_keys={access_keys},'
            f'tags={tags}'
            f')'
        )

    def __dict__(self) -> dict:
        """
        Return a dictionary representation of the IAMUser object.
        :return: Dictionary representation of the IAMUser object.
        :rtype: dict
        """
        account = self.account.__dict__() if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        password_last_used_date = self.password_last_used_date.isoformat() if self.password_last_used_date else None
        permissions_boundary = self.permissions_boundary.__dict__() if self.permissions_boundary else None
        tags = self.tags if self.tags else None
        login_profile = self.login_profile.__dict__() if self.login_profile else None
        access_keys = self.access_keys if self.access_keys and len(self.access_keys) > 0 else None

        return {
            "account": account,
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "arn": self.arn,
            "created_date": created_date,
            "password_last_used_date": password_last_used_date,
            "permissions_boundary": permissions_boundary,
            "login_profile": login_profile,
            "access_keys": access_keys,
            "tags": tags
        }
