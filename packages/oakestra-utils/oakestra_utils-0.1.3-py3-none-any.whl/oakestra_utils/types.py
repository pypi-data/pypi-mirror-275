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
    # DEV note: unsure need to check
    CREATING = "CREATING"
    DEAD = "DEAD"
    FAILED = "FAILED"
    UNDEPLOYED = "UNDEPLOYED"
