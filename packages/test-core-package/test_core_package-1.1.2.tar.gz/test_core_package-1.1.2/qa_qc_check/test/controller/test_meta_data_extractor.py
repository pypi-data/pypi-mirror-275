from qa_qc_check.controller.meta_data_extractor import MetadataExtractor
from qa_qc_check.model.metadata_model import QaQcModel


class TestMetaDataExtractor:
    def test_entry_values_computer(self, mock_computed_values):
        result = MetadataExtractor(
            "s3://satimg-to-be-deleted/Sentinel2/TCX8020/20161101_091032002000000_TCX8020.tif",
            "exit",
        )._entry_values_computer(mock_computed_values)

        assert isinstance(result, QaQcModel) == True
