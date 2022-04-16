class ATM:

    def __init__(self):
        self.banknotes = [0]*5
        self.denoms = [20, 50, 100, 200, 500]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, cnt in enumerate(banknotesCount):
            self.banknotes[idx] += cnt
        

    def withdraw(self, amount: int) -> List[int]:
        notes = [0]*5

        def helper(amt: int, idx: int) -> int:
            nonlocal notes

            num_notes = amt // self.denoms[idx]
            num_notes = min(num_notes, self.banknotes[idx])
            if self.banknotes[idx] < num_notes:
                return -1
            else:
                notes[idx] = num_notes

            return amt - self.denoms[idx] * num_notes

        for idx in range(4, -1, -1):
            if amount >= self.denoms[idx]:
                amount = helper(amount, idx)

        if amount == 0:
            for idx in range(5):
                self.banknotes[idx] -= notes[idx]
            return notes
        else:
            return [-1]
