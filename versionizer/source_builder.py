import ast
from typing import Any, Set

import astor

from versionizer.graph_node import GraphNode


class SourceBuilder(ast.NodeTransformer):
    def __init__(self, original_file: str, new_file_name: str, nodes_to_keep: Set[GraphNode]):
        super().__init__()
        self.original_file: str = original_file
        self.new_file_name: str = new_file_name
        self.nodes_to_keep: Set[GraphNode] = nodes_to_keep

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        g_node: GraphNode = GraphNode(node)
        if g_node in self.nodes_to_keep:
            return self.generic_visit(node)

    def build_source(self):
        original_ast = astor.parse_file(self.original_file)
        pruned_ast = self.visit(original_ast)
        print("SOURCE CODE:")
        print(astor.to_source(pruned_ast))
        with open(self.new_file_name, "w") as f:
            f.write(astor.to_source(pruned_ast))
        print(f"Wrote new source file to {self.new_file_name}")

