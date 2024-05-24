from qa_qc_check.controller.meta_data import MetaData
from qa_qc_check.model.metadata_model import MetadataModel


class TestMetaData:
    def test_entry_values_computer(self, mock_extract_json):
        result = MetaData(
            "s3://satimg-to-be-deleted/Sentinel2/TCX8020/20161101_091032002000000_TCX8020.tif"
        )._extract_stats(mock_extract_json, 0)

        assert isinstance(result, MetadataModel) == True
