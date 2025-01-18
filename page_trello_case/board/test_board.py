
from page_services.board.board import BoardService


class TestBoard:
    def test_delete_board(self, delete_board_setup):
        board_service = BoardService(delete_board_setup)
        board_service.join_work_space("萊斯特")
        board_service.create_board(board_name="test")
