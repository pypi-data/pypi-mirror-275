import os
import pkg_resources
import tempfile

from diamond.container.container import ImageRegistry


class DiamondClient:

    def __init__(self):
        pass

    def generate_temp_file(self):
        return tempfile.mktemp()

    def generate_task_script(self, cmd: str, log_path: str, endpoint_id: str, container_id: str):
        task_template_filepath = pkg_resources.resource_filename(
            'diamond','diamond_client/templates/task_template')
        tmp_script_path = self.generate_temp_file()
        with open(task_template_filepath, 'r') as f:
            task_template = f.read()
            task_script = (
                task_template
                .replace("dummy_command", cmd)
                .replace("dummy_log_path", log_path)
                .replace("dummmy_endpoint_id", endpoint_id)
                .replace("dummy_container_id", container_id)
            )
            with open(tmp_script_path, 'w') as f:
                f.write(task_script)
        print(tmp_script_path)
        return tmp_script_path
    
    def run_task(self, cmd: str, log_path: str, endpoint_id: str, container_id: str):
        task_script_path = self.generate_task_script(cmd, log_path, endpoint_id, container_id)
        return os.system(f'python3 {task_script_path}')
    
    def register_container(
            self,
            endpoint_id: str,
            work_path: str,
            image_file_name: str,
            base_image: str):
        site_config = {
            "endpoint": endpoint_id,
            "work_path": work_path,
        }
        ir = ImageRegistry(site_config)
        container_id = ir.build(base_image, None, image_file_name)
        return container_id
