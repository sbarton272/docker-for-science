"""Command line interface to trying out a few docker images"""
import argparse
import os
from subprocess import check_call

TOOLS = {
    'jupyter-notebook': {
        'image': 'jupyter/datascience-notebook',
        'mount_point': '/home/jovyan',
        'port': '8888',
        'docs': 'https://github.com/jupyter/docker-stacks',
    },
}

def run_image(tool_name, mount_point, port):
    """Run the specified tool_name with the volume mounted"""
    try:
        check_call(['docker', '--version'])
    except:
        print('Make sure docker is installed: https://docs.docker.com/engine/installation/')
        return

    image_name = TOOLS[tool_name]['image']
    port_map = '{}:{}'.format(TOOLS[tool_name]['port'], port or TOOLS[tool_name]['port'])
    volume_map = '{}:{}'.format(mount_point or os.getcwd(), TOOLS[tool_name]['mount_point'])
    check_call(['docker', 'run', '-p', port_map, '-v', volume_map, '-it', image_name])

def command_line_interface():
    """Basic entrypoint"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('tool_name', metavar='TOOL', help='Choose a tool to start', choices=TOOLS.keys())
    parser.add_argument('--mount_point', help='Choose which directory on your computer to connect to the docker image')
    parser.add_argument('--port', help='Choose port where tool will run in your browser localhost:<port>')

    args = parser.parse_args()
    run_image(args.tool_name, args.mount_point, args.port)

if __name__ == '__main__':
    command_line_interface()
