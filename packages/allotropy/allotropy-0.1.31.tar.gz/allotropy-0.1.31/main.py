import json
from pathlib import Path

from allotropy.constants import CHARDET_ENCODING
from allotropy.parser_factory import Vendor
from allotropy.to_allotrope import allotrope_from_file

output_files = [
    "96-Well Trevigen CometAssayCometChip Imaging and Analysis Sample File 23Nov15",
    "HeLa 96well Colony 11pt Doxorubicin UprBF_TAB",
    "Cell_Count_DAPI_GFP",
]
vendor = Vendor.AGILENT_GEN5_IMAGE


if __name__ == "__main__":
    # filename = "Beckman_Vi-Cell-XR_example02_instrumentOutput.xls"
    for filename in output_files:
        # read_mode = "fluorescence"
        # test_filepath = (
        #     f"tests/parsers/agilent_gen5/testdata/{read_mode}/{filename}.txt"
        # )
        # test_filepath = f"tests/parsers/luminex_xponent/testdata/{filename}.csv"
        test_filepath = f"{filename}.txt"

        allotrope_dict = allotrope_from_file(
            test_filepath, vendor, encoding=CHARDET_ENCODING
        )
        target_filename = Path(test_filepath).with_suffix(".json").name
        # print(allotrope_dict)
        with open(target_filename, "w") as fp:
            fp.write(json.dumps(allotrope_dict, indent=4, ensure_ascii=False))
