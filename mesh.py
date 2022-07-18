# Open3D Mesh 网格 CSDN

import open3d as o3d
import numpy as np
import copy

print("Testing mesh in Open3D...")
armadillo_path = "./Armadillo.ply"
mesh = o3d.io.read_triangle_mesh(armadillo_path)

print(mesh)
print('Vertices:')
print(np.asarray(mesh.vertices))
print("&&&&&&&&&&& shape: ", np.shape(mesh.vertices))
print('Triangles:')
print(np.asarray(mesh.triangles))
print("&&&&&&&&&&& shape: ", np.shape(mesh.triangles))
# o3d.visualization.draw_geometries([mesh])

print("Try to render a mesh with normals (exist: " +
      str(mesh.has_vertex_normals()) + ") and colors (exist: " +
      str(mesh.has_vertex_colors()) + ")")
o3d.visualization.draw_geometries([mesh])
print("A mesh with no normals and no colors does not look good.")


print("Computing normal and rendering it.")
mesh.compute_vertex_normals()
print(np.asarray(mesh.triangle_normals))
o3d.visualization.draw_geometries([mesh])

print("We make a partial mesh of only the first half triangles.")
mesh1 = copy.deepcopy(mesh)#import copy
mesh1.triangles = o3d.utility.Vector3iVector(
    np.asarray(mesh1.triangles)[:len(mesh1.triangles) // 2, :])
mesh1.triangle_normals = o3d.utility.Vector3dVector(
    np.asarray(mesh1.triangle_normals)[:len(mesh1.triangle_normals) // 2, :])
print(mesh1.triangles)
o3d.visualization.draw_geometries([mesh1])

print("Painting the mesh")
mesh1.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([mesh1])




