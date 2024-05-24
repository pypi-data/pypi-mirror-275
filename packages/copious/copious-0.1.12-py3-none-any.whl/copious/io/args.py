from typing import Sequence, Any
import argparse

class KeyValueAction(argparse.Action):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Sequence[Any],
        option_string: str = None,
    ) -> None:
        setattr(namespace, self.dest, {})
        for value in values:
            parts = value.split("=")
            if len(parts) != 2:
                raise argparse.ArgumentError(self, f"Invalid key-value pair: {value}. A key and value must be separated by an '='.")
            key, value = parts
            getattr(namespace, self.dest)[key] = value

__all__ = ["KeyValueAction"]
