# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Rotate UV Selection",
    "description": "Rotate UV selection left or right by 90 degrees",
    "author": "Ray Mairlot",
    "version": (1, 0),
    "blender": (2, 72, 0),
    "location": "UV/Image Editor > Shift+R or Ctrl+Shift+R",
    "category": "UV"}
    
import bpy   
from math import radians 
      
      
class RotateUVPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__  
    
    uv_rotation_angle = bpy.props.IntProperty(name="UV Rotation Angle",default=90,description="Angle by which to rotate the selectged UVs by")

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, "uv_rotation_angle")
        row.label("")
        row.label("")
   

class RotateUVLeftOperator(bpy.types.Operator):
    """ Rotate UV selection to the left """
    bl_idname = "uv.rotate_selection_left"
    bl_label = "Rotate UV Selection Left"


    def execute(self, context):
        main(context,"Left")
        return {'FINISHED'}
    
    
class RotateUVRightOperator(bpy.types.Operator):
    """ Rotate UV selection to the right """
    bl_idname = "uv.rotate_selection_right"
    bl_label = "Rotate UV Selection Right"


    def execute(self, context):
        main(context, "Right")
        return {'FINISHED'}    


def main(context, direction=""):        #Same function used for both operators, pass in direction
    
    angle = radians(bpy.context.user_preferences.addons['UV Rotate'].preferences.uv_rotation_angle)
    
    #1.5708
    
    if direction=="Left":
        bpy.ops.transform.rotate(value=-angle)
    else:
        bpy.ops.transform.rotate(value=angle)        


def register():
    bpy.utils.register_class(RotateUVLeftOperator)
    bpy.utils.register_class(RotateUVRightOperator)
    bpy.utils.register_class(RotateUVPreferences)       
    
    kc = bpy.context.window_manager.keyconfigs.addon

    km = kc.keymaps.new(name='Image', space_type='IMAGE_EDITOR')
    km.keymap_items.new("uv.rotate_selection_left", 'R', 'PRESS', ctrl=True, shift=True)
    
    km = kc.keymaps.new(name='Image', space_type='IMAGE_EDITOR')
    km.keymap_items.new("uv.rotate_selection_right", 'R', 'PRESS', shift=True)


def unregister():
    bpy.utils.unregister_class(RotateUVLeftOperator)
    bpy.utils.unregister_class(RotateUVRightOperator)
    bpy.utils.unregister_class(RotateUVPreferences)    
    
    kc = bpy.context.window_manager.keyconfigs.addon
    kc.keymaps.remove(kc.keymaps['Image'])    


if __name__ == "__main__":
    register()





