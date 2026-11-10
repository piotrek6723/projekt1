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
# # Object oriented programming

# %%
class Car:
    name: str

    def __init__(self, name):

        if not isinstance(name, str):
            raise ValueError('Attribute name should have type str')

        if not name:
            self.name = 'Mercedes'
        else:
            self.name = name

    def which_country(self):

        match self.name:
            case 'Peugeot':
                return 'France'
            case 'Volkswagen' | 'Mercedes':
                return 'Germany'


class MyCar:
    pass


# %%
car1 = Car('Peugeot')
car2 = Car('Volkswagen')

# %%
car1.which_country()

# %%
car2.which_country()


# %% [markdown]
# ## Complex numbers

# %%
class ComplexNumber:
    """The class implements complex number (addition and multiplication of complex numbers)


    Attributes:
        real (float): real part of the complex number
        imag (float): imaginary part of the complex number

    """

    def __init__(self, real, imag):

        # Correctness check
        for name, variable in zip(('real', 'imag'), (real, imag)):
            try:
                variable = float(variable)
                exec(f'{name} = {variable}')
            except ValueError:
                raise ValueError(f'Attribute {name} should be convertible to float')

        self.real = real
        self.imag = imag

    def __eq__(self, other):

        return (self.real, self.imag) == (other.real, other.imag)

    def __add__(self, other):

        real = self.real + other.real
        imag = self.imag + other.imag

        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag

        return ComplexNumber(real, imag)

    def __repr__(self):
        return f'ComplexNumber({self.real}, {self.imag})'

    def __str__(self):

        # Default of imaginary part
        imag_part = 'i' if abs(self.imag) == 1 else f'{abs(self.imag)}*i'

        match (self.real, self.imag):
            case (real, 0):
                real_part = f'{real}'
                sign = ''
                imag_part = ''

            case (0, imag):
                real_part = ''
                sign = '-' if imag < 0 else ''

            case (real, imag):
                real_part = f'{real}'
                sign = '-' if imag < 0 else '+'

        result = f'{real_part}{sign}{imag_part}'
        return result


# %%
print(ComplexNumber(2, -1))

# %%
print(ComplexNumber(0, 2))

# %%
print(ComplexNumber(0, -2))

# %%
z1 = ComplexNumber(2.0, 3.0)

# %%
z2 = ComplexNumber(2, 3)

# %%
z1 == z2

# %%
z1 + z2

# %% [markdown]
# ## Print benchmark

# %%
z1 = ComplexNumber(0, 1)
z2 = ComplexNumber(2, 0)
z3 = ComplexNumber(2, -3)
z4 = ComplexNumber(0, -1)
z5 = ComplexNumber(3, 7)

# %%
print(z1)

# %%
print(z2)

# %%
print(z3)

# %%
print(z4)

# %%
print(z5)

# %% [markdown]
# ## Inheritance

# %%
from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def what_is_your_name(self):
        pass


# %%
class B(A):

    def say_hello(self):
        print('Hello')

    def what_is_your_name(self):
        print('My name is class B')


# %%
class_b_object = B()

# %%
class_b_object.say_hello()

# %%
class_b_object.what_is_your_name()

# %%