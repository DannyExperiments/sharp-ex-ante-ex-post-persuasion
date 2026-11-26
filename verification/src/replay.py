"""Finite exact checks of tree discounts and the four-state witness."""

from fractions import Fraction
from functools import cache
from random import Random


@cache
def profiles(leaves):
    """Enumerate the leaf-depth multisets of full binary trees."""
    if leaves == 1:
        return {(0,)}
    return {
        tuple(sorted(depth + 1 for depth in left + right))
        for count in range(1, leaves)
        for left in profiles(count)
        for right in profiles(leaves - count)
    }


def discounted_utility(posterior, discount):
    weights = sorted((weight for weight in posterior if weight > 0), reverse=True)
    return max(
        sum(weight * discount**depth for weight, depth in zip(weights, tree))
        for tree in profiles(len(weights))
    )


def tree_formula(leaves, discount):
    if discount >= Fraction(1, 2):
        depth = leaves.bit_length() - 1
        shallow = 2 ** (depth + 1) - leaves
        return shallow * discount**depth + (leaves - shallow) * discount ** (depth + 1)
    if leaves == 1:
        return Fraction(1)
    return sum(discount**depth for depth in range(1, leaves - 1)) + 2 * discount ** (leaves - 1)


def random_posterior(rng):
    masses = [rng.randrange(5) for _ in range(6)] + [1]
    return tuple(Fraction(mass, sum(masses)) for mass in masses)


def check_closed_forms_and_jensen():
    rng = Random(489)
    for discount in map(Fraction, ("1", "3/4", "1/2", "1/3", "1/10")):
        for leaves in range(1, 17):
            optimum = max(sum(discount**depth for depth in tree) for tree in profiles(leaves))
            assert optimum == tree_formula(leaves, discount)

        for _ in range(100):
            p, q = random_posterior(rng), random_posterior(rng)
            weight = Fraction(rng.randrange(11), 10)
            mixture = tuple(weight * x + (1 - weight) * y for x, y in zip(p, q))
            lhs = discounted_utility(mixture, discount)
            rhs = discount * (weight * discounted_utility(p, discount)
                              + (1 - weight) * discounted_utility(q, discount))
            assert lhs >= rhs
    print("80 exact closed-form comparisons and 500 exact two-point inequalities")


def check_four_states():
    prior = (Fraction(1, 4),) * 4
    vertices = tuple(tuple(Fraction(i == j) for i in range(4)) for j in range(4))
    assert tuple(sum(column) / 4 for column in zip(*vertices)) == prior

    for factor, expected_gap in (
        (1, Fraction(1)), (Fraction(3, 2), Fraction(9, 4)), (2, Fraction(4)),
        (3, Fraction(54, 7)), (4, Fraction(128, 11)),
    ):
        discount = 1 / Fraction(factor)
        ex_ante = sum(discounted_utility(vertex, discount) for vertex in vertices) / 4
        ex_post = discounted_utility(prior, discount)
        assert ex_ante == 1
        assert ex_ante / ex_post == expected_gap

    # Maximize a fixed tree over the infinity ball at the center by placing
    # +r on the largest two coefficients and -r on the smallest two.
    # At beta=1/3 the comb has the larger intercept and slope.
    discount = Fraction(1, 3)
    epsilon = Fraction(1, 16)
    intercept = discounted_utility(prior, discount)
    slope = discount + discount**2 - 2 * discount**3
    for radius in (Fraction(0), epsilon / 2, epsilon):
        endpoint = tuple(Fraction(1, 4) + sign * radius for sign in (1, 1, -1, -1))
        assert discounted_utility(endpoint, discount) == intercept + slope * radius
    smoothed_center = intercept + slope * epsilon / 2
    assert smoothed_center == Fraction(61, 432)
    assert smoothed_center <= intercept + tree_formula(4, discount) * epsilon / 2
    print("Five exact tetrahedron gaps: 1, 9/4, 4, 54/7, 128/11")
    print("Smoothed center for M=3, epsilon=1/16: 61/432")


if __name__ == "__main__":
    check_closed_forms_and_jensen()
    check_four_states()
