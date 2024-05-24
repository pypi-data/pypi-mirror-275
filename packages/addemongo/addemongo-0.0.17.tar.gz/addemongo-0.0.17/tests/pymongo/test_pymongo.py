class PymongoSuite:
    def test_pymongo_import(self):
        try:
            import pymongo
        except ImportError:
            raise ImportError("pymongo is not installed")

        assert pymongo.__name__ == "pymongo"
