# Metadata Module Documentation

## Overview

The `Metadata` module provides a flexible and extensible way to manage metadata for datasets or objects. It leverages `OmegaConf` for hierarchical configuration management and includes features like freezing, merging, and serialization of metadata.

---

## Classes

### `Metadata`
A class to manage metadata for datasets or objects.

#### **Constructor**
````python
Metadata(instance_set: bool = False, **kwargs)
````

- **Parameters:**
  - `instance_set` (bool): If `True`, the metadata will be set as an instance variable. Default is `False`.
  - `**kwargs`: Additional keyword arguments to initialize the metadata.

- **Properties**
  - `metadata`: Returns the metadata object

- **Methods**
  - ``add_metadata(key: str, value: Any) -> None``: Adds a new metadata key-value pair.
  - ``get_metadata(key: str, default: Any = None) -> Any``: Retrieves the value of a metadata key.
  - ``update_metadata(key: str, value: Any, create_new: bool = True) -> None``: Updates an existing metadata key or creates a new one if allowed.
  - ``remove_metadata(key: str) -> None``: Removes a metadata key.
  - ``clear_metadata() -> None``: Clears all metadata.
  - ``freeze_metadata(fallover: bool = False) -> None``: Freezes metadata to prevent modifications.
  - ``unfreeze_metadata() -> None``: Unfreezes metadata to allow modifications.
  - ``as_dict() -> dict``: Returns metadata as a standard dictionary.
  - ``merge_metadata(update_dict: dict) -> None``: Merges a dictionary into the metadata.
  - ``to_yaml() -> str``: Serializes metadata to a YAML string.
  - ``to_json() -> str``: Serializes metadata to a JSON string.

## Functions

### apply_metadata_mixin
A mixin function to add metadata functionality to any object.

````python
apply_metadata_mixin(target_obj, instance_set: bool = False, **kwargs)
````

**Parameters**:
  - ``target_obj``: The object to which metadata functionality is added.
  - ``instance_set (bool)``: If True, initializes instance metadata with default values.
  - ``kwargs``: Initial metadata as key-value pairs.

## Example Usage
