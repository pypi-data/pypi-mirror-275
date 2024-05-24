from pyvisjs import Network, Options
import os
from pathlib import Path


options = Options("800px", "1300px")
options.edges.set(arrows="to")

net = Network(options=options)

for path, subdirs, files in os.walk("."):
    if ".venv" not in path \
        and "__pycache__" not in path \
        and "cachedir.tag" not in path \
        and "egg-info" not in path:
        curr_dir = (Path(os.getcwd()).stem).replace("-", "\n")
        net.add_node(
            node_id = path, 
            label = curr_dir, 
            shape = "circle",
            color = "orange",
            font = {"color": "black"},
            file_type = "dir",
            file_ext = "",
        )

        for name in subdirs:
            if name not in [".venv", "__pycache__", "pyvisjs.egg-info", "cachedir.tag"]:
                full_name = os.path.join(path, name)
                net.add_node(
                    node_id = full_name, 
                    label = name, 
                    shape = "circle",
                    color = "#4eba3f",
                    font = {"color": "black"},
                    file_type = "dir",
                    file_ext = "",
                )            
                net.add_edge(path, full_name, label=f"dir:{subdirs.index(name)}")

        for name in files:
            full_name = os.path.join(path, name)
            ext = Path(name).suffix

            if ext == ".py":
                (color, font_color) = ("#54bede", "black")
            elif ext == ".md":
                (color, font_color) = ("#F02B4B", "black")
            elif ext == ".txt":
                (color, font_color) = ("#DF7DEC", "black")
            elif ext == ".html":
                (color, font_color) = ("#8f2d56", "white")
            elif ext == ".js":
                (color, font_color) = ("#da7422", "black")
            else:
                (color, font_color) = (None, "black")

            net.add_node(
                node_id = full_name, 
                label = name, 
                shape = "box",
                color = color,
                file_type = "file",
                file_ext = ext,
                font = {"color": font_color},
            )            
            net.add_edge(path, full_name, label=f"file:{files.index(name)}")


net.render_tom_template(
                    title="pyvisjs code repo visualisation",
                    open_in_browser=True,
                    enable_highlighting=True,
                    node_filtering=["file_type", "file_ext", "label"],
                    dropdown_auto_close=True,
                    )