import typing


Unset = ...


async def post_join[LI: object, RI: object, K: typing.Any](
    _attribute_: str,
    _from_: typing.Callable[[set[K]], typing.Coroutine[typing.Any, typing.Any, typing.Iterable[RI]]],
    _where_: typing.Callable[[RI], K],
    _equal_: typing.Callable[[LI], K],
    _source_: list[LI],
    /,
    many = False,
    default = Unset,
) -> None:
    """
    Joins list of subrecords from function to list of record by `_attribute_`.
    Group subrecords if many is True.
    Excludes record from `source` if subrecord not found and `default` is unset.

    ```python
    class Author:
        id: UUID
        full_name: str

    class Book:
        id: UUID
        name: str
        author_id: UUID

    async def get_authors(
        ids: set[UUID],
    ) -> list[Author]:
        '''Returns list of authors'''

    books = [<list of books>]
    await post_join(
        'authors',
        get_authors,
        lambda author: author.id,
        lambda book: book.author_id,
        books,
    )
    for b in books:
        list_of_authors = ', '.join([author.full_name for author in b.authors])
        print(f'book {b.name} published by {list_of_authors}')
    ```
    """
    source_map = {}
    for source_item in _source_:
        fkey = _equal_(source_item)
        source_map[fkey] = source_item
        setattr(source_item, _attribute_, default)

    source_fkeys = set(source_map.keys())
    for right_item in await _from_(source_fkeys):
        fkey = _where_(right_item)

        source_item = source_map.get(fkey)
        if source_item is None:
            continue

        if not many:
            setattr(source_item, _attribute_, right_item)
            continue

        nested_items = getattr(source_item, _attribute_, None)
        if nested_items is None:
            nested_items = []
            setattr(source_item, _attribute_, nested_items)
        nested_items.append(right_item)

    if default is Unset:
        n = len(_source_)
        i = 0
        while n > i:
            source_item = _source_[i]
            nested_items = getattr(source_item, _attribute_)
            if nested_items is Unset:
                n -= 1
                _source_.pop(i)
            else:
                i += 1
