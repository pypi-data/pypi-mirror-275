from __future__ import annotations
from enum import Enum
from math import inf, pi, acos, atan2, isclose
from typing import Iterable, Generator, Any, ClassVar
from pydantic import BaseModel


class Vector(BaseModel):
    coords: list[float]
    
    @property
    def x(self) -> float:
        return self.coords[0]
    
    @property
    def y(self) -> float:
        return self.coords[1]
    
    @property
    def z(self) -> float:
        return self.coords[2]
    
    @classmethod
    def from_points(cls, point1, point2) -> Vector:
        return cls(coords=(point2 - point1).coords)
    
    @classmethod
    def dot_product(cls, vector1: Vector, vector2: Vector) -> float:
        if not isinstance(vector1, Vector) or not isinstance(vector2, Vector):
            raise TypeError(f"operands must be of type {Vector}")

        return sum(coord1 * coord2 for coord1, coord2 in zip(vector1.coords, vector2.coords))

    @classmethod
    def cross_product(cls, vector1: Vector, vector2: Vector) -> float:
        if not isinstance(vector1, Vector) or not isinstance(vector2, Vector):
            raise TypeError(f"operands must be of type {Vector}")

        return vector1.x * vector2.y - vector1.y * vector2.x

    def norm(self, metric: str = 'euclidean') -> float:
        try:
            p = {
                'octahedral': 1,
                'euclidean': 2,
                'cubic': inf
            }[metric]
        except KeyError:
            raise ValueError(f'unknown metric "{metric}"')

        if p == inf:
            return max(abs(c) for c in self.coords)
        
        return sum(abs(c**p) for c in self.coords) ** (1 / p)
    
    def normalize(self, metric: str = 'euclidean') -> None:
        self.coords = tuple(c / self.norm(metric) for c in self.coords)
    
    def __str__(self) -> str:
        return f"({', '.join(str(c) for c in self.coords)})"


class Point(BaseModel):
    coords: tuple[float, ...]
    
    @classmethod
    def new(cls, *coords):
        return cls(coords=coords)

    @property
    def x(self) -> float:
        return self.coords[0]
    
    @property
    def y(self) -> float:
        return self.coords[1]
    
    @property
    def z(self) -> float:
        return self.coords[2]
    
    @classmethod
    def centroid(cls, *points: Iterable[Point]) -> Point:
        return cls.new(*(sum(coords) / len(coords) for coords in zip(*[p.coords for p in points])))
    
    @staticmethod
    def angle(point1: Point, point2: Point, point3: Point) -> float:
        v1 = Vector.from_points(point2, point1)
        v2 = Vector.from_points(point2, point3)
        v1.normalize()
        v2.normalize()

        return acos(Vector.dot_product(v1, v2) / (v1.norm() * v2.norm()))

    @staticmethod
    def polar_angle(point: Point, origin: Point) -> float:
        return atan2(point.y - origin.y, point.x - origin.x)
    
    @classmethod
    def nonnegative_polar_angle(cls, point: Point, origin: Point) -> float:
        angle = cls.polar_angle(point, origin)
        return angle if angle >= 0 else 2 * pi + angle

    @classmethod
    def dist(cls, point: Point, obj: Point | Line2D, metric: str ="euclidean") -> float:
        if isinstance(obj, Point):
            try:
                p = {
                    "manhattan": 1,
                    "euclidean": 2,
                    "chebyshev": inf
                }[metric]
            except KeyError:
                raise ValueError(f'unknown metric "{metric}"')
            
            if p == inf:
                return max(abs(c1-c2) for c1, c2 in zip(point.coords, obj.coords))
            
            return sum(abs((c1-c2)**p) for c1, c2 in zip(point.coords, obj.coords)) ** (1 / p)
        
        if isinstance(obj, Line2D):
            try:
                p = {
                    "euclidean": 2,
                    "manhattan": inf
                }[metric]
            except KeyError:
                raise ValueError(f'unknown metric "{metric}"')
            
            denominator = max(abs(obj.a, obj.b)) if p == inf else (obj.a**2 + obj.b**2) ** 0.5
            return abs(obj.a*point.x+obj.b*point.y+obj.c) / denominator

    @staticmethod
    def direction(point1: Point, point2: Point, point3: Point) -> float:
        v1 = Vector.from_points(point1, point3)
        v2 = Vector.from_points(point1, point2)

        return Vector.cross_product(v1, v2)

    def __len__(self) -> int:
        return len(self.coords)
    
    def __getitem__(self, key: int) -> float:
        return self.coords[key]
    
    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, self.__class__)
            and all(isclose(c1, c2, abs_tol=1e-3, rel_tol=0) for c1, c2 in zip(self.coords, other.coords))
        )
    
    def __lt__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f'right operand of "<" must be of {self.__class__} type')
        
        return self.coords < other.coords
    
    def __gt__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f'right operand of ">" must be of {self.__class__} type')

        return self.coords > other.coords
    
    def __le__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f'right operand of "<=" must be of {self.__class__} type')
        
        return self < other or self == other
    
    def __ge__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f'right operand of ">=" must be of {self.__class__} type')
        
        return self > other or self == other

    def __add__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"right operand of addition must be of {self.__class__} type")
        
        return self.__class__.new(*(c1 + c2 for c1, c2 in zip(self.coords, other.coords)))
    
    def __sub__(self, other: Point) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"right operand of subtraction must be of {self.__class__} type")
        
        return self.__class__.new(*(c1 - c2 for c1, c2 in zip(self.coords, other.coords)))
    
    def __hash__(self) -> int:
        return hash(self.coords)
    
    def __str__(self) -> str:
        return f"({', '.join(str(c) for c in self.coords)})"


class Line2D(BaseModel):
    """A 2D line represented by the equation ax + by + c = 0 or y = slope * x + y_intercept."""
    
    point1: Point
    point2: Point

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.point1 == self.point2:
            raise ValueError(f"2D line must be initialized with two distinct points")
    
    @property
    def a(self) -> float:
        return self.point1.y - self.point2.y
    
    @property
    def b(self) -> float:
        return self.point2.x - self.point1.x
    
    @property
    def c(self) -> float:
        return self.point1.x * self.point2.y - self.point2.x * self.point1.y
    
    @property
    def slope(self) -> float:
        return -inf if self.b == 0 else -self.a / self.b
    
    @property
    def y_intercept(self) -> float:
        return -inf if self.b == 0 else -self.c / self.b


class BinTreeNode(BaseModel):
    data: Any
    left: BinTreeNode | None = None
    right: BinTreeNode | None = None
    height: int = 0
    
    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None
    
    @property
    def leftmost_node(self) -> BinTreeNode:
        res = self
        while res.left:
            res = res.left
        
        return res

    @property
    def rightmost_node(self) -> BinTreeNode:
        res = self
        while res.right:
            res = res.right
        
        return res
    
    @property
    def balance_factor(self) -> int:
        return (self.right.height if self.right else 0) - (self.left.height if self.left else 0)

    @classmethod
    def copy_contents_without_children(cls, source: BinTreeNode, destination: BinTreeNode) -> None:
        if not isinstance(source, cls) or not isinstance(destination, cls):
            raise TypeError(f"operands must be of type {cls}")
        if source is destination:
            return

        tmp_source_left, tmp_source_right = source.left, source.right
        tmp_dest_left, tmp_dest_right = destination.left, destination.right
        
        source.left, source.right = None, None
        destination.__dict__.update(source.__dict__)

        source.left, source.right = tmp_source_left, tmp_source_right
        destination.left, destination.right = tmp_dest_left, tmp_dest_right

    def traverse_preorder(self, node: BinTreeNode | None = None, nodes: list[BinTreeNode] | None = None) -> list[BinTreeNode]:
        if node is None:
            node = self
        if nodes is None:
            nodes = []
        
        nodes.append(node)

        if node.left:
            self.traverse_preorder(node.left, nodes)
        if node.right:
            self.traverse_preorder(node.right, nodes)
        
        return nodes

    def traverse_inorder(self, node: BinTreeNode | None = None, nodes: list[BinTreeNode] | None = None) -> list[BinTreeNode]:
        if node is None:
            node = self
        if nodes is None:
            nodes = []
        
        if node.left:
            self.traverse_inorder(node.left, nodes)
        
        nodes.append(node)

        if node.right:
            self.traverse_inorder(node.right, nodes)
        
        return nodes

    def traverse_postorder(self, node: BinTreeNode | None = None, nodes: list[BinTreeNode] | None = None) -> list[BinTreeNode]:
        if node is None:
            node = self
        if nodes is None:
            nodes = []
        
        if node.left:
            self.traverse_postorder(node.left, nodes)
        if node.right:
            self.traverse_postorder(node.right, nodes)
        
        nodes.append(node)
        return nodes

    def set_height(self) -> None:
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1 if self.left or self.right else 0        

    def weak_equal(self, other: Any) -> bool:
        """Weak (non-recursive) equality that only checks whether the nodes are of the same type and their contents match."""
        return isinstance(other, self.__class__) and self.data == other.data

    def __eq__(self, other: Any) -> bool:
        """Strong (recursive) equality that checks whether the nodes are of the same type and their trees are equal."""
        return (
            isinstance(other, self.__class__)
            and self.weak_equal(other)
            and self.left == other.left
            and self.right == other.right
        )
    

class BinTree(BaseModel):
    node_class: ClassVar[type] = BinTreeNode
    root: BinTreeNode | None = None

    @classmethod
    def from_iterable(cls, iterable: Iterable) -> BinTree:
        if isinstance(iterable, Generator):
            iterable = list(iterable)
        
        return cls(root=cls._from_iterable(iterable)) if iterable else cls(root=None)
    
    @classmethod
    def _from_iterable(cls, iterable: Iterable, left: int = 0, right: int | None = None) -> BinTreeNode:
        if right is None:
            right = len(iterable) - 1
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = cls.node_class(data=iterable[mid])
        node.left = cls._from_iterable(iterable, left, mid-1)
        node.right = cls._from_iterable(iterable, mid+1, right)
        node.set_height()

        return node
    
    @classmethod
    def empty(cls) -> BinTree:
        return cls.from_iterable([])

    def traverse_preorder(self) -> Iterable[BinTreeNode]:
        return self.root.traverse_preorder() if self.root else []

    def traverse_inorder(self) -> Iterable[BinTreeNode]:
        return self.root.traverse_inorder() if self.root else []
    
    def traverse_postorder(self) -> Iterable[BinTreeNode]:
        return self.root.traverse_postorder() if self.root else []
    
    def leaves_preorder(self) -> Iterable[BinTreeNode]:
        return [node for node in self.traverse_preorder() if node.is_leaf]
    
    def leaves_inorder(self) -> Iterable[BinTreeNode]:
        return [node for node in self.traverse_inorder() if node.is_leaf]
    
    def leaves_postorder(self) -> Iterable[BinTreeNode]:
        return [node for node in self.traverse_postorder() if node.is_leaf]
    
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and self.root == other.root


class ThreadedBinTreeNode(BinTreeNode):
    left: BinTreeNode | None = None
    right: BinTreeNode | None = None
    prev: BinTreeNode | None = None
    next: BinTreeNode | None = None


class AVLTree(BinTree):
    def insert(self, data: Any, starting_node: BinTreeNode | None = None) -> None:
        if starting_node is None:
            starting_node = self.root

        self.root = self._insert(data, starting_node)
    
    def delete(self, data: Any, starting_node: BinTreeNode | None = None) -> None:
        if starting_node is None:
            starting_node = self.root

        self.root = self._delete(data, starting_node)

    def _insert(self, data: Any, node: BinTreeNode | None = None) -> BinTreeNode:
        data_is_node = isinstance(data, self.node_class)
        if node is None:
            return data if data_is_node else BinTreeNode(data=data)
        
        value = data.data if data_is_node else data
        if value < node.data:
            node.left = self._insert(data, node.left)
        else:
            node.right = self._insert(data, node.right)
        
        node.set_height()
        return self.rebalance(node)

    def _delete(self, data: Any, node: BinTreeNode | None = None) -> BinTreeNode:
        if node is None:
            return None
        
        if data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if not node.left or not node.right:
                child = node.left if node.left else node.right
                node = None
                return child
            
            inorder_successor = node.right.leftmost_node
            BinTreeNode.copy_contents_without_children(inorder_successor, node)
            
            node.right = self._delete(inorder_successor.data, node.right)

        if node is None:
            return None

        node.set_height()
        return self.rebalance(node)
    
    def rebalance(self, node: BinTreeNode) -> BinTreeNode:
        balance_factor = node.balance_factor

        if balance_factor == -2:
            if node.left.balance_factor == 1:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
            
            return self._rotate_right(node)
        if balance_factor == 2:
            if node.right.balance_factor == -1:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            return self._rotate_left(node)
        
        # No imbalance
        return node

    def _rotate_left(self, node: BinTreeNode) -> BinTreeNode:
        heavy_node = node.right
        swapped_subnode = heavy_node.left
        heavy_node.left = node
        node.right = swapped_subnode

        node.set_height()
        heavy_node.set_height()

        return heavy_node
    
    def _rotate_right(self, node: BinTreeNode) -> BinTreeNode:
        heavy_node = node.left
        swapped_subnode = heavy_node.right
        heavy_node.right = node
        node.left = swapped_subnode

        node.set_height()
        heavy_node.set_height()

        return heavy_node


class ThreadedBinTree(AVLTree):
    node_class: ClassVar[type] = ThreadedBinTreeNode

    @classmethod
    def from_iterable(cls, iterable: Iterable[ThreadedBinTreeNode], circular: bool = True) -> ThreadedBinTree:
        tree = super().from_iterable(iterable)
        nodes = tree.traverse_inorder()
        
        for i, node in enumerate(nodes):            
            node.prev = node.left if node.left else nodes[i-1]
            node.next = node.right if node.right else nodes[(i+1)%len(nodes)]
        
        if not circular and nodes:
            nodes[0].prev = None
            nodes[-1].next = None
        
        return tree


class PathDirection(str, Enum):
    left = "left"
    right = "right"


class PointType(Enum):
    convex = 0
    reflex = 1
    left_supporting = 2
    right_supporting = 3

    @classmethod
    def by_nodes(cls, source: BinTreeNode, target: BinTreeNode) -> PointType:
        if target.prev is None:
            direction = Point.direction(source.data, target.data, target.next.data)
            if source.data.x < target.data.x:
                return cls.left_supporting if direction > 0 else cls.convex
            
            return cls.right_supporting if direction >= 0 else cls.reflex
        
        if target.next is None:
            direction = Point.direction(source.data, target.data, target.prev.data)
            if source.data.x < target.data.x:
                return cls.left_supporting if direction >= 0 else cls.reflex
            
            return cls.right_supporting if direction > 0 else cls.convex
        
        return cls.by_points(source.data, target.data, target.prev.data, target.next.data)

    @classmethod
    def by_points(cls, source: BinTreeNode, target: BinTreeNode, left: BinTreeNode, right: BinTreeNode) -> PointType:
        def polar_angle(point):
            """[0, 2*pi) polar angle in coordinate system with axis target -> source (rotated against x axis by rot)"""
            rot = Point.nonnegative_polar_angle(source, target)
            angle = Point.nonnegative_polar_angle(point, target)
            return angle - rot + (2 * pi if angle < rot else 0)
        
        angles = polar_angle(left), polar_angle(right)
        angle1 = min(angles)
        angle2 = max(angles)

        convex_or_reflex = 0 < angle1 <= pi <= angle2 < 2 * pi

        # Convex
        if convex_or_reflex and angle2 < angle1 + pi:
            return cls.convex
        
        # Reflex
        if convex_or_reflex and angle2 > angle1 + pi:
            return cls.reflex

        # Left supporting
        if 0 <= angle1 < angle2 < pi:
            return cls.left_supporting
        
        # Right supporting
        if angle1 == 0:
            angle1 = 2 * pi
            angle1, angle2 = angle2, angle1
        
        if pi < angle1 < angle2 <= 2 * pi:
            return cls.right_supporting
        
        raise ValueError