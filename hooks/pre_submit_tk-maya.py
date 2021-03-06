import os

import maya.cmds as cmds

import tank
from tank import Hook
from tank import TankError


class PreSubmitHook(Hook):
    def execute(self, **kwargs):

        scene_name = cmds.file(query=True, sn=True)
        if not scene_name:
            raise TankError("Please Save your file before Rendering")

        jobname = os.path.splitext(os.path.basename(scene_name))[0]

        start = cmds.getAttr('defaultRenderGlobals.startFrame')
        end = cmds.getAttr('defaultRenderGlobals.endFrame')

        attrs = [
            {'name': 'submit_file', 'value': str(scene_name), 'title': '', 'hidden': True},

            {'name': 'start', 'value': int(start), 'title': 'Start Frame'},
            {'name': 'end', 'value': int(end), 'title': 'End Frame'},
            {'name': 'by', 'value': 1, 'title': 'By Frame'},

            {'name': 'jobname', 'value': str(jobname), 'title': 'Job Name'},
            {'name': 'queue', 'value': ['high', 'mid', 'low'], 'title': 'Queue'},
            {'name': 'submit', 'value': True, 'title': 'Submit Job'}
        ]

        cmds.file(save=True, force=True)

        return attrs
