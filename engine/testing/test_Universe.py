from logic import Theorem
from logic.Universe import Universe
from shared_logic import Hypothesis, Point


def test_step():
    bob = Universe()
    bob.heat_death = 2
    _A, _B, _C, _D, _E, _F, _G, _H = [Point.unbound_point(i) for i in range(8)]
    bob.admit(Theorem.Theorem(5, [Hypothesis.midpoint(_E, _A, _C)],
                              [Hypothesis.midpoint(_D, _A, _B),
                               Hypothesis.parallel(_D, _E, _B, _C),
                               Hypothesis.collinear(_E, _A, _C)],
                              name="Theorem Joe"))
    bob.admit(Theorem.Theorem(6, [Hypothesis.parallel(_A, _B, _C, _D)],
                              [Hypothesis.equal_angles(_A, _B, _E, _F, _C, _D, _E, _F)],
                              name="Theorem Dan"))
    A, B, C, D, E, F, G, H = [Point.Point(chr(ord('A') + i)) for i in range(8)]
    bob.pose_many(Hypothesis.midpoint(A, B, C),
                  Hypothesis.equal_angles(B, H, G, A, H, B, C, F),
                  Hypothesis.collinear(G, F, B))
    bob.run_til_heat_death()
    assert len(bob.knowledge.hypotheses) == 5
    assert bob.knowledge.contains(Hypothesis.midpoint(G, F, B))
    bob.knowledge.print_stack_trace(Hypothesis.midpoint(G, F, B))
    print("Test complete")


if __name__ == '__main__':
    test_step()
