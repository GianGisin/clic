class params:
    def __init__(
        self,
        comment_symbol: str,
        file_extension: str,
        count_comments: bool = False,
        count_whitespaces: bool = False,
    ) -> None:
        self.comment_symbol = comment_symbol
        self.file_extension = file_extension
        self.count_comments = count_comments
        self.count_whitespaces = count_whitespaces

    def __repr__(self) -> str:
        return str(self.__dict__.items())
