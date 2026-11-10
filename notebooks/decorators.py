# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Dekoratory w Pythonie

# %% [markdown]
# ## Podstawowa idea dekoratorów

# %%
def my_decorator(func):

    def wrapper():
        my_character = '\u2764'
        print(my_character * 10)
        func()
        print(my_character * 10)

    return wrapper



# %%
@my_decorator
def hello():
    print('Hello!')

# Powyższy kod jest równoważny czemuś takiemu:

# def hello():
#     print('Hello!')

# hello = my_decorator(hello)


# %%
hello()


# %% [markdown]
# ## Funkcje z argumentami

# %%
from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        my_character = '\u2764'
        print(my_character * 10)
        result = func(*args, **kwargs)
        print(my_character * 10)
        return result

    return wrapper


# %%
@my_decorator
def add(a, b):
    """Adds two numbers"""
    return a+b


# %%
add(2, 3)


# %%
@my_decorator
def power_tower(a, b, c):
    """Computes power tower"""
    return a ** b ** c


# %%
power_tower(2, 3, 4)

# %%

# %%