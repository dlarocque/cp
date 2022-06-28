class SnapshotArray:
    
    def __init__(self, length: int):
        # initialize data structure
        self.snaps = [{0: 0} for _ in range(length)]
        self.snap_id = 0
    
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    
    def set(self, idx, val) -> None:
        self.snaps[idx][self.snap_id] = val

    def get(self, idx, snap_id) -> int:
        for _id, val in self.snaps[idx].items():
            if snap_id >= _id:
                prev = val
            else:
                break
