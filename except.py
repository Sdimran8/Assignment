# if there is no exception raised & it is normal termination -- 1,2,3,4,5,6,8,9,11,12

# try:
#     print("outer try 1")#statment-1
#     print("outer try 2")#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except xxxx:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except yyyy:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

#--------------------------------------------------------------------------------#
# if there is exception at statement-2 & except block match 1,10,11,12
# try:
#     print("outer try 1")#statment-1
#     print(100/0)#statment-2
#     print("outer try 3")#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except xxxx:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError:
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

#--------------------------------------------------------------------------------#
# if there is exception in stataement-2 but not match except block 1 & 11.

# try:
#     print("statement-1")#statment-1
#     print(10/0)#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except xxxx:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except yyyy:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#--------------------------------------------------------------------------------#
# if exception raised at statement-5 and exception match 1,2,3,4,7,8,9,11,12

# try:
#     print("statement-1")#statment-1
#     print('statement-2')#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print(100/0)#statment-5
#         print("statement-6")#statment-6
#     except ZeroDivisionError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except yyyy:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#---------------------------------------------------------------------------#
# if exception raised at statement-5 inner is not,but outside block is matched 1,2,3,4,8,10,11,12

# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print(10/0)#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except ZeroDivisionError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#-------------------------------------------------------------#
# if exception raised at statement-5 but not match any handling 1,2,3,4,8,11.
# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print(10/0)#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except TypeError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#----------------------------------------------------------------#
# if exception raised at statement-7 not handled & exception statement-11 at finally-1,2,3,4,5,6,8,9
# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print(10/0)#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except TypeError:
#     print("statement-10")#statment-10
# finally:
#     print(20/0)#statment-11
# print("statement-12")#statment-12

#---------------------------------------------------------------------------------#
# if exception raised at statement-7 not handled 1,2,3,4,5,6,7,8,9,11,12
# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print(10/0)#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except TypeError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#--------------------------------------------------------------#

# if exception raised at statement-2 not handled 1,11
# try:
#     print("statement-1")#statment-1
#     print(10/0)#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except TypeError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#--------------------------------------------------------------------------#
# if exception raised in statement-1 exception handled 10,11,12
# try:
#     print(10/0)#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except ZeroDivisionError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#-------------------------------------------------------------------------#
# if ex in stat-7 & handled in 10  12345689,11,12
# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print(10/0)#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except ZeroDivisionError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#-----------------------------------------------------------------#
# if ex-3 & ex handl at 7    1,2,11
# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print(10/0)#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except ZeroDivisionError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except TypeError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#-------------------------------------------------------------------#
# if ex is at 6 & handled 12345789,11,12
# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print(10/0)#statment-6
#     except ZeroDivisionError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except TypeError:
#     print("statement-10")#statment-10
# finally:
#     print("statement-11")#statment-11
# print("statement-12")#statment-12

#---------------------------------------------------------------#
# if ex-11 at not handled 12345689

# try:
#     print("statement-1")#statment-1
#     print("statement-2")#statment-2
#     print("statement-3")#statment-3
#     try:
#         print("statement-4")#statment-4
#         print("statement-5")#statment-5
#         print("statement-6")#statment-6
#     except TypeError:
#         print("statement-7")#statment-7
#     finally:
#         print("statement-8")#statment-8
#     print("statement-9")#statment-9
# except ZeroDivisionError:
#     print("statement-10")#statment-10
# finally:
#     print(10/0)#statment-11
# print("statement-12")#statment-12