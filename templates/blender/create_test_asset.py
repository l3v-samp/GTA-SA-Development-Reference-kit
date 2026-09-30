"""Run in Blender's Scripting workspace. Creates a simple test mesh.
Does not export DFF/TXD/COL or configure INU/Ariane automatically.
"""
import bpy

bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
obj = bpy.context.active_object
obj.name = 'ReferenceKit_TestCube'
mat = bpy.data.materials.new(name='ReferenceKit_Gray')
mat.diffuse_color = (0.45, 0.45, 0.45, 1.0)
obj.data.materials.append(mat)
print('Created:', obj.name, '- inspect UVs/materials and configure your exporter before export.')
