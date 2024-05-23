import os
import paramiko

def save_to_sftp(output_file, target_user, target_ip, target_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(target_ip, username=target_user)

        sftp = ssh.open_sftp()

        # Split the output_file path to get the directory structure
        directory_structure = os.path.dirname(output_file)

        # Check if directory_structure exists on SFTP, if not, create it
        try:
            sftp.chdir(target_path)
        except IOError:
            sftp.mkdir(target_path)
            sftp.chdir(target_path)

        # Iterate over the directory structure and create folders on SFTP
        for folder in directory_structure.split('/'):
            try:
                sftp.chdir(folder)
            except IOError:
                sftp.mkdir(folder)
                sftp.chdir(folder)

        # Upload the Parquet file to SFTP
        sftp.put(output_file, os.path.join(target_path, output_file))

        print(f"File '{output_file}' uploaded to SFTP successfully.")

        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"Error occurred while saving file to SFTP: {e}")