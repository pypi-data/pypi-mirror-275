from .SBGeom_cpp import Mesh
import meshio 
def to_meshio(mesh_cpp):
    if mesh_cpp.vertices.shape[1] == 3:
        return meshio.Mesh(mesh_cpp.positions, [("triangle", mesh_cpp.vertices)])
    elif mesh_cpp.vertices.shape[1] == 4:
        return meshio.Mesh(mesh_cpp.positions, [("tetra", mesh_cpp.vertices)])
    else:
        raise Exception("Trying to convert to a meshio.Mesh with neither 3 or 4 vertices...")
    
def write_mesh(mesh_cpp, name : str):
    to_meshio(mesh_cpp).write(name)
Mesh.write = write_mesh

meshio.Mesh.from_cpp_mesh = staticmethod(to_meshio)