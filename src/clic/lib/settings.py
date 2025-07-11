class params:
    def __init__(
        self,
        comment_symbol: str,
        count_comments: bool = False,
        count_whitespaces: bool = False,
    ) -> None:
        self.comment_symbol = comment_symbol
        self.count_comments = count_comments
        self.count_whitespaces = count_whitespaces
