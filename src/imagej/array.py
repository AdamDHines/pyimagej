import xarray as xr


@xr.register_dataarray_accessor("img")
class ImgAccessor:
    def __init__(self, xarr):
        self._data = xarr

    @property
    def is_rgb(self):
        return


@xr.register_dataarray_accessor("metadata")
class MetadataAccessor:
    def __init__(self, xarr):
        self._data = xarr
        self._metadata = None

    @property
    def axes(self):
        """
        Returns a tuple of the ImageJ axes.

        :return: A Python tuple of the ImageJ axes.
        """
        return (
            tuple(self._metadata.get("scifio.metadata.image").get("axes"))
            if "scifio.metadata.image" in self._metadata
            else None
        )

    def set(self, metadata: dict):
        """
        Set the metadata of the parent xarray.DataArray.

        :param metadata: A Python dict representing the image metadata.
        """
        self._metadata = metadata

    def get(self):
        """
        Get the metadata dict of the the parent xarray.DataArray.

        :return: A Python dict representing the image metadata.
        """
        return self._metadata

    def tree(self):
        """
        Print a tree of the metadata of the parent xarray.DataArray.
        """
        self._print_dict_tree(self._metadata)

    def _print_dict_tree(self, dictionary, indent="", prefix=""):
        for idx, (key, value) in enumerate(dictionary.items()):
            if idx == len(dictionary) - 1:
                connector = "└──"
            else:
                connector = "├──"
            print(indent + connector + prefix + " " + str(key))
            if isinstance(value, dict):
                if idx == len(dictionary) - 1:
                    self._print_dict_tree(value, indent + "    ", prefix="── ")
                else:
                    self._print_dict_tree(value, indent + "│   ", prefix="── ")
