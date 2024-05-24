"""Defines the AdsorptionSite, SiteFinder, and MOFSiteFinder classes."""

from abc import ABC
from abc import abstractmethod
from collections.abc import Iterable
from collections.abc import Sequence

import ase
import numpy as np
from numpy import cross
from numpy import dot
from numpy.linalg import norm


# pylint:disable=too-few-public-methods
class SiteAlignment:
    """An alignment that an adsorbate can assume on a site.

    Attributes:
        vector: A numpy.array representing the alignment vector as a unit
            vector.
        description: A string describing the site alignment.
    """

    def __init__(
        self, alignment_vector: Sequence[float], description: str
    ) -> None:
        vector = np.array(alignment_vector)
        self.vector = vector / norm(vector)
        self.description = description


# pylint:disable=too-few-public-methods
class AdsorptionSite:
    """An adsorption site for an adsorbate.

    Attributes:
        location: A numpy.array representing the location of the adsorption
            site.
        description: A description of the adsorption site as a string.
        alignments: A list of SiteAlignment objects defining alignments for
            the site.
        surface_norm: A numpy.array representing the unit normal vector for
        the surface hosting the adsorption site.
    """

    def __init__(
        self,
        location: Sequence[float],
        description: str,
        alignments: Iterable[SiteAlignment],
        surface_norm: Sequence[float],
    ) -> None:
        self.location = np.array(location)
        self.description = description
        self.alignments = alignments
        vector = np.array(surface_norm)
        self.surface_norm = vector / norm(vector)


class MOFSite(AdsorptionSite):
    """An adsorption site within a MOF.

    Attributes:
        location: A numpy.array representing the location of the adsorption
            site.
        description: A description of the adsorption site as a string.
        alignments: A list of SiteAlignment objects defining alignments for
            the site.
        surface_norm: A numpy.array representing the normal vector for the
            surface hosting the adsorption site.
        intermediate_alignments: A boolean indicating whether or not to
            consider intermediate alignments.
    """

    # pylint:disable=too-many-arguments
    def __init__(
        self,
        location: Sequence[float],
        description: str,
        alignment_atoms: Iterable[ase.Atom],
        site_anchor: Sequence[float],
        surface_norm: Sequence[float],
        intermediate_alignments: bool = False,
    ) -> None:
        self.intermediate_alignments = intermediate_alignments
        alignments = self.create_alignments(alignment_atoms, site_anchor)
        super().__init__(location, description, alignments, surface_norm)

    def create_alignments(
        self, alignment_atoms: Iterable[ase.Atom], site_anchor: Sequence[float]
    ) -> list[SiteAlignment]:
        """Creates the SiteAlignment objects for a MOFSite.

        Args:
            alignment_atoms: An iterable containing ase.Atom instances which
                will be used to define alignment directions.
            site_anchor: A sequence of floats representing a reference location
                using for defining alignment directions. This is usually the
                position of the metal atom in the site.

        Returns:
            A list of SiteAlignment instances representing the alignments for a
            MOFSite instance.
        """
        alignments = []
        colinear_vectors = []
        added_elements = []
        for atom in alignment_atoms:
            vector = atom.position - site_anchor
            vector = vector / norm(vector)
            colinear_vectors.append(vector)
            description = f"colinear with {atom.symbol}"
            if atom.symbol not in added_elements:
                alignments.append(SiteAlignment(vector, description))
                added_elements.append(atom.symbol)

        if self.intermediate_alignments:
            alignments.extend(
                self.create_intermediate_alignments(colinear_vectors)
            )

        return alignments

    def create_intermediate_alignments(
        self, colinear_vectors: Iterable[SiteAlignment]
    ) -> list[SiteAlignment]:
        # TODO! Order collinear alignments by angle and define intermediate
        # TODO! alignments as bisectors
        parallel_line = 0.5 * (colinear_vectors[0] + colinear_vectors[1])
        parallel_line = parallel_line / norm(parallel_line)

        perpendicular_line = (
            colinear_vectors[0]
            - dot(colinear_vectors[0], parallel_line) * parallel_line
        )
        perpendicular_line = perpendicular_line / norm(perpendicular_line)
        return [
            SiteAlignment(parallel_line, "parallel"),
            SiteAlignment(perpendicular_line, "perpendicular"),
        ]


# pylint:disable=too-few-public-methods
class SiteFinder(ABC):
    """An abstract base class for objects which find adsorption sites
    for particular surfaces.

    Subclasses must define the abstract method "sites" which returns all
    adsorption sites for a given structure.
    """

    @abstractmethod
    def sites(self) -> Iterable[AdsorptionSite]:
        """Subclasses should override this method."""


class MOFSiteFinder(SiteFinder):
    """A SiteFinder subclass which finds adsorption sites on MOF surfaces.

    Currently, the atoms bonded to the metal within the SBU must possess tags
    of 1 and the metal must possess a tag of 2 for the implementation to work
    correctly.

    Args:
        structure: An ase.Atoms object representing a metal-organic framework.
    """

    def __init__(
        self, structure: ase.Atoms, *, between_linkers: bool = False
    ) -> None:
        super().__init__()
        self.structure = structure
        self.between_linkers = between_linkers

    def sites(self) -> list[AdsorptionSite]:
        """Determines all unique SBU adsorption sites for a given MOF.

        Note that the AdsorptionSites are defined such that the first and
        second elements in their "alignment_atoms" attribute are linker atoms
        and the third element is the metal.

        Returns:
            A list of AdsorptionSite instances representing the SBU adsorption
            sites of the given MOF.
        """
        sites = self.create_linker_sites()
        sites.append(self.create_metal_site())
        if self.between_linkers:
            sites.append(self.create_between_linker_site())

        return sites

    @property
    def adjacent_linkers(self) -> list[ase.Atom]:
        """A list of ase.Atom instances representing two adjacent linker
        atoms."""
        linkers = [atom for atom in self.structure if atom.tag == 1]

        closest_linker = linkers[1]
        for linker in linkers[1:]:
            if norm(linkers[0].position - linker.position) < norm(
                linkers[0].position - closest_linker.position
            ):
                closest_linker = linker

        return [linkers[0], closest_linker]

    @property
    def sbu_metal(self) -> ase.Atom:
        """An ase.Atom instance representing the metal atom within the SBU of
        the MOF."""
        for atom in self.structure:
            if atom.tag == 2:
                return atom

        raise ValueError(
            "No metal atom tagged. (Metal atom must be tagged with 2.)"
        )

    @property
    def surface_norm(self) -> np.array:
        """A unit vector normal to the plane determined by two adjacent linker
        atoms and the metal within the SBU.
        """
        # Calculate upwards-pointing norm vector
        vector1 = self.adjacent_linkers[0].position - self.sbu_metal.position
        vector2 = self.adjacent_linkers[1].position - self.sbu_metal.position
        norm_vector = cross(vector1, vector2)

        if dot(norm_vector, [0, 0, 1]) < 0:
            norm_vector = -norm_vector

        return norm_vector / norm(norm_vector)

    def create_linker_sites(self) -> list[MOFSite]:
        """Returns a list of MOFSite instances representing adsorption sites
        centred on the MOF linker atoms."""
        linkers = self.adjacent_linkers
        sbu_metal = self.sbu_metal
        surface_norm = self.surface_norm

        # Define unique linker sites
        linker_sites = [
            MOFSite(
                linkers[0].position,
                f"on {linkers[0].symbol} linker",
                linkers,
                sbu_metal.position,
                surface_norm,
                True,
            )
        ]
        if linkers[0].symbol != linkers[1].symbol:
            linker_sites.append(
                MOFSite(
                    linkers[1].position,
                    f"on {linkers[1].symbol} linker",
                    linkers,
                    sbu_metal.position,
                    surface_norm,
                    True,
                )
            )

        return linker_sites

    def create_metal_site(self) -> MOFSite:
        """Returns a MOFSite instance representing an adsorption site centred
        on the MOF metal atom."""
        sbu_metal = self.sbu_metal
        linkers = self.adjacent_linkers
        surface_norm = self.surface_norm

        return MOFSite(
            sbu_metal.position,
            f"on {sbu_metal.symbol}",
            linkers,
            sbu_metal.position,
            surface_norm,
            True,
        )

    def create_between_linker_site(self) -> MOFSite:
        """Returns a MOFSite instance representing an adsorption site centred
        between the MOF linker atoms."""
        sbu_metal = self.sbu_metal
        linkers = self.adjacent_linkers
        surface_norm = self.surface_norm

        return MOFSite(
            0.5 * (linkers[0].position + linkers[1].position),
            "between linkers",
            linkers,
            sbu_metal.position,
            surface_norm,
            True,
        )
