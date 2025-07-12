class params:
    def __init__(
        self,
        comment_symbol: str,
        file_extensions: set[str],
        count_comments: bool = False,
        count_whitespaces: bool = False,
    ) -> None:
        self.comment_symbol = comment_symbol
        self.file_extensions = file_extensions
        self.count_comments = count_comments
        self.count_whitespaces = count_whitespaces

    def __repr__(self) -> str:
        return str(self.__dict__.items())
