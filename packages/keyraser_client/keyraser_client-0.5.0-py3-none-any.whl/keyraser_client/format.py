"""Formats for entity ids and data streams"""

import enum
import typing


class IdFormat(enum.Enum):
    """
    Enum type that represents the format of entity ids.
    """

    HEX = "HEX"
    """Entity ids are represented as a string of hexadecimal characters."""

    STRING_UTF8 = "STRING-UTF8"
    """Entity ids are the utf8 encoded strings."""

    DEFAULT = "DEFAULT"
    """Use default format used in binary."""

    def as_cli_params(self) -> typing.List[str]:
        """
        Returns a list of command line parameters.

        Returns:
            [str]: The cli parameters when this format is used.
        """
        if self == IdFormat.DEFAULT:
            return []

        return ['-idFormat', self.value]


class Format:
    """
    Base class for data formats that can be encrypted.
    """

    def __init__(self, type_id: str):
        self.type_id = type_id

    def as_cli_params(self) -> typing.List[str]:
        """
        Returns a list of command line parameters.

        Returns:
            [str]: The cli parameters when this format is used.
        """
        return [self.type_id]


class CsvFormat(Format):
    """
    Format for CSV-files, containing comma-separated values.

    In this format each separate data item is written to a single line that contains
    individual text values separated by a separator, most often ',' or ';'. This
    allows for easy parsing. In order to know, to which entity a single item belongs a
    column must be specified that contains the id.

    The name or index of the id column and the format of the ids can be configured
    using the `id_column` and `id_format` attributes.
    """

    def __init__(
        self,
        *,
        id_column: typing.Optional[str] = None,
        id_format: IdFormat = IdFormat.DEFAULT,
        separator: typing.Optional[str] = None,
        enclosing: typing.Optional[str] = None,
        contains_header: bool = False,
    ):
        """
        Create a new CsvFormat.

        Args:
            id_column: The name of the property in the JSON object that contains the
                entity id.
            id_format: The `IdFormat` that defines how the entity id is encoded in
                the `id_property`.
        """
        self.id_column = id_column
        self.id_format = id_format
        self.separator = separator
        self.enclosing = enclosing
        self.contains_header = contains_header
        super().__init__('csv')

    def as_cli_params(self) -> typing.List[str]:
        """
        Returns a list of command line parameters.

        Returns:
            [str]: The cli parameters when this format is used.
        """
        params = super().as_cli_params()
        if self.id_column is not None:
            params.extend(['-id', self.id_column])
        params.extend(self.id_format.as_cli_params())

        if self.separator is not None:
            params.extend(['-separator', self.separator])

        if self.enclosing is not None:
            params.extend(['-enclosing', self.enclosing])

        if self.contains_header:
            params.extend(['-header'])

        return params


class NdjsonFormat(Format):
    """
    Format for newline-delimited JSON.

    In this format each separate data item is written to a single line that contains
    a JSON object. In order to know, to which entity a single item belongs each JSON
    objects must use the same property that contains the id.

    The name of the id property and the format of the ids can be configured using
    the `id_property` and `id_format` attributes.
    """

    def __init__(
        self,
        *,
        id_property: typing.Optional[str] = None,
        id_format: IdFormat = IdFormat.DEFAULT,
    ):
        """
        Create a new NdjsonFormat.

        Args:
            id_property: The name of the property in the JSON object that contains the
                entity id.
            id_format: The `IdFormat` that defines how the entity id is encoded in
                the `id_property`.
        """
        self.id_property = id_property
        self.id_format = id_format
        super().__init__('ndjson')

    def as_cli_params(self) -> typing.List[str]:
        """
        Returns a list of command line parameters.

        Returns:
            [str]: The cli parameters when this format is used.
        """
        params = super().as_cli_params()
        if self.id_property is not None:
            params.extend(['-id', self.id_property])
        params.extend(self.id_format.as_cli_params())
        return params


class SingleFormat(Format):
    """
    Format for encypting a whole file for a single entity.

    In this format we encrypt the whole data with for a single entity that is defined
    as a command line parameter.

    The entity id and the format of the id can be configured using the `entity_id` and
    `id_format` attributes.
    """

    def __init__(
        self,
        entity_id: str,
        *,
        id_format: IdFormat = IdFormat.DEFAULT,
    ):
        """
        Create a new SingleFormat.

        Args:
            entity_id: The entity_id which is used for encrypting the data.
            id_format: The `IdFormat` that defines how the entity id is encoded in
                the `entity_id`.
        """
        self.entity_id = entity_id
        self.id_format = id_format
        super().__init__('single')

    def as_cli_params(self) -> typing.List[str]:
        """
        Returns a list of command line parameters.

        Returns:
            [str]: The cli parameters when this format is used.
        """
        params = super().as_cli_params()
        params.extend(['-id', self.entity_id])
        params.extend(self.id_format.as_cli_params())
        return params
