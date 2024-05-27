The pysql-repo library is a Python library that is designed to use the session/repository pattern to interact with databases in Python projects. It provides a more flexible notation for running SQL queries and is built on top of SQLAlchemy, a popular Python SQL toolkit. With pysql_repo, users can write SQL queries using a new, more intuitive syntax, simplifying the process of working with SQL databases in Python and making it easier to write and maintain complex queries.

## Installing pysql-repo

To install pysql-repo, if you already have Python, you can install with:

```
pip install pysql_repo
```

## How to import pysql-repo

To access pysql-repo and its functions import it in your Python code like this:

```
from pysql_repo import Database, Repository, Service, with_session, Operators, LoadingTechnique, RelationshipOption
```

To access pysql-repo and its asyncio functions import it in your Python code like this:
```
from pysql_repo.asyncio import AsyncDatabase, AsyncRepository, AsyncService, with_async_session
```

## Reading the example code

```
# MODULES
from typing import List

# SQLALCHEMY
from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = "CITY"

    id: Mapped[int] = mapped_column(
        "ID",
        Integer,
        primary_key=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        "NAME",
        String,
        index=True,
    )
    state: Mapped[str] = mapped_column(
        "STATE",
        String,
        index=True,
    )

    addresses: Mapped[List["Address"]] = relationship(
        "Address",
        back_populates="city",
        lazy="joined",
        cascade="all, delete-orphan",
    )


class Address(Base):
    __tablename__ = "ADDRESS"

    id: Mapped[int] = mapped_column(
        "ID",
        Integer,
        primary_key=True,
        index=True,
    )
    street: Mapped[str] = mapped_column(
        "STREET",
        String,
        index=True,
    )
    zip_code: Mapped[str] = mapped_column(
        "ZIP_CODE",
        Integer,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        "USER_ID",
        Integer,
        ForeignKey("USER.ID"),
    )
    city_id: Mapped[int] = mapped_column(
        "CITY_ID",
        Integer,
        ForeignKey("CITY.ID"),
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="addresses",
        lazy="joined",
    )
    city: Mapped["City"] = relationship(
        "City",
        back_populates="addresses",
        lazy="joined",
    )


class User(Base):
    __tablename__ = "USER"

    id: Mapped[int] = mapped_column(
        "ID",
        Integer,
        primary_key=True,
        index=True,
    )
    email: Mapped[str] = mapped_column(
        "EMAIL",
        String,
        unique=True,
        index=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        "HASHED_PASSWORD",
        String,
    )
    full_name: Mapped[str] = mapped_column(
        "FULL_NAME",
        String,
        index=True,
    )
    is_active: Mapped[bool] = mapped_column(
        "IS_ACTIVE",
        Boolean,
        default=True,
    )

    addresses: Mapped[List["Address"]] = relationship(
        "Address",
        back_populates="user",
        lazy="joined",
        cascade="all, delete-orphan",
    )
```

To create an instance of Database and generate an instance of Session from the factory:

```
import logging

logging.basicConfig()
logger_db = logging.get_logger('demo')

database = DataBase(
    databases_config={
        "connection_string": "foo",
    },
    base=Base,
    logger=logger_db,
)

database.create_database()

with database.session_factory() as session:
    session.execute(...)
```

To create a repository, you just have to inherit your class from Repository.

```
# MODULES
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

# SQLALCHEMY
from sqlalchemy.orm import Column, Session

# PYSQL_REPO
from pysql_repo import Operators, Repository, LoadingTechnique, RelationshipOption

# CONTEXTLIB
from contextlib import AbstractContextManager

# MODEL
from tests.repositories.user._base import UserRepositoryBase as _UserRepositoryBase
from tests.models.database.database import Address, User
from tests.models.schemas.user import UserCreate


class UserRepositoryBase:
    @classmethod
    def get_filters(
        cls,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[str]] = None,
        zip_codes_not_in: Optional[List[str]] = None,
        is_active_equal: Optional[bool] = None,
    ) -> Dict[Column, Any]:
        return {
            User.id: {
                Operators.IN: ids_in,
                Operators.NOT_IN: ids_not_in,
            },
            User.email: {
                Operators.IIN: emails_iin,
                Operators.IN: emails_in,
                Operators.NOT_IIN: emails_not_iin,
                Operators.NOT_IN: emails_not_in,
                Operators.ILIKE: email_ilike,
                Operators.LIKE: email_like,
                Operators.NOT_ILIKE: email_not_ilike,
                Operators.NOT_LIKE: email_not_like,
                Operators.EQUAL: email_equal,
                Operators.IEQUAL: email_iequal,
                Operators.DIFFERENT: email_different,
                Operators.IDIFFERENT: email_idifferent,
            },
            User.is_active: {
                Operators.EQUAL: is_active_equal,
            },
            User.addresses: {
                Operators.ANY: {
                    Address.zip_code: {
                        Operators.IN: zip_codes_in,
                        Operators.NOT_IN: zip_codes_not_in,
                    },
                }
            },
        }

    @classmethod
    def get_relationship_options(
        cls,
        load_addresses: bool = False,
        load_city: bool = False,
        zip_codes_not_in: Optional[List[int]] = None,
        zip_codes_in: Optional[List[int]] = None,
    ):
        extra_join_addresses = []
        if zip_codes_not_in:
            extra_join_addresses.append(Address.zip_code.not_in(zip_codes_not_in))
        if zip_codes_in:
            extra_join_addresses.append(Address.zip_code.in_(zip_codes_in))

        return {
            User.addresses: RelationshipOption(
                lazy=LoadingTechnique.JOINED
                if load_addresses
                else LoadingTechnique.NOLOAD,
                added_criteria=extra_join_addresses
                if len(extra_join_addresses) > 0
                else None,
                children={
                    Address.city: RelationshipOption(
                        lazy=LoadingTechnique.JOINED
                        if load_city
                        else LoadingTechnique.NOLOAD,
                    )
                },
            ),
        }


class UserRepository(Repository, _UserRepositoryBase):
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
    ) -> None:
        super().__init__(session_factory)

    def get_all(
        self,
        session: Session,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
    ) -> Sequence[User]:
        users = self._select_all(
            session=session,
            model=User,
            optional_filters=self.get_filters(
                ids_in=ids_in,
                ids_not_in=ids_not_in,
                emails_iin=emails_iin,
                emails_in=emails_in,
                emails_not_iin=emails_not_iin,
                emails_not_in=emails_not_in,
                email_ilike=email_ilike,
                email_like=email_like,
                email_not_ilike=email_not_ilike,
                email_not_like=email_not_like,
                email_equal=email_equal,
                email_iequal=email_iequal,
                email_different=email_different,
                email_idifferent=email_idifferent,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
                is_active_equal=is_active_equal,
            ),
            relationship_options=self.get_relationship_options(
                load_addresses=load_addresses,
                load_city=load_city,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
            ),
            order_by=order_by,
            direction=direction,
        )

        return users

    def get_paginate(
        self,
        session: Session,
        page: int,
        per_page: int,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
    ) -> Tuple[Sequence[User], str]:
        users, pagination = self._select_paginate(
            session=session,
            model=User,
            optional_filters=self.get_filters(
                ids_in=ids_in,
                ids_not_in=ids_not_in,
                emails_iin=emails_iin,
                emails_in=emails_in,
                emails_not_iin=emails_not_iin,
                emails_not_in=emails_not_in,
                email_ilike=email_ilike,
                email_like=email_like,
                email_not_ilike=email_not_ilike,
                email_not_like=email_not_like,
                email_equal=email_equal,
                email_iequal=email_iequal,
                email_different=email_different,
                email_idifferent=email_idifferent,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
                is_active_equal=is_active_equal,
            ),
            relationship_options=self.get_relationship_options(
                load_addresses=load_addresses,
                load_city=load_city,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
            ),
            order_by=order_by,
            direction=direction,
            page=page,
            per_page=per_page,
        )

        return users, pagination

    def get_by_id(
        self,
        session: Session,
        id: int,
    ) -> Optional[User]:
        user = self._select(
            session=session,
            model=User,
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
        )

        return user

    def create(
        self,
        data: UserCreate,
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> User:
        user = self._add(
            session=session,
            model=User,
            values={
                User.email.key: data.email,
                User.hashed_password.key: data.hashed_password,
                User.full_name.key: data.full_name,
            },
            flush=flush,
            commit=commit,
        )

        return user

    def create_all(
        self,
        data: List[UserCreate],
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> Sequence[User]:
        users = self._add_all(
            session=session,
            model=User,
            values=[
                {
                    User.email.key: item.email,
                    User.hashed_password.key: item.hashed_password,
                    User.full_name.key: item.full_name,
                }
                for item in data
            ],
            flush=flush,
            commit=commit,
        )

        return users

    def patch_email(
        self,
        id: int,
        email: str,
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> User:
        user = self._update(
            session=session,
            model=User,
            values={
                User.email.key: email,
            },
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
            flush=flush,
            commit=commit,
        )

        return user

    def patch_disable(
        self,
        ids: List[int],
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> List[User]:
        users = self._update_all(
            session=session,
            model=User,
            values={
                User.is_active.key: False,
            },
            filters={
                User.id: {
                    Operators.IN: ids,
                },
            },
            flush=flush,
            commit=commit,
        )

        return users

    def delete(
        self,
        id: int,
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> bool:
        is_deleted = self._delete(
            session=session,
            model=User,
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
            flush=flush,
            commit=commit,
        )

        return is_deleted

    def delete_all(
        self,
        ids: List[int],
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> bool:
        is_deleted = self._delete_all(
            session=session,
            model=User,
            filters={
                User.id: {
                    Operators.IN: ids,
                },
            },
            flush=flush,
            commit=commit,
        )

        return is_deleted
```

To create a service, you just have to inherit your class from Service.

```
# MODULES
from logging import Logger
from typing import List, Optional, Tuple

# SQLALCHEMY
from sqlalchemy.orm import Session

# PYSQL_REPO
from pysql_repo import Service, with_session

# REPOSITORIES
from tests.repositories.user.user_repository import UserRepository

# MODELS
from tests.models.schemas.user import UserCreate, UserRead


class UserService(Service[UserRepository]):
    def __init__(
        self,
        user_repository: UserRepository,
        logger: Logger,
    ) -> None:
        super().__init__(
            repository=user_repository,
        )
        self._logger = logger

    @with_session()
    def get_users(
        self,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        session: Optional[Session] = None,
    ) -> List[UserRead]:
        users = self._repository.get_all(
            ids_in=ids_in,
            ids_not_in=ids_not_in,
            emails_iin=emails_iin,
            emails_in=emails_in,
            emails_not_iin=emails_not_iin,
            emails_not_in=emails_not_in,
            email_ilike=email_ilike,
            email_like=email_like,
            email_not_ilike=email_not_ilike,
            email_not_like=email_not_like,
            email_equal=email_equal,
            email_iequal=email_iequal,
            email_different=email_different,
            email_idifferent=email_idifferent,
            zip_codes_in=zip_codes_in,
            zip_codes_not_in=zip_codes_not_in,
            is_active_equal=is_active_equal,
            load_addresses=load_addresses,
            load_city=load_city,
            order_by=order_by,
            direction=direction,
            session=session,
        )

        return [UserRead.model_validate(item) for item in users]

    @with_session()
    def get_users_paginate(
        self,
        page: int,
        per_page: int,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        session: Optional[Session] = None,
    ) -> Tuple[List[UserRead], str]:
        users, pagination = self._repository.get_paginate(
            page=page,
            per_page=per_page,
            ids_in=ids_in,
            ids_not_in=ids_not_in,
            emails_iin=emails_iin,
            emails_in=emails_in,
            emails_not_iin=emails_not_iin,
            emails_not_in=emails_not_in,
            email_ilike=email_ilike,
            email_like=email_like,
            email_not_ilike=email_not_ilike,
            email_not_like=email_not_like,
            email_equal=email_equal,
            email_iequal=email_iequal,
            email_different=email_different,
            email_idifferent=email_idifferent,
            zip_codes_in=zip_codes_in,
            zip_codes_not_in=zip_codes_not_in,
            is_active_equal=is_active_equal,
            load_addresses=load_addresses,
            load_city=load_city,
            order_by=order_by,
            direction=direction,
            session=session,
        )

        users = [UserRead.model_validate(item) for item in users]

        return users, pagination

    @with_session()
    def get_user_by_id(
        self,
        id: int,
        session: Optional[Session] = None,
    ) -> UserRead:
        user = self._repository.get_by_id(
            id=id,
            session=session,
        )

        if user is None:
            return None

        return UserRead.model_validate(user)

    @with_session()
    def create_user(
        self,
        data: UserCreate,
        session: Optional[Session] = None,
    ) -> UserRead:
        user = self._repository.create(
            data=data,
            flush=True,
            session=session,
        )

        return UserRead.model_validate(user)

    @with_session()
    def create_users(
        self,
        data: List[UserCreate],
        session: Optional[Session] = None,
    ) -> List[UserRead]:
        users = self._repository.create_all(
            data=data,
            flush=True,
            session=session,
        )

        return [UserRead.model_validate(user) for user in users]

    @with_session()
    def patch_email(
        self,
        id: int,
        email: str,
        session: Optional[Session] = None,
    ) -> UserRead:
        user = self._repository.patch_email(
            id=id,
            email=email,
            flush=True,
            session=session,
        )

        return UserRead.model_validate(user)

    @with_session()
    def patch_disable(
        self,
        ids: List[int],
        session: Optional[Session] = None,
    ) -> List[UserRead]:
        users = self._repository.patch_disable(
            ids=ids,
            flush=True,
            session=session,
        )

        return [UserRead.model_validate(user) for user in users]

    @with_session()
    def delete_by_id(
        self,
        id: int,
        session: Optional[Session] = None,
    ) -> bool:
        return self._repository.delete(
            id=id,
            flush=True,
            session=session,
        )

    @with_session()
    def delete_by_ids(
        self,
        ids: List[int],
        session: Optional[Session] = None,
    ) -> bool:
        return self._repository.delete_all(
            ids=ids,
            flush=True,
            session=session,
        )
```
To create an instance of AsyncDatabase and generate an instance of AsyncSession from the factory:

```
import logging

logging.basicConfig()
logger_db = logging.get_logger('demo')

database = AsyncDataBase(
    databases_config={
        "connection_string": "foo",
    },
    base=Base,
    logger=logger_db,
)

await database.create_database()

async with database.session_factory() as session:
    await session.execute(...)
```

To create an  async repository, you just have to inherit your class from AsyncRepository.

```
# MODULES
from typing import Callable, List, Optional, Tuple

# SQLALCHEMY
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

# PYSQL_REPO
from pysql_repo import Operators
from pysql_repo.asyncio import AsyncRepository

# CONTEXTLIB
from contextlib import AbstractAsyncContextManager

# MODEL
from tests.repositories.user._base import UserRepositoryBase as _UserRepositoryBase
from tests.models.database.database import User
from tests.models.schemas.user import UserCreate


class AsyncUserRepository(AsyncRepository, _UserRepositoryBase):
    def __init__(
        self,
        session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]],
    ) -> None:
        super().__init__(session_factory)

    async def get_all(
        self,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None,
    ) -> Sequence[User]:
        users = await self._select_all(
            session=session,
            model=User,
            optional_filters=self.get_filters(
                ids_in=ids_in,
                ids_not_in=ids_not_in,
                emails_iin=emails_iin,
                emails_in=emails_in,
                emails_not_iin=emails_not_iin,
                emails_not_in=emails_not_in,
                email_ilike=email_ilike,
                email_like=email_like,
                email_not_ilike=email_not_ilike,
                email_not_like=email_not_like,
                email_equal=email_equal,
                email_iequal=email_iequal,
                email_different=email_different,
                email_idifferent=email_idifferent,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
                is_active_equal=is_active_equal,
            ),
            relationship_options=self.get_relationship_options(
                load_addresses=load_addresses,
                load_city=load_city,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
            ),
            order_by=order_by,
            direction=direction,
        )

        return users

    async def get_paginate(
        self,
        page: int,
        per_page: int,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None,
    ) -> Tuple[Sequence[User], str]:
        users, pagination = await self._select_paginate(
            session=session,
            model=User,
            optional_filters=self.get_filters(
                ids_in=ids_in,
                ids_not_in=ids_not_in,
                emails_iin=emails_iin,
                emails_in=emails_in,
                emails_not_iin=emails_not_iin,
                emails_not_in=emails_not_in,
                email_ilike=email_ilike,
                email_like=email_like,
                email_not_ilike=email_not_ilike,
                email_not_like=email_not_like,
                email_equal=email_equal,
                email_iequal=email_iequal,
                email_different=email_different,
                email_idifferent=email_idifferent,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
                is_active_equal=is_active_equal,
            ),
            relationship_options=self.get_relationship_options(
                load_addresses=load_addresses,
                load_city=load_city,
                zip_codes_in=zip_codes_in,
                zip_codes_not_in=zip_codes_not_in,
            ),
            order_by=order_by,
            direction=direction,
            page=page,
            per_page=per_page,
        )

        return users, pagination

    async def get_by_id(
        self,
        id: int,
        session: Optional[AsyncSession] = None,
    ) -> Optional[User]:
        user = await self._select(
            session=session,
            model=User,
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
        )

        return user

    async def create(
        self,
        data: UserCreate,
        flush: bool = False,
        commit: bool = True,
        session: Optional[AsyncSession] = None,
    ) -> User:
        user = await self._add(
            session=session,
            model=User,
            values={
                User.email.key: data.email,
                User.hashed_password.key: data.hashed_password,
                User.full_name.key: data.full_name,
            },
            flush=flush,
            commit=commit,
        )

        return user

    async def create_all(
        self,
        data: List[UserCreate],
        flush: bool = False,
        commit: bool = True,
        session: Optional[AsyncSession] = None,
    ) -> Sequence[User]:
        users = await self._add_all(
            session=session,
            model=User,
            values=[
                {
                    User.email.key: item.email,
                    User.hashed_password.key: item.hashed_password,
                    User.full_name.key: item.full_name,
                }
                for item in data
            ],
            flush=flush,
            commit=commit,
        )

        return users

    async def patch_email(
        self,
        id: int,
        email: str,
        flush: bool = False,
        commit: bool = True,
        session: Optional[AsyncSession] = None,
    ) -> User:
        user = await self._update(
            session=session,
            model=User,
            values={
                User.email.key: email,
            },
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
            flush=flush,
            commit=commit,
        )

        return user

    async def patch_disable(
        self,
        ids: List[int],
        flush: bool = False,
        commit: bool = True,
        session: Optional[AsyncSession] = None,
    ) -> List[User]:
        users = await self._update_all(
            session=session,
            model=User,
            values={
                User.is_active.key: False,
            },
            filters={
                User.id: {
                    Operators.IN: ids,
                },
            },
            flush=flush,
            commit=commit,
        )

        return users

    async def delete(
        self,
        id: int,
        flush: bool = False,
        commit: bool = True,
        session: Optional[AsyncSession] = None,
    ) -> bool:
        is_deleted = await self._delete(
            session=session,
            model=User,
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
            flush=flush,
            commit=commit,
        )

        return is_deleted

    async def delete_all(
        self,
        ids: List[int],
        flush: bool = False,
        commit: bool = True,
        session: Optional[AsyncSession] = None,
    ) -> bool:
        is_deleted = await self._delete_all(
            session=session,
            model=User,
            filters={
                User.id: {
                    Operators.IN: ids,
                },
            },
            flush=flush,
            commit=commit,
        )

        return is_deleted
```
To create an async service, you just have to inherit your class from AsyncService.

```
# MODULES
from logging import Logger
from typing import List, Optional, Tuple

# SQLALCHEMY
from sqlalchemy.ext.asyncio import AsyncSession

# PYSQL_REPO
from pysql_repo.asyncio import AsyncService, with_async_session

# REPOSITORIES
from tests.repositories.user.async_user_repository import AsyncUserRepository

# MODELS
from tests.models.schemas.user import UserCreate, UserRead


class AsyncUserService(AsyncService[AsyncUserRepository]):
    def __init__(
        self,
        user_repository: AsyncUserRepository,
        logger: Logger,
    ) -> None:
        super().__init__(
            repository=user_repository,
        )
        self._logger = logger

    @with_async_session()
    async def get_users(
        self,
        session: Optional[AsyncSession] = None,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
    ) -> List[UserRead]:
        users = await self._repository.get_all(
            ids_in=ids_in,
            ids_not_in=ids_not_in,
            emails_iin=emails_iin,
            emails_in=emails_in,
            emails_not_iin=emails_not_iin,
            emails_not_in=emails_not_in,
            email_ilike=email_ilike,
            email_like=email_like,
            email_not_ilike=email_not_ilike,
            email_not_like=email_not_like,
            email_equal=email_equal,
            email_iequal=email_iequal,
            email_different=email_different,
            email_idifferent=email_idifferent,
            zip_codes_in=zip_codes_in,
            zip_codes_not_in=zip_codes_not_in,
            is_active_equal=is_active_equal,
            load_addresses=load_addresses,
            load_city=load_city,
            order_by=order_by,
            direction=direction,
            session=session,
        )

        return [UserRead.model_validate(item) for item in users]

    @with_async_session()
    async def get_users_paginate(
        self,
        page: int,
        per_page: int,
        ids_in: Optional[List[int]] = None,
        ids_not_in: Optional[List[int]] = None,
        emails_iin: Optional[List[str]] = None,
        emails_in: Optional[List[str]] = None,
        emails_not_iin: Optional[List[str]] = None,
        emails_not_in: Optional[List[str]] = None,
        email_ilike: Optional[List[str]] = None,
        email_like: Optional[List[str]] = None,
        email_not_ilike: Optional[List[str]] = None,
        email_not_like: Optional[List[str]] = None,
        email_equal: Optional[str] = None,
        email_iequal: Optional[str] = None,
        email_different: Optional[str] = None,
        email_idifferent: Optional[str] = None,
        zip_codes_in: Optional[List[int]] = None,
        zip_codes_not_in: Optional[List[int]] = None,
        is_active_equal: Optional[bool] = None,
        load_addresses: bool = True,
        load_city: bool = True,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None,
    ) -> Tuple[List[UserRead], str]:
        users, pagination = await self._repository.get_paginate(
            page=page,
            per_page=per_page,
            ids_in=ids_in,
            ids_not_in=ids_not_in,
            emails_iin=emails_iin,
            emails_in=emails_in,
            emails_not_iin=emails_not_iin,
            emails_not_in=emails_not_in,
            email_ilike=email_ilike,
            email_like=email_like,
            email_not_ilike=email_not_ilike,
            email_not_like=email_not_like,
            email_equal=email_equal,
            email_iequal=email_iequal,
            email_different=email_different,
            email_idifferent=email_idifferent,
            zip_codes_in=zip_codes_in,
            zip_codes_not_in=zip_codes_not_in,
            is_active_equal=is_active_equal,
            load_addresses=load_addresses,
            load_city=load_city,
            order_by=order_by,
            direction=direction,
            session=session,
        )

        users = [UserRead.model_validate(item) for item in users]

        return users, pagination

    @with_async_session()
    async def get_user_by_id(
        self,
        id: int,
        session: Optional[AsyncSession] = None,
    ) -> UserRead:
        user = await self._repository.get_by_id(
            id=id,
            session=session,
        )

        if user is None:
            return None

        return UserRead.model_validate(user)

    @with_async_session()
    async def create_user(
        self,
        data: UserCreate,
        session: Optional[AsyncSession] = None,
    ) -> UserRead:
        user = await self._repository.create(
            data=data,
            flush=True,
            session=session,
        )

        return UserRead.model_validate(user)

    @with_async_session()
    async def create_users(
        self,
        data: List[UserCreate],
        session: Optional[AsyncSession] = None,
    ) -> List[UserRead]:
        users = await self._repository.create_all(
            data=data,
            flush=True,
            session=session,
        )

        return [UserRead.model_validate(user) for user in users]

    @with_async_session()
    async def patch_email(
        self,
        id: int,
        email: str,
        session: Optional[AsyncSession] = None,
    ) -> UserRead:
        user = await self._repository.patch_email(
            id=id,
            email=email,
            flush=True,
            session=session,
        )

        return UserRead.model_validate(user)

    @with_async_session()
    async def patch_disable(
        self,
        ids: List[int],
        session: Optional[AsyncSession] = None,
    ) -> List[UserRead]:
        users = await self._repository.patch_disable(
            ids=ids,
            flush=True,
            session=session,
        )

        return [UserRead.model_validate(user) for user in users]

    @with_async_session()
    async def delete_by_id(
        self,
        id: int,
        session: Optional[AsyncSession] = None,
    ) -> bool:
        return await self._repository.delete(
            id=id,
            flush=True,
            session=session,
        )

    @with_async_session()
    async def delete_by_ids(
        self,
        ids: List[int],
        session: Optional[AsyncSession] = None,
    ) -> bool:
        return await self._repository.delete_all(
            ids=ids,
            flush=True,
            session=session,
        )
```