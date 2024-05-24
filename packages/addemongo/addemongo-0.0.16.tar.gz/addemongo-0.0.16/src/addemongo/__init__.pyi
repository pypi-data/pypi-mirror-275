from .__version__ import __version__ as __version__
from .builders import AggregationBuilder as AggregationBuilder, QueryBuilder as QueryBuilder
from .main import MongoConnection as MongoConnection

__all__ = ['__version__', 'MongoConnection', 'QueryBuilder', 'AggregationBuilder']

VERSION = __version__
