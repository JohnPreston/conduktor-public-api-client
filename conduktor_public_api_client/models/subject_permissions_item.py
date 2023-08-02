from enum import Enum


class SubjectPermissionsItem(str, Enum):
    SUBJECTCREATEUPDATE = "subjectCreateUpdate"
    SUBJECTDELETE = "subjectDelete"
    SUBJECTEDITCOMPATIBILITY = "subjectEditCompatibility"
    SUBJECTVIEW = "subjectView"

    def __str__(self) -> str:
        return str(self.value)
