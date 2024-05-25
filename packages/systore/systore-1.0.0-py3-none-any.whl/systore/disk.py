import psutil as _psutil

def get_disk_partitions():
    partitions = _psutil.disk_partitions()
    return [partition.device for partition in partitions]

def get_file_system_type(partition_name):
    partitions = _psutil.disk_partitions()
    partition_dict = {partition.device : partition.fstype for partition in partitions}
    return partition_dict[partition_name]

def get_mount_point(partition_name):
    partitions = _psutil.disk_partitions()
    partition_dict = {partition.device : partition.mountpoint for partition in partitions}
    return partition_dict[partition_name]
