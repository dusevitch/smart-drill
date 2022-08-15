# To load and configure access to Reaper open a window and run:  python -c "import reapy; reapy.configure_reaper()"

import reapy

# Connect to current project
project = reapy.Project()



# add a new track
project.add_track(index=0, name="drill_sound")
project.add_track(index=2, name="drill_sound2")
project.add_track(index=10, name="drill_sound1")
# reapy.arm_command(project.command_id, section="")


tracks = project.tracks

print("TRACK NAMES:\n")
for track in tracks:
    print(track.name)

print('disarm all')
project.disarm_rec_on_all_tracks()
