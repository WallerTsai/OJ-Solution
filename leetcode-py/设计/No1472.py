class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0

    def __len__(self):
        return len(self.history)

    def visit(self, url: str) -> None:
        self.cur += 1
        del self.history[self.cur:]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.cur = max(self.cur - steps,0)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps,len(self) - 1)
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)