import re


class TypeConverter:
    """Class to convert SQL types to C++ types with sizes"""

    @classmethod
    def convert(cls, name: str):
        """Transforms SQL type name into a pair of C++ type name and its size in bytes"""
        match name:
            case n if "INT" in name:
                return cls.convert_int(n)
            case "BOOLEAN":
                return {'name': 'bool', 'size': 1}
            case _:
                raise RuntimeError(f"Type '{name}' is not supported yet.")

    @classmethod
    def convert_int(cls, name: str):
        """Transformer specified for INTEGER type family. For now we suppose that all INTEGERs are unsigned ints."""
        typ = {'name': 'unsigned int'}
        s = re.search("(?<=INT)\d", name)  # check if size is explicitly stated in type
        match name:
            case _ if s:
                typ['size'] = int(s.group(0))
            case "TINYINT":
                typ['size'] = 1
            case "SMALLINT":
                typ['size'] = 2
            case "MEDIUMINT":
                typ['size'] = 3
            case "INTEGER" | "INT":
                typ['size'] = 4
            case "BIGINT":
                typ['size'] = 8
            case _:
                raise RuntimeError(f"Unrecognized type '{name}'!")
        return typ
