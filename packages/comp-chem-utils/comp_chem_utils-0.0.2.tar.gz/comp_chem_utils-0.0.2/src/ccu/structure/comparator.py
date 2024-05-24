"""This module defines the Comparator class.

The Comparator class can be used to determine teh similarity of two structures
as follows:

>>> import ase
>>> from ccu.structure.comparator import Comparator
>>> co1 = ase.Atoms('CO', positions=[[0, 0, 0], [1, 0, 0]])
>>> co2 = ase.Atoms('CO', positions=[[0, 1, 1], [1, 1, 1]])
>>> oc = ase.Atoms('OC', positions=[[0, 0, 0], [1, 0, 0]])
>>> Comparator.check_similarity(co1, co2)
True
>>> Comparator.check_similarity(co1, oc)
False
"""

from collections.abc import Iterable
from copy import deepcopy
from itertools import permutations
import math

import ase
import numpy as np
from numpy.linalg import norm

from ccu.structure import fingerprint


class Comparator:
    """An object which compares the similarity of two structures."""

    @staticmethod
    def check_similarity(
        structure1: ase.Atoms, structure2: ase.Atoms, tol: float = 5e-2
    ) -> bool:
        """Determines whether the atomic positions of two structures are
        similar to within a given tolerance.

        Args:
            structure1: An ase.Atoms instance representing the first structure
                to compare.
            structure2: An ase.Atoms instance representing the second structure
                to compare.
            tol: A float specifying the tolerance for the cumulative
                displacement for fingerprint in Angstroms. Defaults to 5e-2.

        Returns:
            A boolean indicating whether or not the two structures are similar
            within the specified tolerance. Two structures are similar if they
            can be superimposed via a translation operation.
        """
        if len(structure1) != len(structure2):
            return False

        fingerprints1 = fingerprint.Fingerprint.from_structure(structure1)
        fingerprints2 = fingerprint.Fingerprint.from_structure(structure2)
        fingerprints2 = Comparator.cosort_fingerprints(
            fingerprints1, fingerprints2
        )
        for i, fingerprint_ in enumerate(fingerprints2):
            if (
                Comparator.calculate_cumulative_displacement(
                    fingerprints1[i], fingerprint_
                )
                > tol
            ):
                return False

        return True

    @staticmethod
    def cosort_histograms(
        fingerprint1: fingerprint.Fingerprint,
        fingerprint2: fingerprint.Fingerprint,
    ) -> dict[str, np.ndarray]:
        """Determines the ordering of the second fingerprint's histogram which
        minimizes the cumulative displacement of the atoms in each structure.

        The two supplied Fingerprints need not have the same keys or the same
        number of entries under each key. Such cases are handled as follows:

        Let k be a key in both the histograms of fingerprint1 and fingerprint2.
        Let p be the iterable corresponding to the key k in the histogram of
        fingerprint1, and let q be the iterable corresponding to the key k in
        the histogram of fingerprint2.

        If len(p) > len(q), then q is ordered according to its match with the
        first len(q) elements of p.

        If len(p) <= len(q), then q is ordered according to the best match with
        p and the first len(p) elements of q.

        Args:
            fingerprint1: The Fingerprint object to be used as a reference for
                each displacement in the other Fingerprint's histogram.
            fingerprint2: The Fingerprint object for which the optimally
                ordered histogram is to be determined.

        Returns:
            A dict constructed from fingerprint2._histogram mapping chemical
            symbols to a numpy.ndarray containing the displacement vectors to
            atoms with the corresponding chemical symbol. The order of the
            displacement vectors is such that the cumulative displacement of
            the displacement vectors is minimized relative to
            fingerprint1._histogram.
        """
        histogram = {}
        for element in fingerprint2:
            minimal_cumulative_displacement = math.inf
            minimally_displaced_ordering = fingerprint2[element]
            if element not in fingerprint1:
                continue

            reference_displacements = fingerprint1[element]
            perm_length = min(
                len(fingerprint1[element]), len(fingerprint2[element])
            )
            displacements_permutations = permutations(
                fingerprint2[element], r=perm_length
            )
            for displacements in displacements_permutations:
                cumulative_displacement = 0
                for i, displacement in enumerate(displacements):
                    cumulative_displacement += norm(
                        reference_displacements[i] - displacement
                    )

                if cumulative_displacement < minimal_cumulative_displacement:
                    minimal_cumulative_displacement = cumulative_displacement
                    minimally_displaced_ordering = list(displacements)

            missing_displacements = Comparator._missing_displacements(
                fingerprint2[element], minimally_displaced_ordering
            )
            minimally_displaced_ordering.extend(missing_displacements)
            histogram[element] = np.vstack(minimally_displaced_ordering)

        return histogram

    @staticmethod
    def _missing_displacements(
        all_displacements: Iterable[np.array],
        minimally_displaced_ordering: Iterable[np.array],
    ) -> list[np.array]:
        missing_displacements = []
        for displacement in all_displacements:
            for included_displacement in minimally_displaced_ordering:
                displacement_missing = True
                if (displacement == included_displacement).all():
                    displacement_missing = False
                    break

            if displacement_missing:
                missing_displacements.append(displacement)

        return missing_displacements

    @staticmethod
    def cosort_fingerprints(
        fingerprints1: Iterable[fingerprint.Fingerprint],
        fingerprints2: Iterable[fingerprint.Fingerprint],
    ) -> tuple[fingerprint.Fingerprint]:
        """Determines the ordering of the second supplied iterable of
        Fingerprints which minimizes the cumulative displacement across the two
        iterables of Fingerprints.

        Args:
            fingerprints1: An iterable containing Fingerprint instances.
            fingerprints2: An iterable containing Fingerprint instances.

            Note that the two iterables must be of the same length and that the
            values() methods of all Fingerprint instances across the two
            iterables must be of the same length.

        Returns:
            A tuple containing the ordering of fingerprints2 which minimizes
            the cumulative displacement across the two iterables of
            Fingerprints.
        """
        minimal_cumulative_displacement = math.inf
        fingerprints_permutations = permutations(
            fingerprints2, r=len(fingerprints2)
        )
        mimimally_displaced_fingerprints = None
        for fingerprints in fingerprints_permutations:
            cumulative_displacement = 0
            for i, fingerprint_ in enumerate(fingerprints):
                fingerprint_.update(
                    Comparator.cosort_histograms(
                        fingerprints1[i], fingerprint_
                    )
                )
                displacement = Comparator.calculate_cumulative_displacement(
                    fingerprints1[i], fingerprint_
                )
                cumulative_displacement += displacement

            if cumulative_displacement < minimal_cumulative_displacement:
                minimal_cumulative_displacement = cumulative_displacement
                mimimally_displaced_fingerprints = deepcopy(fingerprints)

        return mimimally_displaced_fingerprints

    @staticmethod
    def calculate_cumulative_displacement(
        fingerprint1: fingerprint.Fingerprint,
        fingerprint2: fingerprint.Fingerprint,
    ) -> float:
        """Calculates the cumulative displacement of each atomic position in
        fingerprint2 relative to the corresponding atomic position in
        fingerprint1.

        The cumulative displacement is defined as follows:

        Note that each row in each np.ndarray associated with each histogram
        key corresponds to a displacement vector between two atoms. With each
        such displacement vector in the histogram of fingerprint1, we can
        identify a corresponding displacement vector in the histogram of
        fingerprint2 as the displacement vector associated with the same
        histogram key and index. We then define a difference vector as the
        difference between a displacement vector in fingerprint1 and its
        counterpart in  fingerprint2. The set of all difference vectors is
        defined on the basis  of fingerprint1. That is, if X is the set of all
        displacement vectors in fingerprint1 and Y is the set of all
        corresponding vectors in fingerprint2, the set of all difference
        vectors is the set of all vectors x - y where x is a displacement
        vector in fingerprint1 and y is the corresponding displacement vector
        in Y. (Note that this requires that the histogram of fingerprint2 must
        include all the keys that that of the histogram of fingerprint1
        includes. Additionally, this requires that for each key in the
        histogram of fingerprint1, the value in fingerprint2 includes at least
        as many displacement vectors as the value in fingerprint1.) The
        cumulative displacement is then defined as the sum of the norms of all
        the difference vectors corresponding to fingerprint1 and fingerprint2.

        Args:
            fingerprint1: The Fingerprint instance used as a reference to
                calculate the cumulative displacement.
            fingerprint2: The second Fingerprint instance used to calculate the
                cumulative displacement.

        Returns:
            A float representing the cumulative displacement for fingerprint2
            relative to fingerprint1.
        """
        cumulative_displacement = 0
        for element in fingerprint1:
            for i, displacement in enumerate(fingerprint1[element]):
                displacement = norm(displacement - fingerprint2[element][i])
                cumulative_displacement += displacement

        return cumulative_displacement
