from qa_qc_check.controller.qa_qc import QaQc


class TestQaQc:
    def test_main(self, mock_entry_values, mock_check_json):
        result = QaQc(mock_check_json).main(mock_entry_values, "ndvi", "exit")

        assert result["metadata_check"] == "Passed"
