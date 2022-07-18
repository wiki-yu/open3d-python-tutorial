import open3d as o3d
import numpy as np

# pcl = o3d.geometry.PointCloud()
# pcl.points = o3d.utility.Vector3dVector(np.random.randn(500,3))
# o3d.visualization.draw_geometries([pcl])


#create paths and load data
input_path="./"
output_path="./"
dataname="crystal_4000.xyz"
point_cloud= np.loadtxt(input_path+dataname,skiprows=1)


pcd = o3d.geometry.PointCloud()

pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
# pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
# pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])
# o3d.visualization.draw_geometries([pcd])

#radius determination
distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 3 * avg_dist

#computing the mehs
bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))

#decimating the mesh
# dec_mesh = mesh.simplify_quadric_decimation(100000)