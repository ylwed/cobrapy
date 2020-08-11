"""Provide the abstract base summary class."""


import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Union


if TYPE_CHECKING:
    from pandas import DataFrame

    from cobra import Model, Solution


logger = logging.getLogger(__name__)


class Summary(ABC):
    """
    Define the abstract base summary.

    See Also
    --------
    MetaboliteSummary
    ReactionSummary
    ModelSummary

    """

    def __init__(self, **kwargs,) -> None:
        """
        Initialize a summary.

        Other Parameters
        ----------------
        kwargs :
            Further keyword arguments are passed on to the parent class.

        """
        super().__init__(**kwargs)
        self._flux = None

    @abstractmethod
    def _generate(
        self,
        model: "Model",
        solution: Optional["Solution"],
        fva: Optional[Union[float, "DataFrame"]],
    ) -> None:
        """
        Prepare the data for the summary instance.

        Parameters
        ----------
        model : cobra.Model
            The metabolic model for which to generate a metabolite summary.
        solution : cobra.Solution, optional
            A previous model solution to use for generating the summary. If
            ``None``, the summary method will generate a parsimonious flux
            distribution.
        fva : pandas.DataFrame or float, optional
            Whether or not to include flux variability analysis in the output.
            If given, `fva` should either be a previous FVA solution matching the
            model or a float between 0 and 1 representing the fraction of the
            optimum objective to be searched.

        """
        raise NotImplementedError(
            "This method needs to be implemented by the subclass."
        )

    def __str__(self) -> str:
        """Return a string representation of the summary."""
        return self.to_string()

    def _repr_html_(self) -> str:
        """Return a rich HTML representation of the summary."""
        return self.to_html()

    @abstractmethod
    def to_string(
        self,
        names: bool = False,
        threshold: float = 1e-6,
        float_format: str = ".4G",
        column_width: int = 79,
    ) -> str:
        """
        Return a pretty string representation of the summary.

        Parameters
        ----------
        names : bool, optional
            Whether or not elements should be displayed by their common names
            (default False).
        threshold : float, optional
            Hide fluxes below the threshold from being displayed (default 1e-6).
        float_format : str, optional
            Format string for floats (default '.4G').
        column_width : int, optional
            The maximum column width for each row (default 79).

        Returns
        -------
        str
            The summary formatted as a pretty string.

        """
        raise NotImplementedError(
            "This method needs to be implemented by the subclass."
        )

    @abstractmethod
    def to_html(
        self, names: bool = False, threshold: float = 1e-6, float_format: str = ".4G"
    ) -> str:
        """
        Return a rich HTML representation of the metabolite summary.

        Parameters
        ----------
        names : bool, optional
            Whether or not elements should be displayed by their common names
            (default False).
        threshold : float, optional
            Hide fluxes below the threshold from being displayed (default 1e-6).
        float_format : str, optional
            Format string for floats (default '.4G').

        Returns
        -------
        str
            The summary formatted as HTML.

        """
        raise NotImplementedError(
            "This method needs to be implemented by the subclass."
        )

    def to_frame(self) -> "DataFrame":
        """Return the a data frame representation of the summary."""
        return self._flux.copy()
