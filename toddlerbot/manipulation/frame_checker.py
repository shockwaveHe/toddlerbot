import json

import mujoco
import mujoco.viewer
import numpy as np

from toddlerbot.manipulation.teleoperation.data_processing.ip_config import *
from toddlerbot.manipulation.teleoperation.data_processing.retarget_lib.src.retarget_lib import (
    mink_retarget,
)

if __name__ == "__main__":
    # create a mujoco word loading the toddlerbot model
    
    xml_path = "..\\..\\toddlerbot\\descriptions\\toddlerbot_active\\toddlerbot_active_scene.xml"
    ik_config = "..\\..\\toddlerbot\\manipulation\\teleoperation\\ik_configs\\quest_toddy.json" # not exist yet, todo

    model = mujoco.MjModel.from_xml_path(xml_path)
    model.opt.gravity[:] = np.array([0, 0, 0])
    # Create a data structure for simulation
    data = mujoco.MjData(model)
    # Load the IK config
    with open(ik_config) as f:
        ik_config = json.load(f)
    ik_match_table = ik_config.pop("ik_match_table")
    retarget = mink_retarget.MinkRetarget(
        xml_path,
        ik_match_table,
        scale=ik_config["scale"],
        ground=ik_config["ground_height"],
    )


