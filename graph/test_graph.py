import unittest
from graph import Vertex


class TestGraph(unittest.TestCase):
    def test_dfs_traverse(self):
        """
        Depth-First Search Traverse on Graph
        """
        alice = Vertex("Alice")
        bob = Vertex("Bob")
        fred = Vertex("Fred")
        helen = Vertex("Helen")
        candy = Vertex("Candy")
        derek = Vertex("Derek")
        gina = Vertex("Gina")
        elaine = Vertex("Elaine")
        irena = Vertex("Irena")

        alice.add_adjacent_vertex(bob)
        alice.add_adjacent_vertex(candy)
        alice.add_adjacent_vertex(derek)
        alice.add_adjacent_vertex(elaine)

        bob.add_adjacent_vertex(alice)
        bob.add_adjacent_vertex(fred)

        fred.add_adjacent_vertex(bob)
        fred.add_adjacent_vertex(helen)

        helen.add_adjacent_vertex(fred)
        helen.add_adjacent_vertex(candy)

        candy.add_adjacent_vertex(alice)
        candy.add_adjacent_vertex(helen)

        derek.add_adjacent_vertex(alice)
        derek.add_adjacent_vertex(elaine)
        derek.add_adjacent_vertex(gina)

        elaine.add_adjacent_vertex(alice)
        elaine.add_adjacent_vertex(derek)

        gina.add_adjacent_vertex(derek)
        gina.add_adjacent_vertex(irena)

        irena.add_adjacent_vertex(gina)

        vertices = alice.get_all()

        self.assertIn("Alice", vertices)
        self.assertIn("Bob", vertices)
        self.assertIn("Fred", vertices)
        self.assertIn("Helen", vertices)
        self.assertIn("Candy", vertices)
        self.assertIn("Derek", vertices)
        self.assertIn("Gina", vertices)
        self.assertIn("Elaine", vertices)
        self.assertIn("Irena", vertices)

    def test_dfs(self):
        """
        Depth-First Search on Graph
        """
        alice = Vertex("Alice")
        bob = Vertex("Bob")
        fred = Vertex("Fred")
        helen = Vertex("Helen")
        candy = Vertex("Candy")
        derek = Vertex("Derek")
        gina = Vertex("Gina")
        elaine = Vertex("Elaine")
        irena = Vertex("Irena")

        alice.add_adjacent_vertex(bob)
        alice.add_adjacent_vertex(candy)
        alice.add_adjacent_vertex(derek)
        alice.add_adjacent_vertex(elaine)

        bob.add_adjacent_vertex(alice)
        bob.add_adjacent_vertex(fred)

        fred.add_adjacent_vertex(bob)
        fred.add_adjacent_vertex(helen)

        helen.add_adjacent_vertex(fred)
        helen.add_adjacent_vertex(candy)

        candy.add_adjacent_vertex(alice)
        candy.add_adjacent_vertex(helen)

        derek.add_adjacent_vertex(alice)
        derek.add_adjacent_vertex(elaine)
        derek.add_adjacent_vertex(gina)

        elaine.add_adjacent_vertex(alice)
        elaine.add_adjacent_vertex(derek)

        gina.add_adjacent_vertex(derek)
        gina.add_adjacent_vertex(irena)

        irena.add_adjacent_vertex(gina)

        expectedCandy = alice.get(candy.value)

        self.assertEqual(candy, expectedCandy)

        expectedIrena = alice.get(irena.value)

        self.assertEqual(irena, expectedIrena)


if __name__ == "__main__":
    unittest.main()
