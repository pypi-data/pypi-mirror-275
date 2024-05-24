class MotorSuite:

    def test_motor_import(self):
        try:
            import motor
        except ImportError:
            raise ImportError("motor is not installed")

        assert motor.__name__ == "motor"
