# To load and configure access to Reaper open a window and run:  python -c "import reapy; reapy.configure_reaper()"

import reapy

# Connect to current project
project = reapy.Project()

# add a new track
project.add_track(name="drill_sound")


project.record()