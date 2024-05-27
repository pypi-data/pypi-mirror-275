from typing import Any, Dict

from teamai.memory.long_term.long_term_memory_item import LongTermMemoryItem
from teamai.memory.memory import Memory
from teamai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage


class LongTermMemory(Memory):
    """
    LongTermMemory class for managing cross runs data related to overall team's
    execution and performance.
    Inherits from the Memory class and utilizes an instance of a class that
    adheres to the Storage for data storage, specifically working with
    LongTermMemoryItem instances.
    """

    def __init__(self):
        storage = LTMSQLiteStorage()
        super().__init__(storage)

    def save(self, item: LongTermMemoryItem) -> None:
        metadata = item.metadata
        metadata.update({"agent": item.agent, "expected_output": item.expected_output})
        self.storage.save(
            task_description=item.task,
            score=metadata["quality"],
            metadata=metadata,
            datetime=item.datetime,
        )

    def search(self, task: str, latest_n: int = 3) -> Dict[str, Any]:
        return self.storage.load(task, latest_n)
