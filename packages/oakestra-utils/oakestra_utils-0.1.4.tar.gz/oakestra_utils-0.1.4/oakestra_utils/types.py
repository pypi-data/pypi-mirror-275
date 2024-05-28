import enum


class CustomEnum(enum.Enum):
    def __str__(self) -> str:
        return self.value


class ServiceStatus(CustomEnum):
    # DEV note: Exist for sure
    CLUSTER_SCHEDULED = "CLUSTER_SCHEDULED"
    NODE_SCHEDULED = "NODE_SCHEDULED"
    REQUESTED = "REQUESTED"
    ACTIVE = "ACTIVE"
    # Exist but unsure if it fits for service (i.e. other enum might be better)
    NO_WORKER_CAPACITY = "NO_WORKER_CAPACITY"
    # Even stranger
    TARGET_CLUSTER_NOT_FOUND = "TargetClusterNotFound"
    TARGET_CLUSTER_NOT_ACTIVE = "TargetClusterNotActive"
    TARGET_CLUSTER_NO_CAPACITY = "TargetClusterNoCapacity"
    NO_ACTIVE_CLUSTER_WITH_CAPACITY = "NoActiveClusterWithCapacity"
    # DEV note: unsure if exist in non Node-Engine code - need to check
    CREATING = "CREATING"
    DEAD = "DEAD"
    FAILED = "FAILED"
    UNDEPLOYED = "UNDEPLOYED"
