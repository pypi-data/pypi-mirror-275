class LambdaDict(dict):
    """
    The LambdaDict class is a subclass of the built-in dict class in Python. It provides a way to define a default value for missing keys in the dictionary. This default value can be either a constant value or a callable function that accepts the missing key as an argument.

    ## Usage

    ```python
    # Initialize a LambdaDict with a default value of 0
    my_dict = LambdaDict(default=0)

    # Access a missing key, which will return the default value of 0
    value = my_dict["missing_key"]

    # Initialize a LambdaDict with a default function that returns the key multiplied by 2
    my_dict = LambdaDict(default=lambda key: key * 2)

    # Access a missing key, which will return the key multiplied by 2
    value = my_dict["missing_key"]
    ```

    ## Parameters

    - content: (Optional) A dictionary or iterable of key-value pairs to initialize the LambdaDict.
    - default: (Optional) The default value to return for missing keys. This can be either a constant value or a callable function that accepts the missing key as an argument. If default is not provided, each missing key will be returned unchanged.

    ## Methods

    - pop(self, key): This method removes the specified key and returns its value. If the key is not found, it returns None.

    ##Properties

    - default: This property gets or sets the default value for missing keys.

    ## Notes

    - The default attribute can be set to a constant value or a callable function.
    - If the default attribute is set to a callable function, the function will be called with the missing key as an argument.
    - The __missing__ method is called automatically when a key is not found in the dictionary.
    - The pop method can be used to remove keys from the dictionary. If the key is not found, it will return None.
    """
    def __init__(self, content = None, default = None):
        if content is None:
            super().__init__()
        else:
            super().__init__(content)
        if default is None:
            default = lambda missing_key: missing_key
        self.default = default # sets self._default

    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, val):
        if callable(val):
            self._default = val
        else: # constant value
            self._default = lambda missing_key: val

    def __missing__(self, x):
        return self.default(x)

    def pop(self, key):
        return super().pop(key, None)
