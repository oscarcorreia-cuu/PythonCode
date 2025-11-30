# Basic demo decorator

# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs...")
#         func()
#         print("After the function runs...")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello!")

# greet()

# # Another example using logging decorator
# def log(func):
#     def wrapper():
#         print(f"Running {func.__name__}...")
#         func()
#         print(f"Finished {func.__name__}")
#     return wrapper

# @log
# def say_hello():
#     print("Hello, world!")

# say_hello()

# Using a decorator for timing
# import time

# def timing_decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"{func.__name__} took {end - start:.4f} seconds")
#     return wrapper

# @timing_decorator
# def slow_function():
#     print("2 second timer in progress ...")
#     time.sleep(2)
#     print("Done!")

# slow_function()

# Decorator for logging in a user system
# def require_login(func):
#     def wrapper(user):
#         if not user.get("logged_in"):
#             print("Access denied. Please log in.")
#             return
#         return func(user)
#     return wrapper

# @require_login
# def view_profile(user):
#     print(f"Welcome {user['name']}! Here is your profile.")

# view_profile({"name": "Oscar", "logged_in": False})
# view_profile({"name": "Oscar", "logged_in": True})

# A decroatror with arguments
# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hello():
#     print("Hello!")

# say_hello()