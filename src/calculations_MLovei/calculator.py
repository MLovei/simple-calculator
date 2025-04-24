class Calculator:
	"""A simple calculator that maintains a running total in memory.

    This calculator can perform basic arithmetic operations:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Taking the nth root of a number
    - Resetting the memory value

    Example:
        >>> c = Calculator()
        >>> c.add(69.715)
        69.715
        >>> c.sub(13.715)
        56.0
        >>> c.mult(2.5)
        140.0
        >>> c.div(7.5)
        18.6666666667
        >>> c.root(3)
        2.6527048053
    """

	def __init__(self, variable: float = 0.0, memory: float = 0.0) -> None:
		"""Initialize a Calculator instance.

        Args:
            variable (float, optional): Initial variable value. Defaults to 0.0.
            memory (float, optional): Initial memory value. Defaults to 0.0.

        Note:
            Non-numeric inputs will be converted to 0.0.
        """
		self.memory = float(memory) if isinstance(memory, (float, int)) else 0.0
		self.variable = float(variable) if isinstance(variable,
		                                              (float, int)) else 0.0

	def __str__(self) -> str:
		"""Return string representation of the Calculator instance.

        Returns:
            str: String showing the current memory value.
        """
		return f"Calculator value in memory = {self.memory}"

	def add(self, variable: float) -> float:
		"""Add the given value to memory.

        Args:
            variable (float): Value to add to memory.

        Raises:
            TypeError: If variable is not a number.

        Returns:
            float: Updated memory value, rounded to 10 decimal places.
        """
		if not isinstance(variable, (int, float)):
			raise TypeError("Expected an int or float")
		else:
			self.memory += float(variable)
		return round(self.memory, ndigits=10)

	def sub(self, variable: float) -> float:
		"""Subtract the given value from memory.

        Args:
            variable (float): Value to subtract from memory.

        Raises:
            TypeError: If variable is not a number.

        Returns:
            float: Updated memory value, rounded to 10 decimal places.
        """
		if not isinstance(variable, (int, float)):
			raise TypeError("Expected an int or float")
		else:
			self.memory -= float(variable)
		return round(self.memory, ndigits=10)

	def mult(self, variable: float) -> float:
		"""Multiply memory by the given value.

        Args:
            variable (float): Value to multiply memory by.

        Raises:
            TypeError: If variable is not a number.

        Returns:
            float: Updated memory value, rounded to 10 decimal places.
        """
		if not isinstance(variable, (int, float)):
			raise TypeError("Expected an int or float")
		else:
			self.memory *= float(variable)
		return round(self.memory, ndigits=10)

	def div(self, variable: float) -> float:
		"""Divide memory by the given value.

        Args:
            variable (float): Value to divide memory by.

        Raises:
            TypeError: If variable is not a number.
            ValueError: If variable is zero (division by zero).

        Returns:
            float: Updated memory value, rounded to 10 decimal places.
        """
		if not isinstance(variable, (int, float)):
			raise TypeError("Expected an int or float")
		elif variable == 0:
			raise ValueError(f"Division by {variable} is not possible")
		else:
			self.memory /= variable
		return round(self.memory, ndigits=10)

	def root(self, n: int = 2) -> float:
		"""Calculate the nth root of the memory value.

        Args:
            n (int, optional): Root to take. Defaults to 2 (square root).

        Raises:
            TypeError: If n is not an integer.
            ValueError: If memory is negative.

        Returns:
            float: Updated memory value, rounded to 10 decimal places.
        """
		if not isinstance(n, int):
			raise TypeError(f"Expected an int but got {type(n)}")
		elif self.memory < 0:
			raise ValueError(
				f"Root of negative number {self.memory} is not possible")
		else:
			self.memory = (self.memory) ** (1 / n)
		return round(self.memory, ndigits=10)

	def reset(self) -> float:
		"""Reset the memory to zero.

        Returns:
            float: The reset memory value (0.0).
        """
		self.memory = 0.0
		return self.memory


if __name__ == "__main__":
	import doctest

	print(doctest.testmod())
