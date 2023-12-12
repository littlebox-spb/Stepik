# Реализуйте декоратор singleton


def singleton(cls):
    class NewCls:
        instance = None

        def __new__(*args, **kwargs):
            if not NewCls.instance:
                NewCls.instance = cls()
            return NewCls.instance

    return NewCls


@singleton
class Logger:
    pass


@singleton
class AppConfig:
    pass


@singleton
class SMTPServerConfig:
    pass


log = Logger()
app_conf = AppConfig()
app_conf_2 = AppConfig()
smtp_conf = SMTPServerConfig()
assert log is Logger()
assert app_conf is app_conf_2
assert smtp_conf is SMTPServerConfig()
assert log is not app_conf
assert log is not smtp_conf
assert app_conf is not smtp_conf
print("Good")


# class Logger:
#     log_level = ""

#     def __new__(cls, *args, **kwargs):
#         if not Logger.log_level:
#             log = super(Logger, cls).__new__(cls)
#             Logger.log_level = "INFO"
#         return Logger

#     @classmethod
#     def set_level(cls, log_level):
#         if not cls.log_level:
#             raise (ValueError("The instance has not created"))
#         else:
#             cls.log_level = log_level

#     @staticmethod
#     def get_logger():
#         if not Logger.log_level:
#             log = Logger.__new__(Logger)
#         return Logger


# logger_1 = Logger.get_logger()
# print(logger_1.log_level)  # Выведет "INFO"
# Logger.set_level("DEBUG")
# print(logger_1.log_level)  # Выведет "DEBUG"

# logger_2 = Logger.get_logger()
# print(logger_2.log_level)  # Выведет "DEBUG"
# print(logger_2 is logger_1)
# ------------------------------------------------
# logger_1 = Logger()
# print(logger_1.log_level)  # Выведет "INFO"

# logger_2 = Logger.get_logger()
# logger_2.set_level("DEBUG")

# print(logger_1.log_level)  # Выведет "DEBUG"
# print(logger_2.log_level)  # Выведет "DEBUG"
# print(logger_2 is logger_1)
# ------------------------------------------------
# try:
#     logger_1 = Logger.set_level("DEBUG")
# except ValueError as ex:
#     print(ex)
