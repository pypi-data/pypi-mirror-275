from __future__ import annotations

__all__ = ("AggregationBuilder", "QueryBuilder")

from typing import Any, Callable, List


class AggregationBuilder:
    def __init__(self) -> None:
        self.__aggregation_list: List[dict[str, Any]]

    def set_group(
        self,
        query: dict[str, Any],
        body: dict[str, Any],
        condition: Callable[[], bool] = lambda: True,
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$group": {"_id": query, **body}})

        return self

    def set_match(
        self, query: dict[str, Any], condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$match": query})

        return self

    def set_project(
        self, query: dict[str, Any], condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$project": query})

        return self

    def set_sort(
        self, key: str, by: int, condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$sort": {key: by}})

        return self

    def set_limit(
        self, limit: int, condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$limit": limit})

        return self

    def set_skip(
        self, skip: int, condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$skip": skip})

        return self

    def set_unwind(
        self, key: str, condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$unwind": key})

        return self

    def set_lookup(
        self,
        key: str,
        from_collection: str,
        local_field: str,
        foreign_field: str,
        as_field: str,
        condition: Callable[[], bool] = lambda: True,
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append(
                {
                    "$lookup": {
                        "from": from_collection,
                        "localField": local_field,
                        "foreignField": foreign_field,
                        "as": as_field,
                    }
                }
            )

        return self

    def set_add_fields(
        self, query: dict[str, Any], condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$addFields": query})

        return self

    def set_facet(
        self, query: dict[str, Any], condition: Callable[[], bool] = lambda: True
    ) -> "AggregationBuilder":
        if condition():
            self.__aggregation_list.append({"$facet": query})

        return self

    def build(self) -> List[dict[str, Any]]:
        return self.__aggregation_list


class QueryBuilder:
    """
    Query builder for MongoDB queries/filtering.
    """

    def __init__(self) -> None:
        self.__query: dict[str, Any] = {}

    def set_equal(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = value

        return self

    def set_not_equal(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$ne": value}

        return self

    def set_greater_than(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$gt": value}

        return self

    def set_greater_than_or_equal(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$gte": value}

        return self

    def set_less_than(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$lt": value}

        return self

    def set_less_than_or_equal(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$lte": value}

        return self

    def set_in(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$in": value}

        return self

    def set_not_in(
        self, key: str, value: Any, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$nin": value}

        return self

    def set_regex(
        self,
        key: str,
        value: Any,
        case_sensivite: bool = True,
        condition: Callable[[], bool] = lambda: True,
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$regex": value}

            if not case_sensivite:
                self.__query[key]["$options"] = "i"

        return self

    def set_not_regex(
        self,
        key: str,
        value: Any,
        case_sensivite: bool = True,
        condition: Callable[[], bool] = lambda: True,
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$not": {"$regex": value}}

            if not case_sensivite:
                self.__query[key]["$options"] = "i"

        return self

    def set_element_match(
        self,
        key: str,
        query: QueryBuilder,
        condition: Callable[[], bool] = lambda: True,
    ) -> QueryBuilder:
        if condition():
            self.__query[key] = {"$elemMatch": query.build()}

        return self

    def set_or(
        self, *querys: QueryBuilder, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query["$or"] = [q.build() for q in querys]

        return self

    def set_and(
        self, *querys: QueryBuilder, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query["$and"] = [q.build() for q in querys]

        return self

    def set_nor(
        self, *querys: QueryBuilder, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query["$nor"] = [q.build() for q in querys]

        return self

    def update_query(
        self, query: dict[str, Any], condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query.update(query)

        return self

    def remove_key(
        self, key: str, condition: Callable[[], bool] = lambda: True
    ) -> QueryBuilder:
        if condition():
            self.__query.pop(key, None)

        return self

    def build(self) -> dict[str, Any]:
        return self.__query
