# Started from: https://github.com/njanakiev/blender-scripting/blob/master/scripts/simple_sphere.py

import bpy
from math import pi
from mathutils import Euler
tau = 2*pi
from math import sin, cos, pi
import colorsys

# Check if script is opened in Blender program
import os, sys

# UTILS
def rainbowLights(r=5, n=100, freq=2, energy=0.1):
    for i in range(n):
        t = float(i)/float(n)
        pos = (r*sin(tau*t), r*cos(tau*t), r*sin(freq*tau*t))

        # Create lamp
        bpy.ops.object.add(type='LAMP', location=pos)
        obj = bpy.context.object
        obj.data.type = 'POINT'

        # Apply gamma correction for Blender
        color = tuple(pow(c, 2.2) for c in colorsys.hsv_to_rgb(t, 0.6, 1))

        # Set HSV color and lamp energy
        obj.data.color = color
        obj.data.energy = energy

def removeAll(type=None):
    # Possible type: ‘MESH’, ‘CURVE’, ‘SURFACE’, ‘META’, ‘FONT’, ‘ARMATURE’, ‘LATTICE’, ‘EMPTY’, ‘CAMERA’, ‘LAMP’
    if type:
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type=type)
        bpy.ops.object.delete()
    else:
        # Remove all elements in scene
        bpy.ops.object.select_by_layer()
        bpy.ops.object.delete(use_global=False)

def setSmooth(obj, level=None, smooth=True):
    if level:
        # Add subsurf modifier
        modifier = obj.modifiers.new('Subsurf', 'SUBSURF')
        modifier.levels = level
        modifier.render_levels = level

    # Smooth surface
    mesh = obj.data
    for p in mesh.polygons:
        p.use_smooth = smooth

def createSphere(origin=(0, 0, 0)):
    # Create icosphere
    bpy.ops.mesh.primitive_ico_sphere_add(location=origin)
    obj = bpy.context.object
    return obj

def create_plane():
    # Create base plane
    #
    # other way to create mesh! https://www.youtube.com/watch?time_continue=6&v=8wd_EAov6ZE
    bpy.ops.mesh.primitive_plane_add(location=(0,0,0))
    obj = bpy.context.object
    bpy.ops.transform.resize(value=(10, 10, 10))

    # Setup material!
    mat = bpy.data.materials.new(name="grout") # Create new Material
    mat.diffuse_color = (0.08, 0.02, 0.007)
    bpy.context.active_object.data.materials.append(mat)

    bpy.context.object.select = False

    return obj

def create_tile_template():
    bpy.ops.mesh.primitive_plane_add(location=(0,0,0))
    obj = bpy.context.object
    bpy.ops.transform.translate(value=(-9, -9, 0.15))

    bpy.ops.object.editmode_toggle()

    # Extrude!
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate=({"value": (0, 0, -0.3)}))

    # UVs
    bpy.ops.mesh.select_all()
    bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
    bpy.ops.mesh.select_all()
    bpy.ops.uv.smart_project()

    bpy.ops.object.editmode_toggle()

    # tiling
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1.05
    bpy.context.object.modifiers["Array"].count = 10
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
    bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 1.05
    bpy.context.object.modifiers["Array.001"].count = 10

    # Setup material!
    mat = bpy.data.materials.new(name="tiles") # Create new Material
    mat.diffuse_color = (0.85, 0.9, 0.95)
    bpy.context.active_object.data.materials.append(mat)

    return obj

def create_text(text):
    bpy.ops.object.text_add(location=(0,0,0.05))
    obj = bpy.context.object

    bpy.context.object.data.align_x = "CENTER"
    bpy.context.object.data.extrude = 0.2
    bpy.context.object.data.bevel_depth = 0.005
    bpy.context.object.data.bevel_resolution = 3

    # Edit text
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete()
    bpy.ops.font.text_insert(text=text)
    #bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate=({"value": (0, 0, -0.3)}))
    bpy.ops.object.editmode_toggle()

    # TODO: change font to helvetica
    #bpy.ops.fonts.open(filepath="/Users/jesse/projects/mta-app/fake_stations/Helvetica-Regular.ttf")
    #obj.data.font = bpy.data.fonts["HelveticaNeueLT-Roman"]

    return obj

if __name__ == '__main__':
    # TODO: https://www.youtube.com/watch?v=dRzzaRvVDng
    #
    # CYCLES https://www.youtube.com/watch?v=PobPKHuX8pM
   
    # Remove all elements
    removeAll()

    # Create camera + make current cam
    bpy.ops.object.add(type='CAMERA', location=(0, -25, 8.45))
    cam = bpy.context.object
    cam.rotation_euler = Euler((pi/2, 0, 0), 'XYZ')
    bpy.context.scene.camera = cam
    cam.rotation_euler[0] = 1.22

    # TODO set up a constraint to contrain camera to empty
    #bpy.ops.object.empty_add(type="PLAIN_AXES")

    # Create lamps
    #rainbowLights()
    bpy.ops.object.lamp_add(type="SUN")

    # Create objects and their materials
    plane = create_plane()
    tile_template = create_tile_template()

    create_text("Neptune Parkway")
    #setSmooth(sphere, 3)

    # Rendering!
    # Specify folder to save rendering
    # render_folder = 'rendering'
    # if(not os.path.exists(render_folder)):
    #     os.mkdir(render_folder)

    # switch to cycles
    bpy.context.scene.render.engine = 'CYCLES'

    # # Render image
    # rnd = bpy.data.scenes['Scene'].render
    # rnd.resolution_x = 500
    # rnd.resolution_y = 500
    # rnd.resolution_percentage = 100
    # rnd.filepath = os.path.join(render_folder, 'simple_sphere.png')
    # #bpy.ops.render.render(write_still=True)
    # bpy.ops.render.render(write_still=True)
