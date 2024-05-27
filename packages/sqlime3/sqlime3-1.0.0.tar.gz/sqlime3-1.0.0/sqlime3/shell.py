from sqlite3 import Connection


class ChildObject:
    def __init__(self, connection: Connection, parent):
        self._parent = parent
        self._conn = connection
        self._crsr = connection.cursor()

    @property
    def parent(self):
        return self._parent

    def find_parent(self, cls):
        current_parent = self.parent
        while current_parent and cls:
            if isinstance(current_parent, cls):
                return current_parent
            current_parent = current_parent.parent
        return current_parent


class Row(ChildObject):
    def __init__(self, connection: Connection,
                 parent: 'Rows', rowid: int):
        super().__init__(connection, parent)
        self._rowid = rowid

    @property
    def id(self) -> int:
        return self._rowid - 1

    def __len__(self):
        tbl = self.find_parent(Table)
        return len(tbl.columns)

    def __getitem__(self, item):
        tbl = self.find_parent(Table)
        cols = tbl.columns

        if isinstance(item, int):
            if not (0 <= item < len(self)):
                raise IndexError("SqRow index out of range.")
            cmd = f"SELECT {cols[item].name} FROM {tbl.name} WHERE rowid = ?;"
            self._crsr.execute(cmd, (self._rowid,))
            return self._crsr.fetchone()[0]

        if isinstance(item, str):
            if item not in cols.names:
                raise KeyError(item)
            cmd = f"SELECT '{item}' FROM {tbl.name} WHERE rowid = ?;"
            self._crsr.execute(cmd, (self._rowid,))
            return self._crsr.fetchone()[0]

        if isinstance(item, slice):
            _range = range(len(self))[item]
            cmd = f"SELECT * FROM {tbl.name} WHERE rowid = ?;"
            self._crsr.execute(cmd, (self._rowid,))
            return self._crsr.fetchone()

        raise TypeError(item)

    def __setitem__(self, key, value):
        tbl = self.find_parent(Table)

        if isinstance(key, int):
            if not (0 <= key < len(self)):
                raise IndexError("SqRow index out of range.")
            key = tbl.columns[key].name
            return self.__setitem__(key, value)

        if isinstance(key, str):
            if key not in tbl.columns.names:
                raise KeyError(key)
            cmd = f"UPDATE {tbl.name} SET {key} = ? WHERE rowid = ?;"
            self._crsr.execute(cmd, (value, self._rowid))
            return self._conn.commit()

        raise TypeError(type(key))

    def __delitem__(self, key):
        if isinstance(key, int | str):
            return self.__setitem__(key, None)

        if isinstance(key, slice):
            keys = range(len(self))[key]
            for key in keys:
                self.__setitem__(key, None)
            return None

        raise TypeError(type(key))

    def __contains__(self, item):
        try:
            self.__getitem__(item)
            return True
        except (KeyError, IndexError, TypeError):
            return False

    def __iter__(self):
        tbl = self.find_parent(Table)
        cmd = f"SELECT * FROM {tbl.name} WHERE rowid = ?;"
        self._crsr.execute(cmd, (self._rowid,))
        return iter(self._crsr.fetchone())

    def __repr__(self):
        return f"<Row object at 0x{id(self)}: {tuple(self)}>"


class Rows(ChildObject):
    def __init__(self, connection: Connection, parent: 'Table'):
        super().__init__(connection, parent)

    def insert(self, values=None, columns=None, data=None) -> None:
        if (values or columns) and data is None:
            raise ValueError("Either provide 'values' and/or 'columns' or 'data', not both.")
        if columns and values is None:
            raise ValueError("If 'columns' are provided, 'values' must be provided as well.")

        tbl = self.find_parent(Table)

        if all(isinstance(item, tuple) for item in [values, columns]):
            placeholders = ','.join(['?'] * len(values))
            cmd = f"INSERT INTO {tbl.name} ({placeholders}) VALUES({placeholders});"
            items = tuple(columns) + tuple(values)
            self._crsr.execute(cmd, items)
            return self._conn.commit()

        if isinstance(values, tuple) and columns is None:
            columns = tbl.columns.names[:len(values)]
            return self.insert(values=values, columns=columns)

        if isinstance(data, dict):
            columns = tuple(data.keys())
            values = tuple(data.values())
            return self.insert(values=values, columns=columns)

        if isinstance(data, zip):
            return self.insert(data=dict(data))

        if isinstance(data, Row):
            return self.insert(values=tuple(Row))

        if any(isinstance(data, cls) for cls in [tuple, Rows]):
            for row in data:
                self.insert(data=row)
            return None

        raise TypeError('Invalid types of arguments passed.')

    def __len__(self):
        tbl = self.find_parent(Table)
        cmd = f"SELECT COUNT(*) FROM {tbl.name};"
        self._crsr.execute(cmd)
        return self._crsr.fetchone()[0]

    def __getitem__(self, item):
        tbl = self.find_parent(Table)

        if isinstance(item, int):
            if not (0 <= item < len(self)):
                raise IndexError(" Rows index out of range.")
            return Row(self._conn, self, item + 1)

        if isinstance(item, str):
            cmd = f"SELECT rowid FROM {tbl.name} WHERE {item} ORDER BY rowid;"
            self._crsr.execute(cmd)
            items = self._crsr.fetchall()
            if not items:
                raise KeyError(item)
            return tuple(Row(self._conn, self, item[0]) for item in items)

        if isinstance(item, slice):
            items = range(len(self))[item]
            return tuple(Row(self._conn, self, item + 1) for item in items)

        raise TypeError(type(item))

    def __setitem__(self, *columns, values):
        return self.insert(values, columns)

    def __delitem__(self, key):
        tbl = self.find_parent(Table)

        if isinstance(key, int):
            if not (0 <= key < len(self)):
                raise IndexError("Rows index out of range.")
            cmd = f"DELETE FROM {tbl.name} WHERE rowid=?;"
            self._crsr.execute(cmd, (key + 1,))
            return self._conn.commit()

        if isinstance(key, str):
            cmd = f"DELETE FROM {tbl.name} WHERE {key};"
            self._crsr.execute(cmd)
            return self._conn.commit()

        if isinstance(key, slice):
            keys = range(len(self))[key]
            for key in keys:
                self.__delitem__(key)
            return None

        raise TypeError(type(key))

    def __contains__(self, item):
        try:
            self.__getitem__(item)
            return True
        except (KeyError, IndexError, TypeError):
            return False

    def __iter__(self):
        items = range(len(self))
        return iter(Row(self._conn, self, item + 1) for item in items)

    def __repr__(self):
        return f"<Rows object at 0x{id(self)}: {tuple(self)}>"


class Column(ChildObject):
    def __init__(self, connection: Connection,
                 parent: 'Columns', cid: int):
        super().__init__(connection, parent)
        self._cid = cid

    @property
    def pragma(self) -> tuple:
        tbl = self.find_parent(Table)
        cmd = "SELECT * FROM PRAGMA_TABLE_INFO(?) WHERE cid=?;"
        self._crsr.execute(cmd, (tbl.name, self._cid))
        return self._crsr.fetchone()

    @property
    def id(self) -> int:
        return self._cid

    @property
    def name(self) -> str:
        return self.pragma[1]

    @property
    def type(self) -> str:
        return self.pragma[2]

    @property
    def not_null(self) -> bool:
        return bool(self.pragma[3])

    @property
    def default(self) -> any:
        return self.pragma[4]

    @property
    def pk(self) -> bool:
        return bool(self.pragma[5])

    def __repr__(self):
        return f"<Column object at 0x{id(self)}: '{self.name}'>"


class Columns(ChildObject):
    def __init__(self, connection: Connection, parent: 'Table'):
        super().__init__(connection, parent)

    @property
    def pragma(self) -> list[tuple]:
        tbl = self.find_parent(Table)
        cmd = f"SELECT * FROM PRAGMA_TABLE_INFO(?);"
        self._crsr.execute(cmd, (tbl.name,))
        return self._crsr.fetchall()

    @property
    def names(self) -> tuple[str, ...]:
        return tuple(item[1] for item in self.pragma)

    def __len__(self):
        return len(self.pragma)

    def __getitem__(self, item):
        names = self.names
        pragma = self.pragma

        if isinstance(item, int):
            if not (0 <= item < len(pragma)):
                raise IndexError("Columns index out of range.")
            return Column(self._conn, self, item)

        if isinstance(item, str):
            if item not in names:
                raise KeyError(item)
            return Column(self._conn, self, names.index(item))

        if isinstance(item, slice):
            items = range(len(pragma))[item]
            return tuple(Column(self._conn, self, item) for item in items)

        raise TypeError(type(item))

    def __setitem__(self, key, value):
        """Not supported"""
        pass

    def __delitem__(self, key):
        """Not supported"""
        pass

    def __contains__(self, item):
        try:
            self.__getitem__(item)
            return True
        except (KeyError, IndexError, TypeError):
            return False

    def __iter__(self):
        items = range(len(self))
        return iter(Column(self._conn, self, item) for item in items)

    def __repr__(self):
        return f"<Columns object at 0x{id(self)}: {self.names}>"


class Table(ChildObject):
    def __init__(self, connection: Connection,
                 parent: 'Lime', name: str):
        super().__init__(connection, parent)
        self._name = name

    @property
    def sql(self) -> str:
        cmd = f"SELECT sql FROM sqlite_master WHERE type=? AND name=?;"
        self._crsr.execute(cmd, ('table', self.name))
        return self._crsr.fetchone()[0]

    @property
    def name(self) -> str:
        return self._name

    @property
    def columns(self) -> Columns:
        return Columns(self._conn, self)

    @property
    def rows(self) -> Rows:
        return Rows(self._conn, self)

    @property
    def primary_key(self) -> tuple[str, ...]:
        pragma = self.columns.pragma
        return tuple(item[1] for item in pragma if item[5])

    @property
    def foreign_keys(self) -> list[tuple]:
        cmd = f"PRAGMA foreign_key_list({self.name});"
        self._crsr.execute(cmd)
        return [item[2:5] for item in self._crsr.fetchall()]

    def __repr__(self):
        return f"<Table object at 0x{id(self)}: '{self.name}'>"


class Lime(ChildObject):
    def __init__(self, connection: Connection):
        super().__init__(connection, None)

    @property
    def sql(self) -> tuple[str, ...]:
        cmd = f"SELECT sql FROM sqlite_master WHERE type=?;"
        self._crsr.execute(cmd, ('table',))
        return tuple(item[0] for item in self._crsr.fetchall())

    @property
    def names(self) -> tuple[str, ...]:
        cmd = f"SELECT name FROM sqlite_master WHERE type=?;"
        self._crsr.execute(cmd, ('table',))
        return tuple(item[0] for item in self._crsr.fetchall())

    def __len__(self):
        return len(self.names)

    def __getitem__(self, item):
        names = self.names

        if isinstance(item, int):
            if not (0 <= item < len(names)):
                raise IndexError("Lime index out of range.")
            return Table(self._conn, self, names[item])

        if isinstance(item, str):
            if not (item in names):
                raise KeyError(item)
            return Table(self._conn, self, item)

        if isinstance(item, slice):
            return tuple(Table(self._conn, self, item) for item in names[item])

        raise TypeError(type(item))

    def __setitem__(self, key, value):
        cmd = f"CREATE TABLE IF NOT EXISTS {key} ({value});"
        self._crsr.execute(cmd)
        return self._conn.commit()

    def __delitem__(self, key):
        names = self.names

        if isinstance(key, str):
            if not (key in names):
                raise KeyError(key)
            cmd = f"DROP TABLE IF EXISTS {key};"
            self._crsr.execute(cmd)
            return self._conn.commit()

        if isinstance(key, int):
            if not (0 <= key < len(names)):
                raise IndexError("Lime index out of range.")
            return self.__delitem__(names[key])

        if isinstance(key, slice):
            for item in range(len(names))[key]:
                self.__delitem__(item)
            return None

        raise TypeError(type(key))

    def __contains__(self, item):
        try:
            self.__getitem__(item)
            return True
        except (KeyError, IndexError, TypeError):
            return False

    def __iter__(self):
        names = self.names
        return iter(Table(self._conn, self, item) for item in names)

    def __repr__(self):
        return f"<Lime object at 0x{id(self)}: {self.names}>"
