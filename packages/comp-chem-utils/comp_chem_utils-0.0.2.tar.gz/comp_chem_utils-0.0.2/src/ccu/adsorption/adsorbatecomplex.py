"""Defines the AdsorbateComplex and AdsorbateComplexFactory classes."""

from collections.abc import Iterator
import pathlib

import ase
from ase.io import read
import numpy as np
from numpy import dot
from numpy import ndarray
from numpy.linalg import norm

from ccu.adsorption import adsorbateorientation
from ccu.adsorption import adsorbates
from ccu.adsorption import sitefinder
from ccu.structure import axisfinder
from ccu.structure import geometry


# pylint:disable=too-few-public-methods
class AdsorbateComplex:
    """An adsorbate-surface complex.

    Attributes:
        structure_description: A string describing the surface structure.
        site_description: A string describing the adsorption site.
        orientation_description: A string describing the orientation of the
            adsorbate.
        structure: An ase.Atoms object of the adsorbate-surface complex.
    """

    def __init__(
        self,
        adsorbate_description: str,
        site_description: str,
        orientation_description: str,
        structure_desription: str,
        structure: ase.Atoms,
    ) -> None:
        self.structure_description = structure_desription
        self.adsorbate_description = adsorbate_description
        self.site_description = site_description
        self.orientation_description = orientation_description
        self.structure = structure

    def write(self, destination: pathlib.Path | None = None) -> pathlib.Path:
        """Writes the AdsorbateComplex object to an ASE .traj file.

        Args:
            destination: A pathlib.Path instance indicating the directory in
                which to write the .traj file. Defaults to the current working
                directory.

        Returns:
            A pathlib.Path instance indicating the path of the written .traj
            file.
        """
        if destination is None:
            destination = pathlib.Path.cwd()

        if self.orientation_description == "":
            description = (
                self.structure_description.replace(" ", "_"),
                self.adsorbate_description.replace(" ", "_"),
                self.site_description.replace(" ", "_"),
            )
        else:
            description = (
                self.structure_description.replace(" ", "_"),
                self.adsorbate_description.replace(" ", "_"),
                self.site_description.replace(" ", "_"),
                self.orientation_description.replace(" ", "_"),
            )

        filename = "_".join(description)
        index = 0
        while destination.joinpath(f"{filename}_{index}.traj").exists():
            index += 1

        self.structure.write(destination.joinpath(f"{filename}_{index}.traj"))
        return filename


class AdsorbateComplexFactory:
    """An AdsorbateComplex factory.

    Given an adsorbate, a structure, and various configuration specifications
    (e.g., "symmetric", "vertical"), an AdsorbateComplexFactory determines all
    of the adsorption sites and corresponding adsorbate configurations.

    Attributes:
        _adsorbate: An ase.Atoms instance representing the adsorbate.
        _structure: An ase.Atoms instance representing the surface structure.
        separation: How far (in Angstroms) the adsorbate should be placed from
            the surface.
        special_centres: A boolean indicating whether atom-centred
            placement will be used in addition to centre-of-mass placement.

            Note that in addition to be set to true, the ase.Atoms instance
            passed as the adsorbate argument must have the key 'special
            centres' in its info attribute. Further, this key must map to an
            iterable whose elements specify the indices of the atoms to be used
            to centre the adsorbate. If this key is not present in the info
            attribute, then the atom with index 0 will be used to centre the
            adsorbate.
        symmetric: A boolean indicating whether or not the adsorbate is to be
            treated as symmetric.
        vertical: A boolean indicating whether or not to consider vertical
            adsorption sites.
    """

    # pylint:disable=too-many-arguments
    def __init__(
        self,
        adsorbate: ase.Atoms,
        structure: ase.Atoms,
        separation: float = 1.8,
        special_centres: bool = False,
        symmetric: bool = False,
        vertical: bool = False,
    ) -> None:
        self._adsorbate = adsorbate
        self._structure = structure
        self.separation = separation
        self.symmetric = symmetric
        self.vertical = vertical
        self.special_centres = special_centres
        if special_centres and "special centres" not in adsorbate.info:
            self._adsorbate.info["special centres"] = (0,)

    @property
    def adsorbate(self) -> ase.Atoms:
        return self._adsorbate.copy()

    @property
    def structure(self) -> ase.Atoms:
        return self._structure.copy()

    def next_complex(
        self, site: sitefinder.AdsorptionSite, adsorbate_tag: int = -99
    ) -> Iterator[AdsorbateComplex]:
        """Yields next adsorbate-surface complex for a given site as an
        AdsorbateComplex.

        Args:
            site: A sitefinder.AdsorptionSite instance which represents the
                site for which to generate complexes.
            adsorbate_tag: An integer with which to tag the adsorbate to
                enable tracking. Defaults to -99.
        """
        orientations = self.adsorbate_orientations(site)

        for orientation in orientations:
            if len(self._adsorbate) > 1:
                oriented_adsorbate = self.orient_adsorbate(orientation)
            else:
                oriented_adsorbate = self.adsorbate

            # Tags to distinguish adsorbate from surface atoms (useful for
            # vibrational calculations)
            oriented_adsorbate.set_tags(adsorbate_tag)

            oriented_adsorbate.set_cell(self._structure.cell[:])

            centres: ndarray[np.floating] = [
                oriented_adsorbate.get_center_of_mass()
            ]

            if self.special_centres:
                for i in self._adsorbate.info["special centres"]:
                    new_centre: ndarray[np.floating] = (
                        oriented_adsorbate.positions[i]
                    )
                    if not any(
                        all(centre == new_centre) for centre in centres
                    ):
                        centres.append(new_centre)

            for centre in centres:
                adsorbate_to_place = oriented_adsorbate.copy()
                self.place_adsorbate(adsorbate_to_place, site, centre)

                # Add adsorbate to structure
                new_structure = self.structure
                new_structure.extend(adsorbate_to_place)

                adsorbate_complex = AdsorbateComplex(
                    self._adsorbate.info.get("name", "adsorbate"),
                    site.description,
                    orientation.description,
                    new_structure.info["description"],
                    new_structure,
                )

                yield adsorbate_complex

    def adsorbate_orientations(
        self, site: sitefinder.AdsorptionSite
    ) -> list[adsorbateorientation.AdsorbateOrientation]:
        """Returns a list of all adsorbate orientations for a given
        adsorption site.

        Args:
            site: A sitefinder.AdsorptionSite instance representing the site
                for which to generate adsorbate orientations.
        """
        orientation_factory = adsorbateorientation.AdsorbateOrientationFactory(
            site, self._adsorbate, self.symmetric, self.vertical
        )
        return orientation_factory.create_orientations()

    def orient_adsorbate(
        self, orientation: adsorbateorientation.AdsorbateOrientation
    ) -> ase.Atoms:
        """Orients the AdsorbateComplexFactory's adsorbate such that its
        primary axis is aligned with the primary orientation vector of the
        given AdsorbateOrientation object and its secondary axis is in the
        plane defined by the primary axis of the adsorbate and the secondary
        orientation.

        Args:
            orientation: An adsorbateorientation.AdsorbateOrientation instance
                representing the orientation in which the adsorbate is to be
                directed.

        Returns:
            An ase.Atoms instance representing the oriented adsorbate as a
            copy of the AdsorbateComplexFactory's adsorbate.
        """
        new_adsorbate = self.adsorbate

        axis1 = axisfinder.find_primary_axis(new_adsorbate)

        # No first orientation for zero-dimensional molecule
        if norm(axis1) == 0:
            return new_adsorbate

        atom1, _ = axisfinder.find_farthest_atoms(new_adsorbate)

        # Orient along primary orientation axis
        new_adsorbate.rotate(axis1, orientation.vectors[0], atom1.position)

        # Orient using secondary orientation axis
        axis2 = axisfinder.find_secondary_axis(new_adsorbate)

        # No second orientation for one-dimensional molecule
        if norm(axis2) == 0:
            return new_adsorbate

        parallel_component = (
            dot(orientation.vectors[0], orientation.vectors[1])
            * orientation.vectors[0]
        )
        perpendicular_component = orientation.vectors[1] - parallel_component
        atom1, _ = axisfinder.find_farthest_atoms(new_adsorbate)

        new_adsorbate.rotate(
            axis2, perpendicular_component, center=atom1.position
        )

        return new_adsorbate

    def place_adsorbate(
        self,
        adsorbate: ase.Atoms,
        site: sitefinder.AdsorptionSite,
        centre: np.array = None,
    ):
        """Moves adsorbate to specified site respecting the minimum specified
        separation.

        Args:
            new_adsorbate: An ase.Atoms instance representing theadsorbate to
                be moved.
            centre: A numpy.array designating the centre with which to align
                the adsorbate.
            site: A sitefinder.AdsorptionSite instance representing the site
                on which the adsorbate is to be placed.
        """
        if centre is None:
            centre = adsorbate.get_center_of_mass()

        adsorbate.positions += site.location - centre
        separation = geometry.calculate_separation(adsorbate, self._structure)
        while separation < self.separation:
            adsorbate.positions += 0.1 * site.surface_norm
            separation = geometry.calculate_separation(
                adsorbate, self._structure
            )


def _get_structure_with_name(
    structure: pathlib.Path, *, preserve_info: bool = False
) -> ase.Atoms:
    """Loads ase.Atoms object from file path with plain text description.

    The plain text description is stored in the "info" dictionary of the
    structure under the key "description" and can be accessed as follows:
        atoms = _get_structure_with_name(structure)
        structure_description = atoms.info['description']

    Args:
        structure: A pathlib.Path instance indicating the path to the structure
            to be loaded.
        preserve_info: Whether or not to preserve the structure information in the info dictionary.
            If False, the `description` key will be set to the structure name. Defaults to False.

    Returns:
        The ase.Atoms object representing the structure given.
    """
    atoms = read(structure)
    if not preserve_info or "description" not in atoms.info:
        atoms.info["description"] = structure.stem

    return atoms


# pylint:disable=too-many-arguments
def run(
    adsorbate: str,
    structure: pathlib.Path,
    destination: pathlib.Path | None = None,
    separation: float = 1.8,
    special_centres: bool = False,
    symmetric: bool = False,
    vertical: bool = False,
) -> list[tuple[AdsorbateComplex, pathlib.Path]]:
    """Creates MOF-adsorbate complexes for adsorption configurations on the
    SBU of the given MOF and write them to a .traj file.

    Args:
        adsorbate: A string indicating the name of the adsorbate to place on
            the surface.
        structure: A pathlib.Path instance indicating the path to the surface
            on which the adsorbate will be placed.
        destination: A pathlib.Path instance indicating the directory in which
            to write the .traj files. The directory is created if it does not
            exist. Defaults to the current working directory.
        separation: A float indicating how far (in Angstroms) the adsorbate
            should be placed from the surface. Defaults to 1.8.
        symmetric: A boolean indicating whether or not the adsorbate is to be
            treated as symmetric. Defaults to False.
        vertical: A boolean indicating whether or not vertical adsorption
            configurations are to be generated. Defaults to False.

    Returns:
        A list of 2-tuples (complex_i, path_i) where complex_i is the ith
        AdsorbateComplex and path_i is a Path object representing the filename
        under whicn complex_i was saved.
    """
    if destination is None:
        destination = pathlib.Path.cwd()
    elif not destination.exists():
        destination.mkdir()

    adsorbate = adsorbates.get_adsorbate(adsorbate)
    structure = _get_structure_with_name(structure)
    finder = sitefinder.MOFSiteFinder(structure)
    placer = AdsorbateComplexFactory(
        adsorbate, structure, separation, special_centres, symmetric, vertical
    )
    complexes = []
    for site in finder.sites():
        for configuration in placer.next_complex(site):
            complexes.append((configuration, configuration.write(destination)))

    return complexes
