import click
import json

from diamond.container.container import ImageRegistry

SITE_CONFIG_PATH = "/tmp/site_config.json"


def init_ir() -> ImageRegistry:
    with open(SITE_CONFIG_PATH, 'r') as f:
        site_config = json.load(f)
    ir = ImageRegistry(site_config)
    return ir

@click.group()
def cli():
    pass

@cli.command()
@click.argument('endpoint_id')
@click.argument('work_path')
def setup_endpoint(endpoint_id: str, work_path: str):
    site_config = {
        "endpoint_id": endpoint_id,
        "work_path": work_path
    }
    with open(SITE_CONFIG_PATH, 'w') as f:
        json.dump(site_config, f)

@cli.command()
def list_base_image_tags():
    ir = init_ir()
    print(ir.list_base_image_tags())

@cli.command()
def list_avail_containers():
    ir = init_ir()
    print(ir.list_avail_containers())

@cli.command()
@click.argument('img_file_name')
def exists(img_file_name: str):
    ir = init_ir()
    print(ir.exists(img_file_name))

@cli.command()
@click.argument('base_img')
@click.argument('img_file_name')
@click.argument('pkg_config_path')
@click.option('--force', is_flag=False)
def build(base_img: str, pkg_config_path: str, img_file_name: str, force: bool):
    ir = init_ir()
    container_id = ir.build(base_img, pkg_config_path, img_file_name, force)
    if container_id:
        print(f"The container id is {container_id}")
    else:
        print("Failed to build the container.")

if __name__ == '__main__':
    cli()
