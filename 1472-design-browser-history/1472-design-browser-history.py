class Node:
    def __init__(self,url: str):
        self.data=url
        self.next=None
        self.prev=None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr=Node(homepage)
    def visit(self, url: str) -> None:
        new_node=Node(url)
        self.curr.next=new_node
        new_node.prev=self.curr
        self.curr=new_node
    def back(self, steps: int) -> str:
        x=0
        while self.curr.prev and x< steps:
            self.curr=self.curr.prev
            x+=1
        return self.curr.data
    def forward(self, steps: int) -> str:
        x=0
        while self.curr.next and x<steps:
            self.curr=self.curr.next
            x+=1
        return self.curr.data

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)