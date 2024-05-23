from abc import ABC
from dataclasses import dataclass, field
from functools import total_ordering

from cognite.neat.rules.issues import IssueList


@total_ordering
@dataclass
class UploadResultCore(ABC):
    name: str

    def __lt__(self, other: object) -> bool:
        if isinstance(other, UploadResult):
            return self.name < other.name
        else:
            return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UploadResult):
            return self.name == other.name
        else:
            return NotImplemented


@dataclass
class UploadResult(UploadResultCore):
    created: int = 0
    deleted: int = 0
    changed: int = 0
    unchanged: int = 0
    skipped: int = 0
    failed_created: int = 0
    failed_changed: int = 0
    failed_deleted: int = 0
    error_messages: list[str] = field(default_factory=list)
    issues: IssueList = field(default_factory=IssueList)

    @property
    def total(self) -> int:
        return self.created + self.deleted + self.changed + self.unchanged

    @property
    def failed(self) -> int:
        return self.failed_created + self.failed_changed + self.failed_deleted

    def as_report_str(self) -> str:
        line = []
        if self.created:
            line.append(f"created {self.created}")
        if self.changed:
            line.append(f"updated {self.changed}")
        if self.skipped:
            line.append(f"skipped {self.skipped}")
        if self.unchanged:
            line.append(f"unchanged {self.unchanged}")
        if self.deleted:
            line.append(f"deleted {self.deleted}")
        if self.failed_created:
            line.append(f"failed to create {self.failed_created}")
        if self.failed_changed:
            line.append(f"failed to update {self.failed_changed}")
        if self.failed_deleted:
            line.append(f"failed to delete {self.failed_deleted}")

        return f"{self.name.title()}: {', '.join(line)}"
