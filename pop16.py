# import time


# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))


# # ------------------------------------------------------


# class LoggableList(list, Loggable):
#     def append(self, lst):
#         super().append(lst)
#         self.log(lst)


# a = LoggableList([1, 2])
# print(a)
# a.append(7, 8)
# print(a)
