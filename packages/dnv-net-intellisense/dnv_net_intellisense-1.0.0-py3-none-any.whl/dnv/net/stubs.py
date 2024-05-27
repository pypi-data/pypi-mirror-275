import importlib.util
import os


def update():
    module_name = "System"
    file_name = "__init__.pyi"
    content_to_add = '''

# Start: IDisposable interface with intellisense support and type hinting

T = typing.TypeVar("T")

class IDisposable(metaclass=abc.ABCMeta):
    """Supports type hinting and intellisense in development environments."""

    def __enter__(self: T) -> T:
        ...

    def __exit__(self: T, exc_type, exc_value, traceback) -> None:
        ...

    def Dispose(self) -> None:
        ...

# End: IDisposable interface with intellisense support and type hinting
'''

    # Get the module specification
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print(f"INFO: Skipping stubs update as the module '{module_name}' not found.")
        return

    module_path = module_spec.origin
    folder_path = os.path.dirname(module_path)
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(folder_path):
        if os.path.isfile(file_path):
            with open(file_path, "a") as file:
                file.write(content_to_add)
            print("INFO: The stub is updated successfully.")
        else:
            print(
                f"INFO: Skipping stubs update as the file '{file_name}' not found in the module '{module_name}'."
            )
    else:
        print(f"INFO: Skipping stubs update as the folder '{folder_path}' not found.")
